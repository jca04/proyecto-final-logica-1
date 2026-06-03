
import numpy as np
from clases.producto import Producto   # import de angel

from clases.citas import Citas


TAM = 20 #ejemplo
class Veterinaria:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self._citas = Citas()
        

        # atributos agregados por angel:
        self._productos     = np.full(TAM, fill_value=None, dtype=object)
        self._num_productos = 0
        
        #Atributos Alejo
        self.__clients = np.full(TAM, fill_value=None, dtype=Client)
        self.__nroClients = 0
    
    def mostrar_informacion(self):
        print(f"Veterinaria: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")

    # métodos angel:

# pidiendo lso datos del producto al usuario creando el objeto y guardandolo en el arreglo de productos:
    def crear_producto(self):
        if self._num_productos == TAM:
            print("No hay espacio para más productos.")
            return

        print("\n--- REGISTRAR PRODUCTO ---")
        pid       = input("ID del producto: ")
        nombre    = input("Nombre: ")
        cantidad  = int(input("Cantidad inicial: "))
        precio    = float(input("Precio unitario: "))
        categoria = input("Categoría (ej: vacuna, antibiótico): ")
        stock_min = int(input("Stock mínimo de alerta: "))

        nuevo = Producto(pid, nombre, cantidad, precio, categoria, stock_min)
        self._productos[self._num_productos] = nuevo
        self._num_productos = self._num_productos + 1
        print(f"Producto '{nombre}' registrado correctamente.")

    # para actualizar el stock busco por id si esta agg cantidad y mostrar nuevo stock si no esta pues error
    def actualizar_stock(self):
        print("\n--- ACTUALIZAR STOCK ---")
        pid = input("Ingrese el ID del producto: ")

        pos = -1
        for i in range(self._num_productos):
            if self._productos[i].producto_id == pid:
                pos = i

        if pos == -1:
            print("Producto no encontrado.")
        else:
            print(f"Producto encontrado: {self._productos[pos].nombre}")
            print(f"Stock actual: {self._productos[pos].cantidad} unidades")
            cambio = int(input("¿Cuántas unidades agregar (+) o restar (-)? "))
            self._productos[pos].actualizar_stock(cambio)
            print(f"Stock actualizado. Nuevo stock: {self._productos[pos].cantidad} unidades")

    # pillar cuales son los productos de poco stock y mostrar alerta pa estar pendientes
    def productos_bajo_stock(self):
        print("\n--- PRODUCTOS CON POCO STOCK ---")
        encontrados = 0
        for i in range(self._num_productos):
            if self._productos[i].tiene_poco_stock():
                self._productos[i].mostrar()
                print("  STOCK BAJO")
                print("-" * 30)
                encontrados = encontrados + 1

        if encontrados == 0:
            print("Todos los productos tienen stock suficiente.")

# mostrar el inventario completo con sus detalles
    def ver_productos(self):
        print("\n--- INVENTARIO COMPLETO ---")
        if self._num_productos == 0:
            print("No hay productos registrados.")
            return

        for i in range(self._num_productos):
            print(f"\nProducto #{i + 1}")
            self._productos[i].mostrar()
            print("-" * 30)
            
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
            print(f"\n La mascota del cliente {cliente.name}:")
            for i in range(0, cliente.nroPets, 1):
                pet = cliente.pets[i]
                print(f"  - {pet.petName} ({pet.species}, {pet.age} años)")
    
