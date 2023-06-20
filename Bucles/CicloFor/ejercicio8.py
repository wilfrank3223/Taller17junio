n = int(input("Ingrese la cantidad de notas: "))
suma_notas = 0

for i in range(n):
    nota = float(input("Ingrese la nota {}: ".format(i+1)))
    suma_notas += nota

promedio = suma_notas / n

print(f"El promedio de las", {n}, "notas es:", {promedio})