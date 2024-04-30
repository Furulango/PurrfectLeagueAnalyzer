import json

def cargar_datos_objetos(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def imprimir_items(player, ruta_archivo_objetos):
    # Cargar datos de objetos desde el archivo JSON
    datos_objetos = cargar_datos_objetos(ruta_archivo_objetos)

    # Crear un diccionario para mapear ID de objeto a nombre
    nombres_objetos = {str(key): value['name'] for key, value in datos_objetos['data'].items()}

    items = []
    for i in range(7):
        item_id = str(player.get(f'item{i}', ''))
        item_name = nombres_objetos.get(item_id, 'Objeto desconocido')
        items.append(f"Item {i}: {item_name}")
    
    return items

# Ruta al archivo JSON de objetos
ruta_archivo_objetos = 'items.json'
player = {
    'item0': '3070',
    'item1': '3071',
    'item2': '3080',
    'item3': '3081',
    'item4': '3000',
    'item5': '1001',
    'item6': '1018',
}
resultado = imprimir_items(player, ruta_archivo_objetos)
print(resultado)
