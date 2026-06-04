#18)Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
#Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def rellenarLista():

    numero=int(input("Ingrese el numero de elementos de la lista: "))

    i=0
    lista=[]
    while i<numero:
        valor=int(input("Ingrese el numero: "))
        lista.insert(i,valor)
        i=i+1
    return lista


def calcularMaxMin(lista):
    maxi=0
    mini=99999999
    for elemento in lista:
        if elemento>maxi:
            maxi=elemento
        if elemento<mini:
            mini=elemento
    print("El maximo es: ",maxi)
    print("El minimo es: ",mini)

lista=rellenarLista()
calcularMaxMin(lista)
