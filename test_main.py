from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

# Teste 1
def test_helloworld_status():
    response = client.get("/helloworld")
    assert response.status_code == 200

# Teste 2
def test_helloworld_conteudo():
    response = client.get("/helloworld")

    assert response.json() == {"message": "Hello World"}

# Teste 3
def test_funcaoteste_status():
    response = client.get("/funcaoteste")
    assert response.status_code == 200

# Teste 4
def test_rota_inexistente():
    response = client.get("/rota-que-nao-existe")
    assert response.status_code == 404

# Teste 5
def test_metodo_nao_permitido():
    response = client.post("/helloworld")
    assert response.status_code == 405