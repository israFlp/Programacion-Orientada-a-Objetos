import os
import time

def mostrar_codigo(ruta_script):
    """
    Muestra el código del archivo especificado.
    :param ruta_script: Ruta del script cuyo código se desea mostrar.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script_absoluta} ---\n")
            print(archivo.read())  # Muestra el contenido del archivo
    except FileNotFoundError:
        print(f"El archivo '{ruta_script}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def agregar_opcion(opciones):
    """
    Permite al usuario agregar nuevas opciones de scripts al menú.
    :param opciones: Diccionario actual de opciones.
    """
    nombre_script = input("Ingrese el nombre del nuevo script: ")
    ruta_script = input("Ingrese la ruta relativa del script: ")

    if os.path.isfile(ruta_script):
        opciones[str(len(opciones) + 1)] = nombre_script
        print(f"Se ha agregado {nombre_script} al menú.")
    else:
        print("La ruta del script no es válida.")

def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles y permite al usuario seleccionar un script.
    """
    ruta_base = os.path.dirname(__file__)
    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-1. Ejemplo Programacion tradicional frente a POO.py',
        '3': 'Unidad 1/3.1. Estadistica Descriptiva/3.1-1. Ejemplo Estadistica Descriptiva.py',  # Nuevo script agregado
    }

    while True:
        print("\n******** Menu Principal - Dashboard *************")
        print("\nOpciones disponibles:")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("a - Agregar un nuevo script")
        print("0 - Salir")

        eleccion = input("\nElige una opción: ")

        if eleccion == '0':
            break
        elif eleccion == 'a':
            agregar_opcion(opciones)
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
