# Introduction

This section describes how to deploy a Docker image on Google Kubernetes Engine.

Kubernetes Engine allows to create and manage a kubernetes cluster that permits the application container to scale on several machines in the cluster in order to parallelise the processing of a lot of requests. This kind of deployment is **recommended for production**.

# Prerequisites

* A Google account
* A project on Google Cloud Platform
* Google Cloud SDK installed from [https://cloud.google.com/sdk/downloads](https://cloud.google.com/sdk/downloads)
* Google Cloud SDK kubectl component installed

# Create a cluster

* On Google Cloud Platform console [https://console.cloud.google.com](https://console.cloud.google.com)
* Select "Kubernetes Engine"
* Select "Kubernetes clusters"
* Select "Create cluster"
* Configure the cluster with the following data:
    * Name : the cluster name (example: my-cluster)
    * Zone : select "europe-west1-c"
    * Machine type : custom (see below)
    * Node image : Container-Optimized OS
    * Size : 1
* Click "More" to have access to the Advanced Options
    * Auto-scalling : On
    * Minimum size : 0
    * Maximum size : 10 (see below)
    * Pre-empible nodes : Enabled
* Click "Create"

**How to choose the machine type**

The machine type depends on the processing requirements and the number of processing to be executed simultaneously on each node (machine) of the cluster.

**Maximum size**

The maximum number of nodes that can be created by the auto-scalling. Each node has the characteristics of the selected machine type.

# Configure your environment

```bash
gcloud container clusters list
gcloud container clusters get-credentials my-cluster
kubectl config get-contexts
```

# Create the Docker image

TODO

# Push image to the cluster

TODO
