# SmartSpeaker: pruebas automatizadas con Pytest

## Contexto

En la primera fase del laboratorio has diseñado e implementado una clase `Altavoz` que representa un altavoz inteligente.

Has definido sus atributos, establecido qué información puede consultarse y modificarse y programado mecanismos para controlar su estado y validar los datos introducidos.

Sin embargo, ¿cómo puedes comprobar que la clase se comporta correctamente? ¿Cómo puedes detectar si una modificación rompe algo que antes funcionaba?

En esta fase incorporarás **pruebas automatizadas con pytest** para verificar el comportamiento de tu clase.

No se trata únicamente de comprobar que el programa funciona con un ejemplo, sino de diseñar diferentes situaciones que permitan detectar errores y comprobar que se respetan las reglas establecidas.

## Preparación del proyecto

Añade pytest como dependencia de desarrollo:

```powershell
uv add --dev pytest
```

Comprueba que se ha instalado correctamente:

```powershell
uv run pytest --version
```

Organiza el proyecto con una estructura similar a esta:

```text
smart-speaker/
├── .gitignore
├── pyproject.toml
├── uv.lock
├── src/
│   └── smartspeaker/
│       ├── altavoz.py
│       ├── main.py
│       └── __init__.py
├── tests/
│   └── test_altavoz.py
└── docs/
    └── laboratorio.md
```

El archivo `altavoz.py` debe contener la clase desarrollada en la primera fase.

El archivo `test_altavoz.py` contendrá las pruebas automatizadas. Recuerda que pytest identifica por defecto los archivos cuyos nombres empiezan por `test_` y las funciones de prueba cuyos nombres también empiezan por `test_`.

## Primeras pruebas

Antes de diseñar toda la batería de pruebas, crea una prueba sencilla que compruebe que el altavoz se construye correctamente.

Por ejemplo, si has creado un altavoz llamado `Salón`, puedes comprobar que su propiedad `nombre` devuelve ese valor.

```python
from smartspeaker.altavoz import Altavoz


def test_altavoz_se_crea_con_nombre():
    altavoz = Altavoz("Salón", 30)

    assert altavoz.nombre == "Salón"
```

Ejecuta las pruebas desde la raíz del proyecto:

```powershell
uv run pytest
```

Analiza el resultado obtenido.

Debes identificar:

- Cuántas pruebas se han ejecutado.
- Cuántas han superado la comprobación.
- Qué información aparece cuando una prueba falla.

## Diseño de la batería de pruebas

Ahora debes diseñar una batería de pruebas que permita comprobar los requisitos de tu clase `Altavoz`.

No tienes que limitarte a copiar los ejemplos anteriores. Debes identificar qué comportamiento quieres comprobar, qué datos necesitas y cuál debería ser el resultado esperado.

### Pruebas de creación

Comprueba que un altavoz se crea correctamente.

Como mínimo, debes verificar:

- Que se almacena correctamente el nombre.
- Que se almacena correctamente el volumen inicial.
- Que el estado inicial es `apagado`.

### Pruebas de propiedades

Comprueba que las propiedades permiten consultar y modificar correctamente los datos cuando corresponda.

Ten en cuenta las reglas establecidas en la primera fase:

- El nombre debe ser una cadena no vacía.
- Los espacios al principio y al final del nombre deben eliminarse.
- El volumen debe ser un número entero entre 0 y 100, ambos incluidos.
- El estado debe poder consultarse, pero no modificarse directamente mediante su propiedad pública.

Diseña pruebas que permitan comprobar tanto los casos válidos como los inválidos.

### Pruebas de comportamiento

Comprueba que los métodos de la clase modifican correctamente el estado del altavoz.

Como mínimo, debes probar:

- Que `encender()` cambia el estado a `encendido`.
- Que `apagar()` cambia el estado a `apagado`.
- Que puedes apagar un altavoz después de haberlo encendido.

Piensa si existen otros comportamientos que merezca la pena comprobar.

### Pruebas de validación y errores

Una parte importante de las pruebas consiste en comprobar que el programa rechaza correctamente los datos que incumplen las reglas.

Diseña pruebas para situaciones como:

| Propiedad | Dato de prueba | Comportamiento esperado |
|---|---|---|
| Nombre | `""` | Rechazar |
| Nombre | `"   "` | Rechazar |
| Nombre | `25` | Rechazar |
| Volumen | `-1` | Rechazar |
| Volumen | `101` | Rechazar |
| Volumen | `"50"` | Rechazar |
| Volumen | `True` | Rechazar |

Para comprobar que se produce una excepción, pytest proporciona `pytest.raises()`.

Ejemplo:

```python
import pytest


def test_nombre_vacio_no_es_valido():
    with pytest.raises(ValueError):
        Altavoz("", 30)
```

La prueba solo se considera superada si se produce la excepción esperada.

Investiga cómo utilizar `pytest.raises()` para completar el resto de pruebas de validación.

**Importante:** no basta con que el programa genere cualquier error. Debes comprobar que genera el tipo de excepción esperado.

## Prueba de robustez: provoca un fallo

Una vez que tengas varias pruebas implementadas, realiza este experimento:

1. Ejecuta toda la batería de pruebas y comprueba que funciona.
De la batería de pruebas hay una que no funciona que es la del valor booleano al atributo volumen.
collected 16 items                                                                                                                                                                           

tests/test_altavoz.py::test_altavoz_se_crea_con_nombre Salón
PASSED
tests/test_altavoz.py::test_altavoz_se_crea_con_volumen 50
PASSED
tests/test_altavoz.py::test_altavoz_estado_apagado apagado
PASSED
tests/test_altavoz.py::test_altavoz_se_crea_con_cadena_no_empty PASSED
tests/test_altavoz.py::test_altavoz_space_begin_or_final Cocina
PASSED
tests/test_altavoz.py::test_altavoz_volumen_integer_0_a_100 0
PASSED
tests/test_altavoz.py::test_altavoz_estado_getter apagado
PASSED
tests/test_altavoz.py::test_altavoz_change_estado_on encendido
PASSED
tests/test_altavoz.py::test_altavoz_change_estado_off apagado
PASSED
tests/test_altavoz.py::test_altavoz_on_off encendido
apagado
PASSED
tests/test_altavoz.py::test_altavoz_se_crea_con_cadena_no_vacio PASSED
tests/test_altavoz.py::test_altavoz_sin_espacios PASSED
tests/test_altavoz.py::test_altavoz_nombre_string PASSED
tests/test_altavoz.py::test_altavoz_volumen_negativo PASSED
tests/test_altavoz.py::test_altavoz_volumen_string PASSED
tests/test_altavoz.py::test_altavoz_volumen_booleano FAILED

========================================================================================= FAILURES ==========================================================================================
_______________________________________________________________________________ test_altavoz_volumen_booleano _______________________________________________________________________________

    def test_altavoz_volumen_booleano():
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

tests\test_altavoz.py:130: Failed
================================================================================== short test summary info ==================================================================================
FAILED tests/test_altavoz.py::test_altavoz_volumen_booleano - Failed: DID NOT RAISE ValueError
=============================================================================== 1 failed, 15 passed in 0.20s ================================================================================

2. Modifica temporalmente la implementación de `Altavoz` para introducir un error.
Al intentar poner un booleano en la propiedad volumen, como no lo había validado me daba un error

3. Ejecuta de nuevo pytest.
Una vez ajustado altavoz.py y añadir la validación de los booleanos, he ejecutado de nuevo toda la batería de pruebas resultando exitosas.
Por otro lado, al comentar temporalmente el bloque with pytest.raises(ValueError) en test_altavoz.py, se muestra directamente la excepción generada al introducir un valor booleano. De esta manera, comprobamos que la validación implementada funciona correctamente.

collected 16 items                                                                                                                                                                 

tests/test_altavoz.py::test_altavoz_se_crea_con_nombre Salón
PASSED
tests/test_altavoz.py::test_altavoz_se_crea_con_volumen 50
PASSED
tests/test_altavoz.py::test_altavoz_estado_apagado apagado
PASSED
tests/test_altavoz.py::test_altavoz_se_crea_con_cadena_no_empty PASSED
tests/test_altavoz.py::test_altavoz_space_begin_or_final Cocina
PASSED
tests/test_altavoz.py::test_altavoz_volumen_integer_0_a_100 0
PASSED
tests/test_altavoz.py::test_altavoz_estado_getter apagado
PASSED
tests/test_altavoz.py::test_altavoz_change_estado_on encendido
PASSED
tests/test_altavoz.py::test_altavoz_change_estado_off apagado
PASSED
tests/test_altavoz.py::test_altavoz_on_off encendido
apagado
PASSED
tests/test_altavoz.py::test_altavoz_se_crea_con_cadena_no_vacio PASSED
tests/test_altavoz.py::test_altavoz_sin_espacios PASSED
tests/test_altavoz.py::test_altavoz_nombre_string PASSED
tests/test_altavoz.py::test_altavoz_volumen_negativo PASSED
tests/test_altavoz.py::test_altavoz_volumen_string PASSED
tests/test_altavoz.py::test_altavoz_volumen_booleano PASSED

=============================================================================== 16 passed in 0.15s ================================================================================
PS C:\Users\AntonioSS\Desktop\Curso de Especializacion en Python\python\POO 2026-2027\UD2 · Lab 1 · SmartSpeaker diseñar y proteger un objeto\smartspeaker> 

### Pruebas manuales

| ID | Prueba realizada | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| V01 | Crear un altavoz con nombre `"Salón"` y volumen `30`. | Se crea correctamente. | Correcto |
| V02 | Consultar el nombre. | Devuelve `"Salón"`. | Correcto |
| V03 | Consultar el volumen. | Devuelve `30`. | Correcto |
| V04 | Consultar el estado inicial. | Devuelve `"apagado"`. | Correcto |
| V05 | Cambiar el volumen a `50`. | Se acepta el nuevo volumen. | Correcto |
| V06 | Cambiar el volumen a `0`. | Se acepta el valor mínimo. | Correcto |
| V07 | Cambiar el volumen a `100`. | Se acepta el valor máximo. | Correcto |
| V08 | Ejecutar `encender()`. | El estado pasa a `"encendido"`. | Correcto |
| V09 | Ejecutar `apagar()`. | El estado pasa a `"apagado"`. | Correcto |
| V10 | Crear un altavoz con espacios exteriores en el nombre. | Se eliminan los espacios exteriores. | Correcto |
| I01 | Crear un altavoz con nombre vacío. | Lanza `ValueError`. | Rechazado |
| I02 | Crear un altavoz con nombre formado por espacios. | Lanza `ValueError`. | Rechazado |
| I03 | Crear un altavoz con nombre numérico. | Lanza `ValueError`. | Rechazado |
| I04 | Crear un altavoz con volumen `-1`. | Lanza `ValueError`. | Rechazado |
| I05 | Crear un altavoz con volumen `101`. | Lanza `ValueError`. | Rechazado |
| I06 | Crear un altavoz con volumen `25.5`. | Lanza `ValueError`. | Rechazado |
| I07 | Asignar una cadena de texto al volumen. | Lanza `ValueError`. | Rechazado |
| I08 | Intentar modificar directamente el estado. | Lanza `AttributeError`. | Rechazado |

### Pruebas Test_Altavoz

### 1.2. Pruebas automatizadas con pytest

| Prueba | Comprobación realizada | Resultado esperado |
|---|---|---|
| `test_altavoz_se_crea_con_nombre` | Creación con nombre válido. | PASSED |
| `test_altavoz_se_crea_con_volumen` | Creación con volumen válido. | PASSED |
| `test_altavoz_estado_apagado` | Estado inicial del altavoz. | PASSED |
| `test_altavoz_se_crea_con_cadena_no_empty` | Rechazo de nombre vacío. | PASSED |
| `test_altavoz_space_begin_or_final` | Eliminación de espacios exteriores del nombre. | PASSED |
| `test_altavoz_volumen_integer_0_a_100` | Aceptación de volumen entero dentro del rango. | PASSED |
| `test_altavoz_estado_getter` | Consulta de la propiedad estado. | PASSED |
| `test_altavoz_change_estado_on` | Cambio de estado a encendido. | PASSED |
| `test_altavoz_change_estado_off` | Cambio de estado a apagado. | PASSED |
| `test_altavoz_on_off` | Encendido y posterior apagado. | PASSED |
| `test_altavoz_se_crea_con_cadena_no_vacio` | Rechazo de nombre vacío. | PASSED |
| `test_altavoz_sin_espacios` | Rechazo de nombre formado por espacios. | PASSED |
| `test_altavoz_nombre_string` | Rechazo de nombre numérico. | PASSED |
| `test_altavoz_volumen_negativo` | Rechazo de volumen negativo. | PASSED |
| `test_altavoz_volumen_string` | Rechazo de volumen de tipo cadena. | PASSED |
| `test_altavoz_volumen_booleano` | Rechazo de valores booleanos como volumen. | PASSED |

**Resultado final: 16 pruebas superadas (16 passed).

## 4. Identifica qué pruebas detectan el problema.
La prueba que detecta específicamente el problema de aceptar valores booleanos como volumen es test_altavoz_volumen_booleano.

Siendo 24/11/2026 nos comentó la profesora, que esto se debe a que en Python los valores True y False son considerados subclases de los números enteros (int), por lo que una validación convencional mediante isinstance(nuevo_volumen, int) no sería suficiente.

Además, las pruebas test_altavoz_volumen_integer_0_a_100, test_altavoz_volumen_negativo y test_altavoz_volumen_string permiten comprobar que el resto de las restricciones del atributo volumen también se cumplen.

## 5. Explica por qué esas pruebas han fallado.
Tengo que hacer que en el setter de volumen no me deje poner booleanos

## 6. Restaura el código y comprueba que vuelven a superarse.
Con el ajuste del setter de volumen, pasa la prueba de manera correcta, y si comentamos el raise para que no capture el error, salta bien.

Puedes introducir un error en una validación, en el valor inicial del estado o en alguno de los métodos.

El objetivo es comprobar que los tests permiten detectar regresiones, es decir, errores que aparecen cuando modificamos código que anteriormente funcionaba.

## IA como asistente de diseño de pruebas

Utiliza una herramienta de IA para revisar la cobertura de tus pruebas.

Puedes utilizar este prompt:

```text
Estoy desarrollando una clase Python llamada Altavoz.

La clase tiene las siguientes reglas:

- El nombre debe ser una cadena no vacía y se eliminan los espacios exteriores.
- El volumen debe ser un entero entre 0 y 100, ambos incluidos.
- El estado inicial es "apagado".
- El estado solo puede modificarse mediante los métodos encender() y apagar().
- Los datos no válidos deben provocar ValueError.

He implementado pruebas automatizadas con pytest.

Voy a proporcionarte el código de la clase y mis pruebas.

Quiero que:

1. Identifiques qué requisitos están cubiertos por las pruebas.
2. Detectes comportamientos que no se están comprobando.
3. Propongas nuevos casos de prueba positivos y negativos.
4. Señales posibles errores en mis pruebas.

No reescribas el código ni las pruebas.
No afirmes que una prueba funciona si no la has ejecutado.
Explica por qué cada caso de prueba propuesto sería útil.
```

Compara las propuestas de la IA con tus pruebas actuales.

No tienes que incorporar automáticamente todas sus sugerencias: debes valorar si son pertinentes y justificarlas.

## Entregables

La entrega debe mantener esta estructura:

```text
smart-speaker/
├── src/
│   └── smartspeaker/
│       ├── altavoz.py
│       ├── main.py
│       └── __init__.py
├── tests/
│   └── test_altavoz.py
└── docs/
    ├── laboratorio.md
    └── pruebas.md
```

Debes entregar:

| Archivo | Contenido |
|---|---|
| `altavoz.py` | Implementación de la clase Altavoz |
| `tests/test_altavoz.py` | Batería de pruebas automatizadas |
| `docs/pruebas.md` | Documentación del diseño de las pruebas y análisis de resultados |
| `docs/laboratorio.md` | Documentación de la primera fase del laboratorio |

El documento `pruebas.md` debe incluir:

- Relación de requisitos comprobados.
- Descripción de los principales casos de prueba.
- Captura o salida de una ejecución correcta de pytest.
- Ejemplo de una prueba que haya fallado al introducir un error deliberadamente.
- Explicación de qué ha permitido detectar ese fallo.
- Reflexión sobre las sugerencias de la IA: cuáles has incorporado y cuáles has descartado, justificando las decisiones.

## Tip

**Recuerda:** que todos los tests pasen no demuestra que el programa esté libre de errores. Significa que, para los casos que has diseñado, el comportamiento observado coincide con el esperado.