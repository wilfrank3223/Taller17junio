total_facturas = 0
monto_factura = float(input("Ingrese el monto de la factura (0 para finalizar): "))

while monto_factura != 0:
    total_facturas += monto_factura
    monto_factura = float(input("Ingrese el monto de la factura (0 para finalizar): "))

if total_facturas > 1000:
    descuento = total_facturas * 0.1
    total_a_pagar = total_facturas - descuento
else:
    total_a_pagar = total_facturas

print("Total a pagar:", total_a_pagar)