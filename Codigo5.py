def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

def ingresar_palabras():
    return input("Ingresa palabras separadas por espacios: ").split()

def mostrar_palindromas(palabras):
    palindromas = [p for p in palabras if es_palindromo(p)]
    print("\nPalabras palíndromas encontradas:")
    if palindromas:
        for p in palindromas:
            print("-", p)
    else:
        print("No se encontraron palíndromas.")

def menu():
    palabras = []
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar palabras")
        print("2. Mostrar palabras palíndromas")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            palabras = ingresar_palabras()
        elif opcion == "2":
            if palabras:
                mostrar_palindromas(palabras)
            else:
                print("Primero debes ingresar palabras (opción 1).")
        elif opcion == "3":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()
