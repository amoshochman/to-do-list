TASK_TITLE = "buying a glass"


def post(client):
    data = {"task_title": TASK_TITLE}
    return client.post("/tasks", data=data)


def test_post_get(client):
    response = post(client)
    assert response.status_code == 200
    response = client.get("/tasks")
    rows = response.json
    assert [elem for elem in rows if elem['task_title'] == TASK_TITLE]


def test_post_delete(client):
    response = post(client)
    assert response.status_code == 200
    response = client.delete("/tasks")
    assert response.status_code == 200
    response = client.get("/tasks")
    assert response.status_code == 200


def test_delete_specific(client):
    response = post(client)
    task_id = response.json['task_id']
    response = client.get("/tasks/" + str(task_id))
    assert response.json
    response = client.delete("/tasks/" + str(task_id))
    assert response.status_code == 200
    response = client.get("/tasks/" + str(task_id))
    assert not response.json
