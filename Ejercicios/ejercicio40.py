#40)Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o
# devuelva False de lo contrario. Escribir la función usando el bucle for anidado

import random

def cargarLista():

    lista=[];

    for i in range(5):
        entero = random.randint(1, 10)
        lista.insert(i,entero)

    return lista

def compararLista(lista1,lista2):

    tamL1=len(lista1)
    tamL2=len(lista2)
    cont=0
    for i in range(tamL1):
        for j in range(tamL2):
            if lista1[i]==lista2[j]:
                cont+=1

    return cont

lista1=cargarLista()
print(lista1)
lista2=cargarLista()
print(lista2)
cont=compararLista(lista1,lista2)

if cont>0:
    print("Las lista tiene",cont," elementos en comun")
else:
    print("Las lista no tiene ningun elemento en comun")
