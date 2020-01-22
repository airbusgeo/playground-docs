# Useful scripts

## Validate endpoint locally

First install the required libraries in you local virtual environment.
```pip install click loguru requests schema```

To test health check:
```python test_algo.py health```

To test process:
```python test_algo.py process --tile-path /path/to/storage_tank/test_512-512.tif --resolution 1.5```

By default, it checks end-points as defined in the ```stub```but you can changev this behavior by adding the option --endpoint http://0.0.0.0:8080/custom/route/health.

If you do not provide a tile with the ```tile_path``` argument, it creates a black tile with the dimensions as specified by ```tile_width``` and ```tile_height```.