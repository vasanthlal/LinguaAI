from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_questions():
    response = client.get('/questions/')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_questions_with_pagination():
    response = client.get('/questions/?skip=0&limit=5')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_questions_with_sorting():
    response = client.get('/questions/?sort_by=id&order=asc')

    assert response.status_code == 200
    assert isinstance(response.json(), list)