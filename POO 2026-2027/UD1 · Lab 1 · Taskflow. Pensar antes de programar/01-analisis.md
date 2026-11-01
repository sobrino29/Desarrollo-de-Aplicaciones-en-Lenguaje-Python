# 🧪 Laboratorio POO: Diseñar TaskFlow

## Pensar antes de programar

Imagina que una pequeña empresa necesita una aplicación para organizar sus proyectos de desarrollo.

La aplicación debe permitir:

- Crear proyectos.
- Registrar usuarios.
- Crear tareas.
- Asignar tareas a usuarios.
- Cambiar el estado de una tarea.

Una tarea puede encontrarse en diferentes estados:

```text
PENDIENTE → EN PROGRESO → COMPLETADA
```

Nuestro objetivo es diseñar el modelo de objetos y realizar una primera implementación en Python.

---

## Parte 1. Analizar el problema

Antes de escribir código, identifica las entidades importantes del problema.

Completa una tabla como esta:

| Posible objeto | ¿Por qué existe? | ¿Qué información necesita? |
|---|---|---|
| Proyecto | | |
| Tarea | | |

Después responde:

1. ¿Qué otras entidades podrían existir?
2. ¿Cuáles son realmente necesarias?
3. ¿Cuáles son solamente datos o características de otras entidades?

> No busques todavía una única respuesta correcta. Lo importante es justificar tus decisiones.

---

## Parte 2. Identificar el estado

El estado de un objeto es la información que describe cómo se encuentra en un momento determinado.

Para cada objeto que hayas identificado, determina qué información necesita conocer.

Por ejemplo:

### TAREA

**Estado:**
- Título.
- Descripción.
- Estado.
- Responsable.

No incluyas información simplemente porque pueda resultar útil.

¿La aplicación necesita realmente conocer ese dato para funcionar?

---

## Parte 3. Identificar el comportamiento

Ahora vamos a cambiar la pregunta.

Ya no queremos saber qué tiene cada objeto. Queremos saber qué puede hacer.

Por ejemplo:

### TAREA

**Puede:**
- Completar.
- Iniciar.
- Reasignarse.

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
| Completar una tarea | | |
| Iniciar una tarea | | |
| Asignar responsable | | |
| Crear proyecto | | |
| Añadir tarea al proyecto | | |

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

Añade la información y los comportamientos que hayas decidido.

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
