# Standard libraries
import base64
import json

# Third-party libraries
import click
import loguru
import numpy as np
import requests
from schema import And, Optional, Or, Use, Schema, SchemaError

POINT_SCHEMA = Schema(And(
    And(Or(list, tuple, error='Coordinates should be a list or tuple.')),
    And(lambda coords: len(coords) == 2, error='Coordinates should be a tuple/list of a X and Y coordinates.'),
    And(lambda coords: coords[0] >= 0, error='The first coordinate of a point, in pixels, should be positive.'),
    And(lambda coords: coords[1] >= 0, error='The second coordinate of a point, in pixels, should be positive.'),
))
COORDINATES_SCHEMA = Schema(And(
    And(Or(list, tuple, error='Coordinates should be a list or tuple.')),
    And(lambda rings: len(rings) >= 1, error='Polygon should contain a single ring.'),
    And(lambda polygon: len(polygon[0]) >= 4, error='Polygon should contain at least 4 points.'),
    And([[POINT_SCHEMA]])
))
POLYGON_SCHEMA = Schema({
    'type': 'Polygon',
    'coordinates': COORDINATES_SCHEMA
})

PROPERTIES_SCHEMA = Schema({
    'category': And(Use(list), lambda categories: len(categories) >= 2,
                    error='Feature should have at least one category'),
    'confidence': And(Use(float), lambda confidence: 0 <= confidence <= 1,
                      error='Confidence should be a positive float between 0 and 1'),
    Optional(str): Or(bool, str, int, float, list, dict)
})

FEATURE_SCHEMA = Schema({
    'type': 'Feature',
    'properties': PROPERTIES_SCHEMA,
    'geometry': POLYGON_SCHEMA
})

FEATURE_COLLECTION_SCHEMA = Schema({
    'type': 'FeatureCollection',
    'features': [FEATURE_SCHEMA],
    Optional('id'): Use(str),
    Optional('bbox'): Use(list)
})

# Groups
@click.group()
def check():
    """Test CLI"""
    pass

# Commands
@click.command()
@click.option('--endpoint', default='http://0.0.0.0:8080/api/v1/health', type=click.STRING,
              help='End-point to be used to check healthyness')
def health(endpoint):
    """Test if the Health endpoint is responding with a 200 HTTP code."""
    loguru.logger.info('Check HEALTH end point: {endpoint}'.format(endpoint=endpoint))
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        assert response.status_code == 200, 'Expects a 200 HTTP code, got: {}'.format(response.status_code)
    except requests.exceptions.RequestException as error:
        return loguru.logger.error('An error occured during the test: {error}'.format(error=error))
    except AssertionError as error:
        return loguru.logger.error('An error occured during the test: {error}'.format(error=error))

    return loguru.logger.success('The HEALTH end point ({}) successfully returned a 200 HTTP code.'.format(endpoint))


@click.command()
@click.option('--endpoint', default='http://0.0.0.0:8080/api/v1/process', type=click.STRING,
              help='End-point to be used to check healthyness')
@click.option('--tile-width', default=256, type=click.INT, help='Width of the tile to process (pixels)')
@click.option('--tile-height', default=256, type=click.INT, help='Height of the tile to process (pixels)')
@click.option('--resolution', default=0.5, type=click.FLOAT, help='Resolution of the tile to process (m/pixels)')
@click.option('--tile-path', default=None, type=click.Path(exists=True, file_okay=True))
@click.option('--verbose', '-v', is_flag=True)
def process(endpoint, tile_width, tile_height, resolution, tile_path, verbose):
    """Test if the Health endpoint is responding with a 200 HTTP code."""
    # If a tile is given, open it and encode it to base 64
    # If not, create a black tile with the given dimensions (or use the default ones)
    if tile_path is not None:
        loguru.logger.warning('The optional parameters `tile_width` and `tile_height` are not taken into account.')

        # Open image and encode it in base 64
        with open(tile_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    else:
        tile = np.zeros((tile_width, tile_height), dtype=np.uint8)
        encoded_string = base64.b64encode(tile).decode('utf-8')

    # Run check
    loguru.logger.info('Check PROCESS end point: {endpoint}'.format(endpoint=endpoint))
    try:
        payload = {'resolution': resolution, 'tiles': [encoded_string]}
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        assert response.status_code == 200, 'Expects a 200 HTTP code, got: {}'.format(response.status_code)

    except (requests.exceptions.RequestException, AssertionError) as error:
        return loguru.logger.error('An error occured during the test: {error}'.format(error=error))

    # Check result (valid GeoJSON)
    feature_collection = json.loads(response.content)
    try:
        # feature_collection['type'] = 'Feature'
        FEATURE_COLLECTION_SCHEMA.validate(feature_collection)
    except SchemaError as error:
        if verbose is True:
            return loguru.logger.error('Invalid FeatureCollection: {error}'.format(error=error.autos))
        loguru.logger.error('The returned object is an invalid FeatureCollection. Some errors occured:')
        errors = list(filter(lambda error: error is not None, error.errors))
        for index, error_message in enumerate(errors):
            if error_message is not None:
                loguru.logger.error('\t{index}) {error}'.format(index=(index + 1), error=error_message))
        return None

    loguru.logger.success('The PROCESS end point ({}) successfully returned a result.'.format(endpoint))
    loguru.logger.success('{nb_features} polygons found.'.format(nb_features=len(feature_collection['features'])))
    return None

# Register commands
check.add_command(health)
check.add_command(process)

if __name__ == '__main__':
    check()
