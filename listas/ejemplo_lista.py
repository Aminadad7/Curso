"""
    Los pricipales metodos usados con listas so:
    lista = ["amor","paz","misericordia"]
        lista.append("elemnte") = agrega elemento al final de la lista
        lista.pop() = Elimina el ultimo elemento de la lista y lo entrega como un valor de retorno
        lista.insert(index,elemento) = inserta un elemento en la lista en la posicion provista
        lista.remove("amor") = elimina un elemente pasado como parametro
        lista.extend(['1',3]) = agrega los elementos de una lissta dada a la lista anterior
            ejemplo ahora lista sera igual a: ["amor","paz","misericordia","1",3]
"""

my_lista = ["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
print("Valor original=",my_lista)
my_lista.append("otro_dia")
print("Valor despues de appedn=",my_lista)
obj = my_lista.pop()
print(obj)
print("Valor despues de pop()=",my_lista)
my_lista.insert(3,"intruso")
print("Valor despues de insert(3,'intruso')=",my_lista)
my_lista.remove("intruso")
print("Valor despues de remove('intruso')=",my_lista)
new_list = ["nuevo","intruso",535]
my_lista.extend(new_list)
new = my_lista + new_list
print(new)
print()
print(new_list)
