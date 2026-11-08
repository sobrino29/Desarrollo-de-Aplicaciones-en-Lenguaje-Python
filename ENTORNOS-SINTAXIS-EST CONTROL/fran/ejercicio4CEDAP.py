'''Ejercicio 4 CEDAP

Ejercicio 4. Sistema de concesión de becas
Un centro educativo quiere desarrollar un programa en Python para determinar qué tipo de beca puede recibir un alumno.

El programa debe solicitar los siguientes datos:

Nombre del alumno.
Nota media del curso.
Renta familiar anual.
Porcentaje de asistencia a clase.
Si pertenece a una familia numerosa (s o n).
El centro establece las siguientes condiciones:

Beca de excelencia
El alumno obtiene esta beca si cumple todas estas condiciones:

Tiene una nota media igual o superior a 9.
Tiene una asistencia igual o superior al 90 %.
Su renta familiar es inferior a 30.000 €.

Beca general

Si no cumple los requisitos de la beca de excelencia, podrá obtener la beca general si:

Tiene una nota media igual o superior a 6,5.
Tiene una asistencia igual o superior al 80 %.
Además, cumple al menos una de estas condiciones:

Su renta familiar es inferior a 20.000 €.

Pertenece a una familia numerosa.

Sin beca

Si no cumple ninguna de las condiciones anteriores, no obtiene ninguna beca.

Requisitos del programa:

Solicita todos los datos al usuario.
Comprueba si tiene derecho a una beca de excelencia.
Si no cumple los requisitos, comprueba si puede obtener una beca general.
Si tampoco cumple esos requisitos, indica que no tiene derecho a ninguna beca.
Muestra el nombre del alumno y el tipo de beca obtenido.
'''

nombre_alumno = str(input('Introduce tu nombre: '))
nota_media = float(input('Nota media del curso: '))
renta_familiar_anual = float(input('Renta familiar anual: '))
porcentaje_asistencia = float(input('El porcentaje de asistencia a clase es: '))

# Inicializo las variables con valores a False
familia_numerosa = False
beca = False

# Le hago preguntas para poder darle valor a esas variables booleanas
beca = input('¿Eres familia numerosa? (S/N): ')
if beca == "S" or beca == "s":
        
        beca = True
        
else:
        beca = False

############ BECA DE EXCELENCIA #########
#El alumno obtiene esta beca si cumple todas estas condiciones:

#Tiene una nota media igual o superior a 9.
#Tiene una asistencia igual o superior al 90 %.
#Su renta familiar es inferior a 30.000 €.
##########################################

if nota_media >= 9 and porcentaje_asistencia >= 90 and renta_familiar_anual <= 30000:
        print(f"Tienes beca de excelencia")
        print("================================")
        print(f"BECA EXCELENCIA")
        print(f"Nombre: {nombre_alumno}")
        print("================================")    

############# BECA GENERAL ###############
# Si no cumple los requisitos de la beca de excelencia, podrá obtener la beca general si:

# Tiene una nota media igual o superior a 6,5.
#Tiene una asistencia igual o superior al 80 %.
#Además, cumple al menos una de estas condiciones:

# Su renta familiar es inferior a 20.000 €.

# Pertenece a una familia numerosa.
##########################################
        
elif nota_media >= 6.5 and porcentaje_asistencia >= 80 and (renta_familiar_anual < 20000 or familia_numerosa == True or beca == False ):
        print(f"Tienes derecho a la beca general")
        print("================================")
        print(f"BECA GENERAL")
        print(f"Nombre: {nombre_alumno}")
        print("================================")        

else:
        print(f"No tienes derecho a beca")
        print("================================")
        print(f"HABER ESTUDIAO")
        print(f"Nombre: {nombre_alumno}")
        print("================================")


