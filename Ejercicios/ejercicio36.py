#36) Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max(numero1,numero2,numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    else:
        return numero3


numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("Ingrese el tercer numero: "))

print("El numero mayor de los tres es: ",max(numero1,numero2,numero3))

