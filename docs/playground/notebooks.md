# Intelligence Playground Python Client

The Intelligence Playground can be accessed through [API](openapi.md). 

Please, check our [Python API Client](https://github.com/airbusgeo/playground-python-client) and examples Notebooks.

This repository contains a Python Library to easy connection to the Airbus Intelligence Playground API.
It also provide some example of requests organized by themes in Python Notebooks.

## Install the Playground API Python Library

First clone this repository:
```git clone https://github.com/airbusgeo/playground-python-client.git```

Then open a command shell, go to the repository folder and type the following command:
```pip install .```

This will install the Playground API Client in your local Python libraries.

## Get and store your API key

To connect to the API, you need to retrieve your API_KEYS from the OneAtlas website. Follow the simple steps below:

1. Visit this URL: https://data.api.oneatlas.airbus.com/api-keys
2. Click the **Create and API key** button
3. Enter a description for your API_KEY (e.g. Playground Keys)
4. Store the file in the same folder than this notebook and name it **api_key.txt**

Make sure to keep your **api_key.txt** safe! Do not include it in a public github repository for example :-)

The following script will then use this **api_key.txt** file to generate an ACCESS_TOKEN. We will store this ACCESS_TOKEN in HEADERS that we will send with each requests. The ACCESS_TOKEN has a timeout so we will create a function that renew the ACCESS_TOKEN when half of the timeout has expired. 

## Create the Playground Client in Python

Just import and create an instance of the PlaygroundClient object:

```python
# Connect to the Playground API
from playgroundclient import PlaygroundClient
play = PlaygroundClient()
```

You can start using the client immediately:

```python
# Logged in user
user = play.get_logged_user()
print("Logged as user: {} {}".format(user['firstname'], user['lastname']))
```
