# Intelligence Playground processing stub

The stub provides a sample Python 3.6 project to implement a service that process an imagery tile to generate a GeoJSON with detected objects as polygons. It is based on [Sanic](https://github.com/huge-success/sanic) and [Docker](https://docs.docker.com/). 

## Documentation

Documentation on how to implement a process to run into Intelligence Playground:

* [Intelligence Playground Documentation](https://playground-docs.readthedocs.io/en/latest/geopaas/intro/)
* [Geo Processing API Specification](https://github.com/AirbusDefenceAndSpace/geoprocessing-api)

The main features of the processing service are:

* packaged as a ```Docker``` with associated ```description.json``` file
* only allows one single processing at a time
* still responds to health check while processing 

## Docker commands

Build the docker image :

```bash
docker build --rm -f Dockerfile -t stub .
```

Execute the container (redirect service port to 8000 on the host) :

```bash
docker run --rm -ti -p 8000:8080 stub
```

## Check endpoint 

Check that the service is alive:

```bash
curl http://localhost:8000/api/v1/health
```

Call the service description:

```bash
curl http://localhost:8000/api/v1/describe
```

Test service with an image:

```bash
./test.sh
```

Only one process can run at a given time. If the ```/api/v1/process``` end-point is called when a process is already running, the end-point will return a ```429``` error code.

Test service with an empty image (error):

```bash
./test_error.sh
```
