#Creación de un diccionario con pares clave-valor
miDiccionario={
    "España": "Madrid",
    "Italia": "Roma",
    "Francia": "París",
    "Alemania": "Berlín"
}
#Imprimir el diccionario completo
print(miDiccionario)
#Acceder a un valor específico utilizando su clave
print(miDiccionario["Italia"])
#Agregar un nuevo par clave-valor al diccionario
miDiccionario["Portugal"] = "Lisboa"
print(miDiccionario)
#Modificar el valor asociado a una clave existente
miDiccionario["Francia"] = "Marsella"
print(miDiccionario)
#Sobrescribir un valor existente en el diccionario  
miDiccionario["Francia"] = "Paris"
print(miDiccionario)
#Eliminar un par clave-valor del diccionario
del miDiccionario["Alemania"]
print(miDiccionario)
#Obtener la lista de claves del diccionario
print(miDiccionario.keys())
#Obtener la lista de valores del diccionario
print(miDiccionario.values())
#Obtener la lista de pares clave-valor del diccionario
print(miDiccionario.items())
#Comprobar si una clave existe en el diccionario
print("España" in miDiccionario)
#Recorrer el diccionario con un bucle
for pais, capital in miDiccionario.items():
    print("La capital de", pais, "es", capital) 

#Diccionario con distintos tipos de datos
miDiccionario2 = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["fútbol", "música", "viajar"],
    "trabajo": {"empresa": "TechCorp", "puesto": "Desarrollador"}
}
print(miDiccionario2)
   
#Asignar una tupla para valor de un diccionario
miTupla = ("España", "Francia", "Italia","Alemania")
miDiccionario3 = {miTupla[0]: "Madrid", miTupla[1]: "París", miTupla[2]: "Roma", miTupla[3]: "Berlín"}
print(miDiccionario3)

#Incluir una tupla como elemento de un diccionario
miDiccionario4 = {"Nombre Jugador": "Daniel",
                  "Apellido Jugador": "Carvajal",
                  "Posición": "Lateral Derecho",
                  "Equipos": ("Real Madrid", "Bayer Leverkusen"),
                  "Número de camiseta": 2,
                  "Nacionalidad": "Española",
                  "Edad": 34,
                  "Ligas Ganadas": {"Real Madrid": 5, "Bayer Leverkusen": 0},
                  "Champions League": ["2014", "2016", "2017", "2018", "2022", "2024"]
}
print(miDiccionario4)
#Acceder a un valor específico utilizando su clave
print(miDiccionario4["Equipos"])
print(miDiccionario4["Champions League"])
print(miDiccionario4["Ligas Ganadas"]["Real Madrid"])
 


