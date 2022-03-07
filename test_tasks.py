TASK_TITLE = "buying a glass"


def create_new_task(client, task_title=TASK_TITLE):
    data = {"task_title": task_title}
    response = client.post("/tasks", data=data)
    return response.json['task_id']


def test_post_get(client):
    create_new_task(client)
    response = client.get("/tasks")
    rows = response.json
    assert [elem for elem in rows if elem['task_title'] == TASK_TITLE]


def test_post_delete_all(client):
    create_new_task(client)
    response = client.get("/tasks")
    assert response.json
    response = client.delete("/tasks")
    assert response.status_code == 200
    response = client.get("/tasks")
    assert not response.json


def test_post_delete_specific(client):
    task_id = create_new_task(client)
    response = client.get("/tasks/" + str(task_id))
    assert response.json
    response = client.delete("/tasks/" + str(task_id))
    assert response.status_code == 200
    response = client.get("/tasks/" + str(task_id))
    assert not response.json


def test_mark_task_done(client):
    task_id = create_new_task(client)
    response = client.get("/tasks/" + str(task_id))
    assert response.json['task_is_done'] == 0
    response = client.put("/tasks/done/" + str(task_id))
    assert response.status_code == 200
    response = client.get("/tasks/" + str(task_id))
    assert response.json['task_is_done'] == 1
