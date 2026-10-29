
'''

Pruebas
'''
x=30

# Contador incremental
x += 1
print(x)

# Contador decremental
x -= 1
print(x)


# Area de un rectangulo
lado = 20
altura = 30
area = lado * altura


# Par o impar
'''Este programa va a decir si un número es par o impar'''

print("Este programa nos dice si un número es par o impar")
numero = int(input('Introduce el número '))

resultado = numero % 2

# Las condiciones se valuan con boolean

if resultado == 0:

    print(f"El módulo de mi división anterior es par: {resultado} ")

else:
    
    print(f"El módulo de mi división anterior es impar: {resultado} ")  


# Esto también es una condición

numero = 30
nombre = 'Francisco'

print(nombre == 'Francisco')
