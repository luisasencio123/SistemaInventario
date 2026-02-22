import os

# ==============================
# Clase Producto
# ==============================
class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para convertir el objeto en línea de texto
    def to_line(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}\n"

    # Método para mostrar producto
    def __str__(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


# ==============================
# Clase Inventario
# ==============================
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    # ------------------------------------
    # Cargar inventario desde archivo
    # ------------------------------------
    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    
                    # Verifica que la línea tenga datos válidos
                    if len(datos) == 4:
                        codigo, nombre, cantidad, precio = datos
                        self.productos[codigo] = Producto(
                            codigo, nombre, int(cantidad), float(precio)
                        )
            print("Inventario cargado correctamente.")

        except FileNotFoundError:
            # Si no existe el archivo, lo crea vacío
            print("Archivo no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()

        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

        except Exception as e:
            print("Error inesperado al cargar inventario:", e)

    # ------------------------------------
    # Guardar inventario en archivo
    # ------------------------------------
    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(producto.to_line())
            print("Inventario guardado correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print("Error inesperado al guardar inventario:", e)

    # ------------------------------------
    # Añadir producto
    # ------------------------------------
    def añadir_producto(self, codigo, nombre, cantidad, precio):
        if codigo in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[codigo] = Producto(codigo, nombre, cantidad, precio)
            self.guardar_inventario()
            print("Producto añadido exitosamente.")

    # ------------------------------------
    # Actualizar producto
    # ------------------------------------
    def actualizar_producto(self, codigo, cantidad, precio):
        if codigo in self.productos:
            self.productos[codigo].cantidad = cantidad
            self.productos[codigo].precio = precio
            self.guardar_inventario()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    # ------------------------------------
    # Eliminar producto
    # ------------------------------------
    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # ------------------------------------
    # Mostrar productos
    # ------------------------------------
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


# ==============================
# Interfaz de Usuario
# ==============================
def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(codigo, nombre, cantidad, precio)

            elif opcion == "2":
                codigo = input("Código del producto: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(codigo, cantidad, precio)

            elif opcion == "3":
                codigo = input("Código del producto a eliminar: ")
                inventario.eliminar_producto(codigo)

            elif opcion == "4":
                inventario.mostrar_productos()

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Debe ingresar valores numéricos válidos.")

        except Exception as e:
            print("Error inesperado:", e)


# Ejecutar programa
if __name__ == "__main__":
    menu()