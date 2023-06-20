numero = int(input("Ingrese un número: "))

suma = 0
contador = 1
cantidad_impares = 0

while contador <= numero:
    if contador % 2 != 0:
        suma += contador
        cantidad_impares += 1
    contador += 1

print(f"La suma de los números impares desde 1 hasta",{numero} , "es:", {suma})
print(f"Cantidad de números impares:", {cantidad_impares})
