'''Ejercicio 2. Compra en el supermercado
Imagina que tienes 200 euros en tu cuenta corriente y vas a hacer la compra en el supermercado.

Desarrolla un programa en Python que:

Inicialice el saldo de la cuenta corriente en 200 euros.
Pregunte el precio de los siguientes cuatro productos:
Una docena de huevos.
Una caja de helados.
Una barra de pan.
Un racimo de uvas.
Reste del saldo inicial el precio de cada producto.
Cuando el usuario haya introducido el precio del último producto, muestre el saldo final que queda en la cuenta corriente.
Importante: Los precios pueden contener decimales. Para este ejercicio, puedes suponer que hay saldo suficiente para pagar todos los productos.
'''

'''Ampliación del ejercicio 2: IVA por producto
Cuando termines el ejercicio básico, añade una mejora al programa.

Aplica los siguientes tipos de IVA:

Producto	IVA
Una docena de huevos	10 %
Una caja de helados	21 %
Una barra de pan	10 %
Un racimo de uvas	21 %
Nuevos requisitos:

Añade un menú para elegir si se quiere calcular la compra con IVA.
Calcula el precio de cada producto con su IVA incluido.
Muestra el importe total de la compra.
Calcula el saldo final después de pagar.'''

saldo_inicial =  200

print(f"Tu saldo inicial es {saldo_inicial} €")

precio_huevos = float(input("Precio de una docena de huevos es (€): "))
precio_helados = float(input("Precio de una caja de helados (€): "))
precio_barrapan = float(input("Precio de una barra de pan (€): "))
precio_racimouvas = float(input("Precio de un racimo de uvass (€): "))

opcion_menu = input("¿Quieres el precio con IVA (S/N)")
if opcion_menu == "S" or opcion_menu == "s":

        precio_huevos = precio_huevos * 1.10
        precio_helados = precio_helados * 1.21
        precio_barrapan = precio_barrapan * 1.10
        precio_racimouvas = precio_racimouvas * 1.21


saldo_final = saldo_inicial - precio_huevos - precio_helados - precio_barrapan - precio_racimouvas
print(f"Tu saldo final es {saldo_final} €")




