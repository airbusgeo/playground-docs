# Introduction

Description of the Playground [Geo Process API](https://airbusgeo.github.io/geoapi-viewer/?url=https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/api_geo_process_v1.0.0.yaml) for object detection class of processes.

# Describe service

This service returns a JSON document that comply to the [tile-object-detection](http://github.com/airbusgeo/playground-docs/master/api/tile-object-detection-describe.json) template.

Replace `#TODO#` string with correct values.

**Example :**

```json
{
    "name": "#TODO#",
    "title": "#TODO#",
    "family": "#TODO#",
    "version": "#TODO#",
    "description": "#TODO#",
    "organization": "#TODO#",
    "email": "#TODO#",
    "keywords": "#TODO#",
    "template": "tile-object-detection",
    "resources": {
        "cpu": #TODO#,
        "ram": #TODO#
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
            "href": "#TODO#"
        },
        "execution": {
            "href": "#TODO#"
        },
        "config:": {
            "href": "#TODO#"
        },
        "version": {
            "href": "#TODO#"
        }
    }
}
```

# Config service

This service returns a JSON document that comply to the [tile-object-detection](http://github.com/airbusgeo/playground-docs/master/api/tile-object-detection-config.json) config schema.

**Example :**

```json
{
    "zoom" : [ 16 ],
    "padding" : 20
}
```

# Job service

This service executes the process.

## Input data

A JSON document that comply to the [tile-object-detection](http://github.com/airbusgeo/playground-docs/master/api/tile-object-detection-input.json) input schema.

**Example :**

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

**Example :**

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
