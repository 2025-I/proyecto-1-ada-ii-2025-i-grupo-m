import tkinter as tk
from tkinter import filedialog
import time
import re
from itertools import combinations

MAX_LENGTH = 20  # Límite práctico para fuerza bruta

def file_choose():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def procesar_entrada_palindromo1():
    print("\n=== FUERZA BRUTA (limitado a {} caracteres) ===".format(MAX_LENGTH))
    print("Para cadenas más largas usar método dinámico\n")
    
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
            if len(s) > MAX_LENGTH:
                print(f"¡Atención! Cadena truncada a {MAX_LENGTH} caracteres para fuerza bruta")
                s = s[:MAX_LENGTH]
            
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
    """Versión optimizada con límite de longitud"""
    n = len(s)
    mejor = ""
    
    for length in range(min(n, MAX_LENGTH), 0, -1):
        print(f"Probando longitud {length}...", end='\r')
        
        for indices in combinations(range(n), length):
            sub = ''.join(s[i] for i in indices)
            if sub == sub[::-1]:
                if len(sub) > len(mejor):
                    mejor = sub
                elif len(sub) == len(mejor):
                    mejor = min(mejor, sub)
        
        if mejor and len(mejor) == length:
            break  # No puede haber uno más largo
    
    print(" " * 40, end='\r')  # Limpiar línea
    return mejor

if __name__ == "__main__":
    procesar_entrada_palindromo1()