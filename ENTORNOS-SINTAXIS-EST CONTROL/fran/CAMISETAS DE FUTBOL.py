''' CAMISETAS DE FUTBOL. EL USUARIO NO PUEDE PONERLE DE NOMBRE DE CAMISETA RONALDO
SI ES RONALDO TE DICE QUE TE VAYAS A MADRID
'''

# QUE NO SEA NULO (vacío)
# QUE NO SE PUEDA RONALDO ===> OK
# QUE NO SE PUEDA PONER Nºs => OK
# QUE NO LLEVE ESPACIOS =====> OK
# QUE NO LLEVE INTROS =======> OK
# QUE NO LLEVE CARACTERES ESPECIALES ===> OK

nombre = input("Introduce tu nombre: ")

# Eliminar espacios al principio y al final
# Le damos formato correcto a la variable porque devuelve una cadena por eso se valida abajo
nombre = nombre.strip()

# Comprueba si todos los caracteres de una cadena son letras del alfabeto.
nombre_valido = nombre.isalpha()

print(f"Hola, {nombre}")

# Que no lleve digitos solamente es decir 12345
if nombre.isdigit():
    print(f"Tu nombre contiene digitos {nombre} no sirve")
else:
    print(f"Tu nombre es una cadena")
    # SI LLEVA LA PALABRA RONALDO or Ronaldo or RonALDO porque transforma a minúsculas
    if nombre.strip().lower() == "ronaldo":
        print(f"VETE A MADRID CON {nombre}")
    else:
        print(f"Tu nombre es válido {nombre}")

        # Eliminar espacios al principio y al final
        if nombre == "":
            print("El nombre no puede estar vacío")
        
        # Eliminar espacios al principio y al final
        if not nombre == True:
            print("El nombre no puede ser un caracter especial")
        else:
            print(f"El nombre debe tener letras del abecedeario")