from funciones import cont_segura as fn


def escribir_archivo(texto):
    mi_password = fn.new_password()
    file = open(texto,"a")
    file.write(mi_password)
    file.close()
    if len(mi_password)>0:
        print("Contrasena guardada")
        return mi_password
    
escribir_archivo("contrasenas.txt")







