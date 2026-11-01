# Libreria propia de Python no se instala
from pathlib import Path

# Le asigno un acronimo a la libreria
import pandas as pd
import matplotlib.pyplot as plt


ARCHIVO_DATOS= Path("datos/sp500_indice_2021_2026.csv")

def cargar_indice ():
    datos = pd.read_csv(ARCHIVO_DATOS, usecols=["Date", "Close"])
    
    # Lo pasa a formato tiempo    
    datos["Date"] = pd.to_datetime(datos["Date"])
    
    # Usar la fecha como índice, seleccionar lso cierres y ordenarlos cronológicamente
    return datos.set_index("Date")["Close"].sort_index()

def main ():
    
    precios = cargar_indice()
    
    precios.plot(figsize=(14, 8), legend=False)
    
    # Ponwe titulo
    plt.title("Evolución del indice S&P 500")
    
    # Eje X
    plt.xlabel("Fecha")
    
    # Eje Y
    plt.ylabel("Valor del índice")
    
    # Abrir la ventana con el gráfico.
    plt.show()

if __name__ == "__main__":
    main()