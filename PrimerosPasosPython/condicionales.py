def evaluacion(nota):
    valoracion = "Aprobado" 
    if nota < 5:
        valoracion = "Suspendido"
    
    return valoracion
    
nota_usuario = float(input("Introduce tu nota: "))
print(evaluacion(nota_usuario))

