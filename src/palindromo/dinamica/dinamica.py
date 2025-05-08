import re
import tkinter as tk
from tkinter import filedialog

# Normaliza una cadena
def normalizar_cadena(s):
    return ''.join(re.findall(r'[a-zA-Z0-9]', s.lower()))

# Devuelve la subsecuencia palindrómica más larga
def palindromo_maximo_dinamico(s):
    n = len(s)
    if n == 0:
        return ""

    dp = [[0]*n for _ in range(n)]

    # Cada letra individual es un palíndromo
    for i in range(n):
        dp[i][i] = 1

    # Llenar la tabla
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1] if cl > 2 else 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # Reconstrucción del palíndromo
    res = [""] * dp[0][n-1]
    i, j = 0, n - 1
    start, end = 0, dp[0][n-1] - 1

    while i <= j:
        if s[i] == s[j]:
            res[start] = s[i]
            res[end] = s[j]
            start += 1
            end -= 1
            i += 1
            j -= 1
        elif dp[i+1][j] > dp[i][j-1]:
            i += 1
        else:
            j -= 1

    return ''.join(res)

# File chooser
def elegir_archivo():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Selecciona el archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt")]
    )

# Procesamiento principal desde archivo (como el voraz)
def procesar_entrada_palindromo():
    archivo = elegir_archivo()
    if not archivo:
        print("No se seleccionó ningún archivo.")
        return

    with open(archivo, 'r', encoding='utf-8') as f:
        n_lineas = f.readline().strip()
        if not n_lineas.isdigit():
            print("❌ La primera línea debe ser un número.")
            return
        n = int(n_lineas)
        lineas = [f.readline().strip() for _ in range(n)]

    print("Resultados del problema de palíndromos:")
    for linea in lineas:
        normalizada = normalizar_cadena(linea)
        resultado = palindromo_maximo_dinamico(normalizada)
        print(resultado)
