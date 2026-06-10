#37 Diseña un programa que pida el valor de los tres lados de un triangulo y calcule el valor de su area y perımetro.
from cmath import sqrt

lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))
lado3 = float(input("Ingrese lado 3: "))

def calcularArea(lado1, lado2,lado3):

    s=(lado1+lado2+lado3)/2
    area = sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
    return area

def calcularPerimetro(lado1,lado2,lado3):

    perimetro = lado1+lado2+lado3
    return perimetro

area = calcularArea(lado1, lado2,lado3)
perimetro=calcularPerimetro(lado1,lado2,lado3)

print("El area del triangulo es: ",f"{area.real:.2f}")
print("El perimetro del triangulo es: ",perimetro)