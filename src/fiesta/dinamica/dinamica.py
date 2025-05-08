import tkinter as tk
from tkinter import filedialog
import sys


def file_choose():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def procesar_entrada_fiesta():
    from file_chooser import elegir_archivo
    archivo = file_choose()
    with open(archivo, 'r', encoding='utf-8') as f:
        casos = int(f.readline())
        for _ in range(casos):
            m = int(f.readline())
            matriz = [list(map(int, f.readline().split())) for _ in range(m)]
            valores = list(map(int, f.readline().split()))
            resolver_fiesta(matriz, valores)

def resolver_fiesta(matriz, valores):
    """
    Recibe:
    - matriz: lista de adyacencias (matriz[i][j] = 1 si i es padre de j)
    - valores: lista de ganancias por invitar a cada persona

    Devuelve:
    - seleccion: lista binaria (0 o 1) indicando a quién invitar
    - suma_total: suma de los valores de los invitados
    """
    n = len(valores)
    hijos = [[] for _ in range(n)]
    padres = [0] * n

    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                hijos[i].append(j)
                padres[j] = 1

    # Encontrar la raíz
    raiz = padres.index(0)

    memo = {}

    def dp(node, incluir):
        key = (node, incluir)
        if key in memo:
            return memo[key]

        if incluir:
            suma = valores[node]
            for h in hijos[node]:
                suma += dp(h, False)
        else:
            suma = 0
            for h in hijos[node]:
                suma += max(dp(h, False), dp(h, True))

        memo[key] = suma
        return suma

    def reconstruir(node, incluir):
        seleccion[node] = 1 if incluir else 0
        if incluir:
            for h in hijos[node]:
                reconstruir(h, False)
        else:
            for h in hijos[node]:
                if dp(h, True) > dp(h, False):
                    reconstruir(h, True)
                else:
                    reconstruir(h, False)

    seleccion = [0] * n
    if dp(raiz, True) > dp(raiz, False):
        reconstruir(raiz, True)
    else:
        reconstruir(raiz, False)

    suma_total = sum(valores[i] for i in range(n) if seleccion[i] == 1)
    return seleccion, suma_total

    