#9) Hacer un programa que imprima una tabla de multiplicar del 1 al 9 . Cada uno debe mostrar sus valores multiplicados del 1 al 10 inclusive
for i in range(1, 10):
    for j in range(1, 11):
        print(f"{j} x {i} = {j*i}")
    print() 