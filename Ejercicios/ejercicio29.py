#29) Programa que calcule la varianza de cinco numeros depositados en una lista
# y que deje el resultado en la propia lista

def cargarLista():
    lista=[]
    for i in range(6):
        numero=int(input("Introduce un numero: "))
        lista.insert(i,numero)
    return lista

def calcularMedia(lista):

    suma=0
    for elemento in lista:
        suma=suma+elemento

    media=suma/len(lista)
    print("La media es:",media)
    return media

def sumaCuadradoResiduo(lista,media):

    suma=0
    for elemento in lista:
        suma=suma+(elemento-media)**2
    print("La suma de los cuadrados es: ",suma)
    return suma

def calcularVarianza(cuadrado,lista):

    tamlista=len(lista)
    print("El tamaño es:",tamlista)
    return cuadrado//(tamlista-1)


lista=[]
lista=cargarLista()
media=calcularMedia(lista)
cuadrado=sumaCuadradoResiduo(lista,media)
varianza=calcularVarianza(cuadrado,lista)
print("La varianza es:",varianza)







