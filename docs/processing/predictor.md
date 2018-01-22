# Introduction

OneAtlas Playground allows to process tile images in order to detect objects, changes ...

The predictor has to provide a web-service with a specific API.

# Web-Service API

The predictor API implements a REST web-service with the following services:

* describe
* predict

An OpenAPI documentation is also available [here](https://airbusgeo.github.io/geoapi-viewer/?url=https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/process-api.yaml).

## describe service

This service provides informations and parameters to the Playground:

* padding : tile padding / border (0 to 256)
* nb_tiles : number of tiles for each processing (1 or 2)

## predict service

The predict service processes one or two tiles then returns the result.

**Input**

Tiles are 8 bits RGB images of 256x256 pixels.

They are base64 encoded in a JSON document passed as the body request:

```json
{
    "tile_1" : "...",
    "tile_2" : "..."
}
```

**Result**

Expected result is a JSON document. If the process execution has *no error*:

```json
{
    "status" : "DONE",
    "type" : "application/geo+json",
    "result" : ...
}
```

The result field must contain a [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) **MultiPolygon** object.


If the process execution *has an error*:

```json
{
    "status" : "ERROR",
    "error" : "error message"
}
```

