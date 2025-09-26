import json


def test_delete_todo_correct_attributes(client, init_database):
    response = client.delete("/api/todos/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "success"

    # Verify that the todo is actually deleted
    response = client.get("/api/todos/1")
    assert response.status_code == 404


def test_delete_nonexistent_todo(client):
    response = client.delete("/api/todos/999")
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data["status"] == "fail"
