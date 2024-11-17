"""
    Escriba una función de nombre promedio_std(). La función debe recibir una 
    lista de números 
    llamada lista, 
    y debe retornar retornar el promedio de ellos, 
    junto con su desviación estándar.

    Hint 1: La desviación estándar corresponde a la raíz de la suma de los cuadrados 
    de las diferencias de cada elemento respecto al promedio, 
    divididos por la cantidad de elementos.
"""
import math
def promedio_std(lista):
    nums = 0
    for num in lista:
        nums += num
    promedio = nums/len(lista)
    
    varianza = sum((x - promedio) ** 2 for x in lista) / len(lista)
    desviacion_estandar = math.sqrt(varianza)

    return promedio, desviacion_estandar
print("Promedio:","Desv: ",promedio_std([70, 80, 85, 90, 100]))

#OTRA FORMA DE HACERLO CON LA FUNCION sum()
# def promedio_std(lista):
#     # Validar que la lista no esté vacía
#     if len(lista) == 0:
#         return "La lista está vacía, no se puede calcular."
    
#     # Calcular el promedio
#     promedio = sum(lista) / len(lista)
    
#     # Calcular la desviación estándar
#     varianza = sum((x - promedio) ** 2 for x in lista) / len(lista)
#     desviacion_estandar = math.sqrt(varianza)
    
#     return promedio, desviacion_estandar

# # Ejemplo de uso
# numeros = [70, 80, 85, 90, 100]
# promedio, desviacion = promedio_std(numeros)
# print(f"Promedio: {promedio}")
# print(f"Desviación estándar: {desviacion}")