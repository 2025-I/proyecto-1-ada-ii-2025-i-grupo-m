import sys
import os
import time
import random
import string
import matplotlib.pyplot as plt
import csv
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from palindromo.dinamica.dinamica import normalizar_cadena, palindromo_maximo_dinamico
from palindromo.fuerza_bruta.fuerza_bruta import palindromo_maximo_fuerza_bruta
from palindromo.voraz.voraz import palindromo_maximo, normalizar_cadena as normalizar_cadena_voraz


def generar_texto(longitud):
    base = "anaabacabadabacaba"
    texto = (base * (longitud // len(base) + 1))[:longitud]
    return texto

def test_palindromo_comparativo():
    tamaños = {
        "Juguete": 10,
        "Pequeño": 100,
        "Mediano": 1000,
        "Grande": 10000,
        "Extra Grande": 50  # para que entre la fuerza bruta
    }

    repeticiones = 5
    resultados = []

    for nombre_tamaño, longitud in tamaños.items():
        print(f"\n== Tamaño: {nombre_tamaño} ({longitud} caracteres) ==")

        texto = generar_texto(longitud)
        normalizada = normalizar_cadena(texto)
        normalizada_voraz = normalizar_cadena_voraz(texto)  # Para el algoritmo voraz

        for r in range(1, repeticiones + 1):
            # Dinámico
            inicio_dinamico = time.time()
            palindromo_maximo_dinamico(normalizada)
            tiempo_dinamico = time.time() - inicio_dinamico

            # Fuerza Bruta
            inicio_fb = time.time()
            palindromo_maximo_fuerza_bruta(normalizada)
            tiempo_fb = time.time() - inicio_fb

            # Voraz
            inicio_voraz = time.time()
            palindromo_maximo(normalizada_voraz)
            tiempo_voraz = time.time() - inicio_voraz

            resultados.append([nombre_tamaño, r, tiempo_dinamico, tiempo_fb, tiempo_voraz])
            print(f"  Repetición {r}: Dinámico={tiempo_dinamico:.4f}s | Fuerza Bruta={tiempo_fb:.4f}s | Voraz={tiempo_voraz:.4f}s")

    # === Guardar CSV ===
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    csv_filename = f"resultados_comparativo_palindromo_{timestamp}.csv"

    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Tamaño", "Repetición", "Tiempo Dinámico", "Tiempo Fuerza Bruta", "Tiempo Voraz"])
        writer.writerows(resultados)

    print(f"\n✅ Datos guardados en: {csv_filename}")

    # === Graficar ===
    tamaños_unicos = list(tamaños.keys())
    tiempo_promedio_dinamico = []
    tiempo_promedio_fb = []
    tiempo_promedio_voraz = []

    for tamaño in tamaños_unicos:
        tiempos_dinamico = [fila[2] for fila in resultados if fila[0] == tamaño]
        tiempos_fb = [fila[3] for fila in resultados if fila[0] == tamaño]
        tiempos_voraz = [fila[4] for fila in resultados if fila[0] == tamaño]
        tiempo_promedio_dinamico.append(sum(tiempos_dinamico) / repeticiones)
        tiempo_promedio_fb.append(sum(tiempos_fb) / repeticiones)
        tiempo_promedio_voraz.append(sum(tiempos_voraz) / repeticiones)

    plt.figure(figsize=(10, 6))
    plt.plot(tamaños_unicos, tiempo_promedio_dinamico, label="Dinámico", marker='o')
    plt.plot(tamaños_unicos, tiempo_promedio_fb, label="Fuerza Bruta", marker='s')
    plt.plot(tamaños_unicos, tiempo_promedio_voraz, label="Voraz", marker='^')
    plt.xlabel("Tamaño del Texto")
    plt.ylabel("Tiempo Promedio (s)")
    plt.title("Comparación de Tiempos: Dinámico vs Fuerza Bruta vs Voraz")
    plt.legend()
    plt.grid(True)

    grafico_filename = f"grafico_comparativo_palindromo_{timestamp}.png"
    plt.savefig(grafico_filename)
    print(f"✅ Gráfico guardado en: {grafico_filename}")

