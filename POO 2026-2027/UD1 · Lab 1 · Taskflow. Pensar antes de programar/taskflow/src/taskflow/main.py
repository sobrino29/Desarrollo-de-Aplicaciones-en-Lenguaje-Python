from taskflow.tarea import Tarea
from taskflow.usuario import Usuario

def main() -> None:
    print("Hello from taskflow!")
    
    ########################### TAREA 1 ##########################
    
    # Creamos nuestra primera tarea.
    tarea1 = Tarea()
    
    # Mostramos el identificador generado automáticamente para comprobar que funciona.
    print(tarea1.id_tarea)
    
    ### rellenar los atributos de una instancia
    tarea1.titulo = input("Introduce el título de la tarea: ")
    
    # Comprobamos la validación de la tarea.
    tarea1.crear_Tarea()

    # Consultamos su estado.
    print(tarea1.estado)
    
    ########################### TAREA 2 ##########################
    
    # Creamos nuestra primera tarea.
    tarea2 = Tarea()
    
    # Mostramos el identificador generado automáticamente para comprobar que funciona.
    print(tarea2.id_tarea)
    
    ### rellenar los atributos de una instancia
    tarea2.titulo = str(input("Introduce el título de la tarea: "))
    tarea2.descripcion = str(input("Introduce una descripción: "))
    tarea2.crq = str(input("El cambio asociado es el CRQ00000001"))
    
    # Comprobamos la validación de la tarea.
    tarea2.crear_Tarea()

    # Consultamos su estado.
    print(tarea2.estado)
    
    ########################### USUARIO ##########################
    usuario1 = Usuario()
    
    ### rellenar los atributos de una instancia Usuario
    usuario1.nombre = input("Introduce el nombre del usuario: ")
            
    # Mostramos el identificador generado automáticamente para comprobar que funciona.
    print(usuario1.id_usuario)

    ########################### ASIGNAR TAREA A USUARIO ##########################
    # Como ya hemos creado la instancia Usuario solo nos queda iniciar Sesión
    usuario1.iniciar_Sesion()
    
    tarea2.asignar_Responsable(usuario1)
    
    print("Responsable asignado:", tarea2.responsable.nombre)
    
    print("Tarea asignada:", tarea2.id_tarea)
    print("Título de la tarea:", tarea2.titulo)

if __name__ == "__main__":
    main()
