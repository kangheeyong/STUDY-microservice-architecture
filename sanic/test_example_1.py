from example_1 import app


def test_auth_missing_username_or_password():
    request, response = app.test_client.post('/auth', json={})
    assert response.json['reasons'] == ['Missing username or password']


def test_auth_username_and_password():
    data = {'username': 'user1', 'password': 'abcxyz'}
    request, response = app.test_client.post('/auth', json=data)
    assert response.json['access_token'].split('.')[0] == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
    # assert response.json['access_token'].split('.')[1] == 'eyJ1c2VyX2lkIjoxLCJleHAiOjE1OTA5MTE1MDB9'


def test_access():
    request, response = app.test_client.get('/')
    assert response.json['reasons'] == ['Authorization header not present.']


def test_auth_and_access():
    data = {'username': 'user1', 'password': 'abcxyz'}
    request, response = app.test_client.post('/auth', json=data)
    token = response.json['access_token']

    headers = {"Authorization": "Bearer " + token}
    request, response = app.test_client.get('/', headers=headers)
    assert response.json == {'hello': 'world'}




