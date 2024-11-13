"""
    Escriba una función que reciba dos strings como parámetros y 
    retorne un nuevo string que consista del primero, pero con el segundo 
    string intercalado entre cada letra del primero.
    Por ejemplo si los strings son "paz" y "so", entonces tu función debe retornar "psoasozso"

"""

def intercalar(string_a, string_b):
  result = ''
  for i in string_a:
    result += i+string_b  
  return result # aquí debes retornar el resultado
intercalar("paz","so")