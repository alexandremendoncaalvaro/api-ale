from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_me_returns_a_user():
    response = client.get("/me")
    assert response.status_code == 200
    assert "user" in response.json()
