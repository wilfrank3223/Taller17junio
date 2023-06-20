n = int(input("Ingrese la cantidad de temperaturas: "))

if n <= 0:
    print("Error: La cantidad de temperaturas debe ser mayor a cero.")
else:
    temperatura_maxima = float(input("Ingrese la temperatura 1: "))
    temperatura_minima = temperatura_maxima
    suma_temperaturas = temperatura_maxima
    contador = 2

    while contador <= n:
        temperatura = float(input("Ingrese la temperatura " + str(contador) + ": "))
        suma_temperaturas += temperatura

        if temperatura > temperatura_maxima:
            temperatura_maxima = temperatura

        if temperatura < temperatura_minima:
            temperatura_minima = temperatura

        contador += 1

    temperatura_promedio = suma_temperaturas / n

    print("Temperatura máxima:", temperatura_maxima)
    print("Temperatura mínima:", temperatura_minima)
    print("Temperatura promedio:", temperatura_promedio)