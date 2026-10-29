
'''Ejercicio 6. Tiempo
Solicita una cantidad de segundos y conviértela a:
    Horas.
    Minutos.
    Segundos.
'''

cantidad_segundos = int(input('Dime la cantidad de segundos  '))

result_minute = cantidad_segundos / 60
result_hour = cantidad_segundos / 360

#60 seg = 1 min#
#60 min = 1h#

print(f"La cantidad de segundos en minutos es: {result_minute}")
print(f"La cantidad de segundos en horas es: {result_hour}")