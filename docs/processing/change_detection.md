# Introduction

Description of the Playground [Geo Process API](geo_process_api.md) for change detection class of processes.

# Describe service

This service returns a JSON document that comply to the **tile-change-detection** Geo Process API [template](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/tile-change-detection-describe.json).

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
    "template": "tile-change-detection",
    "resources": {
        "cpu": TBC,
        "ram": TBC
    },
    "input": {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "tile-change-detection-input",
        "description": "Geo Process API input schema for tile change detection",
        "type" : "object",
        "required": [
            "zoom",
            "tile1Format",
            "tile1",
            "tile2Format",
            "tile2"
        ],
        "properties": {
            "zoom": {
                "description": "Tile zoom level",
                "type": "integer",
                "minimum": 1,
                "maximum": 20
            },
            "tile1Format": {
                "description": "MIME type of the first tile image format (image/png or image/jpeg)",
                "type": "string"
            },
            "tile1": {
                "description": "The first tile image base64 encoded, may be JPEG or PNG format",
                "type": "string",
                "format": "base64"
            },
            "tile2Format": {
                "description": "MIME type of second tile image format (image/png or image/jpeg)",
                "type": "string"
            },
            "tile2": {
                "description": "The second tile image base64 encoded, may be JPEG or PNG format",
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
        "description": "Tile change detection GeoJSON. Root element has to be a 'FeatureCollection' with one or several 'Feature' objects. Feature geometry is expressed with (0,0) at the top left of the tile image padding included. Feature properties may be 'category' and 'confidence'. The 'category' property is used for tags, labels or classification results. It's value may be a string with several values separated by a comma or an array of strings. The 'confidence' property value is a float between 0. and 1.0.",
        "content": {
            "application/geo+json": {}
        }
    },
    "config": {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "tile-change-detection-config",
        "description": "Geo Process API config schema for tile change detection",
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

# Config service

This service returns a JSON document that comply to the **tile-change-detection** [config schema](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/tile-change-detection-config.json).

*Example :*

```json
{
    "zoom" : [ 16 ],
    "padding" : 20
}
```

# Job service

This service executes the process.

## Input data

A JSON document that comply to the **tile-change-detection** [input schema](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/tile-change-detection-input.json).

*Example :*

```json
{
    "zoom": 16,
    "tile1Format": "image/jpeg",
    "tile1": "",
    "tile2Format": "image/png",
    "tile2": ""
}
```

With tile1 and tile2 fields containing a JPEG and PNG image base64 encoded.
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
