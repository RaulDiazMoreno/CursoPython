#19)Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.


def esMultiplo(numero1, numero2):
    if numero1 % numero2 == 0:
        print("El numero2 es multiplo del numero1")
    elif numero2 % numero1 == 0:
        print("El numero1 es multiplo del numero2")
    else:
        print("Que te den por culo")


numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

esMultiplo(numero1, numero2)
