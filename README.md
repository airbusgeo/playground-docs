# Intelligence Playground

This project manages source code of the Intelligence Playground documentation, samples, stubs and tools.

* Documentation is automatically deployed on [Read the Docs](http://playground-docs.readthedocs.io/)
* Sample processing program in [stub](http://github.com/airbusgeo/playground-docs/tree/master/stub)
* OpenAPI [documentation](https://airbusgeo.github.io/geoapi-viewer/?url=https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/playground_geo_processes_manager_api.yaml) for API access to Playground, [Python API Client](https://playground-docs.readthedocs.io/en/latest/playground/notebooks/) and Jupyter Notebooks.

To create the documentation locally, run the following command:
```
mkdocs build --clean --site-dir build/html --config-file mkdocs.yml
```
