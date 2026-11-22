########################################################## LIBRERÍAS IMPORTADAS #####################################################
# Librería de PathLib esta es propia de python, sirve para rutas
from pathlib import Path

# Librería de pandas
import pandas as pd

# Librería de matplotlib
import matplotlib.pyplot as plt

# Libería de openpyxl
import openpyxl as op

# Libería de numpy
import numpy as np
########################################################## LIBRERÍAS IMPORTADAS #####################################################


######################################################### FICHEROS ##################################################################
######################################################## ruta raíz del proyecto ####################################################
VARIABLE = Path(__file__).resolve().parent
print(f"Esta es la ruta raíz del proyecto:", {VARIABLE})
######################################################## ruta raíz del proyecto ####################################################

######################################################## ruta del fichero excel  ####################################################
ARCHIVO_DATOS= Path(VARIABLE.parent / "datos" / "población_extranjera_españa.xlsx")
print(f"Esta es la ruta del fichero a leer", {ARCHIVO_DATOS})
######################################################## ruta del fichero excel  ####################################################

###################################################### Leer y almacenar en DataFrame ################################################
# El header=None sirve para que no tenga en cuenta la primera fila como encabezado
df = pd.read_excel(ARCHIVO_DATOS, header=None)
#print(df)

# Al estar almacenado en la variable df leo su contenido del DataFrame
#df.info()
###################################################### Leer y almacenar en DataFrame ################################################
######################################################### FICHEROS ##################################################################

########################################################### Extracción de Datos del dataframe #######################################
# Selección del DataFrame primera fila : los años comprendidos entre 2022 y 1998, obtenidos de las celdas B8 hasta Z8 del Excel.
#Como empieza en la posición 0, no sería la fila 8 sino la 7, y el rango de columnas sería de B:Z es decir, de 1:26
anios = df.iloc[7, 1:26]
#print(anios)


# Segunda fila: el número de personas extranjeras correspondiente a cada año, obtenido de las celdas B10 hasta Z10.
#Como empieza en la posición 0, no sería la fila 10 sino la 9, y el rango de columnas sería de B:Z es decir, de 1:26
poblacion = df.iloc[9, 1:26]
#print(poblacion)
########################################################### Extracción de Datos del dataframe ###############################################

####################################################### CÁLCULO NUMÉRICO (NUMPY) ############################################################
# Inicializo el matriz_datos pasándole por parámetros las dos filas como primer argumento, por tanto, te crea 2x25
matriz_datos = np.array([anios, poblacion])
#print(matriz_datos)

# Limpio los datos para que sean integers
matriz_limpia1= matriz_datos.astype(np.int_)
print(matriz_limpia1)

# Forma del array
print("Forma del array:", matriz_limpia1.shape)
####################################################### CÁLCULO NUMÉRICO (NUMPY) ############################################################

##################################################### SEPARACIÓN DE DATOS SEGÚN SU ORIGEN ##################################################
#Aunque yo ya tengo definidas anios y poblacion, el origen de los datos es del DataFrame, y a mi me lo piden, que lo saque de la matriz_limpia1

# Extraigo la primera fila anios
fila_anios = matriz_limpia1[0]
#print("Primer elemento:", fila_anios)

# Extraigo la segunda fila poblacion
fila_poblacion = matriz_limpia1[1]
#print("Segundo elemento:", fila_poblacion)

##################################################### SEPARACIÓN DE DATOS SEGÚN SU ORIGEN ##################################################

##################################################### GRÁFICOS #############################################################################

# Tamaño del gráfico
plt.figure(figsize=(12, 5))

# Mostrar un marcador circular en cada año.
plt.plot(fila_anios, fila_poblacion, marker="o")

# Título del gráfico
plt.title("Evolución de la población extranjera en España")

# Nombre eje X
plt.xlabel("Año")

# Nombre eje Y
plt.ylabel("Número de persona")

# Cuadrículas activadas
plt.grid(True)

# Representación de los años rotados a 45º
plt.xticks(fila_anios, rotation=45)

# Plantilla
plt.tight_layout()

# Mostrar gráfico
plt.show()
##################################################### GRÁFICOS #############################################################################
