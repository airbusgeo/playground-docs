Intelligence Playground allows partners to deploy their own tile processing algorithm.
The best way to do this is using a Docker image.

# What is Docker

From [Docker official website](http://www.docker.com):

Docker is the world’s leading software container platform. Developers use Docker to eliminate “works on my machine” problems when collaborating on code with co-workers. Operators use Docker to run and manage apps side-by-side in isolated containers to get better compute density. Enterprises use Docker to build agile software delivery pipelines to ship new features faster, more securely and with confidence for both Linux, Windows Server, and Linux-on-mainframe apps.

Containers are a way to package software in a format that can run isolated on a shared operating system. Unlike VMs, containers do not bundle a full operating system - only libraries and settings required to make the software work are needed. This makes for efficient, lightweight, self-contained systems and guarantees that software will always run the same, regardless of where it’s deployed.

# Create a Docker image

It is recommended to follow the [Offical Docker tutorials](https://docs.docker.com/get-started/part2/#introduction) for creating Docker images.

* [Another tutorial](https://rominirani.com/docker-tutorial-series-a7e6ff90a023)
* [Yet Another tutorial](https://docker-curriculum.com/)

Sample *Dockerfile* for a Python application:

```Dockerfile
# Create a container image from a stock Python 2.7 Debian image
FROM python:2.7-stretch

# Install system dependencies: libgeos
RUN apt-get update && \
    apt-get install -qy libgeos-c1v5 && \
    apt-get clean

# Create a virtualenv for installing the application
RUN virtualenv --no-download /env -p python
# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
# update pip to avoid debian problems
RUN pip install -U pip

# Set workdir
WORKDIR /app/

# Install application requirements
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Install application
COPY . /app/

# Launch web application
EXPOSE 80
ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "-b", "0.0.0.0:80", "api:app"]
```

# Build a Docker image

[Docker Official tutorial](https://docs.docker.com/get-started/part2/#build-the-app)

Please refer to the [Docker Reference page](https://docs.docker.com/engine/reference/builder/). 

```bash
docker build --rm -t process .
```

# Execute a container

The image can be deployed as a container and executed.

In the following example, the service port is redirected to port 9000 on the docker host:

```bash
docker run --rm -ti -p 9000:80 process
```

# Test the process

```bash
curl http://localhost:9000/api/v1/describe
```
