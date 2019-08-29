# Copyright 2018 Airbus. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Object detection processing.
"""

# utilities
import json
import base64
import io
import geojson

# image processing
from PIL import Image
import shapely.geometry

# matrix processing
import numpy as np

# import TensorFlow deep learning framework
#import tensorflow as tf

# OR import PyTorch
#import torch
#import torch.nn as nn
#import torch.nn.functional as F

#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")



class PredictError(Exception):
    """Predict processing error.
    
    Attributes:
        message (str): Description
    """

    def __init__(self, message):
        """Constructor.
        
        Args:
            message (str): error message
        """
        super(PredictError, self).__init__(message)


class Predict(object):
    """Object detection processing.
    
    Attributes:
        logger (TYPE): the logger
    """

    def __init__(self, logger):
        """Constructor.
        
        Args:
            logger (TYPE): the logger
        """
        self.categories = {0: "no-class", 1: "object"}
        self.logger = logger


    def process(self, resolution, tiles):
        """Process tile.
        
        Args:
            resolution (float): size on the ground of a pixel in meters
            tiles (bytearray): array of tiles

        
        Returns:
            object: GeoJSON FeatureCollection
        """
        if self.logger:
            self.logger.debug('Generate prediction')

        try:
            # convert first tile from byte array to PIL image
            img = Image.open(io.BytesIO(tiles[0]))
            
            # and optionaly to a numpy array
            #img = np.asarray(img, dtype=np.uint8)

            # run machine learning algorithm on tile image
            results = self._predict(img)

            if self.logger:
                self.logger.info('%d polygons found', len(results))

            # create a GeoJSON
            features = []
            for _, (p, confidence, category) in enumerate(results):
                props = {
                    "category": self.categories[category],
                    "confidence": str(round(confidence, 4))
                }
                features.append(geojson.Feature(geometry=geojson.Polygon(p), properties=props))
            data = geojson.FeatureCollection(features)

        except Exception as error:
            if self.logger:
                self.logger.exception(error)
            raise PredictError(error)

        return data


    def _predict(self, img):
        """Process tile.
        
        Args:
            img (numpy array): tile image
            mask (numpy array): mask
        
        Returns:
            array: array of GeoJSON Features
        """
        # TODO process tile image, each detected object is a polygon with category and confidence
        img_width, img_height = img.size
        margin_width = img_width // 4
        margin_height = img_height // 4

        results = []
        results.append(([
                (margin_width, margin_height), 
                (img_width - margin_width, margin_height), 
                (img_width - margin_width, img_height - margin_height), 
                (margin_width, img_height - margin_height), 
                (margin_width, margin_height)],
            0.9,
            0))

        return results

