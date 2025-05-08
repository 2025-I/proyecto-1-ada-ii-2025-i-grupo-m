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
    
    # Inicializar tabla dp donde dp[i][j] = 1 si s[i:j+1] es un palíndromo, 0 en caso contrario
    dp = [[False for _ in range(n)] for _ in range(n)]
    
    # Todos los caracteres individuales son palíndromos
    for i in range(n):
        dp[i][i] = True
    
    # Palíndromos de longitud 2
    inicio = 0
    max_len = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            inicio = i
            max_len = 2
    
    # Palíndromos de longitud mayor a 2
    for longitud in range(3, n+1):
        for i in range(n-longitud+1):
            j = i + longitud - 1  # Índice final
            
            # Verificar si el primer y último carácter son iguales y el resto es un palíndromo
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                
                if longitud > max_len:
                    max_len = longitud
                    inicio = i
    
    # Devolver el palíndromo encontrado
    return s[inicio:inicio + max_len]

# File chooser
def elegir_archivo():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Selecciona el archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt")] 
    )

# Procesamiento principal desde archivo
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
