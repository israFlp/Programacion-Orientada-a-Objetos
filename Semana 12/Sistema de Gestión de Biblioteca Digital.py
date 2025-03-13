# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para almacenar título y autor, ya que son inmutables
        self.datos = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn  # ISBN como identificador único

    def __str__(self):
        return f"Libro: {self.datos[0]} | Autor: {self.datos[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario  # ID único del usuario
        self.libros_prestados = []  # Lista de libros prestados al usuario

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario} | Libros Prestados: {len(self.libros_prestados)}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para almacenar libros (clave: ISBN)
        self.usuarios_registrados = set()  # Conjunto para IDs de usuarios únicos
        self.prestamos = {}  # Diccionario para gestionar préstamos (clave: ID de usuario, valor: lista de libros prestados)

    # Añadir un libro a la biblioteca
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.datos[0]}' añadido correctamente.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    # Quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado correctamente.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")

    # Registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.prestamos[usuario.id_usuario] = []  # Inicializar lista de préstamos
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    # Dar de baja a un usuario
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.prestamos[id_usuario]  # Eliminar préstamos asociados
            print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    # Prestar un libro a un usuario
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        elif isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
        else:
            libro = self.libros_disponibles[isbn]
            self.prestamos[id_usuario].append(libro)
            del self.libros_disponibles[isbn]  # Eliminar libro de disponibles
            print(f"Libro '{libro.datos[0]}' prestado a {id_usuario}.")

    # Devolver un libro a la biblioteca
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
        else:
            for libro in self.prestamos[id_usuario]:
                if libro.isbn == isbn:
                    self.prestamos[id_usuario].remove(libro)
                    self.libros_disponibles[isbn] = libro  # Añadir libro de nuevo a disponibles
                    print(f"Libro '{libro.datos[0]}' devuelto correctamente.")
                    return
            print(f"El libro con ISBN {isbn} no fue prestado a este usuario.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.datos[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.datos[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # Listar libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.prestamos:
            return self.prestamos[id_usuario]
        else:
            return []


# Pruebas del sistema
if __name__ == "__main__":
    # Crear una biblioteca
    biblioteca = Biblioteca()

    # Añadir libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "9788437604947")
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "9780451524935")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("Ana Gómez", "002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("001", "9788437604947")  # Prestar "Cien años de soledad" a Juan
    biblioteca.prestar_libro("002", "9780451524935")  # Prestar "1984" a Ana

    # Buscar libros
    print("\nBúsqueda por título '1984':")
    for libro in biblioteca.buscar_libros("titulo", "1984"):
        print(libro)

    # Listar libros prestados a un usuario
    print("\nLibros prestados a Juan Pérez:")
    for libro in biblioteca.listar_libros_prestados("001"):
        print(libro)

    # Devolver un libro
    biblioteca.devolver_libro("001", "9788437604947")

    # Dar de baja a un usuario
    biblioteca.dar_de_baja_usuario("002")