"""
Escribe una función que reciba dos strings (de largo > 2) como parámetros,
 y retorne un string de largo 4 que consista de las dos primeras letras del primer string
   y las últimas dos letras del segundo.

Por ejemplo, si los strings son "familia" y "abrigarse", 
entonces tu función debe retornar "fase".
"""
def mezclador(string_a, string_b):
  # aquí debes escribir el código de tu programa
  #na = len(string_a)
  n = len(string_b)
  a=string_a[0:2]
  b=string_b[n-2:n]
  return a+b # aquí debes retornar el resultado
mezclador("familia","abrigarse")