from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_quiz_attempts():
    response = client.get('/quiz-attempts/')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_quiz_attempts_with_pagination():
    response = client.get('/quiz-attempts/?skip=0&limit=5')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_quiz_attempts_with_sorting():
    response = client.get('/quiz-attempts/?sort_by=id&order=desc')

    assert response.status_code == 200
    assert isinstance(response.json(), list)