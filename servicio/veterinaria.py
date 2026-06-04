
from clases.cliente import Client
from clases.producto import Producto   # import de angel
from clases.citas import Citas
import csv
import os
from utils.obtener_bd import get_file_path

class Veterinaria:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"Veterinaria: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")

    def __asegurar_archivo_productos(self):
        ruta = get_file_path("productos.csv")

        if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
            with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([
                    "producto_id",
                    "nombre",
                    "cantidad",
                    "precio",
                    "categoria",
                    "stock_minimo"
                ])

    def crear_producto(self):
        self.__asegurar_archivo_productos()
        ruta = get_file_path("productos.csv")

        print("\n--- REGISTRAR PRODUCTO ---")
        producto_id = input("ID del producto: ")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad inicial: "))
        precio = float(input("Precio unitario: "))
        categoria = input("Categoría: ")
        stock_minimo = int(input("Stock mínimo: "))

        with open(ruta, mode="a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([
                producto_id,
                nombre,
                cantidad,
                precio,
                categoria,
                stock_minimo
            ])

        print("Producto registrado correctamente.")

    def ver_productos(self):
        self.__asegurar_archivo_productos()
        ruta = get_file_path("productos.csv")

        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            productos = list(lector)

        if len(productos) == 0:
            print("No hay productos registrados.")
            return

        print("\n--- INVENTARIO COMPLETO ---")
        for producto in productos:
            print(f"ID: {producto['producto_id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Stock mínimo: {producto['stock_minimo']}")
            print("-" * 30)

    def productos_bajo_stock(self):
        self.__asegurar_archivo_productos()
        ruta = get_file_path("productos.csv")

        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            productos = list(lector)

        encontrados = 0
        print("\n--- PRODUCTOS CON POCO STOCK ---")

        for producto in productos:
            cantidad = int(producto["cantidad"])
            stock_minimo = int(producto["stock_minimo"])

            if cantidad <= stock_minimo:
                print(f"ID: {producto['producto_id']}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Stock mínimo: {producto['stock_minimo']}")
                print("-" * 30)
                encontrados = encontrados + 1

        if encontrados == 0:
            print("No hay productos con poco stock.")

    def actualizar_stock(self):
        self.__asegurar_archivo_productos()
        ruta = get_file_path("productos.csv")

        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            productos = list(lector)

        producto_id_buscar = input("Ingrese el ID del producto a actualizar: ")
        encontrado = False

        for producto in productos:
            if producto["producto_id"] == producto_id_buscar:
                print(f"Producto encontrado: {producto['nombre']}")
                print(f"Stock actual: {producto['cantidad']}")

                cambio = int(input("Ingrese la cantidad a sumar (+) o restar (-): "))
                nueva_cantidad = int(producto["cantidad"]) + cambio
                producto["cantidad"] = str(nueva_cantidad)

                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado.")
            return

        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            campos = [
                "producto_id",
                "nombre",
                "cantidad",
                "precio",
                "categoria",
                "stock_minimo"
            ]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(productos)

        print("Stock actualizado correctamente.")
            

#Métodos Alejo
    def registrar_cliente(self, name, phone):
        if self.__nroClients < len(self.__clients):
            self.__clients[self.__nroClients] = Client(name, phone)
            self.__nroClients = self.__nroClients + 1
            print(f"El cliente {name} ha sido registrado con éxito.")
        else:
            print("No hay espacio para más clientes.")

    def consultar_cliente(self, name):
        for i in range(0, self.__nroClients, 1):
            if self.__clients[i].name == name:
                return i
        return -1

    def registrar_mascota(self, name, namePet, species, age):
        indice = self.consultar_cliente(name)
        if indice == -1:
            print(f"El cliente {name} no está registrado")
        else:
            self.__clients[indice].agregar_mascota(namePet, species, age)
            print(f"La mascota llamada {namePet} está asociada a {name}.")

    def listar_mascotas(self, name):
        indice = self.consultar_cliente(name)
        if indice == -1:
            print(f"El cliente {name} no está registrado")
        else:
            cliente = self.__clients[indice]
            print(f"\n Mascotas de {cliente.name}:")
            for i in range(0, cliente.nroPets, 1):
                pet = cliente.pets[i]
                print(f"  - {pet.petName} ({pet.species}, {pet.age} años)")
    
