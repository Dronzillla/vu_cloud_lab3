import json


def test_get_todo_by_id(client, init_database):
    response = client.get("/api/todos/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "success"
    assert data["data"]["todo"]["tid"] == 1


def test_get_nonexistent_todo_by_id(client):
    response = client.get("/api/todos/999")
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data["status"] == "fail"
    assert data["data"]["todo"] == "Todo does not exist"
