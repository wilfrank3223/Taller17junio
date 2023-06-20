numero = int(input("Ingrese un número entero mayor a cero: "))

while numero <= 0:
    numero = int(input("Error. Ingrese un número entero mayor a cero: "))

print("Los divisores de", numero, "son:")

divisor = 1

while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1