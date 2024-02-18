from fastapi.testclient import TestClient

from app.core.openapi import add_custom_openapi_schema
from app.main import app

client = TestClient(app)


def test_custom_openapi_schema_already_set():
    openapi_schema = {
        "openapi": "3.0.2",
        "info": {"title": "Title", "version": "0.1.0"},
    }
    app.openapi_schema = openapi_schema
    add_custom_openapi_schema(app)
    assert app.openapi_schema["info"]["title"] == "Title"


def test_route_root_return_status_code_200():
    response = client.get("/")
    assert response.status_code == 200


def test_route_root_should_redirect_to_docs_with_status_307():
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"
