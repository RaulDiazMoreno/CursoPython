#42) Diseña un programa que pida el valor de la base y la altura de un triangulo y muestre el valor de su area.

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

def calcularArea(base,altura):

    area = (base * altura)//2
    return area

area = calcularArea(base, altura)
print("El area del triangulo es: ", area)