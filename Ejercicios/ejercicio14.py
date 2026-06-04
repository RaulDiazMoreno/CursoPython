#14) Crea un programa que devuelva el cambio exacto de una cantidad introducida por pantalla

cantidad = float(input("Introduce tu cantidad de monedas: "))

billete500=0.0
billete200=0.0
billete100=0.0
billete50=0.0
billete20=0.0
billete10=0.0
billete5=0.0
moneda2=0.0
moneda1=0.0
moneda05=0.0
moneda02=0.0
moneda01=0.0
moneda005=0.0
moneda002=0.0
moneda001=0.0

while cantidad>0:
    if cantidad>=500:
        billete500 = cantidad//500
        resto = cantidad%500
        cantidad = resto
    elif cantidad>=200:
        billete200 = cantidad//200
        resto = cantidad%200
        cantidad = resto

    elif cantidad>=100:
        billete100 = cantidad//100
        resto = cantidad%100
        cantidad = resto

    elif cantidad>=50:
        billete50 = cantidad//50
        resto = cantidad%50
        cantidad = resto

    elif cantidad>=20:
        billete20 = cantidad//20
        resto = cantidad%20
        cantidad = resto
    elif cantidad>=10:
        billete10 = cantidad//10
        resto = cantidad%10
        cantidad = resto
    elif cantidad>=5:
        billete5 = cantidad//5
        resto = cantidad%5
        cantidad = resto
    elif cantidad>=2:
        moneda2 = cantidad//2
        resto = cantidad%2
        cantidad = resto
    elif cantidad>=1:
        moneda1 = cantidad//1
        resto = cantidad%1
        cantidad = resto
    elif cantidad>=0.5:
        moneda05 = cantidad//0.5
        resto = cantidad%0.5
        cantidad=resto
    elif cantidad>=0.2:
        moneda02 = cantidad//0.2
        resto = cantidad%0.2
        cantidad=resto
    elif cantidad>=0.1:
        moneda01 = cantidad//0.1
        resto = cantidad%0.1
        cantidad=resto
    elif cantidad>=0.05:
        moneda005 = cantidad//0.05
        resto = cantidad%0.05
        cantidad=resto
    elif cantidad>=0.02:
        moneda002 = cantidad//0.02
        resto = cantidad%0.02
        cantidad=resto
    else :
        if(cantidad>0.01):
            moneda001 = cantidad // 0.01
        else:
            moneda001 = 1.0;
        break


print("Tu cambio es: ")
print("Billetes de 500 €: " + str(billete500))
print("Billetes de 200 €: " + str(billete200))
print("Billetes de 100 €: " + str(billete100))
print("Billetes de 50 €: " + str(billete50))
print("Billetes de 20 €: " + str(billete20))
print("Billetes de 10 €: " + str(billete10))
print("Billetes de 5 €: " + str(billete5))
print("Monedas 2 € : " + str(moneda2))
print("Monedas 1 € : " + str(moneda1))
print("Monedas 0.5 € : " + str(moneda05))
print("Monedas 0.2 € : " + str(moneda02))
print("Monedas 0.1 € : " + str(moneda01))
print("Monedas 0.05 € : " + str(moneda005))
print("Monedas 0.02 € : " + str(moneda002))
print("Monedas 0.01 € : " + str(moneda001))


