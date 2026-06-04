# 30) Programa que calcule el IVA (21%) de un producto dado su precio de venta sin IVA.


def calcularIva(importe):
    return importe+(importe*21)/100

importe=float(input("Introduce el precio del producto: "))
print("El precio del producto es:",calcularIva(importe))