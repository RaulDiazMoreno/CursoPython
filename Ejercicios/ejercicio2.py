#2) Hacer un programa que solicite por teclado dos número y muestre la suma , la resta ,la multiplicación y la división de esos números

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)
if numero2 != 0:
    print("División:", numero1 / numero2)
else:
    print("No se puede dividir por cero")
    

