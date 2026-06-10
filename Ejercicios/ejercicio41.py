#41) Diseña un programa que pida el valor de los dos lados de un rectangulo y muestre el valor de su perımetro y el de su
#area.


lado1 = float(input("Ingrese base rectangulo: "))
lado2 = float(input("Ingrese altura rectangulo: "))

def calcularPerimetro(lado1, lado2):

    perimetro = 2*(lado1 + lado2)
    return perimetro

def calcularArea(lado1, lado2):

    area = lado1*lado2
    return area

perimetro=calcularPerimetro(lado1,lado2)
print("El valor del perimetro del rectangulo es: ", perimetro)
area=calcularArea(lado1,lado2)
print("El valor del area del rectangulo es: ", area)
