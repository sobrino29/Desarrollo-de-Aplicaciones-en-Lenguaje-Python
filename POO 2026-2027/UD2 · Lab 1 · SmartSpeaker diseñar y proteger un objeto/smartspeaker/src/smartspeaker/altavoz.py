class Altavoz:
    
    def __init__(self, nombre, volumen):
        self.nombre = nombre
        self.volumen = volumen
        ## Un altavoz nuevo comienza apagado.
        self._estado = False
    
    ####-----.PARTE 3, REQUISITO 1, INICIO EJERCICIO 1.-----####
    ### Requisito 1. Validar el nombre
    
    ## Se eliminarán los espacios exteriores antes de almacenar el nombre.    
    @property
    def nombre(self):
        return self._nombre

    ## Debe ser una cadena de texto.
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto")
    
    ## No puede estar vacío ni contener únicamente espacios.
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        self._nombre = nuevo_nombre.strip()
    ####-----.PARTE 3, REQUISITO 1, FIN EJERCICIO 1.-----####
    
    
    ####-----.PARTE 3, REQUISITO 2, INICIO EJERCICIO 2.-----####
    ## Requisito 2. Validar el volumen
    @property
    def volumen(self):
        return self._volumen
    
    ## Debe ser un número entero, por lo que le indicamos que compruebe que no entran booleanos
    @volumen.setter
    def volumen(self, nuevo_volumen):
        if isinstance(nuevo_volumen, bool) or not isinstance(nuevo_volumen, int):
            raise ValueError("El volumen debe ser un número entero")
    
    ## Su valor estará comprendido entre 0 y 100, ambos incluidos. Para poner el 0 y el 100 incluidos los ponemos fuera de escala.
    ## Por eso se pone < 0 y > 100
        if nuevo_volumen < 0 or nuevo_volumen > 100:
            raise ValueError("El volumen debe estar entre 0 y 100")
    
        self._volumen = nuevo_volumen
    ## La misma validación debe aplicarse tanto al crear el objeto como al modificar el volumen.
    ####-----.PARTE 3, REQUISITO 2, FIN EJERCICIO 2.-----####
    
    
    ####-----.PARTE 3, REQUISITO 3, INICIO EJERCICIO 3.-----####
    ## Requisito 3. Controlar el estado
    @property
    def estado(self) -> str:
  
    # Se ajusta porque nos indican que tiene que devolver apagado no false    
        if self._estado == False:
            return "apagado"
        else:
            return "encendido"
            
        # Le indico la manera de consultar un atributo interno, el estado podrá consultarse mediante altavoz.estado.
        #return self._estado
    
    ## El resto del programa no debe poder cambiarlo mediante una asignación ordinaria a altavoz.estado por eso no lleva @setter
    
    ## El método encender() permitirá encender el dispositivo.
    def encender(self):
        self._estado = True
    
    ## El método apagar() permitirá apagarlo.
    def apagar(self):
        self._estado = False
    
    ####-----.PARTE 3, REQUISITO 3, FIN EJERCICIO 3.-----####


    ####-----.PARTE 3, REQUISITO 4, INICIO EJERCICIO 4.-----####
    ## Requisito 4. Mantener una interfaz clara
    
    # El código que utiliza la clase debería poder escribir:
    
    
    #altavoz = Altavoz("Salón", 30)

    #print(altavoz.nombre)
    #print(altavoz.volumen)
    #print(altavoz.estado)

    #altavoz.volumen = 50
    #altavoz.encender()
    #altavoz.apagar()
    
    
    # No debería necesitar acceder a los atributos internos para utilizar las operaciones habituales
    
    ####-----.PARTE 3, REQUISITO 4, FIN EJERCICIO 4.-----####



        
    