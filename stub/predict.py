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

# deep learning
import tensorflow as tf


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
        self.logger = logger


    def process(self, zoom, tile_format, tile, mask=None, debug=False):
        """Process tile.
        
        Args:
            zoom (integer): zoom level
            tile_format (string): tile mime-type
            tile (bytearray): tile
            mask (bytearray): mask as 8 bits PNG
            debug (boolean): debug mode
        
        Returns:
            object: GeoJSON FeatureCollection
        """
        self.logger.debug('Generate prediction')

        try:
            # convert tile from byte array to numpy array
            img = Image.open(io.BytesIO(tile))
            img = np.asarray(img, dtype=np.uint8)
            
            if mask is not None:
                mask = Image.open(io.BytesIO(mask))
                mask = np.asarray(mask, dtype=np.uint8)
        
            # process tile image
            polygons, confidence = self._predict(img, mask)

            if debug:
                self.logger.info('%d polygons found', len(polygons))

            # create a GeoJSON
            features = []
            for p in polygons:
                props = {
                    "category": "test",
                    "conficence": confidence
                }
                features.append(geojson.Feature(geometry=shapely.geometry.mapping(p), properties=props))
            data = geojson.FeatureCollection(features)

        except Exception as error:
            self.logger.exception(error)
            raise PredictError(error.message)

        return data


    def _predict(self, img, mask=None):
        """Process tile.
        
        Args:
            img (numpy array): tile image
            mask (numpy array): mask
        
        Returns:
            array: array of GeoJSON Features
        """
        # TODO process tile image, each detected object is a polygon
        polygons = []
        confidence = 1.0

        return polygons, confidence
