import requests


def test_reqres_single_user():
    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == 200
    data = response.json()['data']
    assert data['first_name'] == 'Janet'
