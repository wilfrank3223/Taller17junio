primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

while primer_numero >= segundo_numero:
    print("Error: El primer número debe ser menor que el segundo.")
    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))

numero_actual = primer_numero

print("Los números desde", primer_numero, "hasta", segundo_numero, "son:")

while numero_actual <= segundo_numero:
    print(numero_actual)
    numero_actual += 1