import json


def test_get_todos_success(client, init_database):
    response = client.get("/api/todos")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "success"
    assert len(data["data"]["todos"]) == 2
