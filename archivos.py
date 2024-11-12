from funciones import cont_segura as fn


mi_password = fn.new_password()

file = open("contrasenas.txt","a")
file.write(mi_password)
file.close()
if len(mi_password)>0:
    print("Contrasena guardada")







