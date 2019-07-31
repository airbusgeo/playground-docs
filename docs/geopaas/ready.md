# When you are ready

Please provide us with the following information so we can hook up your service. Note that this step is not automatic, but the result of a person-to-person interaction and a manual intervention.

This information should also be available in the ```/api/v1/describe```end-point. If your are using the stub that is provided with this documentation, you should update the ```description.json```and, as such, you can also directly provide this file to us. 

* **Resolution:** The resolution at which you wish to receive imagery data, in meters-per-pixel. Example: 0.5 meters/pixel.

* **Image Padding:** If you are unable to operate in the image borders, provide the number of pixels where this happens. We only support services that require at the most 256 pixels of padding.

* **Image Size:** The width and height of a single image unit to process. Example: 256x256 or 1024x1024. Do not include eventual needed padding here; for example, if you request a 256x256 image with 10 pixels of padding, your endpoint will be receiving requests for images that are 276x276. There is no hard coded limit for the size of the imagery but think of the memory available on a GPU board!

* **HTTP endpoints:** URLs where we can access the healthcheck and processing endpoints (see paragraphs below for detailed description). These should be either in the form of ```http://localhost:port/path``` if you are providing a docker service, or a fully compliant ssl endpoint of the form ```https://myserver.tld/path/to/processing``` if you are hosting yourself.

* **Concurrency:** How many requests you are able to process concurrently.

* **Processing Duration Estimation:** An estimate of how many seconds of processing are needed for a single image unit.
