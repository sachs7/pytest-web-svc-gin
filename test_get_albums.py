import requests
import pytest
import json
import os

# BASE_URL = "http://192.168.1.11"
# BASE_URL = "http://localhost"
ip = os.environ["IP"]
BASE_URL = "http://" + ip
print(BASE_URL)
port = os.environ["PORT"]
# BASE_PORT = "8082"
BASE_PORT = port
PATH = "/albums"

FULL_URL = BASE_URL + ":" + BASE_PORT + PATH


def test_get_albums():
    print(FULL_URL)
    resp = requests.get(FULL_URL)
    assert resp.status_code == 200
    print(resp.status_code)
    print(resp.json())

def test_get_album_with_id():
    resp = requests.get(FULL_URL + "/2")
    print(resp.json())
    assert resp.status_code == 200

def test_post_create_album():
    body = json.dumps({'title': "Ero", "artist": "Enigma", "country": "India"})
    resp = requests.post(FULL_URL, body)
    print(resp.json())
    print(resp.status_code)
    get_all = requests.get(FULL_URL)
    print(get_all.json())
    assert len(get_all.json()) > 3