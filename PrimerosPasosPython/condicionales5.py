print("Asignaturas Optativas:")
print("1. Informática")
print("2. Pruebas de Software")
print("3. Diseño Web")  
opcion = int(input("Seleccione una asignatura (1-3): "))
if opcion in [1, 2, 3]:
    print("Asignatura seleccionada correctamente.")
else:
    print("Opción no válida.")
    