#16) Completa el código siguiente para que diga “Coge un pastel” siempre y cuando se introduzca Pastel.
# De lo contrario haz que le ofrezca una Galleta y de lo contrario que te den por culo
#Añade el código necesario al programa anterior para que ofrezca una taza de chocolate sea cual sea la comida favorita.

comida = input("Cual es tu comida favorita: ")
if comida == 'Pastel':
    print("Coge un pastel")
elif comida == 'Galleta':
    print("Coge un galleta")
else:
    print("Que te den por culo")
print("Toma una taza de chocolate")