
'''Ejercicio 5. Precio final
Solicita Precio de un producto.

Porcentaje de IVA.

Calcula:
Importe del IVA. Precio final.

Ejemplo:
Precio: 100IVA: 21IVA: 21 €Precio final: 121 €
'''

cantidad = float(input('Dime el precio de un producto '))
iva = 1.21

operacion = cantidad * iva

print(f"El precio final es: {operacion}")