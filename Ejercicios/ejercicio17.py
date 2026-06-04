#17)Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores
# El programa finalizará cuando se introduce un número menor que el anterior.

numeroAnterior=0
numero = int(input("Ingrese un numero: "))
while numero>numeroAnterior:
    numeroAnterior = numero
    numero = int(input("Ingrese un numero: "))