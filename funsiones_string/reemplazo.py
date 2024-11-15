
"""
Escriba una función que reciba un string como parámetro y retorne el string,
 pero con cada elemento que estuviese en mayúsculas reemplazado por "$". 
Asuma que el string consistirá solamente de letras.
Por ejemplo si el string es "Viva la Vida", 
entonces tu función debe retornar "$iva la $ida".
"""
def reemplazo(string):
  for i in string:
    if i.isupper():
      salida = string.replace(i,"$")
  return salida # aquí debes retornar el resultado
reemplazo("Viva la Vida")