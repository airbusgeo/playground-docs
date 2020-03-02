# Useful scripts and tests

## Utility to validate an endpoint locally

### Installation 

First install the additional libraries in your Python local virtual environment.
```pip install click loguru requests schema```

### Usage

#### To test health check:
```python test_endpoint.py health```

By default the script will test the end-points on the local machine and on the standard expected URI (i.e. ```http://0.0.0.0:8080/health```) but you can modify this behavior by defining the following argument: ```--endpoint http://0.0.0.0:8080/custom/route/health```

#### To test process:
```python test_endpoint.py process --tile-path ../stub/data/tile.png --resolution 1.5```

If you do not provide a tile with the ```tile-path``` argument, you should provide the ```tile_width``` and ```tile_height``` arguments and the script will create a black tile with this dimensions. By default, ```tile_width``` and ```tile_height``` are 256.

