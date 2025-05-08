from src.fiesta.dinamica.dinamica import procesar_entrada_fiesta
from src.palindromo.dinamica.dinamica import procesar_entrada_palindromo

def main():
    print("=== Proyecto Análisis de Algoritmos II ===")
    print("Seleccione una opción:")
    print("1. Resolver problema de la FIESTA (dinámica)")
    print("2. Resolver problema del PALÍNDROMO (dinámica)")
    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        procesar_entrada_fiesta()
    elif opcion == "2":
        procesar_entrada_palindromo()
    else:
        print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
