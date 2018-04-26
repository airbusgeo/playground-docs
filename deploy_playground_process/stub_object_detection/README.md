# OneAtlas Playground Object Detection Processing stub

The processing stub provides a sample Python 2.7 project to implement a Playground tile process.

## Documentation

Documentation on how to implement a Playground process:

* [OneAtlas Playground Documentation](http://playground-docs.readthedocs.io/)
* [Geo Process API](http://playground-docs.readthedocs.io/en/latest/processing/geo_process_api/)

## Docker

Build the docker image :

```bash
docker build --rm -f Dockerfile -t playground-stub:object-detection .
```

Execute the container (redirect service port to 8000 on the host) :

```bash
docker run --rm -p 8000:8080 playground-stub:object-detection
```

Call the service : (these should work)

```bash
curl http://localhost:8000/api/v1/describe
```

```bash
curl http://localhost:8000/api/config
```

```bash
curl http://localhost:8000/api/version
```


```bash
curl http://localhost:8000/api/openapi
```

Test service with an image :

```bash
./test.sh
```

Test service with an empty image (error) :

```bash
./test_error.sh
```
