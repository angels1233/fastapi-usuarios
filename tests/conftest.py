from fastapi.testclient import TestClient
from pytest import fixture

from src.main import app


@fixture
def client():
    print("iniciando fixture cliente")
    with TestClient(app) as client:
        yield client
        print("finalizando fixture cliente")
