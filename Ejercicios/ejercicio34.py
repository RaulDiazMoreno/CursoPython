# 34)Queremos crear un programa que realice calculos de fracciones
from contextlib import nullcontext

from CursoPython.PrimerosPasosPython.funciones2 import multiplicacion

def hallarMultiplos(denominador):

    multiplos=[]
    i=denominador
    x = 0
    for i in range(denominador,100):
        if i%denominador == 0:
            multiplos.insert(x,i)
            x=x+1

    return multiplos

def calculoMcm(multiplosA,multiplosB):

    multiplosComunes=[]
    x=0
    tamI = len(multiplosA)
    tamJ = len(multiplosB)
    for i in range(tamI):
        for j in range(tamJ):
            if multiplosA[i] == multiplosB[j]:
                multiplosComunes.insert(x,multiplosB[j])
                x=x+1

    if len(multiplosComunes)>0:
        return multiplosComunes[0]
    else:
        return 1

def hallarMcm(denominadorA,denominadorB):
    multiplosA=[]
    multiplosA=hallarMultiplos(denominadorA)
    multiplosB = []
    multiplosB=hallarMultiplos(denominadorB)

    return calculoMcm(multiplosA,multiplosB)

def sumaFracciones(numeradorA, numeradorB, denominadorA, denominadorB):

    numeradorS=0
    denominadorS=0
    if denominadorA == denominadorB:
        numeradorS = numeradorA + numeradorB
        denominadorS = denominadorA + denominadorB
    else:
        mcm =  hallarMcm(denominadorA,denominadorB)
        numeradorS = numeradorA + numeradorB
        denominadorS = mcm

    print("La suma de fracciones es: ", numeradorS,"/",denominadorS)

def restaFracciones(numeradorA, numeradorB, denominadorA, denominadorB):

    if denominadorA == denominadorB:
        numeradorS = numeradorA - numeradorB
        denominadorS = denominadorA
    else:
        mcm =  hallarMcm(denominadorA,denominadorB)
        numeradorR = numeradorA - numeradorB
        denominadorR = mcm

    print("La resta de fracciones es: ", numeradorR,"/",denominadorR)

def multiplicacionFracciones(numeradorA, numeradorB, denominadorA, denominadorB):
    numeradorM = numeradorA * numeradorB
    denominadorM = denominadorA * denominadorB
    print("La multiplicacion de fracciones es: ", numeradorM, "/", denominadorM)

def divisionFracciones(numeradorA, numeradorB, denominadorA, denominadorB):
    numeradorD = numeradorA * denominadorB
    denominadorD = denominadorA * numeradorB

    print(numeradorD)
    print(denominadorD)
    if numeradorD > denominadorD:
        numeradorI = numeradorD//denominadorD
        numeradorI2 = numeradorD-(numeradorI*denominadorD)
        print("La division de fracciones es: ", numeradorI, numeradorI2, "/", denominadorD)
    else:
        print("La division de fracciones es: ", numeradorD, "/", denominadorD)



print("Fraccion A")
print("----------")
numeradorA = int(input("Ingrese un numerador: "))
denominadorA = int(input("Ingrese un denominador: "))

print("Fraccion B")
print("----------")
numeradorB = int(input("Ingrese un numerador: "))
denominadorB = int(input("Ingrese un denominador: "))

print("Que quieres hacer?")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")
print("5.Salir")
opcion = int(input("Elige opcion: "))

if opcion == 1:
    sumaFracciones(numeradorA,numeradorB,denominadorA,denominadorB)
elif opcion == 2:
    restaFracciones(numeradorA,numeradorB,denominadorA,denominadorB)
elif opcion == 3:
    multiplicacionFracciones(numeradorA,numeradorB,denominadorA,denominadorB)
elif opcion == 4:
    divisionFracciones(numeradorA,numeradorB,denominadorA,denominadorB)
else:
    print("Vete a tomar por el culo")

