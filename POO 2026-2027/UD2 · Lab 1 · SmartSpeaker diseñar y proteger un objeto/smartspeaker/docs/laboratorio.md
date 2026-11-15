# 🧪 Laboratorio POO: Diseñar TaskFlow

## Parte 1. Analizar el problema

### Identificación de objetos

1.1. Primera versión
Crea un archivo altavoz.py con la siguiente implementación:

class Altavoz:
    def __init__(self, nombre, volumen):
        self.nombre = nombre
        self.volumen = volumen
        self.encendido = False

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

Crea un archivo main.py:

from altavoz import Altavoz


def main() -> None:
    altavoz = Altavoz("Salón", 30)

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.encendido)

    altavoz.nombre = ""
    altavoz.volumen = -50
    altavoz.encendido = "quizá"

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.encendido)


if __name__ == "__main__":
    main()

Ejecuta el programa y observa el resultado.

---

### 1.2. Identificamos los problemas
Responde a estas preguntas:

¿Qué ocurre cuando el nombre está vacío?<br>
<span style="color: #3498DB; font-size: 14px;">
    Al venir vacío el atributo nombre, no se le asigna ninguna instancia.
</span>
<br>
<br>
¿Qué ocurre cuando el volumen es negativo?<br>
<span style="color: #3498DB; font-size: 14px;">
    Los valores van del 0 al 100, por lo tanto, el programa no debería permitir que funcione con un valor negativo.
</span>
<br>
<br>
¿Podemos asignar un texto al atributo encendido?<br>
<span style="color: #3498DB; font-size: 14px;">
    Por default el atributo encendido está a True, si no validas el atributo encendido con un setter, todo lo que pongas se lo va a comer.
</span>
<br>
<br>
¿Quién debería ser responsable de evitar estos valores: el código que utiliza la clase o la propia clase?<br>
<span style="color: #3498DB; font-size: 14px;">
    La propia clase, porque en el constructor estás asignando los valores, y debería pasar unos test unitarios antes de mandar el código a producción.
</span>
<br>
<br>
¿Qué problemas podría provocar que cualquier parte del programa modificase directamente el estado del altavoz?<br>
<span style="color: #3498DB; font-size: 14px;">
    La clase conoce las reglas de un altavoz mejor que el código externo que la utiliza por eso conviene que la propia clase sea responsable de controlar su estado, y así evitamos que el resto del programa dependa de cómo están implementados.
</span>
<br>
<br>
---

## 1.3. Definimos las reglas de negocio

## Completa la siguiente tabla antes de modificar el código

| Elemento | Regla que debe cumplir | Ejemplo inválido |
|---|---|---|
| Nombre | Debe ser una cadena de texto no vacía ni formada solo por espacios. | `""` |
| Volumen | Debe ser un número entero entre 0 y 100, ambos incluidos. | `-5` |
| Estado | Solo puede representar si el altavoz está encendido o apagado. | `"quizá"` |
| Encendido | Debe cambiarse mediante una operación del objeto. | `altavoz.encendido = True` |

El último ejemplo representa un problema de diseño: queremos que el resto del programa utilice operaciones como `encender()` y `apagar()`, en lugar de modificar directamente el estado.

## Parte 2. Diseñamos la interfaz pública

## Diseño de la interfaz pública e interna

Antes de programar, decide qué elementos podrá utilizar directamente otro componente de la aplicación y cuáles estarán destinados al funcionamiento interno de la clase.

Recuerda las convenciones de Python:

| Escritura | Significado | Ejemplo |
|---|---|---|
| `nombre` | Elemento público | `altavoz.nombre` |
| `_nombre` | Elemento interno por convención | `self._volumen` |
| `__nombre` | Activa el *name mangling* | `self.__codigo` |
| `__nombre__` | Nombre especial de Python o de una API | `__init__` |

## 2.1. Diseña la interfaz

## Diseño de la interfaz pública e interna

Completa la tabla:

| Elemento                | ¿Público o interno? | ¿Cómo debería utilizarse?                 |
| ----------------------- | ------------------- | ----------------------------------------- |
| Nombre del altavoz      | <span style="color: #3498DB;">Público, porque el programa principal necesita consultar y modificar el nombre, pero las modificaciones deben validarse. </span> | Consultar y modificar con validación |
| Volumen                 | <span style="color: #3498DB;">Público, porque el programa principal necesita consultar y modificar el volumen, pero las modificaciones deben validarse.  </span> | Consultar y modificar con validación |
| Estado de encendido     | <span style="color: #3498DB;">Público porque el programa principal necesita consultar el estado del altavoz, aunque no debe poder modificarlo directamente.</span> | Consultar, pero no modificar directamente |
| Operación para encender | <span style="color: #3498DB;">Público, porque el programa principal necesita poder ejecutarlos para controlar el altavoz.</span> | Cambiar el estado |
| Operación para apagar   | <span style="color: #3498DB;">Público, porque el programa principal necesita poder ejecutarlos para controlar el altavoz.</span> | Cambiar el estado |

## 2.2. Justifica tus decisiones

## Reflexión sobre el diseño de la clase

Explica brevemente:

- ¿Por qué el volumen necesita validación?<br>
<span style="color: #3498DB; font-size: 14px;">
    El volumen debe validarse porque estaríamos jugando con cualquier tipo de valor (evitamos que se le asignen valores incorrectos o fuera del rango permitido) y oscila entre 0 y 100.
</span>
<br>
<br>
- ¿Por qué no queremos que se modifique directamente el estado de encendido?<br>
<span style="color: #3498DB; font-size: 14px;">
    El estado encendido si lo ponemos directamente a True estamos dando pie a que pueda incluirse cualquier tipo de valor a la operación de encendido (como una cadena de texto o cualquier otro valor distinto de True o False). Por eso, queremos controlar los cambios mediante las operaciones encender() y apagar().
</span>
<br>
<br>
- ¿Qué diferencia existe entre utilizar `_volumen` y utilizar una propiedad pública llamada `volumen`?<br>
<span style="color: #3498DB; font-size: 14px;">
    Con _volumen estamos indicando que es un elemento privado por convención (es decir se utiliza para uso interno de la clase)mientras que con el atributo volumen estamos indicando que es un elemento público (que permite consultar y modificar el valor, aplicando las validaciones correspondientes).
</span>
<br>
### No se trata de ocultar los datos por ocultarlos: se trata de diseñar una interfaz que permita utilizar el objeto sin saltarse sus reglas
---

## Parte 3. Implementamos la clase

---

Modifica `altavoz.py` para cumplir los requisitos siguientes.

### Requisito 1. Validar el nombre

- Debe ser una cadena de texto.
- No puede estar vacío ni contener únicamente espacios.
- Se eliminarán los espacios exteriores antes de almacenar el nombre.

### Requisito 2. Validar el volumen

- Debe ser un número entero.
- Su valor estará comprendido entre 0 y 100, ambos incluidos.
- La misma validación debe aplicarse tanto al crear el objeto como al modificar el volumen.

### Requisito 3. Controlar el estado

- Un altavoz nuevo comienza apagado.
- El estado podrá consultarse mediante `altavoz.estado`.
- El resto del programa no debe poder cambiarlo mediante una asignación ordinaria a `altavoz.estado`.
- El método `encender()` permitirá encender el dispositivo.
- El método `apagar()` permitirá apagarlo.

## Requisito 4. Mantener una interfaz clara

El código que utiliza la clase debería poder escribir:
```
altavoz = Altavoz("Salón", 30)

print(altavoz.nombre)
print(altavoz.volumen)
print(altavoz.estado)

altavoz.volumen = 50
altavoz.encender()
altavoz.apagar()
```
No debería necesitar acceder a los atributos internos para utilizar las operaciones habituales.
---

## Parte 4. Comprobamos el comportamiento

Crea un archivo pruebas_manuales.py. No utilizaremos todavía pytest: en esta actividad queremos comprobar manualmente los resultados y preparar el terreno para automatizarlos pronto.

## 4.1. Pruebas válidas
Comprueba las siguientes situaciones:

## Pruebas manuales

| ID | Operación | Resultado esperado |
|---|---|---|
| V01 | Crear un altavoz con nombre `"Salón"` y volumen `30` | Se crea correctamente |
| V02 | Consultar el nombre | Devuelve `"Salón"` |
| V03 | Consultar el volumen | Devuelve `30` |
| V04 | Consultar el estado inicial | Devuelve `"apagado"` |
| V05 | Cambiar el volumen a `50` | Se acepta |
| V06 | Cambiar el volumen a `0` | Se acepta |
| V07 | Cambiar el volumen a `100` | Se acepta |
| V08 | Ejecutar `encender()` | El estado pasa a `"encendido"` |
| V09 | Ejecutar `apagar()` | El estado pasa a `"apagado"` |
| V10 | Crear un altavoz con nombre `"  Cocina  "` | Se almacena `"Cocina"` |

## 4.2. Pruebas inválidas
Comprueba las siguientes situaciones:

## Pruebas de validación (casos no válidos)

| ID  | Operación                              | Resultado esperado |
| --- | -------------------------------------- | ------------------ |
| I01 | Crear un altavoz con nombre `""`       | `ValueError`       |
| I02 | Crear un altavoz con nombre `"   "`    | `ValueError`       |
| I03 | Crear un altavoz con nombre `25`       | `ValueError`       |
| I04 | Crear un altavoz con volumen `-1`      | `ValueError`       |
| I05 | Crear un altavoz con volumen `101`     | `ValueError`       |
| I06 | Asignar `altavoz.volumen = 25.5`       | `ValueError`       |
| I07 | Asignar `altavoz.volumen = "alto"`     | `ValueError`       |
| I08 | Asignar `altavoz.estado = "encendido"` | `AttributeError`   |

No es necesario probar todos los casos con un único programa. Puedes ejecutar cada comprobación por separado para identificar fácilmente la excepción que se produce.

## 4.3. Registra los resultados
Crea una tabla con tres columnas: ID, resultado obtenido y ¿coincide con el esperado?

Si una prueba falla, no cambies inmediatamente el resultado esperado para hacerla coincidir con el programa. Primero investiga si el error está en la implementación.

## Parte 5. IA como revisora del diseño
Cuando tengas una primera versión funcional, utiliza la IA para revisar el código.

Prompt de revisión
Estoy desarrollando una clase Altavoz en Python.

La clase debe cumplir estas reglas:
- El nombre debe ser una cadena no vacía ni formada solo por espacios.
- Se eliminan los espacios exteriores del nombre.
- El volumen debe ser un entero entre 0 y 100, incluidos.
- El estado inicial debe ser "apagado".
- El estado solo se modifica mediante los métodos encender() y apagar().
- El nombre y el volumen se consultan mediante propiedades.
- Los valores inválidos deben provocar ValueError.
- El estado no debe disponer de un setter público.

Revisa el código que te proporciono.

1. Comprueba cada requisito por separado.
2. Busca errores de validación.
3. Comprueba que los setters no provocan recursión.
4. Señala posibles problemas de diseño.
5. Propón casos de prueba que todavía no haya comprobado.

No reescribas la clase completa.
No afirmes que el código funciona sin haberlo ejecutado.
No introduzcas listas, diccionarios, herencia ni conceptos que todavía no hemos estudiado.

Código:
[PEGA AQUÍ TU IMPLEMENTACIÓN]

Actividad de verificación
Selecciona dos recomendaciones de la IA y decide si son correctas.

Recomendación de la IA	¿La acepto?	Justificación	¿Cómo la he verificado?
Recomendación 1	Sí / No	Explicación	Prueba o análisis del código
Recomendación 2	Sí / No	Explicación	Prueba o análisis del código
La IA no sustituye a las pruebas: sus propuestas deben contrastarse con los requisitos y con el comportamiento real del programa.

## Parte 6. Entrega y reflexión final
Entrega el proyecto con esta estructura:

```text
smart-speaker/
├── altavoz.py
├── main.py
├── pruebas_manuales.py
└── docs/
    └── laboratorio.md
```
El documento docs/laboratorio.md debe incluir:

Las reglas de negocio identificadas.
La tabla de diseño de la interfaz pública.
Una explicación de las propiedades utilizadas.
Los resultados de las pruebas válidas e inválidas.
Dos recomendaciones de la IA y la decisión tomada sobre ellas.
Una reflexión final: ¿qué ventajas tiene que la clase controle sus propias reglas?