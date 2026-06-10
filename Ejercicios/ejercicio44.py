#44) El area A de un triangulo se puede calcular a partir del valor de dos de sus lados, a y b, y del angulo  que estos
#forman entre sı con la formula A = 12 ab sin(). Diseña un programa que pida al usuario el valor de los dos lados (en metros),
#el angulo que estos forman (en grados), y muestre el valor del area.
import math

def pasarRadianes(angulo):

    radianes = math.radians(angulo)

    return radianes

def calcularArea(lado1,lado2,angulo):

    radianes=pasarRadianes(angulo)
    seno=math.sin(radianes)
    den = lado1*lado2*seno
    area=den/2
    return area

lado1=float(input("Introduce lado 1 en metros: "))
lado2=float(input("Introduce lado 2 en metros: "))
angulo=float(input("Introduce el angulo en grados: "))

area=calcularArea(lado1,lado2,angulo)
print("El area del triangulo es: ",area)

