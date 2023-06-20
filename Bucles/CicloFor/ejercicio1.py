# 1.	Suma de los n primeros números, solicite al usuario el numero de elementos a sumar

num_Elementos = int(input("Ingrese la cantidad de números a sumar: "))

suma = 0

for numero in range(3, num_Elementos + 5):
    suma += numero

print("La suma de los", num_Elementos, "primeros números es:", suma)