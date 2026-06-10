#45) Haz un programa que pida al usuario una cantidad de euros, una tasa de interes y un numero de anos. Muestra
#por pantalla en cuanto se habria convertido el capital inicial transcurridos esos años si cada año se aplica la tasa
# de interes introducida.
#Recuerda que un capital de C euros a un interes del x por cien durante n años se convierten en C · (1 + x/100)n euros.
#(Prueba tu programa sabiendo que una cantidad de 10 000 al 4.5% de inter´es anual se convierte en 24 117.14 al cabo
#de 20 años.)

def calcularBeneficios(euros,interes,anyos):

    beneficios=euros*(1+(interes/100))**anyos

    return beneficios


euros=float(input("Ingrese una cantidad en Euros: "))
interes=float(input("Introduce tasa de interes: "))
anyos=int(input("Introduce años: "))

beneficios=calcularBeneficios(euros,interes,anyos)
print("Los beneficios que obtendriamos con esas condiciones: ",beneficios)



