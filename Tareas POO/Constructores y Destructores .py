class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.
        Inicializa el nombre del archivo y abre el archivo en modo escritura.
        """
        self.nombre = nombre
        print(f"[INFO] Creando y abriendo el archivo '{self.nombre}' para escritura.")
        self.archivo = open(self.nombre, 'w')

    def escribir(self, contenido):
        """
        Escribe contenido en el archivo.
        """
        print(f"[INFO] Escribiendo en el archivo '{self.nombre}'.")
        self.archivo.write(contenido + '\n')

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Cierra el archivo al eliminar el objeto.
        """
        if hasattr(self, 'archivo') and not self.archivo.closed:
            print(f"[INFO] Cerrando el archivo '{self.nombre}'.")
            self.archivo.close()


# Uso de la clase Archivo
def main():
    # Crear un objeto de la clase Archivo
    archivo = Archivo("ejemplo.txt")

    # Escribir contenido en el archivo
    archivo.escribir("Primera línea de texto.")
    archivo.escribir("Segunda línea de texto.")


# Llamar a la función principal
if __name__ == "__main__":
    main()

# El destructor (__del__) se ejecutará automáticamente al finalizar el programa
# o al eliminar el objeto archivo.
