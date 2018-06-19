![OneAtlas Playground](images/logo.png "OneAtlas Playground")

An Open Platform to Create New Innovative Services from Satellite Imagery.

For more informations, go to the [official website](https://sandbox.intelligence-airbusds.com/web/).

You will find here documentation regarding:

* Using the OneAtlas Playground Web Interface (coming soon)
* Deploying a processing on OneAtlas Playground

# Introduction

OneAtlas Playground is a development platform for imagery processing services based on OneAtlas data. The core objective of OneAtlas Playground is to provide a "sandboxed" environment connected to OneAtlas imagery in order to develop, deploy and test image processing services in a cloud environment. By taking care of data connection, deployment and scalability, it enables data scientists to concentrate on their jobs. In particular, it has been designed to facilitate the development of machine learning algorithms by making it easy to upload a predictor, run inference on large quantities of data, validate each records, benchmark the overall preformance and generate new updated datasets for training.


# Concepts

OOneAtlas Playground image processing services are based on tiles (along the WMTS Geographic and Mercator grids). When a processing is applied to an image, each single tile that is part of the image is processed and all results are merged together. This is why you need to specify at which zoom level (i.e. resolution) the processing should be applied. OneAtlas Playground relies on the Google Cloud Platform components. 


# Deployment

Abstracting away the deployment of image processing services is done by deploying Docker containers on Google Kubernetes Engine or others cloud providers. As a user, you only have to provide the location of a Docker container in a Docker registry, OneAtlas Playground takes care of the rest!

# Tagging and labelling

OneAtlas Playground offers a web interface to create datasets using OneAtlas images via labelling and detouring of objects on satellite images. It also enables to edit and iterate on datasets by using inference and validation tools.

