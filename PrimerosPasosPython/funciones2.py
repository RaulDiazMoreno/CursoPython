# Funciones con parámetros
def suma(a, b):
    return a + b    

def resta(a, b):
    resta = a - b
    print ("El resultado de la resta es:", resta)

def multiplicacion(a, b):
    return a * b;

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir por cero.")
        return None

resultado = suma(5, 3)
print("El resultado de la suma es:", resultado)
print("El resultado de la multiplicación es:", multiplicacion(5, 3))
print("El resultado de la división es:", division(5, 3))
