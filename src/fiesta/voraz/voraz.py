import tkinter as tk
from tkinter import filedialog

def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        cantidad_problemas = int(f.readline())
        problemas = []

        for _ in range(cantidad_problemas):
            n = int(f.readline())
            matriz = [list(map(int, f.readline().split())) for _ in range(n)]
            calificaciones = list(map(int, f.readline().split()))
            problemas.append((n, matriz, calificaciones))

        return problemas

def resolver_voraz(n, matriz, calificaciones):
    empleados = [(i, calificaciones[i]) for i in range(n)]
    empleados.sort(key=lambda x: -x[1])  # ordenamos por mayor calificación

    invitados = [0] * n
    excluidos = [False] * n

    for i, _ in empleados:
        if not excluidos[i]:
            invitados[i] = 1
            # excluimos supervisores directos
            for j in range(n):
                if matriz[j][i] == 1:
                    excluidos[j] = True
            # excluimos subordinados directos
            for j in range(n):
                if matriz[i][j] == 1:
                    excluidos[j] = True

    total = sum(calificaciones[i] for i in range(n) if invitados[i])
    return invitados, total

def elegir_archivo():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Selecciona el archivo", filetypes=[("Archivos de texto", "*.txt")])

def main():
    archivo = elegir_archivo()
    if not archivo:
        print("No se seleccionó archivo.")
        return

    problemas = leer_archivo(archivo)
    for n, matriz, calificaciones in problemas:
        invitados, total = resolver_voraz(n, matriz, calificaciones)
        print(' '.join(map(str, invitados)), total)
