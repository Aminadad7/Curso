

def reemplazo(string):
  for i in string:
    if i.isupper():
      salida = string.replace(i,"$")
  return salida # aquí debes retornar el resultado
reemplazo("Viva la Vida")