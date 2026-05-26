def evaluadorDeEdad(edad):
    if edad < 18:
        return "No puedes pasar, eres menor de edad."
    else:
        return "Puedes pasar, eres mayor de edad."
    
def evaluadorDeDescuento(edad):
  if edad >= 18 and edad < 25:
        return "Tienes descuento del 25%."
  elif edad >= 25 and edad < 65:
        return "No Tienes descuento."
  else:   
        return "Tienes descuento del 50%."
      
    

edad_usuario = int(input("Introduce tu edad: "))
print(evaluadorDeEdad(edad_usuario))
if edad_usuario > 18:
    print(evaluadorDeDescuento(edad_usuario))   