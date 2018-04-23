# Parsing OneAtlas Playground Data

The data exported from One Atlas Playground is following a specific file structure due to the way data is exported from the Platform. 

You will find below the necessary information that is needed to parse the data from a Playground Export.

## Export filestructure

The OneAtlas Playground exports its data with a certain format that can be represented with the following file structure:

```
export-job-name
|_ export-job-name.json
|_ dataset-id-1
    |_ dataset-id-1.json
    |_ labels
        |_ zone-id-1
            |_ tile-id-1.json
            |_ tile-id-n.json
            |_ (...)
        |_ zone-id-n 
        |_ (...)
    |_ samples
        |_ zone-id-1
            |_ image-id-1
                |_ tile-id-1.jpg
                |_ tile-id-n.jpg
                |_ (...).json
            |_ (...)
        |_ zone-id-n 
        |_ (...)
|_ dataset-id-n
    |_ (...)
```

### Export-Job

An Export-Job is an export task ordered by an user. it can contains several datasets and has several properties such as the padding with which tiles are exported.

The export-job properties as well as its list of datasets is summarized in the json file at its root.

```json
export-job-name/export-job-name.json
{  
   "targetZoom":16,
   "onlyTilesWithData":false,
   "onlyTilesInsideZone":false,
   "jobName":"test-export",
   "creationDate":"2018-04-19T14:38:29.279070+00:00",
   "datasetIds":[  
      "7800f9a5-03fc-4a4f-946e-6420e7064576"
   ],
   "tilesPadding":0
}
```

### Dataset

A Dataset is essentially a list of labelled area of interests, or "zones" that have been put under the same "namespace", usually because they are related to in either labelling type or geographical location.

A dataset is described by its json file that indicates:
- Each zone of interest in the dataset,
- The list of all the images corresponding to each zone of interest,

```json
export-job-name/dataset-id/dataset-id.json
{  
   "targetZoom":16,
   "zoneIds":[  
      "89c6fae0-da82-40cf-8ee3-39a8d7d763d2",
      "abaaf23e-fb88-496b-b9ee-4fa3afd370ba"
   ],
   "imageIds":[  
      [  
         "f2df7de4e2e5",
         "f24c55b545b2"
      ],
      [  
         "f2df7de4e2e5"
      ]
   ],
   "onlyData":false,
   "jobName":"test-export",
   "tilesPadding":0,
   "onlyInside":false,
   "creationDate":"2018-04-19T14:38:29+00:00",
   "datasetId":"7800f9a5-03fc-4a4f-946e-6420e7064576"
}

```
The dataset directory has the following file structure
``` 
dataset-id/
|_ dataset-id.json
|_ labels
    |_ zone-id-n/
        |_ tile-id-n.json
|_ samples
    |_ zone-id-n/
        |_ image-id-1/
            |_ tile-id-n.jpg
```

### Zone (or Area of Interest) and Tiles

An "Area of Interest" or "Zone" can be summarized as a list of [web map tiles](https://en.wikipedia.org/wiki/Tiled_web_map) at a certain geographical location and specific satellite images.

The tile-id represents an unique geographical location, and due to the nature of the data being exported, each tile can "regard" one or several images that are uniquely represented by their image-id. The couple (tile-id,image-id) uniquely represents a web map tile for a specific satellite image.

With those tiles are associated labels that are represented as a [Geojson FeatureCollection](https://macwright.org/2015/03/23/geojson-second-bite) object where the Features' coordinates are tile-wise.

Each tile is a 256x256 px jpg or png image associated with a specific satellite image at a specific geographical location. If the export concerns change detection data, a "tile" represented by one groundtruth FeatureCollection as well as several images. Due to the nature of tiling, the vectors represented in the label file can be applied to every tile at this location.

Example:

For a simple object detection data export, there will only be one image concerned by a single tile groundtruth (feature collection)

```
dataset-id/
|_ dataset-id.json
|_ labels
    |_ zone-id-n/
        |_ tile-id-n.json
|_ samples
    |_ zone-id-n/
        |_ image-id-1/
            |_ tile-id-n.jpg
```

For a change detection data export there will be two images:


```
dataset-id/
|_ dataset-id.json
|_ labels
    |_ zone-id-n/
        |_ tile-id-n.json
|_ samples
    |_ zone-id-n/
        |_ image-id-1/
            |_ tile-id-n.jpg
        |_ image-id-2/
            |_ tile-id-n.jpg
```

Each zone is linked to those two image-ids, and each tile data is composed of the tile-id json groundtruth and the two tile-id jpeg images.

The geojson groundtruth file as the following structure:

```json
{  
   "type":"FeatureCollection",
   "features":[  
      {  
         "geometry":{  
            "type":"Polygon",
            "coordinates":[Image-wise coordinates. Top left is (0,0)]
         },
         "type":"Feature",
         "properties":{  
            "kept_percentage":1.0,
            "state":"ADDED",
            "dataset_id":"7800f9a5-03fc-4a4f-946e-6420e7064576",
            "tags":"test"
         }
      },
      {  
         "geometry":{  
            "type":"Polygon",
            "coordinates":[Image-wise coordinates. Top left is (0,0)]
         },
         "type":"Feature",
         "properties":{  
            "kept_percentage":0.68712486780730231,
            "dataset_id":"7800f9a5-03fc-4a4f-946e-6420e7064576",
            "tile_id":"8a18b0a21586",
            "mask":"data",
            "zone_id":"89c6fae0-da82-40cf-8ee3-39a8d7d763d2"
         }
      }
   ]
}
```

For each tile, the FeatureCollection will have all groundtruth vectors that intersects this tile as well as a specific Feature with the property "mask" corresponding to the part of the tile that has been labelled.

For each Feature in the FeatureCollection, the scalar "kept_percentage" measures the area of the polygon in the tile compared to its original area (if the polygon is on several tile, kept_percentage < 1.)

## Python Utils

You can find a python parser with the relevant classes as well as an example notebook in the [One Atlas Playground repository](https://github.com/airbusgeo/playground-docs).
The `playground_utils` package contains base classes as well as a parser and you can find a notebook showing you how to view data at `notebooks/`