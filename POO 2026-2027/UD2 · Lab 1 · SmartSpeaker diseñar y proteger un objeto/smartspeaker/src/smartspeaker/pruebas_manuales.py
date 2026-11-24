##### LIBRERÍAS ##################
from .altavoz import Altavoz
##### LIBRERÍAS ##################

######-----.EJERCICIO 4, PRUEBAS VÁLIDAS EJERCICIO 4.-----#####

##### V01	Crear un altavoz con nombre "Salón" y volumen 30	Se crea correctamente
altavoz = Altavoz("Salón", 30)
print("V01 - Altavoz creado correctamente")
##### Nota: No lanza ningún error y aparentemente se comporta de forma correcta el objecto #########

##### V02	Consultar el nombre	Devuelve "Salón"
print(altavoz.nombre)
print("V01 - Consultar el nombre	Devuelve Salón")

##### V03	Consultar el volumen	Devuelve 30
print(altavoz.volumen)
print("V03 - Consultar el volumen Devuelve 30")

##### V04	Consultar el estado inicial	Devuelve "apagado"
print(altavoz.estado)
print("V04 - Consultar el estado inicial Devuelve apagado")
##### Nota: En mi caso me devuelve false porque le asigné un booleano, y tuve que ajustar desde la línea 58 a la 65 de altavoz.py

##### V05	Cambiar el volumen a 50	Se acepta
altavoz.volumen = 50
print(altavoz.volumen)
print("V05 - Cambiar el volumen a 50 se acepta")

##### V06	Cambiar el volumen a 0	Se acepta
altavoz.volumen = 0
print(altavoz.volumen)
print("V06 - Cambiar el volumen a 0 se acepta")

##### V07	Cambiar el volumen a 100	Se acepta
altavoz.volumen = 100
print(altavoz.volumen)
print("V07 - Cambiar el volumen a 100 se acepta")

##### V08	Ejecutar encender()	El estado pasa a "encendido"
altavoz.encender()
print(altavoz.estado)
print("V08 - Ejecutar encender() el estado pasa a encendido")

##### V09	Ejecutar apagar()	El estado pasa a "apagado"
altavoz.apagar()
print(altavoz.estado)
print("V08 - Ejecutar apagar() el estado pasa a apagado")

##### V10	Crear un altavoz con nombre "  Cocina  "	Se almacena "Co
altavoz = Altavoz("  Cocina  ", 30)
print(altavoz.nombre)
print('V10	Crear un altavoz con nombre "  Cocina  "	Se almacena Co')
# Nota: Tengo una validación en altavoz.py en la línea 23 a 27 que impide que se guarden los espacios

######-----.EJERCICIO 4, PRUEBAS INVÁLIDAS EJERCICIO 4.-----#####

###### I01	Crear un altavoz con nombre ""	ValueError
#altavoz = Altavoz("", 30)
print("I01	Crear un altavoz con nombre ""	ValueError")
# Nota: raise ValueError("El nombre no puede estar vacío")

###### I02	Crear un altavoz con nombre "   "	ValueError
#altavoz = Altavoz("   ", 30)
print("I02	Crear un altavoz con nombre ""	ValueError")
# Nota: raise ValueError("El nombre no puede estar vacío")

###### I03	Crear un altavoz con nombre 25	ValueError
#altavoz = Altavoz(25, 25)
print("I03	Crear un altavoz con nombre 25	ValueError")
# Nota: raise ValueError("El nombre debe ser una cadena de texto")


###### I04	Crear un altavoz con volumen -1	ValueError
#altavoz = Altavoz("Salón", -1)
print("I04	Crear un altavoz con volumen -1	ValueError")
# Nota: raise ValueError("El volumen debe estar entre 0 y 100")

###### I05	Crear un altavoz con volumen 101	ValueError
#altavoz = Altavoz("Salón", 101)
print("I05	Crear un altavoz con volumen 101	ValueError")
# Nota: raise ValueError("El volumen debe estar entre 0 y 100")

###### I06	Asignar altavoz.volumen = 25.5	ValueError
#altavoz = Altavoz("Salón", 25.5)
print("I06	Asignar altavoz.volumen = 25.5	ValueError")
# Nota: raise ValueError("El volumen debe ser un número entero")

###### I07	Asignar altavoz.volumen = "alto"	ValueError
#altavoz.volumen = "alto"
print(altavoz.volumen)
# Nota: raise ValueError("El volumen debe ser un número entero")

###### I08	Asignar altavoz.estado = "encendido"	AttributeError
altavoz.estado = "encendido"
print(altavoz.estado)
# Nota: AttributeError: property 'estado' of 'Altavoz' object has no setter