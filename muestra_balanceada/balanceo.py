import csv

def generar_muestra_balanceada(archivo_entrada, archivo_salida, num_ejemplos):
    datos = {}
    encabezados = []
    with open(archivo_entrada, 'r') as archivo:
        lector_csv = csv.DictReader(archivo)
        encabezados = lector_csv.fieldnames
        for fila in lector_csv:
            clase = fila['clase']
            if clase in datos:
                datos[clase].append(fila)
            else:
                datos[clase] = [fila]

    muestra_balanceada = []
    for clase, ejemplos in datos.items():
        if len(ejemplos) <= num_ejemplos:
            muestra_balanceada.extend(ejemplos)
        else:
            muestra_balanceada.extend(ejemplos[:num_ejemplos])

    with open(archivo_salida, 'w', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor_csv.writeheader()
        escritor_csv.writerows(muestra_balanceada)

    print(f"Se generó el archivo '{archivo_salida}' con una muestra balanceada.")

# Uso del script
archivo_entrada = 'classified_tweets.csv'
archivo_salida = 'muestra_balanceada.csv'
num_ejemplos = 1000

generar_muestra_balanceada(archivo_entrada, archivo_salida, num_ejemplos)