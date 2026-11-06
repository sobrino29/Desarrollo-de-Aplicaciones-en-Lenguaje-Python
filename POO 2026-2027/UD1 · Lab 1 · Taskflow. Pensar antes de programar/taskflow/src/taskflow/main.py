from taskflow.proyecto import Proyecto
from taskflow.tarea import Tarea
from taskflow.usuario import Usuario

def main() -> None:
    print("================================")
    print("       BIENVENIDO A TASKFLOW")
    print("================================")
    
    ########################### TAREA 1 ##########################
    
    print("================================")
    print("       ESTA ES LA PARTE DE TAREA")
    print("================================")
    print("PRUEBA NEGATIVA: comprobar que una TAREA incompleta no se puede activar")
    
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
    
    ########################### PROYECTO 1 ##########################
    
    print("================================")
    print("    ESTA ES LA PARTE DE PROYECTO")
    print("================================")
    print("PRUEBA NEGATIVA: comprobar que una PROYECTO incompleto no se puede activar")

    # Creamos nuestro primer proyecto.
    proyecto1 = Proyecto()

    # Mostramos el identificador generado automáticamente.
    print(proyecto1.id_proyecto)

    # Rellenamos los atributos del proyecto.
    proyecto1.nombre = input("Introduce el nombre del proyecto: ")
    
     # Comprobamos la validación de la tarea.
    proyecto1.crear_Proyecto()
    
    # Consultamos su estado.
    print(proyecto1.estado)
    
    ########################### PROYECTO 2 ##########################

    # Creamos nuestro primer proyecto.
    proyecto2 = Proyecto()

    # Mostramos el identificador generado automáticamente.
    print(proyecto2.id_proyecto)

    # Rellenamos los atributos del proyecto.
    proyecto2.nombre = input("Introduce el nombre del proyecto: ")
    proyecto2.descripcion = input("Introduce la descripción del proyecto: ")
    
    # Comprobamos la validación de la tarea.
    proyecto2.crear_Proyecto()

    # Consultamos su estado.
    print(proyecto2.estado)
    
    ########################### TAREA 2 ##########################
    
    # Creamos nuestra primera tarea.
    tarea2 = Tarea()
    
    # Mostramos el identificador generado automáticamente para comprobar que funciona.
    print(tarea2.id_tarea)
    
    ### rellenar los atributos de una instancia
    tarea2.titulo = str(input("Introduce el título de la tarea: "))
    tarea2.descripcion = str(input("Introduce una descripción: "))
    tarea2.proyecto = proyecto2
    
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
    print("Proyecto asignado:", tarea2.proyecto.nombre)

    
    ########################### ASIGNAR PROYECTO A USUARIO ##########################
    # Como ya hemos creado la instancia Usuario solo nos queda iniciar Sesión
    # usuario1.iniciar_Sesion()
    
    proyecto2.asignar_Responsable(usuario1)
    
    print("Responsable asignado a proyecto:", proyecto2.responsable.nombre)
       
    print("Proyecto asignado:", proyecto2.id_proyecto, "Estado proyecto:", proyecto2.estado)
    print("Tarea asignada:", tarea2.id_tarea, "Estado tarea:", tarea2.estado)
    
    
    # Validar que todos los datos en tarea están completos
    print("===============================================")
    print("       TODOS LOS DATOS DE TAREA ESTAN COMPLETOS")
    print("===============================================")
    tarea2.crear_Tarea()
    print("Tarea asignada:", tarea2.id_tarea, "Estado tarea:", tarea2.estado)
    tarea2.iniciar_Tarea()
    print("Tarea asignada:", tarea2.id_tarea, "Estado tarea:", tarea2.estado)
    tarea2.completar_Tarea()
    print("Tarea asignada:", tarea2.id_tarea, "Estado tarea:", tarea2.estado)
    
    # Validar que todos los datos en proyecto están completos
    print("==================================================")
    print("       TODOS LOS DATOS DE PROYECTOS ESTAN COMPLETOS")
    print("===================================================")
    proyecto2.crear_Proyecto()
    print("Proyecto asignado:", proyecto2.id_proyecto, "Estado proyecto:", proyecto2.estado)

if __name__ == "__main__":
    main()
