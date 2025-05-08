from src.fiesta.dinamica.dinamica import procesar_entrada_fiesta
from src.palindromo.dinamica.dinamica import procesar_entrada_palindromo
from src.fiesta.fuerza_bruta.fuerza_bruta import procesar_entrada_fiesta1
from src.palindromo.fuerza_bruta.fuerza_bruta import procesar_entrada_palindromo1
from src.palindromo.voraz.voraz import mainvoraz 
from src.fiesta.voraz.voraz import main as procesar_entrada_fiesta_voraz

def main():
    print("=== Proyecto Análisis de Algoritmos II ===")
    print("Seleccione una opción:")
    print("0. Salir")
    print("1. Resolver problema de la FIESTA (dinámica)")
    print("2. Resolver problema del PALÍNDROMO (dinámica)")
    print("3. Resolver problema del FIESTA (fuerza bruta)")
    print("4. Resolver problema del PALÍNDROMO (fuerza bruta)")
    print("5. Resolver problema del FIESTA (voraz)")
    print("6. Resolver problema del PALÍNDROMO (voraz)")

    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        procesar_entrada_fiesta()
        print ("\n")
        return main()
    elif opcion == "2":
        procesar_entrada_palindromo()
        print ("\n")
        return main()
    elif opcion == "3":
        procesar_entrada_fiesta1()
        print ("\n")
        return main()
    elif opcion == "4":
        procesar_entrada_palindromo1()
        print ("\n")
        return main()
    elif opcion == "5":
        procesar_entrada_fiesta_voraz()
        print ("\n")
        return main()
    elif opcion == "6":
        mainvoraz()
        print ("\n")
        return main()
    elif opcion == "0":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente nuevamente.")

    

if __name__ == "__main__":
    main()
