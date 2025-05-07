import os

project_root = os.getcwd()

# Carpeta base de código fuente
src_base = "src"

# Subcarpetas por problema y enfoque
problemas = ["palindromo", "fiesta"]
enfoques = ["fuerza_bruta", "dinamica", "voraz"]

folders = [
    "tests",
    "docs/imagenes",
    ".github/workflows"
]

# Agregar estructura de src/palindromo/{fuerza_bruta, dinamica, voraz} y lo mismo para fiesta
for problema in problemas:
    for enfoque in enfoques:
        folders.append(f"{src_base}/{problema}/{enfoque}")

# Archivos con contenido inicial
files = {
    "README.md": "# Proyecto 1 - ADA II\n\nDescripción general del proyecto.\n",
    ".gitignore": "__pycache__/\n*.pyc\n.env\n",
    "docs/introduccion.md": "# Introducción\n",
    "docs/analisis.md": "# Análisis del sistema\n",
    "docs/diseno.md": "# Diseño del sistema\n",
    "docs/implementacion.md": "# Implementación\n",
    "docs/conclusiones.md": "# Conclusiones\n",
    "tests/test_ejemplo.py": "def test_ejemplo():\n    assert True\n",
    ".github/workflows/ci.yml": '''\
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout del código
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt || echo "No hay requirements.txt"

      - name: Ejecutar pruebas
        run: |
          pytest || python -m unittest discover
'''
}

# Crear carpetas
for folder in folders:
    os.makedirs(os.path.join(project_root, folder), exist_ok=True)

# Agregar al diccionario de archivos
files["requirements.txt"] = '''\
pytest>=7.0.0
pytest-cov>=4.0.0
pandas>=2.0.0
matplotlib>=3.7.0
'''

# Crear archivos
for filename, content in files.items():
    with open(os.path.join(project_root, filename), 'w', encoding='utf-8') as f:
        f.write(content)

# Crear archivos __init__.py y scripts base en cada carpeta de enfoque
for problema in problemas:
    for enfoque in enfoques:
        path = os.path.join(project_root, f"{src_base}/{problema}/{enfoque}")
        init_path = os.path.join(path, "__init__.py")
        script_path = os.path.join(path, f"{enfoque}.py")
        
        with open(init_path, 'w', encoding='utf-8') as f:
            f.write("")
        
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(f"# Solución {enfoque.replace('_', ' ')} para el problema de {problema}\n\n")
            f.write("def resolver():\n    pass\n")

print("✅ Estructura completa del proyecto generada correctamente.")
