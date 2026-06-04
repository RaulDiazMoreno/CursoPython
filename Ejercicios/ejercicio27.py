#27) Escribir dos funciones que permitan calcular:
#La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos,
# convertir a horas,minutos y segundos o salir del programa.

def convertirEnSegundos():
    hora=int(input("Introduce hora: "))
    minutos=int(input("Introduce minutos: "))
    segundos=int(input("Introduce segundos: "))

    segundosH=(hora*60)*60
    segundosM=minutos*60
    segundosT=segundosH+segundosM+segundos

    return segundosT

def convertirEnHorasMinutosSegundos():

    segundos=int(input("Introduce segundos: "))
    horas=segundos//3600
    minutos=(segundos%3600)//60
    segundos=(segundos%3600)%60

    return horas,":",minutos,":",segundos

print("Conversor de tiempo")
print("1.Convertir en segundos")
print("2.Convertir en horas/minutos/segundos")
print("3.Salir")

opcion=int(input("Ingrese su opcion: "))

if opcion==1:
    print("Numero de segundos: ",convertirEnSegundos())
elif opcion==2:
    print(convertirEnHorasMinutosSegundos())
else:
    print("Vete a tomar por el culo")
