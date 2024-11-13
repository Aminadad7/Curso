
"""
Escriba una función que reciba un string consistente de unos y ceros y retorne 
la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.
Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1
 (ya que hay 6 unos y 5 ceros)
"""

def ocurrencias(string):
  cnt_1 = 0
  cnt_0 = 0
  for i in string:
    if i == "1":
      cnt_1 += 1
    if i == "0":
      cnt_0 += 1
  return cnt_1-cnt_0 # aquí debes retornar el resultado
ocurrencias("11000110101")