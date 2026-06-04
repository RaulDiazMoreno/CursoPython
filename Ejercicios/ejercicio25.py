#25)Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado5
#del factorial.

def factorial(i):
    if i==0:
        return 1
    else:
        return i*factorial(i-1)


numero=int(input("Ingrese un numero: "))

print(factorial(numero));
