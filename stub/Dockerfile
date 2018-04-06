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
EXPOSE 8080
ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "-b", "0.0.0.0:8080", "api:app"]
