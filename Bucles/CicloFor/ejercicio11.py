cantidad_temperaturas = int(input("Ingrese la cantidad de temperaturas a introducir: "))

temperatura_maxima = float('-inf')
temperatura_minima = float('inf')
suma_temperaturas = 0

for i in range(cantidad_temperaturas):
    temperatura = float(input("Ingrese la temperatura {}: ".format(i+1)))

    if temperatura > temperatura_maxima:
        temperatura_maxima = temperatura

    if temperatura < temperatura_minima:
        temperatura_minima = temperatura

    suma_temperaturas += temperatura

temperatura_promedio = suma_temperaturas / cantidad_temperaturas

print("Temperatura más alta:", temperatura_maxima)
print("Temperatura más baja:", temperatura_minima)
print("Temperatura promedio:", temperatura_promedio)