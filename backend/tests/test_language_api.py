from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_languages():
    response = client.get('/languages/')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_languages_with_pagination():
    response = client.get('/languages/?skip=0&limit=5')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_languages_with_sorting():
    response = client.get('/languages/?sort_by=name&order=asc')

    assert response.status_code == 200
    assert isinstance(response.json(), list)