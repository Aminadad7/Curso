
# La función utiliza un bucle while que continúa mientras n2 no sea cero.
# En cada iteración, asigna a n1 el valor de n2, y a n2 el residuo de n1 dividido por n2.
# Cuando n2 se convierte en cero, el valor de n1 es el MCD de los dos números.
print("""  
    Calcula el máximo común divisor de dos números enteros positivos.  
    
    Args:  
        n1 (int): Primer número entero positivo.  
        n2 (int): Segundo número entero positivo.  
    
    Returns:  
        int: El máximo común divisor de n1 y n2.  
    """ ) 

def mcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

# Ejemplo de uso
print(mcd(10, 15))