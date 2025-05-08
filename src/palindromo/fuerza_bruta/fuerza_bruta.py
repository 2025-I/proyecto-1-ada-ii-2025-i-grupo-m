import tkinter as tk
from tkinter import filedialog
import time
import re

MAX_LENGTH = 20  # Máxima longitud del palíndromo que se intentará encontrar

def file_choose():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def procesar_entrada_palindromo1():
    print("\n=== FUERZA BRUTA (máx. palíndromo de {} caracteres) ===".format(MAX_LENGTH))
    print("Para palíndromos más largos usar método dinámico\n")
    
    archivo = file_choose()
    if not archivo:
        print("Operación cancelada.")
        return
    
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = [linea.strip() for linea in f if linea.strip()]
        
        n_cadenas = int(lineas[0])
        cadenas = lineas[1:n_cadenas+1]
        
        for i, cadena in enumerate(cadenas, 1):
            print(f"\nProcesando cadena {i}/{n_cadenas}:")
            print("Texto original:", cadena[:50] + "..." if len(cadena) > 50 else cadena)
            
            s = normalizar_cadena(cadena)
            
            inicio = time.time()
            resultado = encontrar_palindromo(s)
            tiempo = time.time() - inicio
            
            print(f"Palíndromo más largo: {resultado}")
            print(f"Tiempo: {tiempo:.2f} segundos")
    
    except Exception as e:
        print(f"Error: {str(e)}")

def normalizar_cadena(cadena):
    cadena = cadena.lower()
    return re.sub(r'[^a-z0-9]', '', cadena)

def encontrar_palindromo(s):
    """Busca subcadenas consecutivas que sean palíndromos con longitud máxima limitada."""
    n = len(s)
    mejor = ""
    
    for i in range(n):
        for j in range(i + 1, min(n + 1, i + MAX_LENGTH + 1)):  
            sub = s[i:j]
            if sub == sub[::-1]:
                if len(sub) > len(mejor):
                    mejor = sub
                elif len(sub) == len(mejor):
                    mejor = min(mejor, sub)
    
    return mejor

if __name__ == "__main__":
    procesar_entrada_palindromo1()
