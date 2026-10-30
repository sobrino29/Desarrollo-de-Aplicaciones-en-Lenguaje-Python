
'''Ejercicio 3. Entradas para un parque de atracciones
Un parque de atracciones quiere crear un programa para calcular cuánto debe pagar una persona por su entrada.

El programa debe pedir los siguientes datos:

Nombre del visitante.
Edad del visitante.
Si quiere añadir un menú de comida. El usuario responderá s si quiere menú o n si no lo quiere.
El precio de la entrada depende de la edad:

Menores de 4 años: entrada gratuita.
Desde los 4 hasta los 12 años, ambos incluidos: descuento del 30 % sobre el precio normal.
Mayores de 12 años y menores de 65: pagan el precio normal.
Personas de 65 años o más: descuento del 20 % sobre el precio normal.
El precio normal de la entrada es de 30 €.

Si el visitante quiere menú, se añadirán 8 € al importe final. El precio del menú no tiene descuento.
'''

'''Requisitos del programa
Solicita el nombre y la edad del visitante.
Calcula el precio de la entrada según la edad.
Pregunta si quiere añadir un menú.
Si responde s, añade 8 € al precio calculado.
Si responde n, no añade ningún importe.
Muestra el nombre del visitante, el precio de la entrada, el coste del menú y el importe total que debe pagar.
Condiciones: resuelve las decisiones utilizando únicamente if y else. No utilices elif. Puedes utilizar condicionales anidados, es decir, escribir un if dentro de un else.

Para este ejercicio, puedes suponer que el usuario introduce una edad válida y responde s o n cuando se le pregunta por el menú.

Ejemplo orientativo 1
Introduce tu nombre: Lucía
Introduce tu edad: 10
¿Quieres añadir un menú por 8 euros? (s/n): s

Visitante: Lucía
Precio de la entrada: 21.00 €
Precio del menú: 8.00 €
Total a pagar: 29.00 €

'''

nombre_visitante = str(input('Introduce tu nombre: '))
edad = int(input('Introduce tu edad: '))

precio_entrada = float(input('Precio de la entrada: '))

# Menores de 4 años: entrada gratuita
if edad < 4:
        precio_entrada = 0

else:
        # Desde los 4 hasta los 12 años, ambos incluidos: descuento del 30 % sobre el precio normal
        if edad >= 4 and edad < 13:
                precio_entrada = precio_entrada * 0.70

        else:
                # Mayores de 12 años y menores de 65: pagan el precio normal. 
                if edad > 12 and edad < 65:
                      # Como en este caso no hace falta modificar la variable, en vez de poner precio_entrada = precio_entrada
                      pass 
                else: 
                        # Personas de 65 años o más: descuento del 20 % sobre el precio normal.
                        if edad >= 65:
                                precio_entrada = precio_entrada * 0.80

print(f"El precio de la entrada es: {precio_entrada} €")
                                
# Si el visitante quiere menú, se añadirán 8 € al importe final. El precio del menú no tiene descuento                                                
ADICION = 8
precio_menu = float(input('Precio del menú: '))

menu_opcion = input('¿Quieres añadir un menú por 8 euros? (S/N): ')
if menu_opcion == "S" or menu_opcion == "s":
        
        total = precio_entrada + precio_menu + ADICION
        
else:
        total = precio_entrada


##### Ampliación opcional
# Añade una pregunta para saber si el visitante quiere comprar una foto de recuerdo por 5 €.

# Añade una pregunta para saber si el visitante quiere comprar una foto de recuerdo por 5 €.
FOTO = 5
        
menu_opcion_foto = input('¿Quieres añadir una foto de recuerdo por 5 euros? (S/N): ')
if menu_opcion_foto == "S" or menu_opcion_foto == "s":
        
        total = total + FOTO
else:
        total = precio_entrada     


print(f"Tu saldo final es {total} €")







    





