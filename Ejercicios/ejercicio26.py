#22)Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:
#Se divide el número mayor entre el menor.
#Si la división es exacta, el divisor es el MCD.
#Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una
# división exacta, siendo el último divisor el MCD.
#Crea un programa principal que lea dos números enteros y muestre el MCD.


def calculoMCD(numero1,numero2):
    if numero1>numero2:
        if numero1%numero2==0:
            return numero2
        else:
            resto=numero1%numero2;
            while(resto!=0):
                if numero2 % resto == 0:
                    return resto
                else:
                    resto = numero2 % resto

    elif numero2>numero1:
            if numero2%numero1==0:
                return numero1
            else:
                resto=numero2%numero1
                while (resto != 0):
                    if numero1 % resto==0:
                        return resto
                    else:
                        resto=numero1%resto

numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese otro numero: "))

mcd = calculoMCD(numero1,numero2)
print("El valor del MCD es: ",mcd)

