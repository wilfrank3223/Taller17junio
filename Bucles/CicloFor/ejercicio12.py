n = int(input("Ingrese la cantidad de estudiantes: "))

nota_maxima = float('-inf')
nota_minima = float('inf')
suma_notas = 0

for i in range(n):
    print("Estudiante", i+1)
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    nota4 = float(input("Ingrese la nota 4: "))

    promedio = (nota1 + nota2 + nota3 + nota4) / 4

    if promedio > nota_maxima:
        nota_maxima = promedio

    if promedio < nota_minima:
        nota_minima = promedio

    suma_notas += promedio

promedio_general = suma_notas / n

print("Nota más alta:", nota_maxima)
print("Nota más baja:", nota_minima)
print("Promedio general:", promedio_general)