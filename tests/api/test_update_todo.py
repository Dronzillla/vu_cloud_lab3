import json


def test_update_todo_correct_attributes(client, init_database):
    updated_todo = {
        "title": "Updated Todo",
        "description": "This todo has been updated",
        "duedate": "2024-09-29",
        "done": True,
    }
    response = client.put(
        "/api/todos/1", data=json.dumps(updated_todo), content_type="application/json"
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "success"


def test_update_nonexistent_todo(client):
    updated_todo = {
        "title": "Updated Todo",
        "description": "This todo has been updated",
        "duedate": "2024-09-29",
        "done": True,
    }
    response = client.put(
        "/api/todos/999", data=json.dumps(updated_todo), content_type="application/json"
    )
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data["status"] == "fail"


def test_update_todo_no_title(client, init_database):
    updated_todo = {
        "description": "This todo has been updated",
        "duedate": "2024-09-29",
        "done": True,
    }
    response = client.put(
        "/api/todos/1", data=json.dumps(updated_todo), content_type="application/json"
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["status"] == "fail"


def test_update_todo_no_duedate(client, init_database):
    updated_todo = {
        "title": "Updated Todo",
        "description": "This todo has been updated",
        "done": True,
    }
    response = client.put(
        "/api/todos/1", data=json.dumps(updated_todo), content_type="application/json"
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["status"] == "fail"
