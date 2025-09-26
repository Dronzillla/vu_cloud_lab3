import json


def test_create_todo_correct_attributes(client):
    new_todo = {
        "title": "New Todo",
        "description": "A new todo created in test",
        "duedate": "2024-10-01",
    }
    response = client.post(
        "/api/todos", data=json.dumps(new_todo), content_type="application/json"
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["status"] == "success"


def test_create_todo_no_title(client):
    new_todo = {
        "description": "A new todo created in test",
        "duedate": "2024-10-01",
    }
    response = client.post(
        "/api/todos", data=json.dumps(new_todo), content_type="application/json"
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["status"] == "fail"


def test_create_todo_title_only_numbers(client):
    new_todo = {
        "title": "1111",
        "description": "A new todo created in test",
        "duedate": "2024-10-01",
    }
    response = client.post(
        "/api/todos", data=json.dumps(new_todo), content_type="application/json"
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["status"] == "fail"


def test_create_todo_no_duedate(client):
    new_todo = {
        "title": "New Todo",
        "description": "A new todo created in test",
    }
    response = client.post(
        "/api/todos", data=json.dumps(new_todo), content_type="application/json"
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["status"] == "fail"


def test_create_todo_invalid_duedate(client):
    new_todo = {
        "title": "New Todo",
        "description": "A new todo created in test",
        "duedate": "2024",
    }
    response = client.post(
        "/api/todos", data=json.dumps(new_todo), content_type="application/json"
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["status"] == "fail"
