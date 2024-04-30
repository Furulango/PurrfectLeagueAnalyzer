import json
import os
from api_requests import get_puuid, get_soloq_match_history, get_match_details
import pandas as pd 

def store_match_detail(match_id, match_detail, api_key, directory):
    file_name = f"{directory}/match_{match_id}.json"
    with open(file_name, 'w') as file:
        json.dump(match_detail, file, indent=4)

# Recopila y almacena los detalles de cada partida
def process_and_store_matches(soloq_match_history, api_key, directory):
    for match_id in soloq_match_history:
        match_detail = get_match_details(match_id, api_key)
        if match_detail:
            # Asegúrate de usar 'directory' para la ruta del archivo
            store_match_detail(match_id, match_detail, api_key, directory)
    

def cargar_datos_objetos(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def imprimir_items(player):

    # Cargar datos de objetos desde el archivo JSON
    datos_objetos = cargar_datos_objetos('items.json')

    # Crear un diccionario para mapear ID de objeto a nombre
    nombres_objetos = {str(key): value['name'] for key, value in datos_objetos['data'].items()}

    items = {}
    for i in range(7):
        item_id = str(player.get(f'item{i}', ''))
        item_name = nombres_objetos.get(item_id, 'Objeto desconocido')
        items[f'Item{i}'] = item_name  # Guarda el nombre del objeto en la clave correspondiente
    return items

def partida_ya_analizada(partida_id, archivo_csv):
    if os.path.exists(archivo_csv):
        df_existente = pd.read_csv(archivo_csv)
        return partida_id in df_existente['ID'].values
    return False

def agregar_nuevas_partidas_a_csv(all_partidas_data, archivo_csv):
    # Comprobar si el archivo CSV existe
    if os.path.exists(archivo_csv):
        df_existente = pd.read_csv(archivo_csv)
        # Filtrar para incluir solo partidas nuevas
        nuevas_partidas = [partida for partida in all_partidas_data if partida['ID'] not in df_existente['ID'].values]
    else:
        # Si el archivo no existe, todas las partidas son nuevas
        nuevas_partidas = all_partidas_data

    # Agregar nuevas partidas al CSV
    if nuevas_partidas:
        df_nuevas_partidas = pd.DataFrame(nuevas_partidas)
        if os.path.exists(archivo_csv):
            # Agregar al archivo existente sin encabezado
            df_nuevas_partidas.to_csv(archivo_csv, mode='a', header=False, index=False)
        else:
            # Crear un nuevo archivo con encabezado
            df_nuevas_partidas.to_csv(archivo_csv, index=False)

def analizar_jugador_especifico(file_path, puuid_jugador):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extraer la fecha de creación del juego
    game_creation = data['info']['gameCreation']
    game_id = data['info']['gameId']

    for player in data['info']['participants']:
        if player['puuid'] == puuid_jugador:
            player_data = {
                'Jugador': player['summonerName'],
                'Campeon': player['championName'],
                'FechaCreacionPartida': game_creation,
                'ID': game_id,
                'EarlySurrender' : player['gameEndedInEarlySurrender'],
                'Ganada': player['win'],
                'Posicion' : player['individualPosition'],
                'TiempoJugado': player['timePlayed'] / 60,  # En minutos
                'OroNeto': player['goldEarned'] - player['goldSpent'] + 500,  # 500 oro inicial
                'KDA': f"{player['kills']}/{player['deaths']}/{player['assists']}",
                'CS': player['totalMinionsKilled'] + player['neutralMinionsKilled'],
                'DanoTotalCampeones': player['totalDamageDealtToChampions'],
                'GuardianesColocados': player['wardsPlaced'],
                'GuardianesEliminados': player['wardsKilled'],
                'ObjetivosTorres': player['turretKills'],
                'ObjetivosDragones': player['dragonKills'],
                'NivelRecompensa': player['bountyLevel'],
                'TiempoMaximoVivo': player['longestTimeSpentLiving'] / 60,  # En minutos
                'DanoTotalInfligidoCampeones': player['totalDamageDealtToChampions'],
                **imprimir_items(player)
            }

            # Agregar datos de desafíos
            challenge_keys = {
                'maxCsAdvantageOnLaneOpponent': "Max CS Advantage on Lane Opponent",
                'controlWardsPlaced': "Control Wards Placed",
                'damagePerMinute': "Damage per Minute",
                'damageTakenOnTeamPercentage': "Damage Taken on Team Percentage",
                'goldPerMinute': "Gold per Minute",
                'maxLevelLeadLaneOpponent': "Max Level Lead on Lane Opponent",
                'soloKills': "Solo Kills",
                'soloTurretsLategame': "Solo Turrets Late Game"
            }

            for key, description in challenge_keys.items():
                player_data[description] = player.get('challenges', {}).get(key, 0)

            return player_data

    return None

def guardar_datos_csv(datos_jugador, archivo_csv):
    # Convertir los datos en un DataFrame
    df = pd.DataFrame([datos_jugador])

    # Guardar en CSV
    # Si el archivo no existe, escribir con encabezado, si no, omitir el encabezado
    df.to_csv(archivo_csv, mode='a', header=not os.path.exists(archivo_csv), index=False)

# Ruta al archivo JSON de objetos
ruta_archivo_objetos = 'items.json' 
datos_objetos = cargar_datos_objetos(ruta_archivo_objetos)
# Crear un diccionario para mapear ID de objeto a nombre
nombres_objetos = {str(key): value['name'] for key, value in datos_objetos['data'].items()}