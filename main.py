from src.fiesta.dinamica.dinamica import procesar_entrada_fiesta
from src.palindromo.dinamica.dinamica import procesar_entrada_palindromo
from src.palindromo.voraz.voraz import mainvoraz
from src.fiesta.voraz.voraz import main as procesar_entrada_fiesta_voraz

def main():
    print("=== Proyecto Análisis de Algoritmos II ===")
    print("Seleccione una opción:")
    print("0. Salir")
    print("1. Resolver problema de la FIESTA (dinámica)")
    print("2. Resolver problema del PALÍNDROMO (dinámica)")
    print("3. Resolver problema del PALINDROMO (Voraz)")
    print("4. Resolver problema de la FIESTA (Voraz)")
    print("===========================================")
    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        procesar_entrada_fiesta()
        return main()
    elif opcion == "2":
        procesar_entrada_palindromo()
        return main()
    elif opcion == "3":
        mainvoraz()
        return main()
    elif opcion == "4":
        procesar_entrada_fiesta_voraz()
        return main()
    elif opcion == "0":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente nuevamente.")

    

if __name__ == "__main__":
    main()