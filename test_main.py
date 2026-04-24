from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_helloworld_status():
    assert client.get("/helloworld").status_code == 200

def test_helloworld_conteudo():
    assert client.get("/helloworld").json() == {"message": "Hello World"}

def test_funcaoteste_status():
    assert client.get("/funcaoteste").status_code == 200

def test_rota_inexistente():
    assert client.get("/rota-que-nao-existe").status_code == 404

def test_metodo_nao_permitido():
    assert client.post("/helloworld").status_code == 405