#24)Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1”
#y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades
#para intentarlo.

def login(usuario,password):
    if usuario=="usuario1" and password=="asdasd":
        return True
    else:
        return False


print("Bienvenido a la pagina")
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su password: ")

acceso = login(usuario,password)

if acceso:
    print("Bienvenido a la pagina",usuario)
else:
    print("Vete a tomar por culo",usuario)