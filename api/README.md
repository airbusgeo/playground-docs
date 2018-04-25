# OneAtlas Playground API

API specifications for OneAtlas Playgroud.

See [documentation](http://playground-docs.readthedocs.io/).

## Geo APIs

### Geo Process API

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API to be implemented by processing components that plugs to the Playground.
Provided as [OpenAPI](https://en.wikipedia.org/wiki/OpenAPI_Specification).

### Geo Processes Management API

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API that allows external applications that are allowed to manage processes and job execution by the Playground.
Provided as [OpenAPI](https://en.wikipedia.org/wiki/OpenAPI_Specification).

## Playground templates

Templates specifies Geo Process API for a kind of process.

* Object detection
* Change detection

Templates are provided as JSON for the following endpoints:

* Geo Process API describe endpoint
* Geo Process API config endpoint
* Input of Geo Process API jobs endpoint
* if no output of Geo Process API jobs endpoint, GeoJSON with a FeatureCollection is expected
