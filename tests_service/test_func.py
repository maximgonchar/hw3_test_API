import requests


def test_url(base_url, response_code):
    resp = requests.get(base_url).status_code
    assert resp == int(response_code)
