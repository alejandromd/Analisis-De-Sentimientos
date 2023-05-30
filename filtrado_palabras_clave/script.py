import pandas as pd
import os

def leer_csv(nombre_archivo):
    palabras = []

    # Leer el archivo CSV utilizando Pandas
    df = pd.read_csv(nombre_archivo)

    # Obtener la columna 'Palabra'
    columna_palabra = df['Palabra']

    # Agregar cada palabra a la lista
    for palabra in columna_palabra:
        palabras.append(palabra)

    return palabras

def filtrar_lineas_csv(archivo_entrada, archivo_salida, palabras_conjunto):
    # Cargar el archivo CSV en un DataFrame usando pandas
    df = pd.read_csv(archivo_entrada, on_bad_lines='skip')

    print(df.columns.tolist())

    # Filtrar las líneas que contengan al menos una de las palabras del conjunto
    df_filtrado = df[df['text'].str.contains('|'.join(palabras_conjunto), case=False, na=False)]

    # Guardar el DataFrame filtrado en un archivo CSV de salida
    df_filtrado.to_csv(archivo_salida, index=False)

# Nombre del archivo CSV que contiene las palabras
nombre_archivo = "conjunto_palabras.csv"

# Llamar a la función para leer el archivo CSV y obtener la lista de palabras
conjunto_palabras = leer_csv(nombre_archivo)

# Ejemplo de uso
archivo_entrada = 'training.1600000.processed.noemoticon.csv'
archivo_salida = 'salida.csv'

filtrar_lineas_csv(archivo_entrada, archivo_salida, conjunto_palabras)