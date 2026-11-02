class Usuario:
    
    # Contador compartido por todos los usuarios.
    # Se utiliza para generar identificadores únicos de forma consecutiva.
    contador_usuario = 1
    
    # Constructor de la clase Usuario.
    # Se ejecuta automáticamente al crear una nueva instancia.
    # Inicializa los atributos del usuario.
    def __init__(self):
        
        # Generamos automáticamente el identificador del usuario.
        self.id_usuario = f"USU-{Usuario.contador_usuario:03d}"
        
        # Incrementamos el contador para el siguiente usuario.
        Usuario.contador_usuario += 1
        
        # Datos básicos del usuario.
        # Inicialmente estos valores son vacíos 
        self.nombre = ""
        
        # Con esto se comprueba que el usuario haya iniciado la sesión
        self.sesion_Iniciada = False
    
    # Método para completar la creación de un usuario.
    # Comprueba que todos los campos obligatorios están informados.
    def iniciar_Sesion(self):
    
        # Inicialmente suponemos que todos los datos están completos.
        datos_completos_usuario = True
        
        # Reviso que esté instanciado el atributo nombre del usuario
        if self.nombre == "":
            print("Error: el nombre del usuario es obligatorio")
            datos_completos_usuario = False
    
        # Saber si alguna condición ha fallado
        if datos_completos_usuario == True:
            # Indicar si el usuario a rellenado el nombre
            print("Inicio de sesión correcto. Bienvenido", self.nombre)
            self.sesion_Iniciada = True

        else:
            # Aquí indicaremos que no se puede completar la tarea.
            print("Introduce el nombre del usuario para iniciar sesión")
            

        

