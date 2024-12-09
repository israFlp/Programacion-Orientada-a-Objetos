class Criatura:

    def __init__(self, nombre, poder, agilidad, resistencia, salud):
        self.nombre = nombre
        self.poder = poder
        self.agilidad = agilidad
        self.resistencia = resistencia
        self.salud = salud

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Poder:", self.poder)
        print("·Agilidad:", self.agilidad)
        print("·Resistencia:", self.resistencia)
        print("·Salud:", self.salud)

    def subir_nivel(self, poder, agilidad, resistencia):
        self.poder += poder
        self.agilidad += agilidad
        self.resistencia += resistencia

    def esta_vivo(self):
        return self.salud > 0

    def morir(self):
        self.salud = 0
        print(self.nombre, "ha sido derrotado.")

    def daño(self, enemigo):
        return max(0, self.poder - enemigo.resistencia)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.salud -= daño
        print(self.nombre, "ha infligido", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Salud de", enemigo.nombre, "es", enemigo.salud)
        else:
            enemigo.morir()


class Dragón(Criatura):

    def __init__(self, nombre, poder, agilidad, resistencia, salud, fuego):
        super().__init__(nombre, poder, agilidad, resistencia, salud)
        self.fuego = fuego

    def atributos(self):
        super().atributos()
        print("·Fuego:", self.fuego)

    def daño(self, enemigo):
        return (self.poder + self.fuego) - enemigo.resistencia


class Unicornio(Criatura):

    def __init__(self, nombre, poder, agilidad, resistencia, salud, magia):
        super().__init__(nombre, poder, agilidad, resistencia, salud)
        self.magia = magia

    def atributos(self):
        super().atributos()
        print("·Magia:", self.magia)

    def daño(self, enemigo):
        return (self.magia * self.agilidad) - enemigo.resistencia


def duelo(criatura_1, criatura_2):
    turno = 0
    while criatura_1.esta_vivo() and criatura_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Turno de", criatura_1.nombre)
        criatura_1.atacar(criatura_2)
        if criatura_2.esta_vivo():
            print(">>> Turno de", criatura_2.nombre)
            criatura_2.atacar(criatura_1)
        turno += 1
    if criatura_1.esta_vivo():
        print("\n¡", criatura_1.nombre, "ha ganado!", sep="")
    elif criatura_2.esta_vivo():
        print("\n¡", criatura_2.nombre, "ha ganado!", sep="")
    else:
        print("\nEmpate. Ambas criaturas han caído.")


# Ejemplo de uso
dragón = Dragón("Fafnir", 30, 10, 15, 120, 25)
unicornio = Unicornio("Etherea", 10, 20, 10, 100, 15)

dragón.atributos()
unicornio.atributos()

duelo(dragón, unicornio)
