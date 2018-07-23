# Introduction

[Geo Processes Manager API](geo_processes_manager_playground.md) template specification for OneAtlas Playground change detection class of processes.

# Job endpoint

This endpoint creates and executes a job.

## Input data

A JSON document that comply to the **change-detection** [input schema](https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/job-change-detection-input.json).

*Examples :*

Using an existing dataset :

```json
{
    "name": "My job on HongKong",
    "sourceId1": "DS_SPOT7_201806191033345_FR1_FR1_SV1_SV1_W003N37_01790",
    "sourceId2": "DS_SPOT6_201806181039596_FR1_FR1_SV1_SV1_W002N38_01871",
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
    "sourceId1": "DS_SPOT7_201806191033345_FR1_FR1_SV1_SV1_W003N37_01790",
    "sourceId2": "DS_SPOT6_201806181039596_FR1_FR1_SV1_SV1_W002N38_01871",
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
