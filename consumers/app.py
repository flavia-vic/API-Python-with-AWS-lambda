from chalice import Chalice  # Importa a biblioteca Chalice, que ajuda a criar aplicativos web serverless

# Cria uma aplicação Chalice com o nome 'consumers'
app = Chalice(app_name='consumers')

# Dados de exemplo para usuários, armazenados em um dicionário
users = {
    "users": [
        {"name": "usuário1", "phone": "47999999999"},
        {"name": "usuário2", "phone": "47999999999"},
        {"name": "usuário3", "phone": "47999999999"},
    ]
}

# Dados de exemplo para empresas, armazenados em um dicionário
companies = {
    "companies": [
        {"name": "empresa1", "telefone": "47999999999"},
        {"name": "empresa2", "telefone": "47999999999"},
        {"name": "empresa3", "telefone": "47999999999"},
    ]
}


# Define uma rota para criar um novo usuário. 
# Quando uma requisição POST é enviada para /consumers/person, esta função é chamada.
@app.route('/consumers/person', methods=['POST'])
def create_user():
    # Obtém os dados enviados no corpo da requisição, que devem estar em formato JSON
    requests_params = app.current_request.json_body
    # Cria uma resposta de sucesso com uma mensagem contendo os dados enviados
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"
    }
    return response  # Retorna a resposta para o cliente





# Define uma rota para atualizar um usuário existente.
# Quando uma requisição PUT é enviada para /consumers/person, esta função é chamada.
@app.route('/consumers/person', methods=['PUT'])
def update_user():
    requests_params = app.current_request.json_body  # Obtém os dados enviados no corpo da requisição
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} atualizado com sucesso!"
    }
    return response  # Retorna a resposta para o cliente





# Define uma rota para deletar um usuário existente.
# Quando uma requisição DELETE é enviada para /consumers/person, esta função é chamada.
@app.route('/consumers/person', methods=['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body  # Obtém os dados enviados no corpo da requisição
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} deletado com sucesso!"
    }
    return response  # Retorna a resposta para o cliente






# Define uma rota para obter a lista de todos os usuários.
# Quando uma requisição GET é enviada para /consumers/persons, esta função é chamada.
@app.route('/consumers/persons', methods=['GET'])
def get_persons():
    response = {
        "statusCode": 200,
        "body": users
    }
    return response  # Retorna a lista de todos os usuários para o cliente





# Define uma rota para obter os detalhes de um usuário específico.
# Quando uma requisição GET é enviada para /consumers/person/{id}, esta função é chamada.
@app.route('/consumers/person/{id}', methods=['GET'])
def get_person(id):
    response = {
        "statusCode": 200,
        "body": {id: {"name": "usuário1", "telefone": "47999999999"}}
    }
    return response  # Retorna os detalhes do usuário solicitado





# Define uma rota para criar uma nova empresa.
# Quando uma requisição POST é enviada para /consumers/company, esta função é chamada.
@app.route('/consumers/company', methods=['POST'])
def create_company():
    requests_params = app.current_request.json_body  # Obtém os dados enviados no corpo da requisição
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criada com sucesso!"
    }
    return response  # Retorna a resposta para o cliente





# Define uma rota para atualizar uma empresa existente.
# Quando uma requisição PUT é enviada para /consumers/company, esta função é chamada.
@app.route('/consumers/company', methods=['PUT'])
def update_company():
    requests_params = app.current_request.json_body  # Obtém os dados enviados no corpo da requisição
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} atualizada com sucesso!"
    }
    return response  # Retorna a resposta para o cliente





# Define uma rota para deletar uma empresa existente.
# Quando uma requisição DELETE é enviada para /consumers/company, esta função é chamada.
@app.route('/consumers/company', methods=['DELETE'])
def delete_company():
    requests_params = app.current_request.json_body  # Obtém os dados enviados no corpo da requisição
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} deletada com sucesso!"
    }
    return response  # Retorna a resposta para o cliente





# Define uma rota para obter a lista de todas as empresas.
# Quando uma requisição GET é enviada para /consumers/companies, esta função é chamada.
@app.route('/consumers/companies', methods=['GET'])
def get_companies():
    response = {
        "statusCode": 200,
        "body": companies
    }
    return response  # Retorna a lista de todas as empresas para o cliente





# Define uma rota para obter os detalhes de uma empresa específica.
# Quando uma requisição GET é enviada para /consumers/company/{id}, esta função é chamada.
@app.route('/consumers/company/{id}', methods=['GET'])
def get_company(id):
    response = {
        "statusCode": 200,
        "body": {id: {"name": "empresa1", "telefone": "47999999999"}}
    }
    return response  # Retorna os detalhes da empresa solicitada
