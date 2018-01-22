"""Playground API stub routes.
"""

# utilities
import base64
import logging

# web framework
from flask import Flask, request, json

# predictor
from predict import Predict


app = Flask(__name__)
predictor = Predict(logging)


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    """
        POST /api/v1/predict
        Return prediction result on given tiles.
    """
    # get tiles images as bytearray
    data = request.get_json()
    tile_1 = base64.b64decode(data['tile_1'])
    if 'tile_2' in data:
        tile_2 = base64.b64decode(data['tile_2'])
    else:
        tile_2 = None

    # predict tiles
    prediction = predictor.predict(tile_1, tile_2)

    # return prediction result
    prediction = json.dumps(prediction)
    logging.debug('Prediction: %s', prediction)

    return prediction


@app.route('/api/v1/describe', methods=['GET'])
def describe():
    """
        GET /api/v1/describe
        Return process description.
    """
    # processing description and parameters
    data = {
        # expected tile padding
        'padding' : 20,
        # expected tile number
        'nb_tiles' : 1
    }

    return json.dumps(data)


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=80)

