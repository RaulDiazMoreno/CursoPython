#38)- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def esVocal():

    caracter = input("Ingrese un caracter: ")

    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "u" or caracter == "o":
        return True
    else:
        return False


vocal = esVocal()
if vocal:
    print("El caracter introducido es una vocal")
else:
    print("El caracter introducido no es una vocal")