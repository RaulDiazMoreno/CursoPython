#35) Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 > numero2:
    print("El numero",numero1," es mayor que el numero ",numero2)
elif numero1 < numero2:
    print("El numero",numero2," es mayor que el numero ",numero1)
