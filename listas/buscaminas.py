

def buscaminas(tablero, i, j):
    # Dimensiones del tablero
    filas = len(tablero)
    columnas = len(tablero[0]) if filas > 0 else 0

    # Lista de movimientos para las posiciones vecinas
    movimientos = [
        (-1, -1), (-1, 0), (-1, 1),  # Vecinos superiores
        (0, -1),         (0, 1),     # Vecinos laterales
        (1, -1), (1, 0), (1, 1)      # Vecinos inferiores
    ]
    
    # Contador de bombas
    bombas = 0

    # Verificar cada posición vecina
    for dx, dy in movimientos:
        nueva_i, nueva_j = i + dx, j + dy
        if 0 <= nueva_i < filas and 0 <= nueva_j < columnas:  # Dentro del tablero
            if tablero[nueva_i][nueva_j] == "X":
                bombas += 1

    return bombas

# Ejemplo de uso
tablero = [
    [' ', 'X', ' ', 'X'],
    ['X', ' ', ' ', ' '],
    [' ', 'X', 'X', ' '],
    ['X', ' ', ' ', 'X']
]

# Pruebas
print(buscaminas(tablero, 0, 0))  
print(buscaminas(tablero, 1, 1))