"""Predict processing.
"""

# utilities
import json
import base64
import io

# image processing
from PIL import Image

# matrix processing
import numpy as np

# deep learning
import tensorflow as tf

# playground
from playground_api import PredictStatus, PredictType


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
        super(PredictError, self).__init__()
        self.message = message


class Predict(object):
    """Prediction processing.
    
    Attributes:
        logger (TYPE): the logger
    """

    def __init__(self, logger):
        """Constructor.
        
        Args:
            logger (TYPE): the logger
        """
        self.logger = logger


    def predict(self, tile_1, tile_2):
        """Predict tiles.
        
        Args:
            tile_1 (bytearray): first tile
            tile_2 (bytearray): second (optional) tile
        
        Returns:
            dict: prediction result
        """
        self.logger.debug('Generate prediction')

        try:
            # convert tile from byte array to numpy array
            img = Image.open(io.BytesIO(tile_1))
            img = np.asarray(img, dtype=np.uint8)
        
            # process tile image
            # TODO
            result = None

            data = {
                'status' : PredictStatus.DONE,
                'type' : PredictType.GEO_JSON,
                'result' : result
            }

        except:
            data = {
                'status' : PredictStatus.ERROR,
                'error' : 'Error processing tile',
                'type' : PredictType.GEO_JSON,
                'result' : None
            }

        return data

