# Introduction

OneAtlas Playground is a cloud environment to process images provided as tiles (in WMTS format). Processings can either be object detection, image segmentation or both as well as change detection. In that last case, the processing will apply on two tiles displaying the same location. If you wish to run your algorithm in OneAtlas Playground, you need to implement a specific API. 

# Implementing Geo Process Web-Service API

The process has to provide a REST web-service that implements the [Geo Process API](../airbus_ds/geo_process_api.md) official API. This API is an open specification that enables inter-operability of algorithms.

In OneAtlas Playground **all processes are synchronous**. This means that *the asynchronous interface of the Geo Process API is not used*. In a nutshell, only the following services must be implemented.

**GET /api/v1/openapi**

This service returns the OpenAPI specification of the Geo Process API in YAML format.

**GET /api/v1/describe**

This service provides generic process informations to OneAtlas Playground.

**GET /config**

This service provides specific informations to OneAtlas Playground.

**POST /jobs**

This service executes the process. The type of input data is described by the input property of the describe service. The result is stored in the format defined by the output property of the describe service.

# Using Templates

OneAtlas Playground defines several templates for the *describe* service.
Using the provided templates will facilitate the integration of a custom processes in OenAtlas Playground.

Templates are defined for the two main kind of processes that are supported by OneAtlas Playground:

* [Object Detection](../playground/process_object_detection.md)
* [Change Detection](../playground/process_change_detection.md)

# Details about input

Tiles are 8 bits RGB images of 256x256 pixels.

The process can ask for a padding of up to 256 pixels in the config endpoint. As a results the maximum size of a tile is 768x768 pixels.

Tiles are base64 encoded in a JSON document passed in the request body of the jobs endpoint.

# Details about output

When process output is defined as [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON), it must comply with the following characteristics :

* Root element has to be a 'FeatureCollection' with one or several 'Feature' objects.
* Feature geometry is expressed with (0,0) at the top left of the tile image with padding included.
* Feature properties may include 'category' and 'confidence'.
    * The 'category' property is used for tags, labels or classification results. Its value may be a string with several values separated by a comma or an array of strings.
    * The 'confidence' property value is a float between 0.0 and 1.0.

**Feature geometry example :**

* tile of 100x100 in red with a padding of 100
* the input tile image is 300x300
* the detected change in green of 20x15

The expected geometry is : `[[0, 0], [20, 0], [20, 15], [0, 15]]`

![Feature geometry example](../images/feature-geometry-sample.jpeg)
