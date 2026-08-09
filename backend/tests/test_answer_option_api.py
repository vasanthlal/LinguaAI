from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_answer_options():
    response = client.get('/answer-options/')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_answer_options_with_pagination():
    response = client.get('/answer-options/?skip=0&limit=5')

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_answer_options_with_sorting():
    response = client.get('/answer-options/?sort_by=id&order=asc')

    assert response.status_code == 200
    assert isinstance(response.json(), list)