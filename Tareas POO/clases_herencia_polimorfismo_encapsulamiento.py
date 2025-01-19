# Clase base que representa un vehículo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Atributos de la clase base
        self.marca = marca
        self.modelo = modelo
        self._año = año  # Atributo con encapsulación (acceso controlado)

    # Método para mostrar detalles del vehículo
    def mostrar_detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self._año}")

    # Método para obtener el año del vehículo
    def obtener_año(self):
        return self._año

    # Método para establecer el año del vehículo
    def establecer_año(self, año):
        if año > 1900 and año <= 2025:
            self._año = año
        else:
            print("Año no válido.")

    # Método que será sobrescrito por las clases derivadas
    def tipo_vehiculo(self):
        return "Vehículo genérico"


# Clase derivada que representa un coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo, año)
        self.puertas = puertas  # Atributo adicional para la clase derivada

    # Sobreescritura del método tipo_vehiculo para proporcionar una implementación específica
    def tipo_vehiculo(self):
        return "Coche"

    # Método adicional específico para la clase Coche
    def mostrar_detalles(self):
        # Llamada al método de la clase base
        super().mostrar_detalles()
        print(f"Puertas: {self.puertas}")


# Clase derivada que representa una moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada  # Atributo adicional para la clase derivada

    # Sobreescritura del método tipo_vehiculo para proporcionar una implementación específica
    def tipo_vehiculo(self):
        return "Moto"

    # Método adicional específico para la clase Moto
    def mostrar_detalles(self):
        # Llamada al método de la clase base
        super().mostrar_detalles()
        print(f"Cilindrada: {self.cilindrada} cc")


# Ejemplo de polimorfismo
def mostrar_tipo(vehiculo):
    print(f"Tipo de vehículo: {vehiculo.tipo_vehiculo()}")
    vehiculo.mostrar_detalles()


# Creación de instancias de las clases derivadas
mi_coche = Coche("Toyota", "Corolla", 2020, 4)
mi_moto = Moto("Yamaha", "MT-07", 2023, 700)

# Demostración de polimorfismo, pasando diferentes tipos de objetos
mostrar_tipo(mi_coche)
mostrar_tipo(mi_moto)

# Modificar el año de un vehículo usando el setter
mi_coche.establecer_año(2025)
print(f"Año actualizado del coche: {mi_coche.obtener_año()}")



