# Documentación del archivo CI.yml

Este archivo define un flujo de trabajo de integración continua (CI) para el proyecto utilizando GitHub Actions. A continuación, se describe cada sección del archivo:

## Nombre del flujo de trabajo
```yml
name: CI
```
El flujo de trabajo se llama `CI`, que significa "Integración Continua".

## Eventos que activan el flujo de trabajo
```yml
on: [push, pull_request]
```
El flujo de trabajo se ejecuta automáticamente cuando se realiza un `push` o se crea un `pull_request` en el repositorio.

## Definición de trabajos (jobs)
### Trabajo: `build`
```yml
jobs:
  build:
    runs-on: ubuntu-latest
```
El trabajo `build` se ejecuta en un entorno de máquina virtual con el sistema operativo `ubuntu-latest`.

### Pasos del trabajo
#### 1. Checkout del código
```yml
- name: Checkout del código
  uses: actions/checkout@v3
```
Este paso utiliza la acción `actions/checkout` para clonar el código del repositorio en la máquina virtual.

#### 2. Configurar Python
```yml
- name: Configurar Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.10'
```
Este paso configura el entorno de Python en la versión `3.10` para ejecutar el flujo de trabajo.

#### 3. Instalar dependencias
```yml
- name: Instalar dependencias
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt || echo "No hay requirements.txt"
    pip install pytest pytest-cov
```
En este paso:
- Se actualiza `pip` a la última versión.
- Se instalan las dependencias listadas en el archivo `requirements.txt`. Si el archivo no existe, se muestra un mensaje.
- Se instalan las herramientas `pytest` y `pytest-cov` para ejecutar pruebas y generar reportes de cobertura.

#### 4. Ejecutar pruebas y generar reporte
```yml
- name: Ejecutar pruebas y generar reporte
  run: |
    pytest --cov=src --cov-report=term
```
Este paso ejecuta las pruebas del proyecto utilizando `pytest` y genera un reporte de cobertura en la terminal.
