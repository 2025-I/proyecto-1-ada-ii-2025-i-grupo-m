import tkinter as tk
from tkinter import filedialog
import sys
from file_chooser import elegir_archivo


def file_choose():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def procesar_entrada_fiesta():
    archivo = file_choose()
    with open(archivo, 'r', encoding='utf-8') as f:
        casos = int(f.readline())
        for _ in range(casos):
            m = int(f.readline())
            matriz = [list(map(int, f.readline().split())) for _ in range(m)]
            valores = list(map(int, f.readline().split()))
            resolver_fiesta(matriz, valores)

def resolver_fiesta(matriz, valores):
    n = len(matriz)
    hijos = [[] for _ in range(n)]
    padres = [0]*n
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                hijos[i].append(j)
                padres[j] = 1

    raiz = padres.index(0)

    def dp(u):
        sin_u = 0
        con_u = valores[u]
        for v in hijos[u]:
            a, b = dp(v)
            sin_u += max(a, b)
            con_u += a
        return sin_u, con_u

    def reconstruir(u, incluir_padre):
        sin_u, con_u = dp(u)
        incluir = con_u > sin_u and not incluir_padre
        resultado[u] = 1 if incluir else 0
        for v in hijos[u]:
            reconstruir(v, incluir)

    resultado = [0]*n
    reconstruir(raiz, False)
    print(' '.join(map(str, resultado)), sum(valores[i] for i in range(n) if resultado[i] == 1))
    