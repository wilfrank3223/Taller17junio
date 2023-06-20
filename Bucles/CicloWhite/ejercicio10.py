n = int(input("Ingrese la cantidad de estudiantes: "))

if n <= 0:
    print("Error: La cantidad de estudiantes debe ser mayor a cero.")
else:
    estudiante = 1
    while estudiante <= n:
        print("Estudiante", estudiante)
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))

        nota_maxima = max(nota1, nota2, nota3)
        nota_minima = min(nota1, nota2, nota3)
        promedio = (nota1 + nota2 + nota3) / 3

        print("Nota más alta:", nota_maxima)
        print("Nota más baja:", nota_minima)
        print("Promedio:", promedio)

        estudiante += 1
        print()  