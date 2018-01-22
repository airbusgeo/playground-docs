# Create a container image from a stock Python 2.7 Debian image
FROM python:2.7-stretch

# Create a virtualenv for installing the application
RUN virtualenv --no-download /env -p python
# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Set workdir
WORKDIR /app/

# Install application requirements
ADD requirements.txt /app/
RUN pip install -r requirements.txt

# Install application
ADD . /app/

# Launch web application
EXPOSE 80
ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "-b", "0.0.0.0:80", "api_stub:app"]

