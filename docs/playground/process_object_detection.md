# Introduction

[Geo Process API](geo_process_api.md) template specification for OneAtlas Playground object detection class of processes.

# Describe endpoint

This endpoint returns a JSON document that comply to the **tile-object-detection** Geo Process API [template](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/tile-object-detection-describe.json).

Replace `TBC` (to be completed) strings with correct values.

*Example :*

```json
{
    "name": "TBC",
    "title": "TBC",
    "family": "TBC",
    "version": "TBC",
    "description": "TBC",
    "organization": "TBC",
    "email": "TBC",
    "keywords": "TBC",
    "template": "tile-object-detection",
    "resources": {
        "cpu": TBC,
        "ram": TBC
    },
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
    "output": {
        "description": "Tile object detection GeoJSON. Root element has to be a 'FeatureCollection' with one or several 'Feature' objects. Feature geometry is expressed with (0,0) at the top left of the tile image padding included. Feature properties may be 'category' and 'confidence'. The 'category' property is used for tags, labels or classification results. It's value may be a string with several values separated by a comma or an array of strings. The 'confidence' property value is a float between 0. and 1.0.",
        "content": {
            "application/geo+json": {}
        }
    },
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
    "asynchronous": false,
    "_links": {
        "self": {
            "href": "TBC"
        },
        "execution": {
            "href": "TBC"
        },
        "config:": {
            "href": "TBC"
        },
        "version": {
            "href": "TBC"
        }
    }
}
```

# Config endpoint

This endpoint returns a JSON document that comply to the **tile-object-detection** [config schema](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/tile-object-detection-config.json).

*Example :*

```json
{
    "zoom" : [ 16 ],
    "padding" : 20
}
```

# Job endpoint

This endpoint executes the process.

## Input data

A JSON document that comply to the **tile-object-detection** [input schema](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/tile-object-detection-input.json).

*Example :*

```json
{
    "zoom": 16,
    "tileFormat": "image/jpeg",
    "tile": ""
}
```

With tile field containing a JPEG image base64 encoded.
Tiles are 8 bits RGB images of 256x256 pixels (without padding).

## Output data

A JSON document that comply to the [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) schema with the following characteristics :

* Root element has to be a 'FeatureCollection' with one or several 'Feature' objects.
* Feature geometry is expressed with (0,0) at the top left of the tile image padding included.
* Feature properties may be 'category' and 'confidence'.
    * The 'category' property is used for tags, labels or classification results. It's value may be a string with several values separated by a comma or an array of strings.
    * The 'confidence' property value is a float between 0. and 1.0.

*Example :*

```json
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[479.0, 351.0], [479.0, 319.0], [415.0, 319.0], [415.0, 351.0], [479.0, 351.0]]
            },
            "properties": {
                "category": "ship",
                "confidence": 0.9
            }
        }
     ]
}
```
