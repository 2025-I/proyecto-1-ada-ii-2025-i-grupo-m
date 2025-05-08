import sys
import os
import time
import random
import matplotlib.pyplot as plt
from datetime import datetime
import csv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from fiesta.dinamica.dinamica import resolver_fiesta

def generar_arbol_y_valores(n):
    matriz = [[0]*n for _ in range(n)]
    for i in range(1, n):
        padre = random.randint(0, i-1)
        matriz[padre][i] = 1
    valores = [random.randint(1, 100) for _ in range(n)]
    return matriz, valores

def test_fiesta_escalado():
    tamanos = [
        ("Juguete", 10),
        ("Pequeño", 100),
        ("Mediano", 1000),
        ("Grande", 10000),
        ("Extra Grande", 50)
    ]

    resultados = {}
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    csv_filename = f"resultados_fiesta_{timestamp}.csv"
    grafico_filename = f"grafico_tiempos_fiesta_{timestamp}.png"

    with open(csv_filename, mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Tamaño", "Promedio (segundos)"])

        for nombre, tamano in tamanos:
            tiempos = []
            print(f"\n== Tamaño: {nombre} ({tamano} nodos) ==")
            for i in range(5):
                matriz, valores = generar_arbol_y_valores(tamano)
                inicio = time.time()
                seleccion, suma = resolver_fiesta(matriz, valores)
                duracion = time.time() - inicio

                assert len(seleccion) == tamano
                assert suma == sum(valores[j] for j in range(tamano) if seleccion[j] == 1)
                print(f"  Repetición {i+1}: {duracion:.4f} segundos")
                tiempos.append(duracion)

            promedio = sum(tiempos) / len(tiempos)
            resultados[nombre] = promedio
            writer.writerow([nombre, f"{promedio:.4f}"])

    # Graficar
    nombres = list(resultados.keys())
    tiempos_prom = list(resultados.values())

    plt.figure(figsize=(10, 6))
    plt.bar(nombres, tiempos_prom, color='skyblue')
    plt.xlabel("Tamaño del árbol")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Tiempo de ejecución promedio por tamaño - Fiesta Dinámica")
    plt.tight_layout()
    plt.savefig(grafico_filename)
    plt.show()

    print(f"\n✅ Gráfico guardado en: {grafico_filename}")
    print(f"✅ Datos guardados en: {csv_filename}")
