#31) Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])debería devolver 24.

def sum(lista):
    suma=0;

    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma

def multiplicacion(lista):
    multiplicacion=1;
    for i in range(len(lista)):
        multiplicacion=multiplicacion*lista[i]
    return multiplicacion

def cargarLista():
    lista=[]
    num=int(input("Ingrese numeros de la lista para acabar escribe 0: "))
    i=0;
    while(num!=0):
        lista.insert(num,i)
        i=i+1
        num = int(input("Ingrese numeros de la lista para acabar escribe 0: "))


    return lista

lista=[1,2,3,4,5]
#lista=cargarLista()
suma=sum(lista)
multi=multiplicacion(lista)

print("La suma de los elementos de la lista es: ",suma)
print("La multiplicacion de la lista es: ",multi)