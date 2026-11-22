'''
Práctica: Buscar el tesoro
1. Objetivo
Desarrollar una aplicación de consola en Python que simule un juego de búsqueda del tesoro.

El programa utilizará una matriz de 3 filas y 3 columnas. En una de sus posiciones se encontrará un tesoro que se colocará de forma aleatoria al iniciar la aplicación.

El jugador deberá intentar localizarlo indicando una fila y una columna.

Con esta práctica trabajaremos listas bidimensionales, índices, bucles, condicionales, funciones, números aleatorios y control de excepciones.

Menú principal
Al iniciar el programa se creará el mapa y se mostrará el siguiente menú:

================================
          BUSCAR EL TESORO
================================
1. Ver mapa actual
2. Ver mapa resuelto
3. Jugar
4. Ver estadísticas
0. Salir
================================
Funcionalidades
Opción 1. Ver mapa actual
Mostrar la matriz sin revelar dónde está el tesoro. Se utilizará ? para representar las casillas.

Opción 2. Ver mapa resuelto
Mostrar la posición real del tesoro utilizando 💎.

Esta opción es informativa y no debe modificar el mapa ni contar como intento.

Opción 3. Jugar
Solicitar al usuario una fila y una columna, ambas entre 1 y 3.

Si la posición no es válida, mostrar un mensaje de error.
Si la posición es válida pero no contiene el tesoro, mostrar: ¡Aquí no está el tesoro! Sigue buscando.
Si el jugador encuentra el tesoro, mostrar un mensaje de felicitación y generar automáticamente un nuevo mapa con el tesoro en una posición aleatoria.
Cuando se selecciona una casilla que ya ha sido consultada se indica un mensaje de que esa casilla ya ha sido consultada, y cuenta como intento.
El nuevo tesoro puede aparecer en cualquier casilla, incluida la posición anterior.

Ver estadísticas
Mostrar:

Número de intentos realizados para encontrar el tesoro actual.
Número total de tesoros encontrados.
Número total de mapas generados.
Mejor partida jugada (encuentra el tesoro más pronto)
Peor partida jugada (encuentra el tesoro con un máximo de intentos)
El contador de intentos se reinicia al encontrar un tesoro. Los demás contadores se mantienen durante toda la ejecución.

Opción 0. Salir
Finalizar el programa mostrando un mensaje de despedida.

Requisitos técnicos
        Crear una matriz de 3x3.
        Colocar el tesoro en una posición aleatoria utilizando el módulo random.
        Utilizar funciones para organizar el código.
        Utilizar bucles para mostrar el menú y recorrer la matriz.
        Utilizar estructuras condicionales para controlar las opciones y comprobar si se ha encontrado el tesoro.
        Controlar los errores cuando el usuario introduzca texto en lugar de números.
        Validar que las filas y columnas estén comprendidas entre 1 y 3.
        Mostrar el mapa actual sin revelar el tesoro.
        Mostrar el mapa resuelto cuando se solicite.
        Generar un nuevo mapa cuando se encuentre el tesoro.
        Mantener y mostrar las estadísticas de la partida.
6. Entrega
Se entregará un único archivo Python llamado buscar_tesoro.py.

El código deberá estar organizado, utilizar nombres de variables descriptivos y contener comentarios que faciliten su comprensión.
'''

########################################################## LIBRERÍAS IMPORTADAS #####################################################
import random
########################################################## LIBRERÍAS IMPORTADAS #####################################################

########################################################### VARIABLES GLOBALES ############################################################
# Inicializo vacío el array al cual se le van añadir los elementos, se utilizará como variable global fuera de los métodos y funciones
matriz = []

# Inicializo vacío el array del usuario se utilizará como variable global fuera de los métodos y funciones
matriz_usuario = []

# Contadores por default los pongo a 0
n_intentos = 0
n_intentos_guardado = 0
tesoros_totales = 0
mapas_totales = 0

# Inicializo vacío el array de las partidas, se utilizará como variable global fuera de los métodos y funciones
partidas = []

########################################################### VARIABLES GLOBALES ############################################################

########################################################### MENÚ CONSOLA TESORO ############################################################
def menu():
        print("=================================")
        print("BUSCAR EL TESORO")
        print("1. Ver mapa actual")
        print("2. Ver mapa resuelto")
        print("3. Jugar")
        print("4. Ver estadísticas")
        print("0. Salir")
        print("=================================")

########################################################### MENÚ CONSOLA TESORO ############################################################

########################################################### Creamos el mapa en una función para poder reutilizar el código #################
def crear_Mapa():
        #print(f"Función en la funcion crear_Mapa")
        global mapas_totales
        
        mapas_totales += 1
        #print(f"{mapas_totales}")
        
        # Limpiamos el mapa
        matriz.clear()
        
        # Una vez importada la librería de random 
        eje_x = random.randint(0, 2)
        eje_y = random.randint(0, 2)

        # Le doy el tamaño que nos han dado, es decir, 3x3
        # El primer bucle recorre la filas
        for i in range(3):
                # Inicializo la fila con 3 elementos
                fila = []
                
                # El segundo buclce recorre las columnas
                for j in range(3):
                        
                        if eje_x == i and eje_y == j:
                                fila.append('💎')
                        else:
                                # Añado filas con append con interrogaciones
                                fila.append('?')
                # Añado al array vacío lo que va recorriendo el buclce, en este caso las filas    
                matriz.append(fila)
########################################################### Creamos el mapa en una función para poder reutilizar el código #################

   
############################################################## OPCION 1 VER MAPA ACTUAL #######################################################
def ver_Mapa():
        #print(f"Función en la funcion ver_Mapa")
        
        # Esta variable se ejecuta solamente en esta opción porque no hace falta jugar para verla y comprobarla
        mapa_oculto = []
        
        # 1. Compruebo si la matriz está vacía
        if not matriz:
                #print(f"La matriz del juego está vacía {matriz}")
                print("No hay ningún mapa generado")
        else:
                #print(f"La matriz del juego no está vacía {matriz}")
                # Le doy el tamaño que nos han dado, es decir, 3x3
                for i in range(3):
                        # Inicializo la fila con 3 elementos
                        fila = []
                        for j in range(3):
                                # Añado filas con append con interrogaciones
                                fila.append('?')
                        # Añado al array vacío lo que va recorriendo el buclce, en este caso las filas    
                        mapa_oculto.append(fila)
                
                # Printeo el nº de columnas
                print("  1 2 3")

                # Printeo el nº de filas
                # Recorro el array con el nombre del primer bucle y además con la variable fila para colocar las filas una debajo de otra por cada vuelta
                for i, fila in enumerate(mapa_oculto):
                        print(f"{i+1}", *fila)

        print("****************************************")
############################################################## OPCION 1 VER MAPA ACTUAL #######################################################

############################################################## OPCION 2 VER MAPA RESUELTO #######################################################
def mapa_Resuelto():
        #print(f"Función mapa resuelto")
        
        # Printeo el nº de columnas
        print("  1 2 3")
                
        for i, fila in enumerate(matriz):
                print(f"{i+1}", *fila)

        print("****************************************")
############################################################## OPCION 2 VER MAPA RESUELTO #######################################################


############################################################## OPCION 3 JUGAR #######################################################
def jugar():
        #print(f"Función jugar")

        global n_intentos, n_intentos_guardado, tesoros_totales
        
        # Para cuando se introduce un string en las opciones se va directamente al ValueError
        try:
                # Solicitar al usuario una fila y una columna, ambas entre 1 y 3.
                fila = int(input('Dime qué posición de la fila quieres: '))
                columna = int(input('Dime qué posición de la columna quieres: '))

                # VALIDACIÓN DEL RANGO
                # Cuando se pase de las coordenadas que introduce el usuario (1-3) a los índices de tu matriz (0-2), hay que restar 1 a fila y columna.
                if (fila >= 1 and fila <=3) and (columna >=1 and columna <= 3):
                        
                        # Conteo cuando esté en rango
                        n_intentos += 1
                        print(f"Nº de intentos es {n_intentos}")
                        
                        print(f" - Tus coordenadas son fila {fila} y columna es {columna} válidas")
                        
                        # Convierto las coordenadas del usuario, por eso le resto 1 a fila, y 1 a columna
                        fila_matriz_usuario = fila -1
                        columna_matriz_usuario = columna -1
                        
                        #print(f"Antes de matriz_usuario {matriz_usuario}")# compruebo que viene vacía
                        
                        # Con verificación de coordenadas consultadas
                        if [fila_matriz_usuario, columna_matriz_usuario] in matriz_usuario:
                                print(" - Esta casilla ya ha sido consultada")
                        else:
                                print(" - Esta casilla no ha sido consultada")
                                # Guardo las coordenadas del usuario en otro array, este trozo lo hace sin nº de intentos
                                matriz_usuario.append([fila_matriz_usuario, columna_matriz_usuario])
                        
                                # Reviso que las coordenadas introducidas por el usuario contienen diamante
                                if matriz[fila_matriz_usuario][columna_matriz_usuario] == '💎':
                                        
                                        # Para llevarmelo a la opcion 4 de estadísticas declaro otra variable para guardar antes de resetear
                                        n_intentos_guardado = n_intentos
                                        
                                        # Reseteo el conteo cuando encuentre el diamante
                                        n_intentos = 0
                                        #print(f"Nº de intentos es {n_intentos}")
                                        
                                        # Si el jugador encuentra el tesoro, mostrar un mensaje de felicitación y generar automáticamente un nuevo mapa con el tesoro en una posición aleatoria.
                                        print("Felicitaciones!! AQUÍ ESTÁ EL TESORO")
                                        
                                        # Aumento el contador de la variable global, tesoros_totales
                                        tesoros_totales += 1
                                        partidas.append(len(matriz_usuario))
                                        
                                        crear_Mapa()
                                        matriz_usuario.clear()
                                else:
                                        # Si la posición es válida pero no contiene el tesoro, mostrar: ¡Aquí no está el tesoro! Sigue buscando.
                                        print("¡Aquí no está el tesoro! Sigue buscando")
                else:
                        print(f"- Coordenadas fuera de rango. Debes introducir una fila y una columna entre 1 y 3.")

        # Con el control de errores try-except logramos que cuando pongas un string te capture el error
        except ValueError:
                print(f"Debes introducir un valor númerico")
        
        print("*****************************************")
############################################################# OPCION 3 JUGAR #######################################################


############################################################# OPCION 4 VER ESTADÍSTICAS #######################################################
def ver_Estadisticas():
        
        #print(f"Función ver_Estadisticas")
        
        print(f" - Nº de intentos del tesoro actual es {n_intentos}")
        print(f" - Nº total de tesoros encontrados {tesoros_totales}")
        print(f" - Nº total de mapas generados {mapas_totales}")
        print(f" - Mejor partida jugada {min(partidas)} intentos")
        print(f" - Peor partida jugada {max(partidas)} intentos")

        print("*****************************************")

############################################################# OPCION 4 VER ESTADÍSTICAS #######################################################

############################################################## CONSTRUCTOR ########################################################################
if __name__ == '__main__':
        
        # Llamo a la funcion crear_Mapa() para que me genere un mapa antes de llamar al menú siempre
        crear_Mapa()

########################################################### LÓGICA MENÚ CONSOLA TESORO ############################################################        
        while True:
                menu()
                try:
                        opc = int(input('¿qué opción eliges?: '))
                        # Si introduzco un valor dentro del rango 0-4 ambos incluidos, ejecuto las distintas opciones
                        if opc >= 0 and opc <= 4:
                                
                                if opc == 1:
                                        ver_Mapa()
                                elif opc == 2:
                                        mapa_Resuelto()
                                elif opc == 3:
                                        jugar()
                                elif opc == 4:
                                        ver_Estadisticas()
                                elif opc == 0:
                                        print("Fin del programa. ¡Hasta luego!")
                                        break
                        else:
                                print("Ese nº no sirve")
                
                # Capturo el error para indicar que debe hacer el usuario       
                except ValueError:
                        print("Debes introducir un nº")

########################################################### LÓGICA MENÚ CONSOLA TESORO ############################################################
############################################################## CONSTRUCTOR ########################################################################