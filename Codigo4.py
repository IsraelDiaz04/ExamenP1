import random

def llenar_vector(longitud):

    return [random.randint(-100, 100) for _ in range(longitud)]

def mostrar_vector(nombre, vector):

    print(f"\nVector {nombre}: {vector}\n")

def main():
    longitud = int(input("Ingrese la longitud de los vectores: "))
    A = []
    B = []
    C = []

    while True:
        print("\n----- MENÚ -----")
        print("1. Llenar Vector A de manera aleatoria")
        print("2. Llenar Vector B de manera aleatoria")
        print("3. Realizar C = A + B")
        print("4. Realizar C = B - A")
        print("5. Mostrar un vector (A, B o C)")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            A = llenar_vector(longitud)
            mostrar_vector("A", A)

        elif opcion == "2":
            B = llenar_vector(longitud)
            mostrar_vector("B", B)

        elif opcion == "3":
            if not A or not B:
                print("Error: primero llena los vectores A y B.")
            else:
                C = [a + b for a, b in zip(A, B)]
                print("Operación realizada: C = A + B.")

        elif opcion == "4":
            if not A or not B:
                print("Error: primero llena los vectores A y B.")
            else:
                C = [b - a for a, b in zip(A, B)]
                print("Operación realizada: C = B - A.")

        elif opcion == "5":
            eleccion = input("¿Qué vector deseas mostrar? (A/B/C): ").upper()
            if eleccion == "A":
                if A:
                    mostrar_vector("A", A)
                else:
                    print("Vector A no ha sido llenado.")
            elif eleccion == "B":
                if B:
                    mostrar_vector("B", B)
                else:
                    print("Vector B no ha sido llenado.")
            elif eleccion == "C":
                if C:
                    mostrar_vector("C", C)
                else:
                    print("Vector C no ha sido calculado.")
            else:
                print("Opción inválida.")

        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta nuevamente.")

if __name__ == "__main__":
    main()

