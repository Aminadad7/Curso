def leer_archivo(texto):
    file = open(texto,"r")
    leer = file.readlines()
    for i in leer:
        print(f"{i.replace('\n','')}")

leer_archivo("contrasenas.txt")