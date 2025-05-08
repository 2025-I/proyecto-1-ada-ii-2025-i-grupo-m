import tkinter as tk
from tkinter import filedialog
import time 

def file_choose():
    
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()


def procesar_entrada_fiesta1():
    """Función con la misma interfaz que la versión dinámica para ser intercambiable"""
    archivo = file_choose()
    with open(archivo, 'r', encoding='utf-8') as f:
        casos = int(f.readline())
        for _ in range(casos):
            m = int(f.readline())
            matriz = [list(map(int, f.readline().split())) for _ in range(m)]
            valores = list(map(int, f.readline().split()))
            
            inicio = time.time()
            resolver_fiesta_fuerza_bruta(matriz, valores)
            fin = time.time()
            
            print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos\n")

def resolver_fiesta_fuerza_bruta(matriz, valores):
    """Versión fuerza bruta con misma salida que la dinámica y medición de tiempo"""
    n = len(matriz)
    max_sum = 0
    best_invitation = [0] * n
    
    for mask in range(1, 1 << n):
        current_inv = [0] * n
        current_sum = 0
        valid = True
        
        for i in range(n):
            if mask & (1 << i):
                current_inv[i] = 1
                current_sum += valores[i]
        
        for i in range(n):
            if current_inv[i] == 1:
                for j in range(n):
                    if matriz[i][j] == 1 and current_inv[j] == 1:
                        valid = False
                        break
                if not valid:
                    break
        
        if valid and current_sum > max_sum:
            max_sum = current_sum
            best_invitation = current_inv.copy()
    
    print(' '.join(map(str, best_invitation)), max_sum)