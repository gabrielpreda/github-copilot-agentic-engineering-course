def test_healthz_reports_service_is_running(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_tasks_starts_empty(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task_defaults_to_incomplete(client):
    response = client.post("/tasks", json={"title": "Write API docs"})

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Write API docs",
        "completed": False,
    }


def test_created_task_appears_in_list(client):
    created = client.post(
        "/tasks",
        json={"title": "Review test feedback", "completed": True},
    )

    listed = client.get("/tasks")

    assert created.status_code == 201
    assert listed.status_code == 200
    assert listed.json() == [created.json()]
