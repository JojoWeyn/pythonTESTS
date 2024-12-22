#Сайланкин Дамир 107b
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class User():
    index: int
    name: str
    role: str
    
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}

@pytest.mark.parametrize("user_data", [
    ({"index": 1, "name": "John", "role": "admin"}),
    ({"index": 2, "name": "Alice", "role": "user"}),
    ({"index": 3, "name": "Bob", "role": "manager"})
])
def test_create_user(user_data):
    response = client.post("/user", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}

def test_create_user_with_duplicate_index():
    user_data = {"index": 1, "name": "John", "role": "admin"}
    response = client.post("/user", json=user_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "User with this index already exists"}

def test_get_users():
    response = client.get("/user")
    assert response.status_code == 200
    assert len(response.json()) > 0

@pytest.mark.parametrize("user_index", [1, 2, 3])
def test_get_user(user_index):
    response = client.get(f"/user/{user_index}")
    assert response.status_code == 200
    assert response.json()["index"] == user_index

def test_get_user_not_found():
    response = client.get("/user/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

@pytest.mark.parametrize("user_index", [1])
def test_delete_user(user_index):
    client.post("/user", json={"id": user_index, "name": f"User {user_index}", "role": "user"})
    
    response = client.delete(f"/user/{user_index}")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}


def test_delete_user_not_found():
    response = client.delete("/user/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
