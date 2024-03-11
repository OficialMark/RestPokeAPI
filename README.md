# Pokemon Teams API - Desafio Triágil

Esta é uma API simples em Flask para gerenciar equipes de Pokémon. Ela permite criar, listar e buscar times de Pokémon.

## Funcionalidades

- **Listar Todos os Times:** `GET /api/teams`
  - Retorna um json de todos os times registrados.

- **Buscar Time por Usuário:** `GET /api/teams/<user>`
  - Retorna as informações do time associado ao usuário especificado.

- **Criar Time:** `POST /api/teams`
  - Cria um novo time associado a um usuário, com base na lista de Pokémon fornecida.

## Endpoints

### Página Inicial

- `GET /`
  - Retorna uma mensagem indicando que a API está funcionando.
  
### Listar Todos os Times

- `GET /api/teams`
  - Retorna uma lista de todos os times registrados.

### Buscar Time por Usuário

- `GET /api/teams/<user>`
  - Retorna as informações do time associado ao usuário especificado.

### Criar Time

- `POST /api/teams`
  - Cria um novo time associado a um usuário, com base na lista de Pokémon fornecida.
  - Exemplo com script python:
```python
import requests
import json

base_url = 'http://localhost:5000/api/teams'
team_data = {
    'user': 'AshKetchum',
    'pokemon_list': ['Charizard', 'Pikachu', 'Zapdos']
}

headers = {'Content-Type': 'application/json'}
team_json = json.dumps(team_data)
response = requests.post(base_url, data=team_json, headers=headers)

print(response.status_code)
print(response.json())

```

## Estrutura do Projeto

- `app.py`: Script principal que contém a lógica da API.
- `teams.json`: Arquivo de persistência para armazenar os times.

## Como Executar

- Local:
1. Instale as dependências com `pip install -r requirements.txt`.
2. Execute o script com `python app.py`.

- Docker:
1. No terminal, navegue até a pasta com os arquivos
2. use o comando `docker-compose up`

## Observações

- Os times são armazenados em memória durante a execução. Ao encerrar a aplicação, eles são salvos no arquivo `teams.json`.
- As rotas retornam um objeto JSON indicando o sucesso da operação ou especificando um código de status: 200 para operações bem-sucedidas, 400 para inconsistências nos dados de entrada e 404 quando a informação solicitada não é encontrada.
