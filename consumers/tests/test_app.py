from chalice.test import Client  # Importa o cliente de teste do Chalice
from app import app  # Importa a aplicação Chalice configurada
import json  # Importa o módulo json para manipulação de dados JSON

def test_create_person():
    # Testa a criação de um novo usuário
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição POST para criar um usuário
        response = client.http.post(
            '/consumers/person',  # Endpoint para criar usuário
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),  # Corpo da requisição com dados do usuário
            headers={"Content-Type": "application/json"}  # Define o tipo de conteúdo como JSON
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_update_person():
    # Testa a atualização de um usuário existente
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição PUT para atualizar um usuário
        response = client.http.put(
            '/consumers/person',  # Endpoint para atualizar usuário
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),  # Corpo da requisição com novos dados do usuário
            headers={"Content-Type": "application/json"}  # Define o tipo de conteúdo como JSON
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_delete_person():
    # Testa a exclusão de um usuário existente
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição DELETE para excluir um usuário
        response = client.http.delete(
            '/consumers/person',  # Endpoint para excluir usuário
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),  # Corpo da requisição com dados do usuário a ser excluído
            headers={"Content-Type": "application/json"}  # Define o tipo de conteúdo como JSON
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_get_persons():
    # Testa a obtenção de todos os usuários
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição GET para obter todos os usuários
        response = client.http.get(
            '/consumers/persons'  # Endpoint para obter todos os usuários
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_get_person():
    # Testa a obtenção de um usuário específico
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição GET para obter um usuário específico
        response = client.http.get(
            '/consumers/person/1'  # Endpoint para obter usuário com ID específico (neste caso, ID 1)
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_create_company():
    # Testa a criação de uma nova empresa
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição POST para criar uma empresa
        response = client.http.post(
            '/consumers/company',  # Endpoint para criar empresa
            body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),  # Corpo da requisição com dados da empresa
            headers={"Content-Type": "application/json"}  # Define o tipo de conteúdo como JSON
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_update_company():
    # Testa a atualização de uma empresa existente
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição PUT para atualizar uma empresa
        response = client.http.put(
            '/consumers/company',  # Endpoint para atualizar empresa
            body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),  # Corpo da requisição com novos dados da empresa
            headers={"Content-Type": "application/json"}  # Define o tipo de conteúdo como JSON
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_delete_company():
    # Testa a exclusão de uma empresa existente
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição DELETE para excluir uma empresa
        response = client.http.delete(
            '/consumers/company',  # Endpoint para excluir empresa
            body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),  # Corpo da requisição com dados da empresa a ser excluída
            headers={"Content-Type": "application/json"}  # Define o tipo de conteúdo como JSON
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_get_companies():
    # Testa a obtenção de todas as empresas
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição GET para obter todas as empresas
        response = client.http.get(
            '/consumers/companies'  # Endpoint para obter todas as empresas
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200

def test_get_company():
    # Testa a obtenção de uma empresa específica
    with Client(app) as client:
        # Utiliza o cliente HTTP para enviar uma requisição GET para obter uma empresa específica
        response = client.http.get(
            '/consumers/company/1'  # Endpoint para obter empresa com ID específico (neste caso, ID 1)
        )
        print(response.json_body)  # Exibe o corpo da resposta JSON no console
        assert response.json_body["statusCode"] == 200  # Verifica se a resposta tem código de status HTTP 200
