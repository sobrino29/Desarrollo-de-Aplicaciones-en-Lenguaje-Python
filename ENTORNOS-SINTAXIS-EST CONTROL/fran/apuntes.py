'''Ejercicio 4 CEDAP
'''

# Si se
#for 

# Si no se
#while condición de salida porque sino a infinito

i = 10
while i <= 100:
        print(i)
        i += 10

# Bucle infinito
#seguir = True
#while seguir:
#        print('QUE DESEAS HACER')
#        opc = input(f'Dime si quieres esguir ejecutando o n si no')
#        if opc.strip().lower() == 'n':
#           # Mala práctica te sales del bucle     
#           # break 
#           seguir = False
#        print("SIGO EN LA SIGUIENTE")     

# JAVA
# for (int i=10; i < 100; i ++)
# declaracion; Condicion; Incremento        

# PYTHON
# for i in range(100):
# si no pongo nada interpreta 0

# ARGUMENTOS QUE RECIBE
#for i in range(10, 100, 10):
#        print(i)
        
#for i in range(100):
#        print(i)


for i in range(2,100,2):
        print(i)

# Par o impar
for i in range(1,100,1):
        if i % 2 == 0:
                print(f"Este numero es par: {i}")
        
        else:
                print(f"Este numero es: {i}")

tabla = 2
for nodo in range(2,21):
        resultado = nodo * 2
        if nodo % 2 == 0:
                print(f"2 x {nodo} = {resultado}")

# RECORRER ESTRUCTURA
# Francisco es la composición de varios char F,r,a,n,c,i,s,c,o
# Los tipos String -> char
nombre = 'Francisco'
print(len(nombre))

for letra in nombre:
        if letra == 'c':
                letra == '-'
        print(letra)

def visualizar_lista(lista):
        for i in lista:
                print(i)
        print("------------------------------")
                
lista = ["Carlos", "Diego", "Esteban"]
# CONSULTA O ACCESO
#print(lista[3])

# AGREGAR ELEMENTOS
lista.append("Javi")
visualizar_lista(lista)


# ACTUALIZACIONE DE VALROES EN UNA LISTA
lista[0]="Francisco"
visualizar_lista(lista)

# ELIMINAR ELMENTOS DE UNA LISTA
lista.remove('Francisco')
visualizar_lista

# ORDENAR LISTA
lista.sort(reverse=True)
visualizar_lista

lista_numeros = [1,2,3,5,2,7,8]
lista_numeros.sort(reverse=True)
print(lista_numeros)

lista1 = [1,2,4,5]
# Su dirección de memoria y sus valores son distintos
lista2 = lista1.copy()

# Su dirección de memoria y sus valores son iguales MALA PRAXIS
lista2 = lista1

# Asignación de memoria, estás modificando en las dos variables
lista1.append(6)
print(lista2)

# OPERACIONES CON LISTAS
lista = ["Roberto", "Jose"]
elemento = lista.pop()
print(lista)
print(elemento)

# FUNCIONES Y MÉTODOS (PROGRAMAR EN BLOQUE)
# Metodos = hacen operaciones no devuelven nada

# APP que calculadora
resultado = 0
def menu():
        print(f"Inicio programa calculadora")
        print(f"1. Operacion")
        print(f"2. Mostrar Resultado última operación")
        print(f"3. Fin del programa")
        print(f"4. Quiero que me enseñes el historial de resultado que has tenido")

def operaciones():
        numero1 = int(input('Dime el numero 1'))
        numero2 = int(input('Dime el numero 2'))
        operacion = input('Dime qué operación que quieres * / + -')
        
        if operacion == "*":
                resultado = numero1 * numero2
        elif operacion == "/":
                resultado = numero1 / numero2
        elif operacion == "+":
                resultado = numero1 + numero2
        print(f"El resultado es {resultado}")

def mostrar_ultimo_resultado():
        resultado = operaciones().operacion

# LLAMO A MI MÉTODO        
if __name__ == '__main__':
        menu()
        opc = input(f"Dime que opción eliges")
        # QUIERO QUE SE EJECUTE SIEMPRE
        while True:
                if opc == "1":
                        pass
                elif opc == "2":
                        pass   
                else:
                        break






