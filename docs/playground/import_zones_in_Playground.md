<p style='text-align: center; color: red; font-size: 20px;'>To Import Zones in the Playground</p>

-----------------

##### Input Data :

For this example you need to have one (or more) json file, the dataset_id and the dataset_name. That have to be an existing dataset. If you have not an existing dataset you can see the *[creation dataset page](dataset_creation.md)*.

**To get the dataset id :**

It visible in the url page :

- In the object detection (or change detection) page : https://playground.intelligence-airbusds.com/apps/object-detection/**{project_id}**/edit/**{dataset_id}**

For the json files you have to give in the terminal the full folder path.

*Example of file format*:

```json
{
    "type": "FeatureCollection",
    "features": [
      {
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [3.0036664, 42.6940282],
              [3.0297375, 42.6940282],
              [3.0297375, 42.7062023],
              [3.0036664, 42.7062023],
              [3.0036664, 42.6940282]
            ]
          ]
        },
        "type": "Feature",
        "properties": {
          "image_id": "13df6070438089b7d7f2b531e5d4c14c88944a1b",
          "type": "zone",
          "image_2_id": null,
          "name": "job_2019-03-14_Test new tags"
        }
      },
      {
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [3.0071211, 42.7018738],
              [3.0114555, 42.7018738],
              [3.0114555, 42.7049645],
              [3.0071211, 42.7049645],
              [3.0071211, 42.7018738]
            ]
          ]
        },
        "type": "Feature",
        "properties": {
          "comment": null,
          "tags": "truck",
          "type": "record"
        }
      }
    ]
  }
```

##### 1. Implementation

To use this script you need to these components and url :

```python
import os
import json
import requests
import time
import base64

PLAYGROUND_IMPORT_URL = 'https://import-service.playground.airbusds-geo.com/api/imports'
```

**You have to execute the *[common step](connection_build_header_step.md)* (Connection & Build Headers).**

##### 2. Read config file

With the *input* you enter all data what you need :

```python
dataset = {}
dataset['id'] = input("Input target dataset_id: ")
dataset['name'] = input("Enter target dataset name: ")
folder = input("Input full path of folder containing files to import: ")
```

Then you read the files :

```python
files = os.listdir(folder)
for x in files:
    with open('{}/{}'.format(folder, x)) as i:
        import_file =  json.load(i)
```

##### 3. Launch Import Request

For all files you launch your request in two steps :

```python
payload = build_payload(dataset, import_file, count)
job = launch_request(payload)
count+=1
if job.status_code == 200:
  content = json.loads(job.content)
else:
  print('Job failed. Error {status_code}: {reason}'.format(status_code=job.status_code, reason=job.reason))
```

**First step** : The build_payload method enables you to get your imported data (zones and records) :

```python
def build_payload(dataset, import_file, count):
  payload = {}
  payload["dataset_id"] = dataset['id']
  payload["name"] = '{number} - {zone_name} - {dataset_name}'.format(
    number=count,
    zone_name=import_file['features'][0]['properties']['name'][0:60],
    dataset_name=dataset['name']
  )
  payload["filename"] = import_file['features'][0]['properties']['name']+'.json'
  b64_import_file = base64.b64encode(json.dumps(import_file).encode())
  payload["file"] = b64_import_file.decode('UTF-8')
  return payload
```

**Second step** : The launch_request method enables you to send the request with the imported data (POST request) :

```python
def launch_request(payload):
  response = requests.post(
    url=PLAYGROUND_IMPORT_URL,
    data=json.dumps(payload),
    headers=HEADERS)
  return response
  pass
```
