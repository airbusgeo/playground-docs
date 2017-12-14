# Deploying Docker Image on the Playground

The following section will provide you with:

- How external services are interfaced with the Playground
- A presentation of Google App Engine
- The configuration prerequisites to deploy your service image
- Insights on testing your image
- A note on service Deployment

## Deployment Process

!!! note "Automated Deployment"
    Currently the deployment process is essentially managed by the OneAtlas Playground team. Automated integration tools and per-project mangement is under development.

As stated in the previous pages, the service deployment process follows several steps:

1. The developer, partner or data scientist push the service's docker image on a public docker hub or the GCP Container Registry
1. The image location (ex. `eu.gcr.io/theplayground_repo/my_service:latest`) is sent to the playground team
1. Additional configuration options are sent to the OneAtlas team (see below)
1. The OneAtlas Playground team generates the necessary config files and wraps the Docker image inside the docker

## Google App Engine Flex

We use [GAE Flex environment](https://cloud.google.com/appengine/docs/flexible/) to deploy OneAtlas Playground Applications.

Based on Google Compute Engine, the App Engine flexible environment automatically scales your app up and down while balancing the load. Microservices, authorization, SQL and NoSQL databases, traffic splitting, logging, versioning, security scanning, and content delivery networks are all supported natively. In addition, the App Engine flexible environment allows you to customize the runtime and even the operating system of your virtual machine using Dockerfiles.

## Configuration Prerequisites

### Checking your Image for deployment

!!! note "This section is FIY only"

    The playground team will for the moment handle the integration process so the following section is FIY-only. All the files below are generated playground-side, the playground team does not require you to generate any configuration file.

The integration Dockerfile:

```Dockerfile
ARG base_id
# Base image is your dockerfile
FROM $base_id:latest

# Do App Related Stuff
EXPOSE 8080
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt
COPY ./app/* /api/

WORKDIR /api/

# Start App
CMD ["gunicorn", "--config", "/api/gunicorn.conf.py", "app:APP"]
```

The final structure of the `/api/` folder will be:

```text
/api/
    |_predictor_package/
        |_predictor_module.py
            |_ predictor(BaseProcess)
    |_app.py
    |_app.yaml # App Config generated playground-side
    |_app_utils.py # utils called by app. Not relevant
    |_gunicorn.conf.py # Gunicorn config generated playground-side
```

The `app.yaml` configuration file will contain the following information that you will need to provide.

```yaml
PREDICTOR_CLASS: Your_Predictor_Class
PREDICTOR_PACKAGE: Your_Predictor_Package (or package.module if class is not importable from package)
PROJECT_NAME: (Not specified by partners: The project where it will be deployed)
```

The `app.py` script will interfaces itself by calling predictor.predict() on a Tile and formatting the corresponding PredictionResult

```python
result_prediction = PROCESS.predict(tile)
# Format results
if isinstance(result_prediction, PredictionResult):
    response['prediction'] = result_prediction.format()
elif isinstance(result_prediction, FeatureCollection):
    response['prediction'] = result_prediction
else:
    result_prediction['prediction'] = FeatureCollection()
```

In order to know which predictor to import, it will lookup its yaml configuration and import relevant data:

```python
# Import the target package
target_module = importlib.import_module(CONFIG.PREDICTOR_PACKAGE)
Process = getattr(target_module, CONFIG.PREDICTOR_CLASS)
PROCESS = Process()
```

### Additional information to be provided:

!!! note

    As stated earlier, the configuration files generation is done playground-side. We formatted the information below in YAML for clarity purposes but we do not require, for now, that the config files are already present in your docker image.

You will need to provide the integration team (for example with a readme sent by e-mail) with the following information when providing your docker:

Docker image: Your docker image url

Tile Engine Configuration:

```yaml
ZOOM_LEVEL: 16 # Your required zoom level
PADDING: 24 # Your required padding around the tile
```

Application configuration:

```yaml
PREDICTOR_CLASS: Your_Predictor_Class
PREDICTOR_PACKAGE: Your_Predictor_Package.YourPredictor_Module (if class is not available from package)
```

App Engine Deployment configuration: This is the basic App Engine Flex configuration that is used. Please specify if your application needs more resources

```yaml
resources:
  cpu: 4
  memory_gb: 3.2
  disk_size_gb: 10
```

Gunicorn server configuration: We use the following gunicorn server configuration. Please specify if you would like to change the number of workers.

```python
workers = 2
backlog = 6
timeout = 60
```

## Deploying your service

!!! note

    This section is just FIY only

Once you will have provided the OneAtlas Playground team with every necessary information we will:

- Wrap the predictor base image with the playground container
- Do some integration tests (mainly POST requests to the Flask Application)
- Generate the necessary configurations with the provided information (see above)
- Deploy the service

You will then have access to the service on OneAtlas Playground
