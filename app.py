from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

# Caminho do arquivo para persistência dos times
TEAMS_FILE = 'teams.json'

# Dicionário para armazenar os times em memória
teams = {}

# Função para obter os dados do Pokémon da PokeAPI
def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            'id': pokemon_data['id'],
            'name': pokemon_name,
            'weight': pokemon_data['height'],
            'height': pokemon_data['weight']
        }
    else:
        return None

# Função para ler os times do arquivo
def read_teams():
    try:
        with open(TEAMS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Função para salvar os times no arquivo
def save_teams():
    with open(TEAMS_FILE, 'w') as file:
        json.dump(teams, file, indent=2)

# Pagina Inicial
@app.route('/')
def index():
    return {'success': "API funcionando. Para ver a lista de times registrados, va para /api/teams"}, 200

# Rota para listar todos os times registrados
@app.route('/api/teams', methods=['GET'])
def get_all_teams():
    return jsonify(teams)

# Rota para buscar um time registrado por usuário
@app.route('/api/teams/<user>', methods=['GET'])
def get_team_by_user(user):
    print(user)
    for _, team in teams.items():
        if team['owner'] == f"{user}":
            return jsonify(team)
    
    return jsonify({'error': f'Time com usuario {user} nao identificado'}), 404

# Rota para criar um time
@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.get_json()

    user = data.get('user')
    pokemon_list = data.get('pokemon_list')

    if not user or not pokemon_list:
        return jsonify({'error': 'Usuario ou lista de pokemons ausentes'}), 400

    pkmns = []
    for pokemon_name in pokemon_list:
        pokemon_data = get_pokemon_data(pokemon_name)
        if not pokemon_data:
            return jsonify({'error': f'Pokemon {pokemon_name} nao encontrado'}), 400
        
        pokemon = {"id": pokemon_data['id'], 'name': pokemon_data['name'], 'weight': pokemon_data['weight'], 'height': pokemon_data['height']}
        pkmns.append(pokemon)

    team = {'owner': user, 'pokemons': pkmns}
    teams[f'{len(teams)+1}'] = team
    save_teams()
    
    return jsonify({'message': 'Time registrado com sucesso', 'time_id': len(teams)})

if __name__ == '__main__':
    teams = read_teams()
    app.run()
