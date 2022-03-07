import pytest
from app import create_app, db


@pytest.fixture
def client():
    app = create_app(True)
    db.create_all(app=app)

    with app.test_client() as client:
        yield client
