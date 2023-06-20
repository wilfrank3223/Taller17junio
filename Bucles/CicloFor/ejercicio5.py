numero = int(input("Ingrese un número: "))
suma = 0
ContadorImpares = 0

for i in range(1, numero+1, 2):
    suma += i
    ContadorImpares += 1

print(f"La suma de los números impares desde 1 hasta, {numero}, es:, {suma}")
print(f"Hay", {ContadorImpares}, "números impares.")