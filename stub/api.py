"""Playground API routes.
"""

# utilities
import base64
import logging
from datetime import datetime

# web framework
from flask import Flask, request, json

# predictor
from predict import Predict, PredictError


# constants and global variables
app = Flask(__name__)
predictor = Predict(logging)

ZOOM_LEVEL = [ 16, 17 ]


@app.route('/api/v1/openapi', methods=['GET'])
def openapi():
    """
        GET /api/v1/openapi
        Return Geo Process API OpenAPI specification.
    """
    with open('api_geo_process.yaml', 'r') as content_file:
        content = content_file.read()
    
    return content


@app.route('/api/v1/describe', methods=['GET'])
def describe():
    """
        GET /api/v1/describe
        Return process description.
    """
    # processing description and parameters
    data = {
        # to be changed by each process implementation
        "name": "eu.gcr.io/playground-doc/tile-object-detection-stub",
        "title": "Playground tile object detection stub",
        "family": "",
        "version": "1.0",
        "description": "Geo Process API stub for ",
        "organization": "Airbus Defence and Space Intelligence",
        "email": "playground-stub@airbus.com",
        "keywords": "TBC",
        "resources": {
            "cpu": 1,
            "ram": 1048576
        },

        # valid values for Playground: tile-object-detection, tile-change-detection
        "template": "tile-object-detection",

        # specific to tile-object-detection
        "input": {
            "$schema": "http://json-schema.org/draft-06/schema#",
            "title": "tile-object-detection-input",
            "description": "Geo Process API input schema for tile object detection",
            "type" : "object",
            "required": [
                "zoom",
                "tileFormat",
                "tile"
            ],
            "properties": {
                "zoom": {
                    "description": "Tile zoom level",
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 20
                },
                "tileFormat": {
                    "description": "MIME type of tile image format (image/png or image/jpeg)",
                    "type": "string"
                },
                "tile": {
                    "description": "The tile image base64 encoded, may be JPEG or PNG format",
                    "type": "string",
                    "format": "base64"
                },
                "mask": {
                    "description": "Mask image base64 encoded in 8 bits PNG format",
                    "type": "string",
                    "format": "base64"
                }
            }
        },

        # specific to tile-object-detection
        "output": {
            "description": "Tile object detection GeoJSON. Root element has to be a 'FeatureCollection' with one or several 'Feature' objects. Feature geometry is expressed with (0,0) at the top left of the tile image padding included. Feature properties may be 'category' and 'confidence'. The 'category' property is used for tags, labels or classification results. It's value may be a string with several values separated by a comma or an array of strings. The 'confidence' property value is a float between 0. and 1.0.",
            "content": {
                "application/geo+json": {}
            }
        },
        
        # specific to tile-object-detection
        "config": {
            "$schema": "http://json-schema.org/draft-06/schema#",
            "title": "tile-object-detection-config",
            "description": "Geo Process API config schema for tile object detection",
            "type" : "object",
            "required": [
                "zoom",
                "padding"
            ],
            "properties": {
                "zoom": {
                    "description": "Zoom levels that can be processed",
                    "type" : "array",
                    "minItems": 1,
                    "items": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 17
                    }
                },
                "padding": {
                    "description": "Padding / border needed to process the tile. 0 for no padding.",
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 256
                }
            }
        },

        # Playground do not manage asynchronous processes
        "asynchronous": False,

        # can be changed by each process implementation
        "_links": {
            "self": {
                "href": "/api/v1/describe"
            },
            "execution": {
                "href": "/api/jobs"
            },
            "config:": {
                "href": "/api/config"
            },
            "version": {
                "href": "/api/version"
            }
        }
    }

    return json.dumps(data)


@app.route('/api/jobs', methods=['POST'])
def jobs():
    """
        POST /api/jobs
        Return detected objects from the given tile.
    """
    try:
        # get input parameter
        correlation_id = request.headers.get('X-Correlation-ID')
        debug = request.headers.get('X-ADS-Debug').lower() in ("yes", "true", "t", "1")

        # get input data
        data = request.get_json()
        zoom = int(data['zoom'])
        tile_format = data['tileFormat']
        tile = base64.b64decode(data['tile'])
        if 'mask' in data:
            mask = base64.b64decode(data['mask'])
        else:
            mask = None

        if zoom not in ZOOM_LEVEL:
            raise Exception('Invalid zoom: ' + str(zoom))

    except Exception as error:
        logging.error('requestId: %s error: %s', correlation_id, error.message)
        # return invalid input error
        return '', 400

    try:
        # detect objects
        prediction = predictor.process(zoom, tile_format, tile, mask, debug)

        # return prediction result
        prediction = json.dumps(prediction)
        logging.debug('Prediction: %s', prediction)

        return prediction

    except PredictError as error:
        # return error message
        data = {
            "message": "Prediction failed",
            "hint": error.message,
            "correlationId": correlation_id,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        logging.error(data)
        return json.dumps(data), 500


@app.route('/api/config', methods=['GET'])
def get_config():
    """
        GET /api/config
        Return process configuration.
    """
    data = {
        # to be changed by each process implementation
        "zoom": ZOOM_LEVEL,
        "padding": 20
    }

    return json.dumps(data)


@app.route('/api/config', methods=['PUT'])
def set_config():
    """
        PUT /api/config
        Set process configuration.
    """
    # do nothing as this process is asynchronous and not statefull
    return '', 200


@app.route('/api/version', methods=['GET'])
def version():
    """
        POST /api/version
        Return internal versions.
    """
    # implementation specific (can put VCS version, compiler, build environment ...)
    data = {
    }

    return json.dumps(data)


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=80)

