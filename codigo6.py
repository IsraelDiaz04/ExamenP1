class Terreno:
    def __init__(self, terr_ini, generaciones, herederos):
        self.terr_ini = terr_ini
        self.generaciones = generaciones
        self.herederos = herederos

    def calc_terr_final(self):
        superficie = self.terr_ini
        for i in range(self.generaciones):
            superficie = superficie / self.herederos
        return superficie 

terr_ini = float(input("Ingresa la superficie inicial del terreno: "))
generaciones = int(input("Ingresa el número de generaciones: "))
herederos = int(input("Ingresa el número de herederos por generación: "))

terreno1 = Terreno(terr_ini, generaciones, herederos)
resultado = terreno1.calc_terr_final()

print("La superficie final que corresponde al heredero es:", resultado "M²")
