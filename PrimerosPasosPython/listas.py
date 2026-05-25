#Ejemplos de listas en Python(arrays)
#Crear una lista de frutas
frutas = ["manzana", "banana", "naranja", "uva"] 
#Imprime la lista completa
print(frutas[:]) 
#Acceder a una porción de la lista
print(frutas[1:3])
#Acceder desde el final de la lista
print(frutas[-2:])
#Acceder a los ultimos elementos de la lista
print(frutas[-2:])
#Acceder a un elemento específico de la lista
print(frutas[1])
#Modificar un elemento de la lista  
frutas[2] = "pera"
print(frutas)   
#Agregar un nuevo elemento a la lista
frutas.append("kiwi")
print(frutas)
#Agregar un nuevo elemento en una posición específica
frutas.insert(1, "fresa")
print(frutas)
#Agregar varios elementos a la lista
frutas.extend(["melón", "sandía"])
print(frutas)
#Devolver el indice de un elemento en la lista
print(frutas.index("uva"))     
#Comprobar si un elemento está en la lista
print("banana" in frutas)
#Almacenar en una lista distintos tipos de datos
mi_lista = ["texto", 123, 3.14, True]   
print(mi_lista)
#Eliminar un elemento de la lista
frutas.remove("banana")
print(frutas)
#Eliminar el ultimo elemento de la lista
frutas.pop()
print(frutas)   
#Sumar dos listas en una nueva lista    
otras_frutas = ["piña", "cereza"]
frutas_nuevas = frutas + otras_frutas
print(frutas_nuevas)    
#Repetir una lista varias veces
frutas_repetidas = frutas * 2
print(frutas_repetidas)
#Obtener la longitud de la lista
print("La cantidad de frutas es:", len(frutas))
#Ordenar la lista alfabéticamente
frutas.sort()
print(frutas)
#Recorrer la lista con un bucle
for fruta in frutas:
    print(fruta)    
#Revertir el orden de la lista
frutas.reverse()
print(frutas)


