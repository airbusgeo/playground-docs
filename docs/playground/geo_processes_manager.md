<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="../stylesheets/swagger-ui.css" >
<style>
html
{
    box-sizing: border-box;
    overflow: -moz-scrollbars-vertical;
    overflow-y: scroll;
}
*,
*:before,
*:after
{
    box-sizing: inherit;
}

body {
    margin:0;
    background: #fafafa;
}
</style>

# API

<div id="swagger-ui"></div>

<script src="../scripts/swagger-ui-bundle.js"> </script>
<script src="../scripts/swagger-ui-standalone-preset.js"> </script>
<script>
window.onload = function() {
  const ui = SwaggerUIBundle({
    url: "https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/api_geo_processes_manager_playground.yaml",
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
    ]
  })

  window.ui = ui
}
</script>

# Object detection input

Template specification for OneAtlas Playground object detection class of processes.

A JSON document that comply to the **object-detection** [input schema](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/job-object-detection-input.json).

*Examples :*

Using an existing dataset :

```json
{
    "name": "My job on HongKong",
    "imageId": "DS_SPOT7_201806191033345_FR1_FR1_SV1_SV1_W003N37_01790",
    "geom": {
        "type": "Polygon",
        "coordinates": [[
            [-3.38992361111,37.4653125],
            [-2.67482638889,37.4653125],
            [-2.67482638889,36.9102847222],
            [-3.38992361111,36.9102847222],
            [-3.38992361111,37.4653125]
        ]]
    },
    "projectId": "ab4358f0-30f2-11e8-b467-0ed5f89f718b",
    "datasetId": "bb4358f0-30f2-11e8-b467-0ed5f89f718b"
}
```

While creating a new dataset :

```json
{
    "name": "My job on HongKong",
    "imageId": "DS_SPOT7_201806191033345_FR1_FR1_SV1_SV1_W003N37_01790",
    "geom": {
        "type": "Polygon",
        "coordinates": [[
            [-3.38992361111,37.4653125],
            [-2.67482638889,37.4653125],
            [-2.67482638889,36.9102847222],
            [-3.38992361111,36.9102847222],
            [-3.38992361111,37.4653125]
        ]]
    },
    "projectId": "ab4358f0-30f2-11e8-b467-0ed5f89f718b",
    "datasetName": "Ship detection 1"
}
```

# Change detection input

Template specification for OneAtlas Playground change detection class of processes.

A JSON document that comply to the **change-detection** [input schema](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/job-change-detection-input.json).

*Examples :*

Using an existing dataset :

```json
{
    "name": "My job on HongKong",
    "imageId1": "DS_SPOT7_201806191033345_FR1_FR1_SV1_SV1_W003N37_01790",
    "imageId2": "DS_SPOT6_201806181039596_FR1_FR1_SV1_SV1_W002N38_01871",
    "geom": {
        "type": "Polygon",
        "coordinates": [[
            [-3.38992361111,37.4653125],
            [-2.67482638889,37.4653125],
            [-2.67482638889,36.9102847222],
            [-3.38992361111,36.9102847222],
            [-3.38992361111,37.4653125]
        ]]
    },
    "projectId": "ab4358f0-30f2-11e8-b467-0ed5f89f718b",
    "datasetId": "bb4358f0-30f2-11e8-b467-0ed5f89f718b"
}
```

While creating a new dataset :

```json
{
    "name": "My job on HongKong",
    "imageId1": "DS_SPOT7_201806191033345_FR1_FR1_SV1_SV1_W003N37_01790",
    "imageId2": "DS_SPOT6_201806181039596_FR1_FR1_SV1_SV1_W002N38_01871",
    "geom": {
        "type": "Polygon",
        "coordinates": [[
            [-3.38992361111,37.4653125],
            [-2.67482638889,37.4653125],
            [-2.67482638889,36.9102847222],
            [-3.38992361111,36.9102847222],
            [-3.38992361111,37.4653125]
        ]]
    },
    "projectId": "ab4358f0-30f2-11e8-b467-0ed5f89f718b",
    "datasetName": "Change detection 1"
}
```
