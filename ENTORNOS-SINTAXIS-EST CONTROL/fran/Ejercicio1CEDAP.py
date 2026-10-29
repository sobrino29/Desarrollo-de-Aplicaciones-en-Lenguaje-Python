
'''Ejercicio 1. Presupuesto de reparación de un coche
Desarrolla un programa en Python que solicite al usuario los siguientes datos:

Nombre.
Apellido.
Precio del aceite de coche.
Precio de los inyectores.
Precio de las bujías.
Precio del filtro del habitáculo.
Cuando el usuario haya introducido todos los datos, el programa debe mostrar por pantalla:

El nombre y el apellido del usuario.
El precio total de todos los productos, sin IVA.
El precio total con el IVA del 21 % incluido.
Importante: Los precios deben poder introducirse con decimales.
'''

IVA =  1.21

nombre = str(input('Introduce tu nombre ...'))

apellido = str(input('Introduce tu apellido ...'))

precio_aceite = float(input("Precio del aceite de coche (€): "))

precio_inyectores = float(input("Precio de los inyectores (€): "))

precio_bujias = float(input("Precio de las bujías: (€) "))

precio_filtro = float(input('Precio del filtro del habitáculo: '))

cuenta_total = precio_aceite + precio_inyectores + precio_inyectores + precio_bujias

print(f"Precio total sin IVA {cuenta_total} €")

cuenta_total_iva = cuenta_total * IVA
print(f"Precio total con IVA {cuenta_total_iva} €")


