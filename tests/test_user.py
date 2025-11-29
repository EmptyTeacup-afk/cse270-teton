import pytest
import requests
import requests_mock

# URL of the API endpoint
url = "http://127.0.0.1:8000/users"

def test_get_users_with_invalid_auth(requests_mock):
    """
    Mock a 401 Unauthorized response and an empty *text* body
    when using invalid credentials.
    """
    # Mock the GET request for invalid credentials
    requests_mock.get(url, status_code=401, text="")

    params = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.get(url, params=params)

    # Expect plain text, not JSON
    assert response.headers.get("Content-Type", "").startswith("text"), \
        "Response is expected to be plain text"

    assert response.status_code == 401
    assert response.text.strip() == ""


def test_get_users_with_valid_auth(requests_mock):
    """
    Mock a 200 OK response and an empty *text* body
    when using valid credentials.
    """
    # Mock the GET request for valid credentials
    requests_mock.get(url, status_code=200, text="")

    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(url, params=params)

    # Expect plain text, not JSON
    assert response.headers.get("Content-Type", "").startswith("text"), \
        "Response is expected to be plain text"

    assert response.status_code == 200
    assert response.text.strip() == ""
