import requests
import json

def get_puuid(game_name, tag_line, api_key):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["puuid"]
    else:
        print(f"Error al obtener PUUID: {response.status_code}")
        return None
    
def get_soloq_match_history(puuid, number_of_games, api_key, ):
    # Endpoint para obtener IDs de partidas clasificatorias Solo Queue
    match_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count={number_of_games}&api_key={api_key}"
    response = requests.get(match_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener historial de partidas clasificatorias Solo Queue: {response.status_code}")
        return None

def get_match_details(match_id, api_key, region='AMERICAS'):
    match_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    response = requests.get(match_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener detalles de la partida {match_id}: {response.status_code}")
        return None
