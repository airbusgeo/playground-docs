<p style='text-align: center; color: red; font-size: 20px;'>Common steps : Connection & Build the headers</p>

-----------------

The first step : **Connection**

##### 1 - Authentification

To launch jobs batch, you need to have a token for the authentification. You can see [Authentification API](auth.md) page for further details.

##### 2 - Retrieve access token and build headers

When you have access to your refresh token :

``` python

ACCESS_TOKEN = get_access_token()

```

The get_access_token method enables you to create a connection :

``` python

def get_access_token():
    payload = {'refresh_token': REFRESH_TOKEN}
    response = requests.get('https://playground.intelligence-airbusds.com/oauth2/refresh', params=payload)
    assert response.status_code == 200, 'An error occured when accessing refresh endpoint'
    content = json.loads(response.content)
    assert 'access_token' in content.keys(), 'No access_token field in reponse'
    access_token = content['access_token']
    return access_token

```

The second step : **Build headers**

``` python

HEADERS = {
    'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
    'Content-Type': 'application/json'
}

```
