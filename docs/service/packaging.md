# Preparing your Service

This section will:

- Introduce the code prerequisites to interface a service with the playground
- Provide you with a code example

## Developing a predictor on OneAtlas Imagery

!!!warning
    The core concept of OneAtlas is that it can iterfaces itself with any service that from a **OneAtlas Tile** (which is a 256x256 px image at any zoom taken from any OneAtlas image) returns a result, preferably in **vector form**.

Any service deployed on OneAtlas Playground will implement the following logic:

```python
# input_tile is a "Tile" requested by the API
prediction = predictor.predict(input_tile)
# prediction is a geojson FeatureCollection containing predictions information for this Tile
```

You will be able to specify a zoom level and padding for your 256 x 256 tile but the principle stay the same.

## Service Interface with the playground

### Wrapping

Your predictor will be wrapped into a Flask application that will call the predictor when it receives Tiles to predict. The OneAtlas service deployment App will manage the Tile fetching and decoding as well as formatting the output to geojson.

Basically, the Flask application will import the `predictor_package.predictor_module.predictor_class` and call it when it receives a Tile. It will then receive either a`playground_interfaces.PredictionResult`or a `geojson.FeatureCollection` and will pass the necessary information through google pubsub.

### Expected file structure

The final structure of your predictor inside the docker image should then be:

```text
/api/
    |_predictor_package/
        |_ __init__.py # example: from .predictor_module import Predictor
        |_ predictor_module.py
            |_ class Predictor(BaseProcess) # Just an example
        |_ (other files, packages etc you may need)
```

We will then append the following files with our wrapper image:

```text
/api/
    |_app.py # App generated playground-side
    |_app.yaml # App Config generated playground-side
    |_app_utils.py # utils called by app
    |_gunicorn.conf.py # Gunicorn config generated playground-side
```

So that the `predictor` implementing the "abtract class" `BaseProcess` is importable from `app.py`.

## The playground_interfaces package

We make available a package named [playground_interfaces](https://storage.googleapis.com/oneatlas_playground_utils/playground_interfaces-0.2.tar.gz) that contains the classes used by the services.

It is available at:

```text
pip install https://storage.googleapis.com/oneatlas_playground_utils/playground_interfaces-0.2.tar.gz
```

## Code prerequisites

Integrating a service on OneAtlas Playground requires developing a predictor compatible with the Playground Services App.

```python
Output = Predictor.predict(Input)
```

### Predictor (Function)

Namely, your predictor should implement the BaseProcess abstract class from `playground_interfaces`

```python
from geojson import Feature, FeatureCollection, Polygon
from abc import ABCMeta, abstractmethod
import numpy as np
import urlfetch
import io
from .tile import Tile
from .prediction_result import PredictionResult


class BaseProcess:
    """
    This is the base interface for a predictor taking a single tile as input
    You should register your predictor class BaseProcess.register(your_predictor_class)
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        """
        Init the predictor. This function is called during the service initialization by the API
        """
        pass

    @abstractmethod
    def predict(self, tile):
        """
        The API calls this function for each tile it receives

        Args:
            tile (Tile): A tile

        Returns:
            PredictionResult
        """
        prediction = PredictionResult(tile)
        return prediction
```

### Tile (Input)

A Tile is the container for the 256x256 (+padding) image to be passed to the predictor.

```python
class Tile(object):
    """
    This is the Tile class containing the url and image to be passed to the predictor
    """

    def __init__(self, url, img_array):
        """
        Initialize a tile from an URL and the corresponding urlfetched bytearray

        To read an image:
        in opencv: (returns a BGR image)
        tile_array = cv2.imdecode(np.asarray(tile.image, dtype=np.uint8), 1)

        in PIL: (returns an RGB image)
        img_pil = Image.open(io.BytesIO(tile.image))
        img_pil = np.asarray(img_pil, dtype=np.uint8) if decode to numpy array

        Args:
            url (string): The Tile Url
            img_array (bytearray): The bytearray containing the image
        """
        self.image = img_array
        self.url = url
```

### Prediction Result (Output)

The predictor can return either:

- A `PredictionResult` object that is populated with the list of results (see below) using `add_result`. You may call `.format()` to return a FeatureCollection hower this is not mandatory as the Flask App will do it.

- A Feature collection where **each feature must implement**  the property `category`

```python
from geojson import Feature, FeatureCollection, Polygon
from .tile import Tile
import numpy as np


class PredictionResult(object):
    """
    This is the result class containing all objects detected in a Tile.
    """

    def __init__(self, tile):
        """
        Initialize the PredictionResult object. Should be called and populated by the predictor.
        Args:
            tile (Tile): The Tile used for prediction
        """
        self.tile = tile
        self.list_results = []

    def add_result(self, category, bbox, confidence=1.0):
        """
        Add result (object) in the list_results attribute. Should be called by the predictor when populating the result for a tile.
        Args:
            category (string): The class of each object
            bbox (list): The bbox in the form of a list of coordinates that can be called using Polygon([bbox])
            confidence (float): The score or confidence for each object (float

        Returns:

        """
        self.list_results.append((category, bbox, float(confidence)))

    def format(self):
        """
        Formats the list_result in geojson format
        Returns: A geojson FeatureCollection

        """
        geo_results = []
        for cat, bbox, conf in self.list_results:
            pol = Polygon([bbox])
            # Rounding coordinates just in case, since these are local...
            pol['coordinates'] = np.round(np.array(pol['coordinates']),
                                          2).tolist()
            geo_results.append(
                Feature(
                    geometry=pol,
                    properties={"category": cat,
                                "score": round(conf, 2)}))
        return FeatureCollection(geo_results)

```

## Example code

Here is a simple example code that uses Tile, PredictionResult and BaseProcess

```python
from playground_interfaces import Tile, PredictionResult, BaseProcess


class Process(BaseProcess):
    """"
    Example Process Class that must be implemented as predict.py in root
    """

    def __init__(self):
        super(Process, self).__init__()

    def predict(self, tile, debug=False):
        my_result = PredictionResult(Tile(tile))
        my_result.add_result("roi", [(0.0, 0.0), (1.0, 1.0), (1.0, 0.0),
                                     (0.0, 0.0)], 1.0)
        my_result.add_result("ior", [(0.1, 0.1), (1.1, 1.1), (1.1, 0.1),
                                     (0.1, 0.1)], 0.5)
        # There is no need to call my_result.format()
        return my_result


BaseProcess.register(Process)
```

A simple workflow reproducing what your predictor will encounter is available here: `playground_interfaces/example`

You can script your test code and run it when building your docker.

```python
from playground_interfaces import Tile, PredictionResult, BaseProcess

def test():
    import traceback
    import urlfetch
    import io
    predictor = Process()

    urls = [
        "https://storage.googleapis.com/oneatlas_playground_utils/tile_1.jpg",
        "https://storage.googleapis.com/oneatlas_playground_utils/tile_2.jpg",
        "https://storage.googleapis.com/oneatlas_playground_utils/tile_3.jpg",
        "https://storage.googleapis.com/oneatlas_playground_utils/tile_4.jpg",
        "https://storage.googleapis.com/oneatlas_playground_utils/tile_5.jpg",
    ]

    for url in urls:
        try:
            result = urlfetch.get(url)
            result_content = result.content
            io_content = io.BytesIO(result_content)
            img_array = bytearray(io_content.read())
            tile = Tile(url, img_array)
            prediction = predictor.predict(tile)
            assert isinstance(prediction, PredictionResult)
            prediction.format()
            print("Passed for url %s" % url)
        except:
            print("Not passed for url %s" % url)
            exc = "Failure \n"
            exc += traceback.format_exc()
            print(exc)

```
