from http import HTTPStatus


def test_controler_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["data"]) == 10

def test_controler_id(client):
    id = 5
    response = client.get(f"/users/{id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json()['id'] == id

def test_ERRO_controler_id(client):
    id = 500
    response = client.get(f"/users/{id}")
    assert response.status_code == 404

#Em projetos mais complexos testar todas as possibilidades possiveis!