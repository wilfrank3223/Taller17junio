numero = int(input("Ingrese un número: "))

resultado = 0

if numero > 10:
    resultado = 1
    for i in range(1, 11):
        resultado *= i
else:
    for i in range(1, numero + 1):
        resultado += i

print(f"El resultado es:{resultado}")