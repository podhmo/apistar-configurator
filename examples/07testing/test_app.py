from apistar import test
from app import make_app

# pytest .


def test_it():
    app = make_app()
    client = test.TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to API Star!"}
