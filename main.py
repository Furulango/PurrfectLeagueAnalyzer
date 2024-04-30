from api_requests import get_puuid, get_soloq_match_history, get_match_details
from data_processing import process_and_store_matches, analizar_jugador_especifico, agregar_nuevas_partidas_a_csv
import os
import pandas as pd 

# Ejemplo de uso
api_key = "RGAPI-0352b742-da9e-48d4-8c59-3691aa07057f"
game_name = "Aerlik"
tag_line = "LAN"
num_games = 100
directory = f'matches/{game_name}'
archivo_csv = f'matches/{game_name}/analisis_partidas.csv'

# Obtener PUUID
puuid = get_puuid(game_name, tag_line, api_key)
if not puuid:
    print("No fue posible obtener el PUUID. Por favor, verifica los datos del invocador.")
else:
    # print(f"PUUID: {puuid}")

    # Crear directorio si no existe
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Obtener y procesar el historial de partidas
    soloq_match_history = get_soloq_match_history(puuid, num_games, api_key)
    if soloq_match_history:
        process_and_store_matches(soloq_match_history, api_key, directory)

        # Analizar cada partida y almacenar los resultados
        all_partidas_data = []
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                partida_data = analizar_jugador_especifico(os.path.join(directory, filename), puuid)
                if partida_data:
                    all_partidas_data.append(partida_data)

        archivo_csv = f'matches/{game_name}/analisis_partidas.csv'
        agregar_nuevas_partidas_a_csv(all_partidas_data, archivo_csv)

        print(f"Análisis completado. Total de partidas analizadas: {len(all_partidas_data)}")
    else:
        print("No se encontraron partidas para analizar.")
