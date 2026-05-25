#Creación de una tupla
mitupla=("Juan",13,1,1995)
print(mitupla)

#Acceder a un elemento de la tupla
print(mitupla[1])
#Comprobar si un elemento está en la tupla
print(13 in mitupla)
#Averiguar cuantos elementos tiene la tupla
print(len(mitupla))
#Averiguar cuantas veces aparece un elemento en la tupla
print(mitupla.count(13))
#Crear tuplas con un solo elemento(unitarias)
tupla_un_elemento=(5,)
print(tupla_un_elemento)
#Crear tuplas sin paréntesis(empaquetado de tuplas)
otra_tupla=1, 2, 3 
print(otra_tupla) 
#Desempaquetado de tuplas
nombre, dia, mes, año = mitupla
print("Nombre:", nombre)
print("Día:", dia)      
print("Mes:", mes)
print("Año:", año)
#Conversión de una tupla a una lista
milista=list(mitupla)
print(milista)
#Convertir la lista de nuevo a una tupla
mitupla2=tuple(milista)
print(mitupla2)
#index en una tupla
print(mitupla[0])






