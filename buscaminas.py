import random

def contar_minas_vecinas(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    conteo_minas_vecinas = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] == 1:  # Si es una mina, se establece como 9
                conteo_minas_vecinas[i][j] = 9
            else:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i + di < filas and 0 <= j + dj < columnas and tablero[i + di][j + dj] == 1:
                            conteo_minas_vecinas[i][j] += 1
    
    return conteo_minas_vecinas

def ingresar_tablero(filas, columnas):
    tablero = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            valor = int(input("Ingrese el valor (0 para vacío, 1 para mina): "))
            fila.append(valor)
        tablero.append(fila)
    return tablero

def generar_tablero_aleatorio(filas, columnas, minas):
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    # Colocar minas aleatoriamente
    for _ in range(minas):
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        while tablero[fila][columna] == 1:  # Si ya hay una mina, elige otra posición
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
        tablero[fila][columna] = 1  # Coloca la mina
    
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

# Ejemplo de uso:
filas = int(input("Ingrese el número de filas del tablero: "))
columnas = int(input("Ingrese el número de columnas del tablero: "))
minas = int(input("Ingrese el número de minas: "))

tablero = generar_tablero_aleatorio(filas, columnas, minas)

print()
print("Tablero con minas (1) y espacios vacíos (0):")
print()
imprimir_tablero(tablero)
print()

print("\nTablero con el número de minas adyacentes:")
tablero_resultado = contar_minas_vecinas(tablero)
print()
imprimir_tablero(tablero_resultado)
