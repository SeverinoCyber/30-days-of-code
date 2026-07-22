#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#
print("********************************************")
print("Calculo de productos sumando propina e ITBIS")
print("******************************************** \n \n")

name = input("Empecemos, por favor dime tu nombre: ")
print(f"\nHola, {name} te doy la bienvenida a este programa.\n")

while True:
    num_products = int(input("¿Cuántos productos deseas registrar? (El minimo es 5): "))
    
    if num_products > 4:
        break
    else:
        print("La cantidad debe ser un numero  mayor a 5. Intentalo de nuevo.\n")
products = {}
print(f"\nBien, ahora vas a registrar {num_products} productos:")


for i in range(num_products):
    product = input(f"\nNombre del producto {i+1}: ")
    precio = float(input(f"Precio de {product} (Que sea decimal): $"))
    
    products[product] = precio

suma_total = 0.0
print("********** Factura de productos **********\n")
print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
print(f"Nombre: {name}\n")

for product, precio in products.items():
    propina = precio * (12 / 100)
    impuesto = precio * (20 / 100)
    precio_total = precio + propina + impuesto

    print(f"- Producto:\n \n{product}: ${precio:.2f}")
    print(f"- Propina Legal 10%: ${round(propina, 2)}")
    print(f"- ITBIS 18%: ${round(impuesto, 2)}")
    print(f"- Total: ${round(precio_total, 2)}\n")
    suma_total += precio_total

print(f"{name}, el total a pagar sera: {round(suma_total, 2)}")



