import re
import tkinter as tk
from tkinter import filedialog

# Función para normalizar la cadena (convierte a minúsculas y elimina caracteres no alfanuméricos)
def normalizar_cadena(s):
    # Eliminar caracteres no alfanuméricos y convertir a minúsculas
    return ''.join(re.findall(r'[a-zA-Z0-9]', s.lower()))

# Función para encontrar la subsecuencia palindrómica más larga utilizando expansión
def palindromo_maximo(s):
    n = len(s)
    if n == 0:
        return ""
    
    # Variables para almacenar el inicio y la longitud del palíndromo máximo encontrado
    inicio = 0
    longitud_max = 1
    
    # Expansión para encontrar palíndromos con centro en cada índice
    for i in range(n):
        # Caso 1: Palíndromos de longitud impar (centrados en un solo carácter)
        izquierda, derecha = i, i
        while izquierda >= 0 and derecha < n and s[izquierda] == s[derecha]:
            if derecha - izquierda + 1 > longitud_max:
                longitud_max = derecha - izquierda + 1
                inicio = izquierda
            izquierda -= 1
            derecha += 1
        
        # Caso 2: Palíndromos de longitud par (centrados entre dos caracteres)
        izquierda, derecha = i, i + 1
        while izquierda >= 0 and derecha < n and s[izquierda] == s[derecha]:
            if derecha - izquierda + 1 > longitud_max:
                longitud_max = derecha - izquierda + 1
                inicio = izquierda
            izquierda -= 1
            derecha += 1
    
    # Devolver el palíndromo más largo
    return s[inicio:inicio + longitud_max]

# Función para resolver el problema con el archivo
def resolver_palindromos_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        # Leemos el número de cadenas
        n = int(archivo.readline().strip())
        # Leemos las cadenas y procesamos
        cadenas = [archivo.readline().strip() for _ in range(n)]
        
    resultados = []
    for cadena in cadenas:
        # Normalizamos la cadena
        cadena_normalizada = normalizar_cadena(cadena)
        # Encontramos el palíndromo más largo
        resultado = palindromo_maximo(cadena_normalizada)
        # Añadir resultado a la lista de resultados
        resultados.append(resultado)
    return resultados

# Función para abrir el file chooser y obtener la ruta del archivo
def elegir_archivo():
    # Crear la ventana principal
    root = tk.Tk()
    root.withdraw()  # Ocultamos la ventana principal de Tkinter
    # Abrir el file chooser
    archivo = filedialog.askopenfilename(title="Selecciona el archivo de entrada", filetypes=[("Archivos de texto", "*.txt")])
    return archivo

# Función principal para ejecutar el programa
def mainvoraz():
    # Llamamos a la función para elegir el archivo
    archivo = elegir_archivo()
    
    if archivo:
        # Resolver el problema con el archivo seleccionado
        resultados = resolver_palindromos_desde_archivo(archivo)
        # Mostrar los resultados
        for resultado in resultados:
            print(resultado)
    else:
        print("No se seleccionó ningún archivo.")