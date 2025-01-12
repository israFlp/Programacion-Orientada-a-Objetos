# Clase que representa una Habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Constructor de la clase Habitacion.
        :param numero: Número de la habitación.
        :param tipo: Tipo de habitación (e.g., simple, doble, suite).
        :param precio: Precio por noche.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True  # Indica si la habitación está disponible

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo} - ${self.precio}/noche"


# Clase que representa un Huésped
class Huesped:
    def __init__(self, nombre, identificacion):
        """
        Constructor de la clase Huesped.
        :param nombre: Nombre del huésped.
        :param identificacion: Identificación del huésped (e.g., cédula o pasaporte).
        """
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f"Huésped: {self.nombre}, ID: {self.identificacion}"


# Clase que gestiona las reservas
class Reserva:
    def __init__(self, huesped, habitacion, dias):
        """
        Constructor de la clase Reserva.
        :param huesped: Objeto de la clase Huesped.
        :param habitacion: Objeto de la clase Habitacion.
        :param dias: Número de días de la reserva.
        """
        self.huesped = huesped
        self.habitacion = habitacion
        self.dias = dias
        self.total = self.calcular_total()

    def calcular_total(self):
        """
        Calcula el costo total de la reserva.
        :return: Total a pagar.
        """
        return self.habitacion.precio * self.dias

    def confirmar_reserva(self):
        """
        Confirma la reserva y marca la habitación como no disponible.
        """
        if self.habitacion.disponible:
            self.habitacion.disponible = False
            print(f"Reserva confirmada para {self.huesped.nombre} en la {self.habitacion}.")
        else:
            print("La habitación no está disponible.")

    def __str__(self):
        return (f"Reserva de {self.huesped.nombre} para la {self.habitacion} por {self.dias} días. "
                f"Total: ${self.total}")


# Clase principal para gestionar el sistema de reservas del hotel
class Hotel:
    def __init__(self, nombre):
        """
        Constructor de la clase Hotel.
        :param nombre: Nombre del hotel.
        """
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        """
        Agrega una nueva habitación al hotel.
        :param habitacion: Objeto de la clase Habitacion.
        """
        self.habitaciones.append(habitacion)

    def listar_habitaciones_disponibles(self):
        """
        Lista todas las habitaciones disponibles.
        """
        disponibles = [hab for hab in self.habitaciones if hab.disponible]
        if disponibles:
            print("Habitaciones disponibles:")
            for hab in disponibles:
                print(hab)
        else:
            print("No hay habitaciones disponibles.")

    def hacer_reserva(self, huesped, numero_habitacion, dias):
        """
        Crea una reserva para un huésped.
        :param huesped: Objeto de la clase Huesped.
        :param numero_habitacion: Número de la habitación deseada.
        :param dias: Número de días de la reserva.
        """
        habitacion = next((hab for hab in self.habitaciones if hab.numero == numero_habitacion), None)
        if habitacion and habitacion.disponible:
            reserva = Reserva(huesped, habitacion, dias)
            reserva.confirmar_reserva()
            self.reservas.append(reserva)
        else:
            print(f"La habitación {numero_habitacion} no está disponible.")

    def __str__(self):
        return f"Hotel {self.nombre}"


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear el hotel
    hotel = Hotel("Paraíso Tropical")

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "Simple", 50))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
    hotel.agregar_habitacion(Habitacion(201, "Suite", 150))

    # Crear un huésped
    huesped1 = Huesped("Carlos Pérez", "1234567890")

    # Mostrar habitaciones disponibles
    hotel.listar_habitaciones_disponibles()

    # Hacer una reserva
    hotel.hacer_reserva(huesped1, 102, 3)

    # Mostrar habitaciones disponibles después de la reserva
    hotel.listar_habitaciones_disponibles()
