# Expected Output

## Successful Output

A successful result MUST be returned with a 200 OK.

The output body follows the principles of [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON), it must comply with the following characteristics :

* Root element MUST be a 'FeatureCollection' with one or several 'Feature' objects. Currently only Polygon, Multipolygon, and Point features are supported.
* Geometries MUST be topologically correct (i.e. no degeneracies or self-intersections)
* Geometry coordinates are given in pixel space, with (0,0) at the top left of the image. If you have requested padding, features that intersect the padding area will **not** be discarded on our end.
* Feature properties MAY include 'category' and 'confidence'.
    * The 'category' property is used for tags, labels or classification results. Its value MUST be an array of strings.
    * The 'confidence' property value MUST be a float between 0.0 and 1.0.

**Feature geometry example :**

![Feature geometry example](../images/geopaas-geometry-sample.jpeg)

* service requested an image of 256x256 with a padding of 5
* the input image is 266x266
* the detected change drawn in green does not overlap the padding area
* the detected change drawn in blue overlaps the padding area

The result in this case would be:

```json
{
	"type":"FeatureCollection",
	"features": [
		{
			"type":"Feature",
			"properties": {"category":["building"]},
			"geometry": {
				"type": "Polygon",
				"coordinates": [[[10,5],[10,105],[103,105],[103,5],[10,5]]]
			}
		},
		{
			"type":"Feature",
			"properties": {"category":["road"]},
			"geometry": {
				"type": "Polygon",
				"coordinates": [[[240,220],[240,266],[266,266],[266,220],[240,220]]]
			}
		}
	]
}

```

## Unsuccessful Output

The service should return a body of the following format if it wishes to inform of a permanent processing error for the current image:

```json
{
	"message":"a goblin ate my GPU!",
	"hint":"(optional) message to prevent this error from happening again"
}
```

If the service is unable to produce a result or a correctly formatted error, the 408, 423, 429, 500, 502, 503 and 504 HTTP
return codes will be interpreted as transient errors and will be retried in a later subsequent request. All other HTTP
status codes will be interpreted as permanent.



