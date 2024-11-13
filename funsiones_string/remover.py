"""
Escriba una función que reciba un string s y un número n como parámetros y retorne el mismo string s pero sin el elemento en el índice n.
Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego".
Hint: cuidado con aquellos casos en los que se tenga que eliminar un elemento de los bordes.

"""

def remover_enesimo(s, n):
  result = s.replace(s[n],'')
  return result # aquí debes retornar el resultado
remover_enesimo("Hasta luego",3)