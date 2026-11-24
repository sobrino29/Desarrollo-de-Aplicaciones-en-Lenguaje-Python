from smartspeaker.altavoz import Altavoz
import pytest

######################## PRUEBAS DE CREACIÓN #########################
### Verificación que se almacena correctamente el valor del nombre.
def test_altavoz_se_crea_con_nombre():
    altavoz = Altavoz("Salón", 30)

    assert altavoz.nombre == "Salón"
    print(altavoz.nombre)
# Pasa la prueba y se revisa que el comportamiento es el normal

### Verificación que se almacena correctamente el valor de volumen inicial
def test_altavoz_se_crea_con_volumen():
    altavoz = Altavoz("Salón", 50)
    
    assert altavoz.volumen == 50
    print(altavoz.volumen)
# Pasa la prueba y se revisa que muestra el atributo volumen con 50

### Verificación que el valor de estado inicial es apagado
def test_altavoz_estado_apagado():
    altavoz = Altavoz("Cocina", 40)
    
    assert altavoz.estado == "apagado"
    # Si pruebo assert altavoz.estado también me extrae apagado
    print(altavoz.estado)
# Pasa la prueba y muestra el atributo estado en apagado    
######################## PRUEBAS DE CREACIÓN #########################

######################## PRUEBAS DE PROPIEDADES #########################
# El nombre debe ser una cadena no vacía.
def test_altavoz_se_crea_con_cadena_no_empty():
    with pytest.raises(ValueError):
        Altavoz("", 50)
# No muestra nada por pantalla pytest.raises cuando la excepción se produce correctamente, para ello utilizar uv run pytest -v

# Los espacios al principio y al final del nombre deben eliminarse.
def test_altavoz_space_begin_or_final():
    altavoz = Altavoz(" Cocina ", 60)
    assert altavoz.nombre == "Cocina"
    print(altavoz.nombre)
# No muestra nada por pantalla pytest.raises cuando la excepción se produce correctamente, para ello utilizar uv run pytest -v

# El volumen debe ser un número entero entre 0 y 100, ambos incluidos.
def test_altavoz_volumen_integer_0_a_100():
    altavoz = Altavoz("Habitación", 0)
    assert isinstance(altavoz.volumen, int)
    assert altavoz.volumen >= 0 and altavoz.volumen < 101 
    print(altavoz.volumen)

# El estado debe poder consultarse, pero no modificarse directamente mediante su propiedad pública.
def test_altavoz_estado_getter():
    altavoz = Altavoz("Habitación", 0)
    assert altavoz.estado == "apagado"
    print(altavoz.estado)
######################## PRUEBAS DE PROPIEDADES #########################


######################## PRUEBAS DE COMPORTAMIENTO #########################
## Que encender() cambia el estado a encendido.
def test_altavoz_change_estado_on():
    altavoz = Altavoz("Salón", 20)
    altavoz.encender()
    assert altavoz.estado == "encendido"
    print(altavoz.estado)
    
## Que apagar() cambia el estado a apagado.
def test_altavoz_change_estado_off():
    altavoz = Altavoz("Salón", 20)
    altavoz.apagar()
    assert altavoz.estado == "apagado"
    print(altavoz.estado)

## Que puedes apagar un altavoz después de haberlo encendido.
def test_altavoz_on_off():
    altavoz = Altavoz("Pasillo", 50)
    # Parte de encendido
    altavoz.encender()
    assert altavoz.estado == "encendido"
    print(altavoz.estado)
    
    # Parte de apagado
    altavoz.apagar()
    assert altavoz.estado == "apagado"
    print(altavoz.estado)
######################## PRUEBAS DE COMPORTAMIENTO #########################


######################## PRUEBAS DE VALIDACIÓN Y ERRORES ###################
## Nombre	""	Rechazar
def test_altavoz_se_crea_con_cadena_no_vacio():
    with pytest.raises(ValueError):
        Altavoz("", 50)
# nota: Capturamos la excepción y se comporta PASSED, para probarlo bien se puede comentar with pytest.raises(ValueError) y verlo como salta ValueError: El nombre no puede estar vacío

## Nombre	"   "	Rechazar
def test_altavoz_sin_espacios():
    with pytest.raises(ValueError):
        Altavoz("  ", 60)
# nota: Capturamos la excepción y se comporta PASSED, para probarlo bien se puede comentar with pytest.raises(ValueError) y verlo como salta ValueError: El nombre no puede estar vacío

## Nombre	25	Rechazar
def test_altavoz_nombre_string():
    with pytest.raises(ValueError):
        Altavoz(25, 25)
# nota: Capturamos la excepción y se comporta PASSED, para probarlo bien se puede comentar with pytest.raises(ValueError) y verlo como salta ValueError: El nombre debe ser una cadena de texto


## Volumen	-1	Rechazar
def test_altavoz_volumen_negativo():
    with pytest.raises(ValueError):
        Altavoz("Patio", -1)
# nota: Capturamos la excepción y se comporta PASSED, para probarlo bien se puede comentar with pytest.raises(ValueError) y verlo como salta ValueError: El volumen debe estar entre 0 y 100, al salirse de rango

## Volumen	101	Rechazar
def test_altavoz_volumen_negativo():
    with pytest.raises(ValueError):
        Altavoz("Patio", 101)
# nota: Capturamos la excepción y se comporta PASSED, para probarlo bien se puede comentar with pytest.raises(ValueError) y verlo como salta ValueError: El volumen debe estar entre 0 y 100, al salirse de rango

## Volumen	"50"	Rechazar
def test_altavoz_volumen_string():
    with pytest.raises(ValueError):
        Altavoz("Patio", "50")
# nota: Capturamos la excepción y se comporta PASSED, para probarlo bien se puede comentar with pytest.raises(ValueError) y verlo como salta ValueError: El volumen debe ser un número entero

## Volumen	True	Rechazar
def test_altavoz_volumen_booleano():
    with pytest.raises(ValueError):
        Altavoz("Patio", True)
# nota: Capturamos la excepción y se comporta FAILED, por lo tanto, se ha producido una excepción inesperada y no sirve
######################## PRUEBAS DE VALIDACIÓN Y ERRORES ####################
