from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_quizzes():
    response = client.get('/quizzes/')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_quizzes_with_pagination():
    response = client.get('/quizzes/?skip=0&limit=5')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_quizzes_with_sorting():
    response = client.get('/quizzes/?sort_by=title&order=asc')

    assert response.status_code == 200
    assert isinstance(response.json(), list)