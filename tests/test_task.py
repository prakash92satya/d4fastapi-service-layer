from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={
        "title": "Test Task",
        "priority": "high"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"


def test_delete_task_fail():
    # create first
    res = client.post("/tasks", json={
        "title": "High Task",
        "priority": "high"
    })
    task_id = res.json()["id"]

    # try delete as normal user
    response = client.delete(f"/tasks/{task_id}?user_role=user")
    assert response.status_code == 400


def test_delete_task_success():
    res = client.post("/tasks", json={
        "title": "Another Task",
        "priority": "high"
    })
    task_id = res.json()["id"]

    response = client.delete(f"/tasks/{task_id}?user_role=manager")
    assert response.status_code == 200