# Endpoint Descriptions

Wether you are hosting the service yourself or providing a docker image implementing the service, you will need to implement two endpoints:

## Healthcheck endpoint

This endpoint should return an http 200 OK on GET requests once the service is ready to accept incoming processing requests. If this endpoint cannot be reached or does not return a 200 OK , the service will be considered as unhealthy and will not receive requests to process. Typically, if the service needs time to initialize at startup, the healthcheck endpoint should return a non-200 code until the initialization is over and requests can actually be served.

## Processing endpoint

This endpoint should accept POST requests and will receive requests containing an base64 encoded image payload embedded in a JSON document. The image you will receive will respect the specifications asked by your process, namely size and resolution. The payloads received by this endpoint are fixed and cannot be extended, if you require additional information this should be set in the URL (e.g.: ```https://service.tld/process?api_key=foo&version=1.0```)

### Detection/Segmentation Payloads

```json
{
	"resolution": 0.5,
	"tiles": ["base64encodedimagedata"]
}
```

If you want the end-point to support batching, it should be able to receive a single playload OR an array of payloads.

### Change-Detection Payloads

```json
{
	"resolution": 0.5,
	"tiles": [
		"base64encodedimagedatafortile1",
		"base64encodedimagedatafortile2"
	]
}
```

If you want the end-point to support batching, it should be able to receive a single playload OR an array of payloads.

# OpenAPI Specification

<div id="swagger-ui"></div>

<script src="../scripts/swagger-ui-bundle.js"> </script>
<script src="../scripts/swagger-ui-standalone-preset.js"> </script>
<script>
window.onload = function() {
  const ui = SwaggerUIBundle({
    url: "https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/tile-geo-process-api.yaml",
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
    ]
  })

  window.ui = ui
}
</script>