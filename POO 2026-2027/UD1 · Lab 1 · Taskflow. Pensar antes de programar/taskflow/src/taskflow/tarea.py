class Tarea:
    
    # Contador compartido por todas las tareas.
    # Se utiliza para generar identificadores únicos de forma consecutiva.
    contador = 1
    
    # Constructor de la clase Tarea.
    # Se ejecuta automáticamente al crear una nueva instancia.
    # Inicializa los atributos de la tarea con sus valores iniciales.
    # Genera automáticamente un identificador único para cada tarea.
    def __init__(self):
        
        # Generamos automáticamente el identificador de la tarea.
        self.id_tarea = f"TASK-{Tarea.contador:03d}"
        
        # Incrementamos el contador para la siguiente tarea.
        Tarea.contador += 1
        
        # Datos básicos de la tarea.
        # Inicialmente estos valores son vacíos
        self.titulo = "" 
        self.descripcion = ""
        
        # Todas las tareas se crean inicialmente en estado BORRADOR.
        # Durante esta fase se permite modificar su información.
        # Una vez que la tarea abandona BORRADOR, no se permiten modificaciones.
        self.estado = "BORRADOR"
        
        # La tarea puede crearse sin un usuario responsable.
        # Se podrá asignar posteriormente mientras esté en estado BORRADOR.
        self.responsable = None # Esto significa que todavía no hay ningún usuario asociado
        self.crq = None # Esto significa que todavía no hay CRQ asociado.
    
    
    # Método para completar la creación de una tarea.
    # Comprueba que todos los campos obligatorios están informados.
    def crear_Tarea(self):
    
        # Inicialmente suponemos que todos los datos están completos.
        datos_completos = True
        
        # Reviso que esté instanciado el atributo titulo
        if self.titulo == "":
            print("Error: el título es obligatorio")
            datos_completos = False
        
        if self.descripcion == "":
            print("Error: La descripción es obligatoria")
            datos_completos = False
        
        if self.responsable is None:
            print("Error: Tiene que existir un responsable asignado")
            datos_completos = False
        
        if self.crq is None:
            print("Error: Tiene que existir un CRQ asociado")
            datos_completos = False
    
        # Saber si alguna de las cuatro condiciones ha fallado para cambiar el estado de BORRADOR en PENDIENTE
        if datos_completos == True:
            
            # Aquí cambiaremos el estado a PENDIENTE.
            respuesta = input("¿Quieres pasar la tarea a PENDIENTE? (S/N): ")
            
            if respuesta == "S" or respuesta == "s":
                self.estado = "PENDIENTE"
            else:
                self.estado = "BORRADOR"
        else:
            # Aquí indicaremos que no se puede completar la tarea.
            print("Completa todos los campos para que pueda cambiar el estado")

################################# FASE DE ASIGNACIÓN TAREA A USUARIO ##########################
    # Método para asignar una tarea a un usuario
    # Comprueba que todos los campos obligatorios están informados.
        
    def asignar_Responsable(self, usuario):

        if self.estado == "BORRADOR":

            if usuario.sesion_Iniciada == True:
                
                # Aquí preguntaremos si queremos asignar el usuario.
                # Si acepta, guardaremos el usuario como responsable.
                respuesta_asignacion_tarea = input(f"¿Quieres asignar la tarea {self.id_tarea} al usuario {usuario.nombre}? (S/N): ")
                
                if respuesta_asignacion_tarea == "S" or respuesta_asignacion_tarea == "s":

                        self.responsable = usuario
                else:
                    print("No se ha asignado ningún responsable a la tarea")

            else:
                print("El usuario debe iniciar sesión antes de poder ser asignado como responsable")

        else:
            print("La tarea ya no está en estado BORRADOR, no se puede asignar ni modificar el responsable")