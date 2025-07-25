# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello FastAPI CI!"}

def test_read_item():
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "message": "This is an item"}

def test_read_item_invalid():
    response = client.get("/items/not-a-number")
    assert response.status_code == 422 # FastAPI's validation error
