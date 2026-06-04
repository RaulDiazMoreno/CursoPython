#28) Programa que calcule la media de cinco numeros depositados en una lista
#y que deje el resultado en la propia lista

def cargarLista():
    lista=[]
    for i in range(5):
        numero=int(input("Introduce un numero: "))
        lista.insert(i,numero)
    return lista

def calcularMedia(lista):

    suma=0
    for elemento in lista:
        suma=suma+elemento
    media=suma/len(lista)

    lista.insert(len(lista),media)
    return lista

def mostrarLista(lista):
    for elemento in lista:
        print(elemento)


lista=[]
lista=cargarLista()
calcularMedia(lista)
mostrarLista(lista)



