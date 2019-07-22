# To Export Zones from the Playground

-----------------

## Input Data

For this example you need to have the project_id and the dataset_id.
You have to give the complete path of a json file to write all exported zones.

**To get the project id and the dataset id :**

It visible in the url page :

- In the project page : https://playground.intelligence-airbusds.com/apps/**{project_id}**/datasets
- In the object detection (or change detection) page : https://playground.intelligence-airbusds.com/apps/object-detection/**{project_id}**/edit/**{dataset_id}**

## Implementation

To use this script you need to these components and url :

```python
import requests
import json

PLAYGROUND_API_URL = 'https://playground.intelligence-airbusds.com/api/zones?project_id={projectId}&dataset_id={datasetId}'
```

**You have to execute the *[common step](connection_build_header_step.md)* (Connection & Build Headers).**

## Get "input" data

With the *input* you enter all data what you need :

```python
zones=[]

project_id = input("Input project ID: ")
dataset_id = input("Input dataset ID: ")

output_path = input("Enter full output file path: ")
```

## Launch Export Request

You can launch your request with the PLAYGROUND_API_URL :

```python
response = requests.get(PLAYGROUND_API_URL.format(projectId=project_id, datasetId=dataset_id), headers=HEADERS)

assert response.status_code == 200, 'A problem occured during connection with the Playground'
```

## Write exported zones in a json file

To write the exported zones in a file you use the output_path (in step 2).

```python
rjson = response.json()
for item in rjson:
    zones.append(item)

json_data = {"zones": zones}

with open(output_path, "w",) as jsonfile:
    jsonfile.write(json.dumps(json_data))
```
