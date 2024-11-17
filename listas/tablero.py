
tablero = [[' ', 'X', ' ', 'X'],
           ['X', ' ', ' ', ' '],
           [' ', 'X', 'X', ' '],
           ['X', ' ', ' ', 'X']]

for i in range(len(tablero)):
    for j in range(len(tablero)):
        tablero[i][j] = input(f'Introduce un objeto en la posicion{i,j}')
print(tablero)

