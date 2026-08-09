from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_lessons():
    response = client.get('/lessons/')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_lessons_with_pagination():
    response = client.get('/lessons/?skip=0&limit=5')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_lessons_with_sorting():
    response = client.get('/lessons/?sort_by=title&order=asc')

    assert response.status_code == 200
    assert isinstance(response.json(), list)