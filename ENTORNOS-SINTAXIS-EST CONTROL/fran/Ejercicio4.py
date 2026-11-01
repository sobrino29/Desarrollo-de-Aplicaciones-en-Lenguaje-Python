
'''Ejercicio 4. Conversor de temperatura
Solicita una temperatura en grados Celsius y conviértela a Fahrenheit.'''

# F = C × 9 / 5 + 32

grados_celsius = float(input('Dime la Temperatura '))
f = grados_celsius * 9 / 5 + 32

print(f"La temperatura en Fahrenheit es : {f}" )