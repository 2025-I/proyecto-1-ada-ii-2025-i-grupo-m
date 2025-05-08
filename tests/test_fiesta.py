import sys
import os
import time
import random
import matplotlib.pyplot as plt
import signal
from datetime import datetime
import csv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from fiesta.dinamica.dinamica import resolver_fiesta as resolver_dinamico
from fiesta.fuerza_bruta.fuerza_bruta import resolver_fiesta_fuerza_bruta
from fiesta.voraz.voraz import resolver_voraz

# Para matar fuerza bruta si se excede
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

signal.signal(signal.SIGALRM, timeout_handler)

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
        ("Grande", 10000)
        # Se omite "Extra Grande"
    ]

    resultados = {nombre: {"dinamico": 0, "fuerza_bruta": 0, "voraz": 0} for nombre, _ in tamanos}
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    csv_filename = f"resultados_fiesta_{timestamp}.csv"
    grafico_filename = f"grafico_tiempos_fiesta_{timestamp}.png"

    with open(csv_filename, mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Tamaño", "Dinámico", "Fuerza Bruta", "Voraz"])

        for nombre, tamano in tamanos:
            tiempos_d, tiempos_fb, tiempos_v = [], [], []

            print(f"\n== Tamaño: {nombre} ({tamano} nodos) ==")
            for _ in range(5):
                matriz, valores = generar_arbol_y_valores(tamano)

                # Dinámico
                inicio = time.time()
                seleccion_d, suma_d = resolver_dinamico(matriz, valores)
                tiempo_d = time.time() - inicio
                tiempos_d.append(tiempo_d)

                # Voraz
                inicio = time.time()
                seleccion_v, suma_v = resolver_voraz(tamano, matriz, valores)
                tiempo_v = time.time() - inicio
                tiempos_v.append(tiempo_v)

                # Fuerza bruta con timeout de 2 segundos
                try:
                    signal.alarm(2)
                    inicio = time.time()
                    seleccion_fb, suma_fb = resolver_fiesta_fuerza_bruta(matriz, valores, retorno=True)
                    tiempo_fb = time.time() - inicio
                    tiempos_fb.append(tiempo_fb)
                except TimeoutException:
                    print("⚠️  Fuerza bruta excedió el tiempo límite.")
                    tiempos_fb.append(2.0)
                finally:
                    signal.alarm(0)

                print(f"  Repetición: Dinámico={tiempo_d:.4f}s | Fuerza Bruta={tiempos_fb[-1]:.4f}s | Voraz={tiempo_v:.4f}s")

            # Promedios
            prom_d = sum(tiempos_d) / len(tiempos_d)
            prom_fb = sum(tiempos_fb) / len(tiempos_fb)
            prom_v = sum(tiempos_v) / len(tiempos_v)

            resultados[nombre]["dinamico"] = prom_d
            resultados[nombre]["fuerza_bruta"] = prom_fb
            resultados[nombre]["voraz"] = prom_v

            writer.writerow([nombre, f"{prom_d:.4f}", f"{prom_fb:.4f}", f"{prom_v:.4f}"])

    # === Gráfico agrupado como palíndromo ===
    nombres = list(resultados.keys())
    tiempos_d = [resultados[n]["dinamico"] for n in nombres]
    tiempos_fb = [resultados[n]["fuerza_bruta"] for n in nombres]
    tiempos_v = [resultados[n]["voraz"] for n in nombres]

    x = range(len(nombres))
    width = 0.25

    plt.figure(figsize=(10, 6))
    plt.bar([i - width for i in x], tiempos_d, width, label='Dinámico', color='skyblue')
    plt.bar(x, tiempos_fb, width, label='Fuerza Bruta', color='salmon')
    plt.bar([i + width for i in x], tiempos_v, width, label='Voraz', color='lightgreen')

    plt.xlabel("Tamaño del árbol")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Comparación de tiempos por estrategia - Fiesta")
    plt.xticks(x, nombres)
    plt.legend()
    plt.tight_layout()
    plt.savefig(grafico_filename)
    plt.show()

    print(f"\n✅ Gráfico guardado en: {grafico_filename}")
    print(f"✅ CSV guardado en: {csv_filename}")
