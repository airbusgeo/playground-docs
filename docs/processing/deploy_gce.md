# Introduction

This section describes how to deploy a Docker image on Google Compute Engine.

Compute Engine provides virtual machines.
With a VM it is easy to **test the processing** and its deployment.

# Prerequisites

* A Google account
* A project on Google Cloud Platform
* Google Cloud SDK installed from [https://cloud.google.com/sdk/downloads](https://cloud.google.com/sdk/downloads)

# Create a VM

* On Google Cloud Platform console [https://console.cloud.google.com](https://console.cloud.google.com)
* Select "Compute Engine"
* Select "VM instances"
* Select "Create an instance"
* Configure the instance with the following data:
    * Name : the VM instance name (example: my-process)
    * Zone : select "europe-west1-c"
    * Machine type : micro (see below)
    * Container : NO
    * Image : Debian GNU/Linux 9 (stretch)
    * Firewall : Authorize HTTP trafic
* Click "Create"

**How to choose your VM**

The VM type depends on what to do with the VM:

* For *ML training*, you need a lot of computing power, choose either 32 or 64 vCPU like ```n1-highcpu-32``` configuration
* For *ML predict* testing, a ```micro``` or ```small``` VM configuration is good
* For *Docker testing*, choose a ```micro``` VM configuration

In all cases, keep in mind that you will **pay** for the VM while it is **running**. If you choose a big expensive one, you have to **stop it when not been used**.

# Configure the VM

TODO

# Push code to the VM

```bash
gcloud beta compute scp * my-process:
```

# Create the Docker image

```bash
gcloud beta compute ssh my-process
docker build --rm -t process .
```

# Execute the Docker container

```bash
docker run --rm -ti -p 80:80 process
```
