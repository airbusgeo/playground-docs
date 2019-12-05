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

# utilities
import base64
import logging
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from predict import Predict
import time
import asyncio
import logging
import os

# web framework
from sanic import Blueprint, response
from sanic.exceptions import ServerError
from sanic.request import Request
from sanic.response import HTTPResponse
from sanic.log import logger
from sanic_openapi import doc

# predictor
from predict import Predict, PredictError

# initialize app
v1 = Blueprint('v1', url_prefix='/api/v1')

# initialize predictor
predictor = Predict(logger=logger)

# define a lock to allow only one thread of processing
lock = None

# initialize the lock
@v1.listener('before_server_start')
async def init(sanic, loop):
    global lock
    lock = asyncio.Lock()

# return the global OpenAPI specification 
@v1.route('/openapi')
@doc.summary('Open API specification of this service in YAML format')
async def openapi(request: Request) -> HTTPResponse:
    return await response.file('tile_geo_process_api.yaml')

# return OK is the service is still alive
@v1.route('/health')
@doc.summary('Check if service is alive')
async def get(request: Request) -> HTTPResponse:
    result = response.text('OK', 200)
    result.headers['content-type'] = 'text/plain'
    return result

# return a description of this service
@v1.route('/describe')
@doc.summary('The description of this service in JSON schema')
async def describe(request: Request) -> HTTPResponse:
    return await response.file('description.json')

# Implementation specifics endpoints
@v1.route('/process', methods=['POST'])
@doc.summary('Launch processing service')
@doc.produces('JSON')
async def process_post(request: Request) -> HTTPResponse:
    data = request.json
    if not data:
        return response.text('JSON payload is empty, or payload is not JSON.', 500)

    if lock.locked():
        return response.text('A processing is already running.', 429)

    await lock.acquire()
    try:
        # get input data
        resolution = data['resolution']
        tiles = [base64.b64decode(data['tiles'][i]) for i in range(len(data['tiles']))]

        # detect objects
        def _processing():
            return predictor.process(resolution, tiles)

        # launch detection in a specific thread
        prediction = await asyncio.wait_for(async_exec(_processing), timeout=None)

        # log prediction result
        logging.debug('Prediction: %s', json.dumps(prediction))

        # return prediction results
        return response.json(prediction, 200)

    except Exception as e:
        # return invalid input error
        data = {
            "message": "Error in inference.",
            "hint": str(e),
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        logging.error(data)
        return response.json(data, 400)

    finally:
        lock.release()


async def async_exec(callback):
    with ThreadPoolExecutor(max_workers=1) as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, callback)

