email=input("Introduce tu email: ")
contador=0
for i in range(len(email)):
    if email[i]=="@" or email[i]==".":
        contador+=1
if contador>=2:
    print("El correo es válido")
else:
    print("El correo no es válido")