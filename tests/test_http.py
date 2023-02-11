import pytest
import requests

@pytest.mark.http
def test_first_request():
    url = 'https://api.github.com/zen'
    r = requests.get(url)
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    url = 'https://api.github.com/users/defunkt'
    r = requests.get(url)
    body = r.json()
    headers = r.headers 

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    url = 'https://api.github.com/users/sergii_butenko'
    r = requests.get(url)

    assert r.status_code == 404

