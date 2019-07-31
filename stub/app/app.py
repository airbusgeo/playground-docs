from sanic import Sanic, Blueprint
from sanic_openapi import swagger_blueprint
from v1 import v1

from sanic import Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse

# Declare Sanic application
app = Sanic(__name__)

# API Configuration
app.config.REQUEST_TIMEOUT = 120
app.config.RESPONSE_TIMEOUT = 3600

# API V1 routes
app.blueprint(swagger_blueprint)
app.blueprint(v1)

@app.route('/')
async def get(request: Request) -> HTTPResponse:
    result = response.text('OK', 200)
    result.headers['content-type'] = 'text/plain'
    return result

app.config.API_VERSION = 'YOUR_API_VERSION'
app.config.API_TITLE = 'YOUR_API_TITLE'
app.config.API_DESCRIPTION = 'YOUR_API_DESCRIPTION'
app.config.API_TERMS_OF_SERVICE = 'YOUR_API_LICENCE'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json', 'mimetypes/jpeg', 'mimetypes/tiff']
app.config.API_CONTACT_EMAIL = 'YOUR_EMAIL'

def main():
    app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    main()
