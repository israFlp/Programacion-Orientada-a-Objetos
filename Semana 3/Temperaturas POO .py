class Clima:
    def __init__(self, ciudad):
        self.ciudad = ciudad  # Nombre de la ciudad
        self.semanas = []  # Lista para almacenar las semanas

    # Método para agregar una semana de temperaturas a la ciudad
    def agregar_semana(self, semana):
        self.semanas.append(semana)

    # Método para calcular el promedio de las temperaturas de la ciudad
    def calcular_promedio(self):
        suma_temperaturas = 0
        total_dias = 0
        for semana in self.semanas:
            for dia in semana:
                suma_temperaturas += dia['temp']
                total_dias += 1
        return suma_temperaturas / total_dias if total_dias > 0 else 0


# Definimos las temperaturas de las tres ciudades
temperaturas_ciudad_1 = [
    [  # Semana 1
        {"day": "Lunes", "temp": 78},
        {"day": "Martes", "temp": 80},
        {"day": "Miércoles", "temp": 82},
        {"day": "Jueves", "temp": 79},
        {"day": "Viernes", "temp": 85},
        {"day": "Sábado", "temp": 88},
        {"day": "Domingo", "temp": 92}
    ],
    [  # Semana 2
        {"day": "Lunes", "temp": 76},
        {"day": "Martes", "temp": 79},
        {"day": "Miércoles", "temp": 83},
        {"day": "Jueves", "temp": 81},
        {"day": "Viernes", "temp": 87},
        {"day": "Sábado", "temp": 89},
        {"day": "Domingo", "temp": 93}
    ],
    [  # Semana 3
        {"day": "Lunes", "temp": 77},
        {"day": "Martes", "temp": 81},
        {"day": "Miércoles", "temp": 85},
        {"day": "Jueves", "temp": 82},
        {"day": "Viernes", "temp": 88},
        {"day": "Sábado", "temp": 91},
        {"day": "Domingo", "temp": 95}
    ],
    [  # Semana 4
        {"day": "Lunes", "temp": 75},
        {"day": "Martes", "temp": 78},
        {"day": "Miércoles", "temp": 80},
        {"day": "Jueves", "temp": 79},
        {"day": "Viernes", "temp": 84},
        {"day": "Sábado", "temp": 87},
        {"day": "Domingo", "temp": 91}
    ]
]

# Creamos los objetos para cada ciudad
ciudad_1 = Clima("Ciudad 1")
for semana in temperaturas_ciudad_1:
    ciudad_1.agregar_semana(semana)

# Agrega las temperaturas para las otras ciudades de manera similar
# Para simplificar, solo creamos una ciudad aquí. Sigue el mismo patrón para Ciudad 2 y Ciudad 3

# Menú interactivo para seleccionar ciudad y calcular el promedio
while True:
    print("\nSeleccione una ciudad ")
    print("1 - Ciudad 1")
    print("2 - Ciudad 2")
    print("3 - Ciudad 3")
    print("4 - Salir ")

    opcion = input("Ingrese la opción: ")

    if opcion == "1":
        promedio = ciudad_1.calcular_promedio()
        print(f"El promedio de {ciudad_1.ciudad} es: {promedio:.2f}")
    elif opcion == "2":
        # Se crearía un objeto de la ciudad 2, igual que para la ciudad 1
        pass
    elif opcion == "3":
        # Se crearía un objeto de la ciudad 3, igual que para la ciudad 1
        pass
    elif opcion == "4":
        print("Salir del programa.")
        break
    else:
        print("Opción no válida, intente nuevamente.")
