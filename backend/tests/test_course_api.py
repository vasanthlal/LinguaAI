from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_courses():
    response = client.get('/courses/')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_courses_with_pagination():
    response = client.get('/courses/?skip=0&limit=5')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_courses_with_sorting():
    response = client.get('/courses/?sort_by=title&order=asc')

    assert response.status_code == 200
    assert isinstance(response.json(), list)