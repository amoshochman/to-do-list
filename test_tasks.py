from app import app


TEST_TITLE = "buying a glass"


# @pytest.fixture(scope="session", autouse=True)
# def before_tests():
#     create_app()

def test_post_get():
    data = {"title": TEST_TITLE}
    response = app.test_client().post("/tasks", data=data)
    assert response.status_code == 200
    response = app.test_client().get("/tasks")
    rows = response.json
    assert [elem for elem in rows if elem['title'] == TEST_TITLE]


def test_post_delete():
    data = {"title": TEST_TITLE}
    app.test_client().post("/tasks", data=data)
    response = app.test_client().delete("/tasks")
    assert response.status_code == 200
    response = app.test_client().get("/tasks")
    #...
