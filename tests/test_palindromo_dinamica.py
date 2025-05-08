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

def generar_entrada_palindromo(tamano):
    letras = string.ascii_letters + string.digits + "     "
    return ''.join(random.choices(letras, k=tamano))

def test_palindromo_juguete():
    entrada = "El ministro dijo Se es o no se es un ministro"
    esperado = "seesonosees"
    resultado = palindromo_maximo_dinamico(normalizar_cadena(entrada))
    assert resultado == esperado

def test_palindromo_escalado():
    tamanos = [
        ("Juguete", 10),
        ("Pequeño", 100),
        ("Mediano", 1000),
        ("Grande", 10000),
        ("Extra Grande", 50)
    ]

    resultados = {}
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    csv_filename = f"resultados_palindromo_{timestamp}.csv"
    grafico_filename = f"grafico_tiempos_palindromo_{timestamp}.png"

    with open(csv_filename, mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Tamaño", "Promedio (segundos)"])

        for nombre, tamano in tamanos:
            tiempos = []
            print(f"\n== Tamaño: {nombre} ({tamano} caracteres) ==")
            for i in range(5):
                entrada = generar_entrada_palindromo(tamano)
                normalizada = normalizar_cadena(entrada)
                inicio = time.time()
                resultado = palindromo_maximo_dinamico(normalizada)
                duracion = time.time() - inicio

                assert resultado == resultado[::-1]
                assert len(resultado) <= len(normalizada)
                print(f"  Repetición {i+1}: {duracion:.4f} segundos")
                tiempos.append(duracion)

            promedio = sum(tiempos) / len(tiempos)
            resultados[nombre] = promedio
            writer.writerow([nombre, f"{promedio:.4f}"])

    # Graficar resultados
    nombres = list(resultados.keys())
    tiempos = list(resultados.values())

    plt.figure(figsize=(10, 6))
    plt.plot(nombres, tiempos, marker='o', linestyle='-', color='green')
    plt.xlabel("Tamaño del texto")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Tiempo de ejecución promedio por tamaño - Palíndromo Dinámico")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(grafico_filename)
    plt.show()

    print(f"\n✅ Gráfico guardado en: {grafico_filename}")
    print(f"✅ Datos guardados en: {csv_filename}")
