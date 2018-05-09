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
"""Playground API routes.
"""

# utilities
import base64
import logging
import os
from datetime import datetime
from .api_utils import APIHelper

# web framework
from flask import Flask, request, json, jsonify, Response

# predictor
from predict import Predict, PredictError

# constants and global variables
APP = Flask(__name__)
API_HELPER = APIHelper()
PREDICTOR = Predict(logging)

# note: user-defined variables are declared here for readability only

# config variables
ZOOM_LEVELS = [16, 17]
PADDING = 20

# version data to be returned by the /version route
# implementation specific (can put VCS version, compiler, build environment ...)
VERSION_DATA = {
    "version": "1.0.0",
}

# processing description and parameters that needs to be changed for each process
# this will override the template data
PROCESS_DATA = {
    # to be changed by each process implementation
    "name": "eu.gcr.io/playground-doc/tile-object-detection-stub",
    "title": "Playground tile object detection stub",
    "family": "",
    "version": "1.0",
    "description": "Geo Process API stub for ",
    "organization": "Airbus Defence and Space Intelligence",
    "email": "playground-stub@airbus.com",
    "keywords": "tile",
    "resources": {
        "cpu": 1,
        "ram": 1048576
    },

    # valid values for Playground: tile-object-detection, tile-change-detection
    "template": "tile-object-detection",

    # can be changed by each process implementation. Should be reflected in the flask app
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

try:
    DESCRIBE_DATA = API_HELPER.load_process_data(PROCESS_DATA)
except ValueError as e:
    logging.error(e)
    logging.error("Invalid Config File")

# below is the definition of the Flask App.
# You may not have to modify anything, except if you modified the default _links above
# predict.py should contain your prediction code and is defined above via PREDICTOR

@APP.route("/")
def default_backend():
    """Default backend check for GKE Ingress
    """
    LOGGER.debug("Received /readiness_check request")
    """ Check service health """
    if PREDICTOR is not None:
        LOGGER.debug("Responding Ready OK")
        return Response("live ok", status=200)
    else:
        LOGGER.debug("Responding Ready KO")
        return Response("not live", status=500)

@APP.route("/liveness_check")
def check_liveness():
    """Liveness check for GKE/GAE
    """
    LOGGER.debug("Received /liveness_check request")
    """ Check service health """
    if PREDICTOR is not None:
        LOGGER.debug("Responding Live OK")
        return Response("live ok", status=200)
    else:
        LOGGER.debug("Responding Live KO")
        return Response("not live", status=500)


@APP.route("/readiness_check")
def check_readiness():
    """Readiness check for GKE/GAE
    """
    LOGGER.debug("Received /readiness_check request")
    """ Check service health """
    if PREDICTOR is not None:
        LOGGER.debug("Responding Ready OK")
        return Response("live ok", status=200)
    else:
        LOGGER.debug("Responding Ready KO")
        return Response("not live", status=500)

@APP.route('/api/v1/openapi', methods=['GET'])
def openapi():
    """
        GET /api/v1/openapi
        Return Geo Process API OpenAPI specification.
    """
    open_api_data = API_HELPER.open_api_data
    return Response(open_api_data, mimetype="text/yaml", status=200)


@APP.route('/api/v1/describe', methods=['GET'])
def describe():
    """
        GET /api/v1/describe
        Return process description.
    """
    return jsonify(DESCRIBE_DATA)


@APP.route('/api/jobs', methods=['POST'])
def jobs():
    """
        POST /api/jobs
        Return detected objects from the given tile.
    """
    try:
        # get input parameter
        correlation_id = request.headers.get('X-Correlation-ID')
        if request.headers.get('X-ADS-Debug') is not None:
            debug = request.headers.get('X-ADS-Debug').lower()
            debug = debug in ("yes", "true", "t", "1")
        else:
            debug = False
        # get input data
        data = request.get_json()
        API_HELPER.validate_input(data)
        zoom = int(data['zoom'])
        tile_format = data['tileFormat']
        tile = base64.b64decode(data['tile'])
        if 'mask' in data:
            mask = base64.b64decode(data['mask'])
        else:
            mask = None

        if zoom not in ZOOM_LEVELS:
            raise Exception('Invalid zoom: ' + str(zoom))

    except Exception as error:
        logging.error('requestId: %s error: %s', correlation_id, error.message)
        # return invalid input error
        return Response(error.message, status=400)

    try:
        # detect objects
        prediction = PREDICTOR.process(zoom, tile_format, tile, mask, debug)

        # return prediction result
        logging.debug('Prediction: %s', prediction)

        return jsonify(prediction)

    except PredictError as error:
        # return error message
        data = {
            "message": "Prediction failed",
            "hint": error.message,
            "correlationId": correlation_id,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        logging.error(data)
        return Response(json.dumps(data), mimetype="application/json", status=500)


@APP.route('/api/config', methods=['GET'])
def get_config():
    """
        GET /api/config
        Return process configuration.
    """
    correlation_id = request.headers.get('X-Correlation-ID')
    config_data = {
        # to be changed by each process implementation
        "zoom": ZOOM_LEVELS,
        "padding": PADDING
    }
    try:
        API_HELPER.validate_config(config_data)

        return jsonify(config_data)
    except Exception as error:
        logging.error('requestId: %s error: %s', correlation_id, error.message)
        # return invalid input error
        return Response(error.message, status=400)


@APP.route('/api/config', methods=['PUT'])
def set_config():
    """
        PUT /api/config
        Set process configuration.
    """
    # do nothing as this process is asynchronous and not statefull
    return Response('ok', status=200)


@APP.route('/api/version', methods=['GET'])
def version():
    """
        POST /api/version
        Return internal versions.
    """
    return jsonify(VERSION_DATA)
