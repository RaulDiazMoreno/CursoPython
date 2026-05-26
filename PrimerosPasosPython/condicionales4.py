distancia = float(input("Ingrese la distancia en kilómetros: "))
ingresos = float(input("Ingrese sus ingresos anuales: "))
numero_hermanos = int(input("Ingrese el número de hermanos: "))
if distancia > 40 and numero_hermanos > 2 or ingresos < 20000:
    print("Usted es elegible para la beca.")
else:
    print("Usted no es elegible para la beca.")
    