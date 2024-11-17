"""
Pregunta 2
Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser: 
azul, rojo, verde y amarillo. Desea saber cual de esos colores es el que más se repite. 
Escriba una función color_frecuente 
que reciba como argumento a una lista de strings llamada lista y
 retorne el string más repetido y el número de ocurrencias del mismo.

Por ejemplo para la lista ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']

Debe retornar: "verde", 8

En caso de que haya varios colores con el máximo número, 
se retornará con la siguiente prioridad: azul, rojo, verde, amarillo. 
Es decir, por ejemplo si la lista es l = ['rojo', 'rojo', 'azul', azul'], 
la función debe retornar "azul", 2
"""
def color_frecuente(lista):
    # Prioridad de colores en caso de empate
    prioridad = ['azul', 'rojo', 'verde', 'amarillo']
    
    # Contar las ocurrencias de cada color
    conteo = {color: lista.count(color) for color in prioridad}
    
    # Encontrar el color más repetido basado en la prioridad
    color_max = max(prioridad, key=lambda color: conteo[color])
    max_ocurrencias = conteo[color_max]
    
    return color_max, max_ocurrencias

# Ejemplo de uso
lista = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 
         'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
resultado = color_frecuente(lista)
print(resultado)  # Salida: ("verde", 8)

"""
    Explicación:
1. Definir la prioridad: Se usa una lista prioridad que define el orden a seguir en caso de empate.
2. Contar ocurrencias: Se utiliza una comprensión de diccionario para contar cuántas veces aparece cada color en lista.
3. Determinar el color más frecuente: La función max() con un key personalizado compara los valores en el diccionario conteo según la prioridad. 
    Esto asegura que el desempate siga el orden dado.
4. Retornar el color y su cantidad: Devuelve el color más repetido y el número de ocurrencias
"""