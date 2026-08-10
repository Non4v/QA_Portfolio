import requests


def test_get_user_returns_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200


def test_get_user_returns_correct_name():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert data["name"] == "Leanne Graham"


def test_get_nonexistent_user_returns_404():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    assert response.status_code == 404


def test_get_all_users_returns_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200


def test_get_all_users_returns_list():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert isinstance(data, list)


def test_get_all_users_returns_ten():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert len(data) == 10


def test_create_post_returns_201():
    payload = {
        "title": "test post",
        "body": "this is a test",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201


def test_create_post_returns_correct_title():
    payload = {
        "title": "test post",
        "body": "this is a test",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=payload)
    data = response.json()
    assert data["title"] == "test post"
