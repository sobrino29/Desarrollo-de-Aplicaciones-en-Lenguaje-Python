class Proyecto:
    # Contador compartido por todos los PROYECTOS.
    # Se utiliza para generar identificadores únicos de forma consecutiva.
    contador = 1
    
    # Constructor de la clase Proyecto.
    # Se ejecuta automáticamente al crear una nueva instancia.
    # Inicializa los atributos de la tarea con sus valores iniciales.
    # Genera automáticamente un identificador único para cada tarea.
    def __init__(self):
        
        # Generamos automáticamente el identificador del Proyecto
        self.id_proyecto = f"PROJECT-{Proyecto.contador:03d}"
        
        # Incrementamos el contador para la siguiente tarea.
        Proyecto.contador += 1
        
        # Datos básicos del proyecto.
        # Inicialmente estos valores son vacíos
        self.nombre = "" 
        self.descripcion = ""
        
        # Todas los PROYECTOS se crean inicialmente en estado BORRADOR.
        # Durante esta fase se permite modificar su información.
        # Una vez que el PROYECTO abandona BORRADOR, no se permiten modificaciones.
        self.estado = "BORRADOR"
        
        # El PROYECTO puede crearse sin un usuario responsable.
        # Se podrá asignar posteriormente mientras esté en estado BORRADOR.
        self.responsable = None # Esto significa que todavía no hay ningún usuario asociado
        
    
    # Método para completar la creación de una tarea.
    # Comprueba que todos los campos obligatorios están informados.
    def crear_Proyecto(self):
    
        # Inicialmente suponemos que todos los datos están completos.
        datos_completos = True
        
        # Reviso que esté instanciado el atributo titulo
        if self.nombre == "":
            print("Error: el nombre del proyecto es obligatorio")
            datos_completos = False
        
        if self.descripcion == "":
            print("Error: La descripción del proyecto es obligatoria")
            datos_completos = False
        
        if self.responsable is None:
            print("Error: Tiene que existir un responsable asignado al proyecto")
            datos_completos = False
    
        # Saber si alguna de las cuatro condiciones ha fallado para cambiar el estado de BORRADOR en PENDIENTE
        if datos_completos == True:
            
            # Aquí cambiaremos el estado a PENDIENTE.
            respuesta_proyecto = input("¿Quieres pasar el proyecto a PENDIENTE? (S/N): ")
            
            if respuesta_proyecto == "S" or respuesta_proyecto == "s":
                self.estado = "PENDIENTE"
            else:
                self.estado = "BORRADOR"
        else:
            # Aquí indicaremos que no se puede completar la tarea.
            print("Completa todos los campos para que pueda cambiar el estado")

################################# FASE DE ASIGNACIÓN PROYECTO A USUARIO ##########################
    # Método para asignar una tarea a un usuario
    # Comprueba que todos los campos obligatorios están informados.
        
    def asignar_Responsable(self, usuario):

        if self.estado == "BORRADOR":

            if usuario.sesion_Iniciada == True:
                
                # Aquí preguntaremos si queremos asignar el usuario.
                # Si acepta, guardaremos el usuario como responsable.
                respuesta_asignacion_proyecto = input(f"¿Quieres asignar el proyecto {self.id_proyecto} al usuario {usuario.nombre}? (S/N): ")
                
                if respuesta_asignacion_proyecto == "S" or respuesta_asignacion_proyecto == "s":

                        self.responsable = usuario
                else:
                    print("No se ha asignado ningún responsable al proyecto")

            else:
                print("El usuario debe iniciar sesión antes de poder ser asignado como responsable al proyecto")

        else:
            print("El proyecto ya no está en estado BORRADOR, no se puede asignar ni modificar el responsable")
