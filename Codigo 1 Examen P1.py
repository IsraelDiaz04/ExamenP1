 # crea dos listas (arreglos unidimensionales). 
# Una almacena nombres de personas y la otra almacena la longitud de esos nombres.
    
def main():

    try:
        size = int(input("Ingresa el número de nombres que deseas almacenar: "))

        
        if size <= 0:
            print("El tamaño debe ser un número positivo.")
            return

        names = []
        lengths = []

        print("\n Ingresa los nombres")
        for i in range(size):
            name = input(f"Ingresa el nombre {i + 1}: ")
            names.append(name)
            lengths.append(len(name))

        print("\n Nombres y sus longitudes ")
        for i in range(size):
            print(f"Nombre: '{names[i]}' | Longitud: {lengths[i]}")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero para el tamaño.")

if __name__ == "__main__":
    main()