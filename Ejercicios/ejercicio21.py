#16)Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
#Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada
# día y vaya mostrando la media.
#El programa pedirá el número de días que se van a introducir.

def temperaturaMedia(maxima,minima):
    temperatura=(maxima+minima)/2
    return temperatura

dias = int(input("Ingrese la cantidad de dias: "))
i=0;
while i<dias:
    maxima=float(input("Ingrese la temperatura maxima: "))
    minima=float(input("Ingrese la temperatura minima: "))
    print("La temperatura media del día",i,"es: ",temperaturaMedia(maxima,minima))
    i=i+1
