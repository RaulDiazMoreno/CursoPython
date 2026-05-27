# Bucle While
import math

# contador = 1
# while contador <= 10:
#     print(f"Valor del contador: {contador}")
#     contador += 1 

# edad = int(input("Introduce tu edad: "))
# while edad < 0 or edad > 120:
#     print("Edad no válida, introduce una edad entre 0 y 120")
#     edad = int(input("Introduce tu edad: "))
# print(f"Edad válida: {edad}")

print("Programa de calculo de una raiz cuadrada")
numero = int(input("Introduce un numero: "))

intentos = 0
while numero < 0:
    print("No se pueden calcular raices cuadradas de numeros negativos")
    if intentos == 2:
        print("Demasiados intentos, el programa se cerrará")
        break
    numero = int(input("Introduce un numero: "))
    if numero < 0:
        intentos += 1
    if intentos < 2:
        solucion = math.sqrt(numero)
        print(f"La raiz cuadrada de {numero} es {solucion}")
    
    
    
    

