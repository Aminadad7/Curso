"""
funciones
    len() = longitud de la lista
    in = saber si esta un elemento en la lista
    lista.index('elemento') = conocer la posicion de un elemento
    string.split convierte el string en una lista
    lista.sort = ordena la lista en forma alfabetica o de menor a mayor
"""
#CONVERTIR STR EN LISTA con ciclo

texto = input("Ingresa una lista")
print("Primero",texto[0])
print("String:",texto)
lista = []
inicio = 0
for i in range(0,len(texto)):
    if texto[i] == ",":
        lista.append(texto[inicio:i])
        inicio = i+1
lista.append(texto[inicio:])
#lista.sort()
print("Lista original:",lista)

print(" \nAhora con split")
#CONVERTIR STR EN LISTA con split.  string.split
lista2 = texto.split(",")
lista2.sort()
print("Ordenada:",lista2)
print()
datos = ["semillas", 500, "cerveza", 2, "despacho", 4100, "pago", "bitcoin", "confianza", 95.4]
trozo = datos[1:9:2]
print(trozo)

tablero = [ [1,2,3], [4,5,6], [7,8,9] ]
for j in range(3):
  for i in range(3):
    print(tablero[j][i],end=" ")
for i in range(9):
  print(tablero[i%3][i//3],end=" ")

contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")
print(splitted)

unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
muestra = unidades[2:3] + unidades[3:7:3] + unidades[7:8]
print(muestra)