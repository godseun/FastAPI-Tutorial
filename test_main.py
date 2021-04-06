import random

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_model():
    fake_params = ["alexnet", "resnet", "lenet"]
    response = client.get(f"/models/{random.choice(fake_params)}")
    assert response.status_code == 200


def test_read_user_me():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {"user_id": "the current user"}


def test_read_user():
    fake_param = "admin"
    response = client.get(f"/users/{fake_param}")
    assert type(fake_param) == str
    assert response.status_code == 200
    assert response.json() == {"user_id": fake_param}


def test_read_item():
    fake_param = 2
    response = client.get(f"/items/{fake_param}")
    assert type(fake_param) == int
    assert response.status_code == 200
    assert response.json() == {"item_id": fake_param}


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
