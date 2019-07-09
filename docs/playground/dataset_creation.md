<p style='text-align: center; color: red; font-size: 20px;'>To create a new dataset</p>

-----------------

##### Input Data :

For this example you need to have the project_id from an existing project.
You have to give the dataset informations : name and description.

##### 1 - Implementation

To use this script you need to these components and url :

```python
import json
import requests

PLAYGOUND_DATASET_URL = "https://api.playground.airbusds-geo.com/api/v1/datasets"
```

**You have to execute the [common step](connection_build_header_step.md) (Connection & Build Headers).**

##### 2. Get "input" data

With the *input* you enter all data what you need :

```python
project_id = input("Input the project id f an existing project : ")
dataset_name = input("Input the dataset name : ")
description = input("Input the dataset description : ")
```

##### 3. Launch the POST request

To launch your request you have to get all input data and ou have to put them in the method following method :

```python
response = create_new_dataset(project_id, dataset_name, description, HEADERS)

def create_new_dataset(projectID, databset_name, description, headers):
    playload = {
        "projectId": projectID,
        "name": databset_name,
        "description": description
    }
    response_obj = requests.post(PLAYGOUND_DATASET_URL, data=json.dumps(playload), headers=headers)
    if response_obj.status_code != 200:
        raise Exception("The request failed, got a {}".format(response_obj.status_code))
    response = json.loads(response_obj.content.decode())
    return response["datasetId"], response
```
