"""Playground processing API.
"""


class PredictStatus(object):
    """Predict status constants.
    
    Attributes:
        DONE (str): Prediction executed without errors
        ERROR (str): Error while executing the prediction
    """
    DONE = 'DONE'
    ERROR = 'ERROR'


class PredictType(object):
    """Predict result type constants.
    
    Attributes:
        GEO_JSON (str): GeoJSON result in pixel coordinates from top-left corner
    """
    GEO_JSON = 'application/geo+json'


