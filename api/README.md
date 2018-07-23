# OneAtlas Playground API

API specifications for OneAtlas Playground.

See [documentation](http://playground-docs.readthedocs.io/).

## Airbus Defence and Space Geo APIs

### Geo Process API

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API to be implemented by processing components that plugs to the Playground.
Provided as [OpenAPI](https://en.wikipedia.org/wiki/OpenAPI_Specification).

### Geo Processes Management API

[REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API that allows external applications that are allowed to manage processes and job execution by the Playground.
Provided as [OpenAPI](https://en.wikipedia.org/wiki/OpenAPI_Specification).

## Playground Geo API implementations

### Geo Process API templates

Templates specifies Geo Process API for a kind of process.

* Object detection
* Change detection

Templates are provided as JSON schemas for the following endpoints:

* Geo Process API describe endpoint
* Geo Process API config endpoint
* Input of Geo Process API jobs endpoint
* if no output of Geo Process API jobs endpoint, GeoJSON with a FeatureCollection is expected

### Geo Processes Management API implementation and templates

OneAtlas Playground adds the concept of project to the core Geo Processes Manager API by extending it.

Templates specifies Geo Processes Manager API job input for a kind of process.

* Object detection
* Change detection

Templates are provided as JSON schemas for the following endpoints:

* Input of Geo Processes Manager API jobs creation endpoint
