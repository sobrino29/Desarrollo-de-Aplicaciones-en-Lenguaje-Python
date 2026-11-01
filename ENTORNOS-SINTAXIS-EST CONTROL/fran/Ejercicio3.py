
'''Ejercicio 3. Conversor de euros
Solicita una cantidad en euros y muestra su equivalente en dólares.
Utiliza un tipo de cambio almacenado en una variable.'''


cantidad = float(input('Dime la cantidad en euros '))
const = 1.08

operacion = cantidad * const

print(f"El precio final es: {operacion}")