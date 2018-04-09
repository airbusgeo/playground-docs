# OneAtlas Playground API

API specifications for OneAtlas Playgroud.

See [documentation](http://playground-docs.readthedocs.io/).

**Geo Process API**

REST API to be implemented by processing components that plugs to the Playground.
Provided as OpenAPI.

**Playground templates**

Templates specifies Geo Process API for a kind of process.

* Object detection
* Change detection

Templates are provided as JSON for the following interfaces :

* Geo Process API describe endpoint
* Geo Process API config endpoint
* Input of Geo Process API jobs endpoint
* if no output of Geo Process API jobs endpoint, GeoJSON with a FeatureCollection is expected
