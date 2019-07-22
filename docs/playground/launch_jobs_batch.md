# To Launch jobs Batch

-----------------

## Input Data

For this example you need to have one (or more) json file. That have to be an existing dataset. If you have not an existing dataset you can see the *[creation dataset page](dataset_creation.md)*. For the json files you have to give in the terminal the **full** folder path.

*Example of file format*:

```json
{
  "processes": [
    {
      "dataset_id": "dataset_id",
      "id": "process_id",
      "name": "process_name",
      "project_id": "project_id"
    }
  ],
  "zones": [
    {
      "id": 1,
      "image_id": "d98ab6c52efeeec3e8d46595c6897b28d5465c3b",
      "project": "NC_Kea Trader",
      "location": "Nouvelle Caledonie",
      "geom": {
        "type": "Polygon",
        "coordinates": [
          [
            [168.445696759259, -21.9644143518518],
            [168.817655092593, -21.9644143518518],
            [168.817655092593, -22.1155023148148],
            [168.445696759259, -22.1155023148148],
            [168.445696759259, -21.9644143518518]
          ]
        ]
      }
    }
  ]
}
```

## Implementation

To use this script you need to these components and url :

```python
import json
import requests
import time
import os

PLAYGROUND_JOB_URL = 'https://api.playground.airbusds-geo.com/api/v1/processes/{processId}/jobs'
```

**You have to execute the [common step]*(connection_build_header_step.md)* (Connection & Build Headers).**

## Read config file

With the *input* you enter the full folder path  :

```python
jsondir = input("Input full folder path: ")
```

Then you read the files and you get data in these files :

```python
for root, subdirs, files in os.walk(jsondir):
  for filename in files:
    processes, zones = get_data('{filepath}'.format(filepath=os.path.join(root, filename)))
    jobs_progress = {}
```

The *get_data* method enables you to get all processes and all zones witch are in the json file :

```python
def get_data(filepath):
  with open(filepath) as file:
    data = json.load(file)
  assert isinstance(data, dict), 'It should be a dictionnary'
  assert 'processes' in data.keys(), 'Should have processes list'
  assert isinstance(data['processes'], list), 'Processes should be a list'
  assert len(data['processes']) > 0, 'Processes list should not be empty'
  assert 'zones' in data.keys(), 'Should have zones list'
  assert isinstance(data['zones'], list), 'Zones should be a list'
  assert len(data['zones']) > 0, 'Zones list should not be empty'
  return data['processes'], data['zones']
```

## Launch Jobs

For all processes and for all zones you launch your request in two steps :

```python
for process in processes:
  jobs_progress[process['name']] = {}
  for zone in zones:
    payload = build_payload(process=process, zone=zone)
    job = launch_job(process=process, payload=payload)
    if job.status_code == 200:
      content = json.loads(job.content)
      key = '{zone_project}'.format(zone_project=zone['location'])
      jobs_progress[process['name']][key] = content['_links']['self']['href']
    else:
      print('Job failed. Error {status_code}: {reason}'.format(status_code=job.status_code, reason=job.reason))
    time.sleep(1)
```

**First step** : The *build_payload* method enables you to create your job data with the process data and zone data :

```python
def build_payload(process, zone):
  payload = {}
  payload['name'] = '{zone_name} - {process_name}'.format(
    zone_name=zone['location'][0:40],
    process_name=process['name']
  )
  if "image_2_id" in zone:
    payload['imageId'] = '{image_id}'.format(image_id=zone['image_id'])
    payload['imageId2'] = '{image_2_id}'.format(image_2_id=zone['image_2_id'])
  else :
    payload['imageId'] = '{image_id}'.format(image_id=zone['image_id'])
  payload['datasetId'] = '{dataset_id}'.format(dataset_id=process['dataset_id'])
  payload['projectId'] = '{project_id}'.format(project_id=process['project_id'])
  payload['geom'] = zone['geom']
  return payload
```

**Second step** : The *launch_job* method enables you to send the request with the job data (POST request) :

```python
def launch_job(process, payload):
  response = requests.post(
    url=PLAYGROUND_JOB_URL.format(processId=process['id']),
    data=json.dumps(payload),
    headers=HEADERS)
  return response
  pass
```