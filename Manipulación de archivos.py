import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos.append(Producto(int(id), nombre, int(cantidad), float(precio)))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo al añadir productos.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        self.productos.append(producto)
        self.guardar_inventario()
        print(f"Producto '{producto.nombre}' añadido exitosamente.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                print(f"Producto ID {id} actualizado exitosamente.")
                return
        print(f"Producto ID {id} no encontrado.")

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.id != id]
        self.guardar_inventario()
        print(f"Producto ID {id} eliminado exitosamente.")

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

def main():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Listar Productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            inventario.añadir_producto(Producto(id, nombre, cantidad, precio))

        elif opcion == '2':
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '3':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == '4':
            inventario.listar_productos()

        elif opcion == '5':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()