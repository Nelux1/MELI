import requests

def obtener_mejor_serie_por_genero(genero):
    # Límite de páginas a consultar
    limite_paginas = 15
    
    for pagina in range(1, limite_paginas + 1):
        url = f"https://jsonmock.hackerrank.com/api/tvseries?page={pagina}"
        response = requests.get(url)
        data = response.json()['data']

        # Filtrar series por género
        series_por_genero = [serie for serie in data if genero.lower() in serie['genre'].lower()]

        if series_por_genero:
            # Encontrar la serie con la calificación IMDb más alta
            mejor_serie = max(series_por_genero, key=lambda x: (x['imdb_rating'], x['name']))
            return mejor_serie

    # Si no se encuentra el género después de consultar todas las páginas
    return None

# Solicitar al usuario ingresar el género
genero_busqueda = input("\nIngrese el género de la serie de televisión que desea buscar:  ")

# Obtener y mostrar la mejor serie por género
mejor_serie = obtener_mejor_serie_por_genero(genero_busqueda)
if mejor_serie:
    print()
    print(mejor_serie['name'])
else:
    print("No se encontró el género de series de televisión después de consultar todas las páginas.")
