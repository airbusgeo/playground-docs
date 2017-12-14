![OneAtlas Playground](images/logo.png "OneAtlas Playground")

# [OneAtlas Playground](https://sandbox.intelligence-airbusds.com/web/) Documentation

An Open Platform to Create New Innovative Services from Satellite Imagery.

For more informations, go to the [official website](https://sandbox.intelligence-airbusds.com/web/).

You will find here documentation regarding:

- Deploying services on OneAtlas Playground
- Using the OneAtlas Playground Web Interface

## Introduction

The OneAtlas Playground is the sandbox development platform for imagery services based on OneAtlas.

## Core Concepts

The core principle of OneAtlas Playground is to provide a "sandboxed" environment connected to OneAtlas Imagery in order to develop, deploy and test Machine Learning Services in a Cloud Environment.
It relies on the Google Cloud Platform and is based on Google App Engine.

The main objective of the Playground is to abstract away data connection, deployment and scalability for any Data Scientist and to provide an integrated platform to directly assess the performance and scalability of ML services. 

![OneAtlas Playground](images/playground.png "OneAtlasPlayground")

## Sandboxed Deployment

Abstracting away the deployment of ML services is done via deploying Docker containers that are wrapped by the Playground own docker container before being deployed on Google App Engine.

![OneAtlas Playground](images/playground2.png "OneAtlasPlayground")

## Tagging and Labelling directly on One Atlas

The Playground also offers a Web Interface to create, edit and refine datasets using OneAtlas images via tagging, detouring and markin Area of Interests, Region of Interests and objects on satellite images.
