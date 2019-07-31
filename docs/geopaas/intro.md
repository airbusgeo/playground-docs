# Introduction

The Intelligence Playground is a cloud environment to run machine learning algorithms on satellite images. To add a custom algorithm to the Intelligence Playground, you can either reference an external end-point or submit a Docker image. In both case, you will need to implement a specic API that is described in the following page.

Intelligence Playground image processing services are based on tiles (along with the WebMercator and Squared Pixel grids). When a processing is applied to an image, each single tile that is part of the image is processed and all results are merged together. This is why you need to specify at which resolution the processing should be applied.

Jump to [End-points description](specs.md).

# Reference an external processing

If you wish to make your algorithm available in the Intelligence Playground but prefer hosting the processing by yourself note that your end-point should allow some scalability. When you are ready, just provide the end-points to us by following [this page](ready.md).

# Deploy a processing as a Docker

Alternatively, you can deliver to us a Docker image which implement the same API and end-points. In that case, you only have to provide the location of a Docker container in a Docker registry, the Intelligence Playground takes care of the rest! When you are ready, just provide the end-point URLs to us by following [this page](ready.md).

For your convenience, we have provided a sample Docker application implementing this specification. You can check it up [here](https://github.com/airbusgeo/playground-docs/tree/master/stub).
