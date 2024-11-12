def new_password():
    print("\n***********CREANDO CONTRASENA SEGURA**************")
    caracteres = "@#$%&*._"
    numeros = "0123456789"
    has_number = False
    has_char = False
    while True:
        password = input("\nIntroduce una contrasena segura: ")
        if len(password) >= 8:
            for i in numeros:
                if i in password:
                    has_number = True
                else:
                    continue
            for i in caracteres:
                if i in password:
                    has_char = True
                else:
                    continue
            if has_number == False or has_char == False:
                print("\n \033[31mTu contrasena no es segura,\ndebe tener numeros y caracteres especiales\033[0m")
            else:
                return password
        else:
             print("Tu contrasena  debe tener minimo 8 caracter")
