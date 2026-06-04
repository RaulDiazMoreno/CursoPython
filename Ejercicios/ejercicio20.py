# 20 )Crea un programa que devuelva todos los multiplos de un numero

numero = int(input("Ingresa un numero: "))
i=1
print("Los multiplos de",numero,"son :")
while i<=numero:
    if numero % i == 0:
        print(i)
    i=i+1

