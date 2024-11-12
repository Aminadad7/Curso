def leer_archivo(texto):
    file = open(texto,"r")
    leer = file.readlines()
    for i in leer:
        passw = i.split("\n")
        print(passw)