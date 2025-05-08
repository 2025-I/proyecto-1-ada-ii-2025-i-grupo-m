from src.fiesta.dinamica.dinamica import procesar_entrada_fiesta
from src.palindromo.dinamica.dinamica import procesar_entrada_palindromo
from src.fiesta.fuerza_bruta.fuerza_bruta import procesar_entrada_fiesta1

def main():
    print("=== Proyecto Análisis de Algoritmos II ===")
    print("Seleccione una opción:")
    print("0. Salir")
    print("1. Resolver problema de la FIESTA (dinámica)")
    print("2. Resolver problema del PALÍNDROMO (dinámica)")
    print("3. Resolver problema del FIESTA (fuerza bruta)")
    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        procesar_entrada_fiesta()
        return main()
    elif opcion == "2":
        procesar_entrada_palindromo()
        return main()
    elif opcion == "3":
        procesar_entrada_fiesta1()
        return main()
    elif opcion == "0":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente nuevamente.")

    

if __name__ == "__main__":
    main()
