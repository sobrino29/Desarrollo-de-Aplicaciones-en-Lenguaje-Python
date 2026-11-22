# Análisis y representación de la población extranjera en España con Python

## 1. Objetivo de la actividad

En esta práctica aprenderás a trabajar con datos procedentes de archivos Excel utilizando Python. Para ello, emplearás diferentes bibliotecas especializadas en el tratamiento, manipulación y representación gráfica de datos.

El objetivo será analizar la evolución de la población extranjera en España a lo largo de los años, utilizando datos reales proporcionados en un archivo Excel.

## 2. Material necesario

- Visual Studio Code.
- Python instalado.
- Un entorno virtual (`.venv`).

### Bibliotecas necesarias

- **pandas:** lectura y tratamiento de datos.
- **openpyxl:** lectura de archivos Excel.
- **numpy:** creación y manipulación de matrices.
- **matplotlib:** representación gráfica.
- **pathlib:** gestión de rutas y archivos.

Instala las bibliotecas necesarias mediante el archivo `requerimientos.txt`.

## 3. Organización del proyecto

Crea un proyecto llamado `poblacion` con la siguiente estructura de directorios:

```text
poblacion/
│
├── .venv/
│
├── datos/
│   └── población_extrangera_españa.xlsx
│
└── src/
    └── leerdatos.py
```

Descarga el archivo Excel proporcionado para la actividad y guárdalo dentro de la carpeta `datos`.

## 4. Desarrollo de la actividad

Desarrolla un programa Python (`leerdatos.py`) que realice las siguientes operaciones:

### Apartado 1. Gestión de rutas con Pathlib

- Importa la biblioteca `Path` de `pathlib`.
- Obtén la ruta del directorio raíz del proyecto a partir de la ubicación del propio archivo Python.
- Construye la ruta completa del archivo Excel situado en la carpeta `datos`.

### Apartado 2. Lectura de datos con Pandas

- Importa la biblioteca Pandas.
- Lee el archivo Excel utilizando `pd.read_excel()`.
- Evita que Pandas interprete la primera fila como encabezado.
- Almacena los datos en un DataFrame.

### Apartado 3. Creación de una matriz con NumPy

Utilizando NumPy, crea una matriz de dos filas y 25 columnas que contenga:

- **Primera fila:** los años comprendidos entre 2022 y 1998, obtenidos de las celdas B8 hasta Z8 del Excel.
- **Segunda fila:** el número de personas extranjeras correspondiente a cada año, obtenido de las celdas B10 hasta Z10.

La matriz deberá contener valores enteros.

Muestra por pantalla:

- El contenido completo de la matriz.
- Sus dimensiones mediante el atributo `shape`.

### Apartado 4. Separación de los datos

Extrae de la matriz dos variables independientes:

- `anios`: contendrá los años.
- `poblacion`: contendrá el número de personas extranjeras de cada año.

### Apartado 5. Representación gráfica con Matplotlib

Crea un gráfico de líneas que represente la evolución de la población extranjera en España.

El gráfico deberá cumplir los siguientes requisitos:

- **Título:** «Evolución de la población extranjera en España».
- **Eje X:** Año.
- **Eje Y:** Número de personas.
- Mostrar un marcador circular en cada año.
- Mostrar todos los años en el eje X.
- Girar las etiquetas del eje X 45 grados.
- Incorporar una cuadrícula.
- Ajustar los márgenes para que no se corten las etiquetas.

Finalmente, muestra el gráfico mediante `plt.show()`.

## 5. Entrega

Entrega un único documento PDF que incluya:

1. **Enlace al repositorio de GitHub:** deberá ser público para que el profesor pueda acceder y revisar el código fuente.
2. **Captura de la matriz NumPy:** mostrando su contenido y dimensiones.
3. **Captura del gráfico Matplotlib:** mostrando correctamente la representación de los datos.

**Importante:** el código fuente (`leerdatos.py`) deberá estar incluido en el repositorio de GitHub. No es necesario adjuntarlo por separado.

## 6. Criterios de evaluación

| Criterio | Puntuación |
|---|---:|
| Organización del proyecto y gestión de rutas con Pathlib | 1 punto |
| Lectura correcta del Excel con Pandas | 1,5 puntos |
| Selección de los datos y creación de la matriz NumPy | 2 puntos |
| Extracción y separación de las variables | 1 punto |
| Representación gráfica con Matplotlib | 3 puntos |
| Organización, comentarios y limpieza del código | 1,5 puntos |
| **TOTAL** | **10 puntos** |

**Importante:** el programa debe ejecutarse correctamente desde el entorno virtual. Se valorará especialmente que el código esté organizado, utilice nombres de variables descriptivos y contenga comentarios que expliquen las operaciones realizadas.