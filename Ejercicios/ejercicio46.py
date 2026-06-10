#46) Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.

import random

def cargarLista():

    lista=[]

    for i in range(5):
        entero = random.randint(1, 5)
        lista.insert(i,entero)

    return lista

def pintarHistograma(lista):


    for i in range(len(lista)):
        elemento=lista[i]
        for j in range(elemento):
            print("*",end=" ")
        print(end="\n")

lista=[]
lista=cargarLista()
print(lista)
pintarHistograma(lista)

