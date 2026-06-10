#33)El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado.
#Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:
#EsBisiesto: Recibe un año y nos dice si es bisiesto.
#Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.
#Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.
from operator import truediv


def comprobarBisiesto(ano):

    if ano%4==0 and ano%100!=0 or ano%400==0:
        return True
    else:
        return False


def validarFecha(dia,mes,ano):

    print(ano)
    print(mes)
    print(dia)
    if ano <= 0:
        print("El año es negativo")
        return False
    else:
        if mes == 2:
            if dia==28:
                return True
            if dia > 28:
                esBisiesto = comprobarBisiesto(ano)
                print("El año es Febrero")
                if esBisiesto == True:
                    return True
                else:
                    return False
            else:
                return False
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia<31:
                print("El mes tiene 31")
                return True
            else:
                return False
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia<30:
                print("El mes tiene 30")
                return True
            else:
                return False


def calcularDiaJuliano(dia,mes,ano):

    if mes==1 or mes==2:
        ano = ano-1
        if mes==1:
            mes=13
        if mes==2:
            mes=14

    parteA = 367*ano
    parteB = (7*(ano+5001+(mes/4)))/4
    parteC=(275*mes)/9

    diaJuliano = parteA - parteB + parteC+dia+1721028.5

    return diaJuliano

dia = int(input("Ingrese dia: "))
mes = int(input("Ingrese mes: "))
ano = int(input("Ingrese anos: "))

esValida=validarFecha(dia,mes,ano)
if esValida == True:
   esBisiesto=comprobarBisiesto(ano)
   diaJuliano=calcularDiaJuliano(dia,mes,ano)
   if esBisiesto == True:
       print("El año es Bisiesto")
   else:
       print("El año NO es Bisiesto")
   print("El dia Juliano correspondiente es: ",diaJuliano)
else:
   print("Vete a tomar por el culo")


