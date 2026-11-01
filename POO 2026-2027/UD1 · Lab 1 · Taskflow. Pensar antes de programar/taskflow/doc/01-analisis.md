# 🧪 Laboratorio POO: Diseñar TaskFlow

## Parte 1. Analizar el problema

### Identificación de objetos

| Posible objeto | ¿Por qué existe? | ¿Qué información necesita? |
|---|---|---|
| Proyecto | Permite controlar las tareas asociadas al proyecto. | <br> - Nombre del proyecto: Permite saber cómo se llama el proyecto. <br> - Descripción: Permite explicar en qué consiste. <br> - Identificador (ID): Permite distinguirlo de otros proyectos. <br> - crqs: Permite relacionar el proyecto con el cambio que hay que realizar|
| CRQ | Representa una solicitud de cambio que agrupa las tareas necesarias para realizar una modificación en un proyecto. | <br> - Identificador del CRQ (id_crq): Permite distinguirlo de otros CRQ. <br> - Nombre del CRQ: Permite identificar el cambio que se va a realizar. <br> - Descripción: Permite explicar en qué consiste el cambio. <br> - Estado del CRQ: Permite conocer la situación en la que se encuentra. <br> - Fecha de inicio prevista: Indica cuándo está previsto comenzar el cambio. <br> - Fecha de finalización prevista: Indica cuándo está previsto terminar el cambio. <br> - Proyecto al que pertenece el CRQ. <br> - Tareas asociadas al CRQ. |
| Tarea | Representa un trabajo concreto que hay que realizar. | <br> - Nombre de tarea: Permite saber cómo se llama la tarea. <br> - Descripción tarea: Permite explicar en qué consiste. <br> - Identificador de tarea (id_tarea): Permite distinguirla de otras tareas dentro del mismo proyecto. <br> - Estado de la tarea: Los valores son pendiente, en progreso y completada. <br> - Proyecto al que pertenece la tarea. <br> - Usuario asignado |
| Usuario | Permite registrar a las personas que utilizan la aplicación. | <br> - Nombre de usuario: Permite saber cómo se llama el usuario. <br> - Identificar (id_usuario): Permite distinguir un usuario de otro. |


### Otras entidades
**¿Qué otras entidades podrían existir?**
<span style="color: #3498DB;">
    Un rol de usuario, por ejemplo, administrador o desarrollador, para diferenciar los permisos de cada usuario.
</span>

**¿Cuáles son realmente necesarias?**
<span style="color: #3498DB;">
    Proyecto, tarea y usuarios
</span>

**¿Cuáles son solamente datos o características de otras entidades?**
<span style="color: #3498DB;">
    El estado de una tarea es un atributo de Tarea, y el rol es un atributo de Usuario
</span>

> No busques todavía una única respuesta correcta. Lo importante es justificar tus decisiones.

---

## Parte 2. Identificar el estado

El estado de un objeto es la información que describe cómo se encuentra en un momento determinado.

Para cada objeto que hayas identificado, determina qué información necesita conocer.

### PROYECTO

**Estado de proyecto:**

<span style="color: #3498DB;">
    - Nombre del proyecto<br>
    - Descripción<br>
    - Identificador proyecto (ID_proyecto)<br>
    - crqs asociados <br>
</span>

### CRQ

**Estado de cambio:**

<span style="color: #3498DB;">
    - Identificador del CRQ (id_crq).<br>
    - Nombre del CRQ.<br>
    - Descripción del cambio.<br>
    - Fecha de inicio prevista.<br>
    - Fecha de finalización prevista.<br>
    - Proyecto al que pertenece.<br>
    - Tareas asociadas.<br>
</span>

### TAREA

**Estado de tarea:**

<span style="color: #3498DB;">
    - Título.<br>
    - Descripción.<br>
    - Estado.<br>
    - Responsable.<br>
    - Identificador tarea (ID_tarea).<br>
    - Proyecto al que pertenece.<br>
</span>

### USUARIO

**Estado:**

<span style="color: #3498DB;">
    - Nombre de usuario.<br>
    - Identificador usuario (ID_usuario).<br>
</span>

<br>

> No incluyas información simplemente porque pueda resultar útil. <br>

> ¿La aplicación necesita realmente conocer ese dato para funcionar? <br>

---

## Parte 3. Identificar el comportamiento

Ahora vamos a cambiar la pregunta.

Ya no queremos saber qué tiene cada objeto. Queremos saber qué puede hacer.

### PROYECTO

**Puede realizar las siguientes acciones:**

- Crear proyecto.
- Añadir CRQ al proyecto.
- Consultar información del proyecto.
- Modificar los datos del proyecto (mientras se encuentre en fase de borrador).

### GESTIÓN DE CAMBIOS (CRQ)

- Crear CRQ.
- Modificar la información del CRQ mientras esté en estado BORRADOR.
- Añadir o quitar tareas mientras esté en estado BORRADOR.
- Cambiar el estado del CRQ.
- Consultar la información y el estado del CRQ.
- Cancelar CRQ.

### TAREA

**Puede realizar las siguientes acciones:**
- Crear tarea.
- Asignar tarea a un grupo técnico.
- Cambiar el estado de la tarea.
- Cerrar tarea.

### USUARIO

**Puede:**

- Iniciar sesión.
- Consultar los proyectos asignados.
- Consultar las tareas asignadas.
- Realizar acciones sobre las tareas asignadas.

Piensa en comportamientos para cada objeto.

**Regla:** expresa los comportamientos como acciones.

---

## Parte 4. Responsabilidades

Ahora viene una de las decisiones más importantes de la POO.

¿Quién debería encargarse de cada acción?

Supongamos que queremos completar una tarea.

Tenemos varias posibilidades:

- Tarea.
- Usuario.
- Proyecto.
- CRQ.
- `main.py`.

¿Quién debería ser responsable?

Justifica tu decisión.

Haz lo mismo con:

- Asignar una tarea.
- Cambiar el estado de una tarea.
- Crear un proyecto.
- Añadir una tarea a un proyecto.

Puedes utilizar esta tabla:

| Acción | Objeto responsable | ¿Por qué? |
|---|---|---|
| Completar una tarea | Tarea | Porque es el objeto que gestiona su propio estado y puede cambiarlo a completada. |
| Iniciar una tarea | Tarea | Porque es el objeto que gestiona su estado y lo cambia a EN_CURSO cuando el usuario solicita iniciarla. |
| Asignar responsable | Tarea | Porque la tarea almacena el grupo técnico responsable y permite actualizar esa información cuando un usuario realiza la asignación. |
| Crear proyecto | Proyecto | Porque es el objeto encargado de representar y almacenar la información del proyecto. |
| Añadir tarea al proyecto |  Proyecto | Porque es el objeto que contiene y gestiona la colección de tareas asociadas. |

---

## Parte 5. Diseñar el modelo

Ahora reúne tus decisiones.

Construye un primer modelo conceptual:

```text
             PROYECTO
                 |
                 | contiene
                 v
               TAREA
                 |
                 | asignada a
                 v
              USUARIO
```

## Parte 5. Diseñar el modelo

![Modelo conceptual del proyecto](modelo-conceptual.png)

 > Añade la información y los comportamientos que hayas decidido.

---

## Parte 6. Diseñar las clases con UML

Por ejemplo:

```text
┌─────────────────────────────┐
│            Tarea            │
├─────────────────────────────┤
│ - titulo: str               │
│ - descripcion: str          │
│ - estado: str               │
│ - responsable: Usuario      │
├─────────────────────────────┤
│ + iniciar(): None           │
│ + completar(): None         │
│ + reasignar(): None         │
└─────────────────────────────┘
```

![Modelo UML](02-modelo-uml.png)

Haz lo mismo para el resto de objetos que hayas determinado.

No es necesario representar todavía las relaciones UML posibles.

---

## Parte 7. Primera implementación con Python

Ahora sí podemos programar.

Crea el proyecto utilizando el entorno profesional que hemos visto en clase.

La estructura inicial será:

```text
taskflow/
├── .gitignore
├── README.md
├── pyproject.toml
└── src/
    └── taskflow/
        └── __init__.py
```

Crea primero la clase `Tarea` y, a continuación, el resto.

Crea también el repositorio correspondiente en GitHub.

---

## Parte 8. El historial de Git

Durante el laboratorio utiliza Git para registrar la evolución del proyecto.

No esperes hasta el final.

Realiza commits cuando completes partes significativas.

Por ejemplo:

**Primer commit:**

```bash
git add .
git commit -m "chore: crear proyecto TaskFlow"
```

**Segundo commit:**

```bash
git add .
git commit -m "feat: crear clase Tarea"
```

**Tercer commit:**

```bash
git add .
git commit -m "feat: implementar comportamiento de Tarea"
```

**Subir los cambios:**

```bash
git push
```

Consulta el historial:

```bash
git log --oneline
```

Tu repositorio debe permitir observar cómo ha evolucionado el diseño.

---

## Parte 9. La IA como analista

En este laboratorio vamos a utilizar IA, pero no para que nos diseñe y programe TaskFlow.

Primero realiza tu propio análisis.

Después puedes utilizar una IA para contrastarlo.

Utiliza un prompt como este:

### Prompt de análisis

```text
Estoy diseñando una aplicación de gestión de proyectos
llamada TaskFlow.

He identificado estos objetos:

- Proyecto
- Usuario
- Tarea

Para cada uno he definido este estado:
[PEGA AQUÍ TU PROPUESTA]

Y estos comportamientos:
[PEGA AQUÍ TU PROPUESTA]

Analiza mi diseño como si fueras un analista de software.

No escribas código.

Indica:

1. Qué decisiones parecen coherentes.
2. Qué responsabilidades podrían estar mal asignadas.
3. Qué información podría faltar.
4. Qué información podría sobrar.
5. Qué preguntas debería hacerme antes de programar.

No rediseñes la solución completa.

Si no sabes algo, no te lo inventes.
```

Después compara los resultados:

```text
MI DISEÑO
    |
    ├── Coincidencias
    |
    ├── Diferencias
    |
    └── Decisiones que cambio
```

La IA no sustituye tu diseño.

La utilizamos para hacer preguntas y detectar posibles problemas.

---

# 📦 Entregables del laboratorio

La estructura final del proyecto será:

```text
taskflow/
├── .gitignore
├── README.md
├── pyproject.toml
│
├── src/
│   └── taskflow/
│       ├── __init__.py
│       ├── main.py
│       ├── tarea.py
│       ├── usuario.py
│       └── proyecto.py
│
└── doc/
    ├── 01-analisis.md
    ├── 02-modelo-uml.png
    └── 03-ia-prompt.md
```

## Contenido de la documentación

El documento `01-analisis.md` debe recoger:

- Objetos identificados.
- Estado de cada objeto.
- Comportamiento.
- Responsabilidades.
- Decisiones de diseño.
- Cambios realizados después de utilizar IA.
- Aclaraciones.

## Responsabilidad de cada archivo

### `__init__.py`

Indica que este directorio forma parte de un paquete Python.

### `main.py`

Desde aquí arranca nuestra aplicación.

### `tarea.py`

Define la clase `Tarea`.

### `usuario.py`

Define la clase `Usuario`.

### `proyecto.py`

Define la clase `Proyecto`.

---

## Ejemplo de utilización de una clase

En `main.py`, para hacer uso de `Tarea` y poder crear instancias, por ejemplo, tendríamos que importar la clase:

```python
from taskflow.tarea import Tarea


def main() -> None:
    tarea = Tarea("Diseñar la página de inicio")

    print(tarea.titulo)


if __name__ == "__main__":
    main()
```

---

# ➕ Ampliación

Investiga cómo podríamos implementar las siguientes funcionalidades:

1. Listar las tareas de un responsable en concreto.
2. Listar los proyectos y las tareas asociadas.

**Reflexiona:**

- ¿Qué objeto debería encargarse de estas operaciones?
- ¿Dónde deberíamos almacenar las tareas?
- ¿Cómo podemos relacionar un usuario con sus tareas?
- ¿Cómo podemos consultar todas las tareas de un proyecto?

No es necesario implementar estas ampliaciones inicialmente. Primero piensa cómo encajarían en el modelo de objetos.
