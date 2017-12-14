# Docker and the Playground

The following section will provide you with:

- An introduction on Docker
- Some information to build your Docker image
- Insights on pushing and building docker containers on GCP
- An example of a Dockerfile

## What is Docker

From [Docker official website](http://www.docker.com):

Docker is the world’s leading software container platform. Developers use Docker to eliminate “works on my machine” problems when collaborating on code with co-workers. Operators use Docker to run and manage apps side-by-side in isolated containers to get better compute density. Enterprises use Docker to build agile software delivery pipelines to ship new features faster, more securely and with confidence for both Linux, Windows Server, and Linux-on-mainframe apps.

Containers are a way to package software in a format that can run isolated on a shared operating system. Unlike VMs, containers do not bundle a full operating system - only libraries and settings required to make the software work are needed. This makes for efficient, lightweight, self-contained systems and guarantees that software will always run the same, regardless of where it’s deployed.

## Creating your Docker Image

It is recommended to follow the [Offical Docker tutorials](https://docs.docker.com/get-started/part2/#introduction) for creating Docker images.

[Another tutorial](https://rominirani.com/docker-tutorial-series-a7e6ff90a023)

[Yet Another tutorial](https://docker-curriculum.com/)

## Building a Docker Image

[Docker Official tutorial](https://docs.docker.com/get-started/part2/#build-the-app)

Please refer to the [Docker Reference page](https://docs.docker.com/engine/reference/builder/)

It is often very useful to specify [Args Variables](https://docs.docker.com/engine/reference/builder/#arg) in your Docker Image to be able to parameterise it.

## Pushing a Docker Image

If you want to publish your Docker image you can publish it on various Docker Containers Hub, such as the [Docker Hub](https://hub.docker.com/) or [Google Cloud Platform Container Registry](https://cloud.google.com/container-registry/docs/)

If you have access to any Google Cloud Platform Project we recommend that you push on the GCP Container Registry.

Here is a [guide containing relevant information](https://cloud.google.com/container-registry/docs/pushing-and-pulling) about GCP Container Registry.

Briefly, your Docker should be tagged as such `eu.grc.io/your_project_name/your_base_service_name` and pushed to your project.

If you use your internal GCP Project it is necessary that you [share your image publicly](https://cloud.google.com/container-registry/docs/access-control) so we can call it.

## GCP Docker Container Builder

It is possible to automate building docker images or simply building Docker image on the cloud using the [Container Builder](https://cloud.google.com/container-builder/docs/).
This service makes it possible to build image when working on Windows for example (without Docker locally installed).

In your working directory, just create a `cloudbuild.yaml` file with the following configuration (see the doc for more information):

```yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '--build-arg', 'config=${_CONFIG}','--build-arg','model=${_MODEL}','--tag=eu.gcr.io/$PROJECT_ID/${_SERVICE_ID}_base:${_VERSION}','.']
  id: 'dockerbuild'
images: 'eu.gcr.io/$PROJECT_ID/${_SERVICE_ID}_base'
```

!!! note
    The --build-arg in the yaml config are of course dependent on your image and just showcase an example of using them in the cloudbuild configuration.

Calling the GCP Container builder is done via this command:

```bash
SERVICE_NAME="my_service_name"
MODEL="my_model_weights.pb"
CONFIG="my_config.yaml"
VERSION="20171001_model_v1"

gcloud config configurations activate dev
gcloud container builds submit . --config cloudbuild.yaml --substitutions _SERVICE_ID="${SERVICE_NAME}",_CONFIG="${CONFIG}",_MODEL="${MODEL}", _VERSION="${VERSION}"
```

!!!note
    Note the use of substitutions in the bash script that replaces the arguments in the `cloudbuild.yaml`

## Full Example Docker Image & File structure

You will find below a Dockerfile example that:

- Builds from the official ubuntu:16.04 docker image
- Install package dependencies
- Install python 2.7 from Conda
- Install pip packages from `requirements.txt` located at the workdir
- Copy the predictor code and model weights/configuration in the docker
- Copy a test script and runs it to validate the predictor

### workdir structure

Local workdir structure:

```text
/workdir/
|_ app_detection/
    |_ __init__.py
    |_ predictor.py
    |_ config.yaml
    |_ (other utils)
|_ models/
    |_ weights.pb
|_ config/
    |_ ship.yaml
Dockerfile
requirements.txt
build.sh
```

### requirements.txt

```text
geojson
h5py
numpy
opencv-python==3.2.0.7
pprint
pyyaml
scipy
shapely==1.5.17.post1
https://storage.googleapis.com/oneatlas_playground_utils/playground_interfaces-0.2.tar.gz
```

### Dockerfile

````Dockerfile
FROM ubuntu:16.04

ARG config
ARG model

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Pick up some TF dependencies
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends \
        build-essential \
        bzip2 \
        ca-certificates \
        curl \
        git \
        libcurl3-dev \
        libxext6 \
        libfreetype6-dev \
        libgeos-dev \
        libglib2.0-0 \
        libpng12-dev \
        libsm6 \
        libxrender1 \
        libzmq3-dev \
        mercurial \
        pkg-config \
        rsync \
        software-properties-common \
        subversion \
        unzip \
        zip \
        zlib1g-dev \
        openjdk-8-jdk \
        openjdk-8-jre-headless \
        wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fSsL -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py


# Install Miniconda2
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENV PATH /opt/conda/bin:$PATH

RUN conda install -y python=2.7

# Install requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -I --upgrade setuptools && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

# Install TF
RUN pip install tensorflow
# Alternatively you can compile tensorflow from sources with specific optimization flags. See below

### Predictor/Model packaging below

# COPY predictor package located in app_detection
COPY ./app_detection/ /api/app_detection/
# COPY predictor configuration stored elsewhere
COPY config/$config /api/app_detection/predictor.yaml
# COPY MODELS in a layer to not repull if no changes
COPY models/$model/* /api/app_detection/model/

# Run tests
COPY test.py /api/
RUN python /api/test.py && \
    rm /api/test.py
````

Final Structure (inside the image):

```text
/api/
    |_predictor_package/
        |_predictor_module.py
            |_ class Predictor(BaseProcess)
        |_ model_weights.pb
        |_ (other utils)
```

This docker is built using the following command:

```bash
STAGING_PROJECT_NAME="theplayground-dev"
SERVICE_NAME="shipdetection"
MODEL="0922_0821_vgg_unet_x8_elubn__scratch_ship_oneatlas_v2_softmax_050_crop_sgd"
VERSION="_v1"
CONFIG="ship.yaml"
docker build . --build-arg config=${CONFIG} --build-arg model=${MODEL} --tag="eu.gcr.io/${STAGING_PROJECT_NAME}/${SERVICE_NAME}_base:${MODEL}${VERSION}"
```

### Compiling Tensorflow from sources for App Engine Flex deployment

!!! warning

    This does not seem to work with TF 1.3.0. Investigation is ongoing. Safest way is to just pip-install.

!!! tip

    Tensorflow can be optimized for running on Intel CPUs using various compilation flags. This significatively improve TF runtime on CPU. However, App Engine Flex does not (for now) let you choose the CPU architecture and allocates machines on demand. This is problematic as a Skylake-optimized install of tensorflow will crash when run on Sandy Bridge CPUs.
    We provide you with an example script compiled for running on Intel Xeon CPUs from Sandy Bridge.

    ```Dockerfile
    # Install requirements
    COPY requirements.txt /tmp/requirements.txt
    RUN pip install --upgrade pip && \
        pip install -I --upgrade setuptools && \
        pip install -r requirements.txt && \
        python -m ipykernel.kernelspec && \
        rm -rf /tmp/requirements.txt

    # Compile TF from Sources
    # Set up Bazel.

    # Running bazel inside a `docker build` command causes trouble, cf:
    #   https://github.com/bazelbuild/bazel/issues/134
    # The easiest solution is to set up a bazelrc file forcing --batch.
    RUN echo "startup --batch" >>/etc/bazel.bazelrc
    # Similarly, we need to workaround sandboxing issues:
    #   https://github.com/bazelbuild/bazel/issues/418
    RUN echo "build --spawn_strategy=standalone --genrule_strategy=standalone" \
        >>/etc/bazel.bazelrc
    # Install the most recent bazel release.
    ENV BAZEL_VERSION 0.5.0
    WORKDIR /
    RUN mkdir /bazel && \
        cd /bazel && \
        curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" -fSsL -O https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \
        curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36" -fSsL -o /bazel/LICENSE.txt https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE && \
        chmod +x bazel-*.sh && \
        ./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \
        cd / && \
        rm -f /bazel/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh

    # Download and build TensorFlow.

    RUN git clone https://github.com/tensorflow/tensorflow.git && \
        cd tensorflow && \
        git checkout r1.2
    WORKDIR /tensorflow

    ENV CI_BUILD_PYTHON python

    # Create PIP from source
    # Compile with minimal CPU instructions to run TF on Flex (Sandy Bridge)
    RUN tensorflow/tools/ci_build/builds/configured CPU \
        bazel build -c opt \
            --copt="mavx" --copt="-msse4.1" --copt="-msse4.2"\
            --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" \
            tensorflow/tools/pip_package:build_pip_package

    # Other available compilation flags.
    # --copt="-mavx" --copt="-mavx2" --copt="-mfma" --copt="-msse4.1" --copt="-msse4.2" \
    # You can also investigate --march-native and intel MKL support

    RUN bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/pip

    # Install the created Pip
    # Clean up pip wheel and Bazel cache when done.
    RUN  pip --no-cache-dir install /tmp/pip/tensorflow-*.whl && \
        rm -rf /tmp/pip && \
        rm -rf /root/.cache
    ```
