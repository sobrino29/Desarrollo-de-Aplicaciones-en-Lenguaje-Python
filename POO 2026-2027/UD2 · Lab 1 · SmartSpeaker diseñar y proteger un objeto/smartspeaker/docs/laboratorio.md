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

### Explicación del uso de propiedades

<span style="color: #3498DB; font-size: 14px;">

    He utilizado `@property` para consultar (que no modificar) los atributos internos de la clase mediante interfaz pública.

    Los atributos nombre, volumen y estado se pueden consultar con getter (@property), y dependiendo el caso se pueden modificar (setter).

    - **nombre:** permite consultar el nombre y modificarlo mediante un setter que comprueba que sea una cadena no vacía y elimina los espacios exteriores.

    - **volumen:** permite consultar y modificar el volumen mediante un setter que comprueba que sea un número entero entre 0 y 100.

    - **estado:** permite consultar si el altavoz está encendido o apagado, pero no dispone de setter público. Su modificación se realiza mediante los métodos `encender()` y `apagar()`.
</span>

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

### 4.3. Registro de resultados

| ID  | Resultado obtenido                  | ¿Coincide? |
| --- | ----------------------------------- | ---------- |
| V01 | Altavoz creado correctamente        | Sí         |
| V02 | Devuelve `"Salón"`                  | Sí         |
| V03 | Devuelve `30`                       | Sí         |
| V04 | Devuelve `"apagado"`                | Sí         |
| V05 | Se acepta el volumen `50`           | Sí         |
| V06 | Se acepta el volumen `0`            | Sí         |
| V07 | Se acepta el volumen `100`          | Sí         |
| V08 | Estado `"encendido"`                | No         |
| V09 | Estado `"apagado"`                  | No         |
| V10 | Devuelve `"Cocina"`                 | Sí         |
| I01 | `raise ValueError("El nombre no puede estar vacío")`                        | Sí         |
| I02 | `raise ValueError("El nombre no puede estar vacío")`                        | Sí         |
| I03 | `raise ValueError("El nombre debe ser una cadena de texto")`                        | Sí         |
| I04 | `raise ValueError("El volumen debe estar entre 0 y 100")`                        | Sí         |
| I05 | `raise ValueError("El volumen debe estar entre 0 y 100")`                        | Sí         |
| I06 | `raise ValueError("El volumen debe ser un número entero")`                        | Sí         |
| I07 | `raise ValueError("El volumen debe ser un número entero")`                        | Sí         |
| I08 | `AttributeError: property 'estado' of 'Altavoz' object has no`                    | Sí         |

Si una prueba falla, no cambies inmediatamente el resultado esperado para hacerla coincidir con el programa. Primero investiga si el error está en la implementación.

En las pruebas V08 y V09 he tenido que ajustar el código porque tenía puesto booleanos, para con una condición indicarle un string.

    `@property
    def estado(self) -> str:
  
    # Se ajusta porque nos indican que tiene que devolver apagado no false    
        if self._estado == False:
            return "apagado"
        else:
            return "encendido"
            
        # Le indico la manera de consultar un atributo interno, el estado podrá consultarse mediante altavoz.estado.
        return self._estado`

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
[PEGA AQUÍ TU IMPLEMENTACIÓN]<br>
<span style="color: #34db3f; font-size: 14px;">
    He revisado los tres ficheros: altavoz.py, main.py y pruebas_manuales.py. Voy a seguir el prompt de tu actividad: comprobar cada requisito, señalar errores y proponerte pruebas, sin reescribirte la clase completa.<br>
</span>

<span style="color: #34db3f; font-size: 14px;">
    En general, vas por buen camino. Has utilizado correctamente @property, los setters y los atributos internos con guion bajo (_nombre, _volumen, _estado).
    1. Revisión de altavoz.py
    Requisito 1. Validar el nombre
    Correcto
    Tu código comprueba tres cosas:
    - Que el nombre sea una cadena (str).
    - Que no esté vacío ni contenga únicamente espacios.
    - Que elimine los espacios exteriores con .strip() antes de almacenarlo.
    Además, utilizas self._nombre para guardar el dato internamente. Correcto.<br>
    Requisito 2. Validar el volumen
    Correcto, con una mejora
    Has comprobado que:
    - Sea un número entero.
    - No sea inferior a 0.
    - No sea superior a 100.
    - Se aplique la misma validación al crear el objeto y al modificarlo.
    La condición nuevo_volumen < 0 or nuevo_volumen > 100 está bien planteada: permite los valores 0 y 100.

    Hay un pequeño caso especial de Python que conviene conocer: bool es una subclase de int. Por eso, True y False también pasan tu comprobación con isinstance(nuevo_volumen, int).

    Podrías estudiar cómo impedir que se acepten valores booleanos como volumen. No es necesario cambiar nada más de tu validación.
</span>
    Requisito 3. Controlar el estado
    Correcto, con código sobrante
    Has hecho bien en:
    - Inicializar _estado como False.
    - Devolver "apagado" cuando es False.
    - Devolver "encendido" cuando es True.
    - Modificarlo únicamente mediante encender() y apagar().
    - No crear un setter para estado.
    Hay una cosa que debes limpiar: después del if/else tienes otro return self._estado. Ese código nunca se ejecuta, porque las dos ramas anteriores ya devuelven un resultado.

    No es un error que cambie el comportamiento, pero sobra.
    Requisito 4. Mantener una interfaz clara
    Correcto
    Tu main.py utiliza la interfaz pública:
    altavoz.nombrealtavoz.volumenaltavoz.estadoaltavoz.volumen = 50altavoz.encender()altavoz.apagar()
</span>
<span style="color: #34db3f; font-size: 14px;">


    No necesita acceder a _nombre, _volumen ni _estado. Esto cumple lo que pide el ejercicio.
    2. Revisión de main.py
    Correcto en general
    El programa crea el altavoz, consulta sus propiedades, cambia el volumen y utiliza los métodos de encendido y apagado.

    También has añadido bloques try-except para comprobar las excepciones. Es una buena forma de verificar que las validaciones funcionan sin detener todo el programa.

    Dos observaciones:
    1. Llamas primero a apagar() y después a encender(). No está mal, pero si quieres comprobar ambas operaciones, consulta altavoz.estado después de cada una.
    2. La prueba de asignar altavoz.estado = True está bien planteada: debe provocar AttributeError, porque no has definido un setter.
    3. Revisión de pruebas_manuales.py
    Aquí hay algunas cosas que conviene mejorar.

    A. Pruebas válidas

    Las pruebas V01-V10 están planteadas correctamente. Compruebas creación, consultas, modificaciones, límites del volumen, estado y eliminación de espacios.

    He visto dos pequeños errores en los mensajes:
    - En V02 imprimes V01 en lugar de V02.
    - En V09 imprimes V08 en lugar de V09.
    No afectan al funcionamiento, pero conviene corregirlos para que el registro sea claro.

    B. Pruebas inválidas

    Tienes las pruebas I01-I07 comentadas con #. Eso significa que no se ejecutan.

    Además, en I08 tienes esto:
    altavoz.estado = "encendido"print(altavoz.estado)



    La primera línea debe provocar AttributeError, por lo que la segunda no llegará a ejecutarse.

    Mi recomendación es que utilices un try-except independiente para cada prueba inválida, como ya has hecho en main.py.

    Así podrás comprobar todas sin que la primera excepción detenga el resto.
    4. Posibles problemas de diseño
    Hay tres recomendaciones que me parecen especialmente útiles:
    Recomendación	Motivo
    Eliminar el return self._estado sobrante	Evitas código innecesario.
    Corregir los mensajes V02 y V09	Facilitas la identificación de cada prueba.
    Capturar las excepciones de I01-I08	Permites ejecutar todas las pruebas inválidas.

    También he detectado algo importante en I06:

    En el enunciado de tu prueba pone:
    altavoz.volumen = 25.5



    Pero en el fichero tienes comentado:
    #altavoz = Altavoz("Salón", 25.5)



    No son exactamente la misma prueba. La primera comprueba que el setter rechaza un volumen decimal al modificar un objeto ya creado. Es la que te pide la tabla.
    5. Pruebas adicionales que te propongo
    Estas son pruebas que puedes añadir para comprobar casos que no aparecen expresamente en tu tabla:
    Prueba	Operación	Resultado esperado
    Extra 1	Asignar altavoz.nombre = "   "	ValueError
    Extra 2	Asignar altavoz.volumen = 25.5	ValueError
    Extra 3	Asignar altavoz.volumen = True	Actualmente tu código lo acepta; sería interesante corregirlo
    Extra 4	Encender y consultar el estado	"encendido"
    Extra 5	Apagar y consultar el estado	"apagado"

    6. Mi valoración general
    Diseño de la clase
    Bien planteado


    Validación del nombre
    Correcta

    Validación del volumen
    Correcta, con mejora

    Control del estado
    Correcto

    Interfaz pública
    Correcta

    Pruebas manuales
    Por completar


    Mi conclusión: no veo problemas importantes en el diseño general de tu clase. Has entendido la idea principal del laboratorio: la propia clase debe proteger sus datos y controlar cómo se modifican.

    Una última aclaración: esta es una revisión estática del código que me has enviado; no he ejecutado los ficheros. Por tanto, no voy a afirmar que todas las pruebas pasan.

    Para tu apartado 5 del laboratorio.md, puedes utilizar dos recomendaciones reales de esta revisión: la comprobación de valores booleanos en el volumen y la corrección de las pruebas inválidas para que se ejecuten con try-except. Después tendrás que decidir si las aceptas y comprobarlas.
</span>

Actividad de verificación
Selecciona dos recomendaciones de la IA y decide si son correctas.

Recomendación de la IA	¿La acepto?	Justificación	¿Cómo la he verificado?
<br>
<span style="color: #344ddb; font-size: 14px;">
    Acepto lo que me recomienda la IA pero no lo comparto, porque para probar los try-except si dejo todos activos en el momento que salte uno, se me sale de la ejecución.
<span>

Recomendación 1	Sí / No	Explicación	Prueba o análisis del código <br>
<span style="color: #344ddb; font-size: 14px;">
    Acepto lo que me recomienda la IA acerca de la comprobación de valores booleanos en el atributo volumen, prefiero trabajar con este tipo de datos antes que con string, lo veo más seguro
<span>
Recomendación 2	Sí / No	Explicación	Prueba o análisis del código
La IA no sustituye a las pruebas: sus propuestas deben contrastarse con los requisitos y con el comportamiento real del programa. <br>
<span style="color: #344ddb; font-size: 14px;">
    No acepto lo que me recomienda la IA acerca de que no aparecen las pruebas, dado que si aparecen, tanto en el fichero pruebas_manuales.py como en el fichero main.py y el hecho de que esté comentadas es para probar una por una, sin que ello suponga la salida de la ejecución.
<span>
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

1.Las reglas de negocio identificadas. <br>
2.La tabla de diseño de la interfaz pública. <br>
3.Una explicación de las propiedades utilizadas. <br>
4.Los resultados de las pruebas válidas e inválidas. <br>
5.Dos recomendaciones de la IA y la decisión tomada sobre ellas. <br>

6.Una reflexión final: ¿qué ventajas tiene que la clase controle sus propias reglas?
<span style="color: #3498DB; font-size: 14px;">
    <br>Que se encarga de proteger sus datos y garantizar que se cumplan las reglas establecidas de negocio, evitando que otras partes del programa introduzcan valores incorrectos.
</span>