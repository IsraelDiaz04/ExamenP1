class SemanaTemperaturas:
    def __init__(self):
        self.temperaturas = []

    def registrar(self):
        self.temperaturas.clear()
        for i in range(7):
            try:
                temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
                self.temperaturas.append(temp)
            except ValueError:
                print("Entrada inválida. Solo se permiten números.")
                self.temperaturas.clear()
                return

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def minima(self):
        return min(self.temperaturas)

    def dias_superiores(self):
        prom = self.promedio()
        return sum(1 for t in self.temperaturas if t > prom)

    def mostrar_resultados(self):
        if len(self.temperaturas) == 7:
            print("Temperatura promedio de la semana:", self.promedio())
            print("Temperatura más alta:", self.maxima())
            print("Temperatura más baja:", self.minima())
            print("Días con temperatura superior al promedio:", self.dias_superiores())
        else:
            print("Primero debe registrar correctamente las temperaturas.")


def menu():
    semana = SemanaTemperaturas()
    while True:
        print("\n--- Menú ---")
        print("1. Registrar temperaturas de la semana(Solo números, grados celsius)")
        print("2. Mostrar resultados")
        print("3. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            semana.registrar()
        elif opcion == "2":
            semana.mostrar_resultados()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


menu()
