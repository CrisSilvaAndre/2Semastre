class Auto:

    def __init__(self, marca, velocidad, costo, diseño, utilidad):
        self.marca = marca
        self.velocidad = velocidad
        self.costo = costo
        self.diseño = diseño
        self.utilidad = utilidad

    def caracteristicas(self):
        print(self.marca, ":", sep="")
        print("·Velocidad:", self.velocidad)
        print("·Costo:", self.costo)
        print("·Diseño:", self.diseño)
        print("·Urilidad:", self.utilidad)

    def mejor_opcion(self, velocidad, costo, diseño):
        self.velocidad = self.velocidad + velocidad
        self.costo = self.costo + costo
        self.diseño = self.diseño + diseño

    def ganador(self):
        return self.utilidad > 0

    def perdedor(self):
        self.utilidad = 0
        print(self.marca, "perdedor")

    def diferencia(self, enemigos):
        return self.velocidad - enemigos.diseño

    def comparar(self, enemigos):
        diferencia = self.diferencia(enemigos)
        enemigos.utilidad = enemigos.utilidad - diferencia
        print(self.marca, "es mejor en", diferencia, "a comparacion de", enemigos.marca)
        if enemigos.esta_utilidad():
            print("La utilidad de", enemigos.marca, "es", enemigos.marca)
        else:
            enemigos.perdedor()


class Ferrari(Elecciones):

    def __init__(self, marca, velocidad, costo, diseño, utilidad, rapidez):
        super().__init__(marca, velocidad, costo, diseño, utilidad)
        self.rapidez = rapidez

    def otras_caracteristicas(self):
        opcion = int(input("Elige otras caracteristicas: (1) Velocidad maxima, 300 km/h. (2) Velocidad maxima, 350 km/h"))
        if opcion == 1:
            self.rapidez = 300
        elif opcion == 2:
            self.rapidez = 350
        else:
            print("Caracteristica no disponible")

    def caracteristicas(self):
        super().caracteristicas()
        print("Rapidez:", self.rapidez)

    def diferencia(self, enemigos):
        return self.velocidad * self.rapidez - enemigos.diseño


class Mercedes(Elecciones):

    def __init__(self, marca, velocidad, costo, diseño, utilidad, rapidez2):
        super().__init__(marca, velocidad, costo, diseño, utilidad)
        self.rapidez2 = rapidez2

    def caracteristicas(self):
        super().caracteristicas()
        print("·Rapidez:", self.rapidez2)

    def diferencia(self, enemigos):
        return self.costo * self.rapidez2 - enemigos.diseño


def comparacion(carro_1, carro_2):
    turno = 0
    while carro_1.ganador() and carro_2.ganador():
        print("\nComparacion", turno)
        print(">>> Comparacion de ", carro_1.marca, ":", sep="")
        carro_1.comparar(carro_2)
        print(">>> Comparacion de ", carro_2.marca, ":", sep="")
        carro_2.comparar(carro_1)
        turno = turno + 1
    if carro_1.ganador():
        print("\nHa ganado", carro_1.marca)
    elif carro_2.ganador():
        print("\nHa ganado", carro_2.marca)
    else:
        print("\nEmpate")


eleccion_1 = Ferrari("Ferrari", 325, 100000, 8, 100, 180)
eleccion_2 = Mercedes("Mercedes", 300, 95000, 7, 100, 170)

eleccion_1.caracteristicas()
eleccion_2.caracteristicas()

comparacion(eleccion_1, eleccion_2)
