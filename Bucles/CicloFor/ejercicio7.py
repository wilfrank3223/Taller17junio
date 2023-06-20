numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del", {numero}, ":")

for i in range(0, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)