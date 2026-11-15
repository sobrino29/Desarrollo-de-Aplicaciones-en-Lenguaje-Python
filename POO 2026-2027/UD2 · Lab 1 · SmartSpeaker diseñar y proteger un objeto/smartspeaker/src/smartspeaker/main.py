from .altavoz import Altavoz

def main() -> None:
    altavoz = Altavoz("Salón", 30)
    
    
    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.estado)
    
    altavoz.volumen = 50
    
    # Llamo  a los métodos encender y apagar
    altavoz.apagar()
    altavoz.encender()
    
    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.estado)

    ### Este es para ver el comportamiento cuando no se validan las cosas
        
    #altavoz.nombre = ""
    #altavoz.volumen = -50
    #altavoz.encendido = "quizá"
    
    ## COMPRUEBO LA VALIDACIÓN DEL NOMBRE CAPTURANDO EL ERROR
    
    ######-----.PARTE 3, REQUISITO 1, COMPROBACION EJERCICIO 1.-----#####
    ### Compruebo que no esté vacío ni contenga espacios
    try:
        altavoz.nombre = ""
    except ValueError as error:
        print(f"Validación correcta: {error}")
    
    ### Compruebo que sea un string     
    try:
        altavoz.nombre = 38
    except ValueError as error:
        print(f"Validación correcta: {error}")
    ######-----.PARTE 3, REQUISITO 1, COMPROBACION EJERCICIO 1.-----#####
    
    ######-----.PARTE 3, REQUISITO 2, COMPROBACION EJERCICIO 2.-----#####
    ### Debe ser un número entero.
    try:
        altavoz.volumen = "cadena"
    except ValueError as error:
        print(f"Validación correcta: {error}")
    
    ## Su valor estará comprendido entre 0 y 100, ambos incluidos.    
    try:
        altavoz.volumen = -1
    except ValueError as error:
        print(f"Validación correcta: {error}")
    ######-----.PARTE 3, REQUISITO 2, COMPROBACION EJERCICIO 2.-----#####
        
    
    ######-----.PARTE 3, REQUISITO 3, COMPROBACION EJERCICIO 3.-----#####
        #Como no tengo que modificar nada (@setter) no debo comprobarlo
    try:
        altavoz.estado = True
    except AttributeError as error:
        print(f"Validación correcta: {error}")   
    ######-----.PARTE 3, REQUISITO 3, COMPROBACION EJERCICIO 3.-----#####

        
if __name__ == "__main__":
    main()
    
