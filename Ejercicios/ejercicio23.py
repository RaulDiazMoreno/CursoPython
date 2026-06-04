#19)Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa
# principal que lea el radio de una circunferencia y muestre su área y perímetro.

def areaPerimetroCircunferencia(r):

    pi=3.1416
    print("El área de la circunferencia es: ",(r*r)*pi)
    print("El perimetro de la circunferencia es: ", 2*r*pi)


radio=float(input("Ingrese el valor de la radio: "))
areaPerimetroCircunferencia(radio)


