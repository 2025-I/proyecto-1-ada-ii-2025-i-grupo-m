# file_chooser.py

import tkinter as tk
from tkinter import filedialog

def elegir_archivo():
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    return archivo
