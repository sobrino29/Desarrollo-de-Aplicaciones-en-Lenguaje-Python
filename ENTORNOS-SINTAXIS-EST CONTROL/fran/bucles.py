'''Ejercicio 4 CEDAP
'''

# VARIABLE GLOBAL TODOS LOS MÉTODOS ACCEDEN A ELLA
resultado = 0

# INICIALIZO UNA LISTA VACÍA PARA IR GUARDANDO LOS RESULTADOS
lista = []

# MENU CONSOLA
def menu():
    print("=======================================")
    print("INICIO PROGRAMA CALCULADORA")
    print("1. Operación")
    print("2. Mostrar Resultado última operacion")
    print("3. Quiero que me enseñes el historial de resultados que has tenido")
    print("4. Fin del programa")
    print("=======================================")

# OPCION 1 OPERACION
def operaciones():
    # DECLARAR LA VARIABLE COMO GLOBAL PORQUE ESTÁ COMO EN LÍNEA 4    
    global resultado
    numero1 = int(input('Dime el numero 1: '))
    numero2 = int(input('Dime el numero 2: '))
    operacion = input('Dime que operacion quieres hacer * / + -: ')
    if operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        resultado = numero1 / numero2
    elif operacion == "+":
        resultado = numero1 + numero2
        
    lista.append(resultado)
    print(len(lista))
    
    print("*********************************************")
    print(f"El resultado de la operacion es: {resultado}")
    print("*********************************************")

# OPCION 2 MOSTRAR RESULTADO
def mostrar_ultimo_resultado():
    # DECLARAR LA VARIABLE COMO GLOBAL
    global resultado
    print(resultado)

# OPCION 3 MOSTRAR HISTORIAL DE RESULTADOS
def mostrar_historial():
    # RECORRO EL ARRAY DE LISTA QUE DE PRIMERAS ESTÁ VACIO
    for valor in lista:
        print (valor)


# CONSTRUCTOR
if __name__ == '__main__':

    while True:
        menu()
        opc = input('Dime que opcion eliges: ')
        if opc == "1":
            operaciones()
        elif opc == "2":
            mostrar_ultimo_resultado()
        elif opc == "3":
            mostrar_historial()
        elif opc == "4":
            print("Fin del programa. ¡Hasta luego!")
            break  






