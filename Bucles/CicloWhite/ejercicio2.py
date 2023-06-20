numero = int(input("Ingrese un número: "))

suma = 0
contador = 0

while contador <= numero:
    if contador % 2 == 0:
        suma += contador
    contador += 1

print(f"La suma de los números pares desde 0 hasta", {numero}, "es:", {suma})