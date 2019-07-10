# Authentication

To call any Playground APIs, you need to have a valid access token or a refresh token.
Please, check the *[Authentification API](auth.md)* page for further details.

## Retrieve access token from refresh token

First, you need to store your refresh token :
``` python
REFRESH_TOKEN = 'INSERT_YOUR_REFRESH_TOKEN_HERE'
```

Then the following method enables you to use the refresh token to retrieve a valid access token:

``` python
def get_access_token():
    payload = {'refresh_token': REFRESH_TOKEN}
    response = requests.get('https://playground.intelligence-airbusds.com/oauth2/refresh', params=payload)
    assert response.status_code == 200, 'An error occured when accessing refresh endpoint'
    content = json.loads(response.content)
    assert 'access_token' in content.keys(), 'No access_token field in reponse'
    access_token = content['access_token']
    return access_token

ACCESS_TOKEN = get_access_token()
```

## Build headers

The access token is directly used as an aurthorization token in the HTTP headers.
In most case, the content is also JSON, so we define this as well.

``` python
HEADERS = {
    'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
    'Content-Type': 'application/json'
}
```

Then, include the HEADERS in any request to the Playground APIs.

```
response = requests.get('https://playground.intelligence-airbusds.com/api/projects', headers=HEADERS)
```
