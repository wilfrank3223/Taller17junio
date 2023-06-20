n = int(input("Ingrese la cantidad de notas: "))

suma_notas = 0
contador = 0

while contador < n:
    nota = float(input("Ingrese la nota: "))
    suma_notas += nota
    contador += 1

promedio = suma_notas / n

print("El promedio de las", n, "notas es:", promedio)