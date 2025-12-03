import requests
import pytest

def test_authentication_failed(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'admin'
    }

    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ''

    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text.strip() == ''


def test_authentication_successful(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ''

    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text.strip() == ''