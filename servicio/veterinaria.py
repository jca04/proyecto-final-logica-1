import numpy as np
from clases.cliente import Cliente
from clases.producto import Producto   # import de angel
from clases.citas import Citas
from clases.veterinario import Veterinario
from utils.citas import existe_cita_para_mascota, obtener_veterinarios_disponibles
from utils.obtener_bd import get_file_path

class Veterinaria:

    __TAM = 200 # tamaño que vamos a usar para llenar los arreglos


    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

        self.__clientes = np.full(self.__TAM, fill_value=None, dtype=Cliente)
        self.__nroClientes = 0

        self.__citas = np.full(self.__TAM, fill_value=None, dtype=Citas)
        self.__nroCitas = 0

        self.__productos = np.full(self.__TAM, fill_value=None, dtype=Producto)
        self.__nroProductos = 0

        self.__veterinarios = np.full(self.__TAM, fill_value=None, dtype=Veterinario)
        self.__nroVeterinarios = 0

        self.__cargar_todo()

    def mostrar_informacion(self):
        print(f"Veterinaria: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")

    def __cargar_todo(self):
        self.__cargar_clientes()
        #self.__cargar_mascotas()    # depende de que clientes ya estén cargados
        #self.__cargar_registros()   # depende de que mascotas ya estén cargadas
        self.__cargar_citas()
        #self.__cargar_productos() # pendiente

    
    def __cargar_clientes(self):
        with open(get_file_path("clientes.csv"), "r") as f:
            for linea in f:
                cliente_id, nombre, telefono, cedula = linea.strip().split(",")
                self.__clientes[self.__nroClientes] = Cliente(cliente_id, nombre, telefono, cedula)
                self.__nroClientes += 1

    def __cargar_citas(self):
        with open(get_file_path("citas.csv"), "r") as f:
            for linea in f:
                cita_id, fecha, hora, motivo, estado, mascota_id, vet_id = linea.strip().split(",")
                self.__citas[self.__nroCitas] = Citas(mascota_id, vet_id, fecha, hora, motivo, estado, cita_id)
                self.__nroCitas += 1

    ## generación y validacion de ids para no pisar ninguno existente, se tendria que hacer por cada clase


    # esta logica se repetiria para validar y generar cada id
    def __siguiente_id_cliente(self):
        if self.__nroClientes == 0:
            return 1
        
        ids = np.array([], dtype=int)

        for c in self.__clientes[:self.__nroClientes]:
            ids = np.append(ids, int(c.cliente_id))

        return max(ids) + 1
    
    def __siguiente_id_cita(self):
        if self.__nroCitas == 0:
            return 1
        
        ids = np.array([], dtype=int)

        for c in self.__citas[:self.__nroCitas]:
            ids = np.append(ids, int(c.cita_id))

        return max(ids) + 1


    def crear_producto(self, nombre, cantidad, precio, categoria, stock_minimo):
        return self.__producto.registrar_producto(nombre, cantidad, precio, categoria, stock_minimo)

    def ver_productos(self):
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
    

    ## Metodos para las citas
    def crear_cita(self, fecha, hora, motivo, especialidad, mascota_id):
        
        citas_activas = self.__citas[:self.__nroCitas] # aqui obtengo solo las citas que ya están registradas, no todo el arreglo

        cita_duplicada = False

        for c in citas_activas:
            if c.mascota_id == mascota_id and c.fecha == fecha and c.hora == hora:
                cita_duplicada = True
                break

        if cita_duplicada:
            print("La mascota ya tiene una cita agendada en ese horario.")
            return
        
        veterinarios_activos = self.__veterinarios[:self.__nroVeterinarios]

        veterinarios_disponibles = np.array([], dtype=Veterinario)

        for v in veterinarios_activos:
            disponible = True

            for c in citas_activas:
                if c.vet_id == v.vet_id and c.fecha == fecha and c.hora == hora:
                    disponible = False
                    break

            if disponible and v.especialidad.lower() == especialidad.lower():
                veterinarios_disponibles = np.append(veterinarios_disponibles, v)

        if len(veterinarios_disponibles) == 0:
            print("No hay veterinarios disponibles en ese horario para la especialidad seleccionada.")
            return
        
        veterinario_asignado = veterinarios_disponibles[0]

        cita_id = self.__siguiente_id_cita()
        self.__citas[self.__nroCitas] = Citas(mascota_id, veterinario_asignado.veterinario_id, fecha, hora, motivo, "agendada", cita_id)
        self.__nroCitas = self.__nroCitas + 1
        self.__guardar_citas()

    
    def __guardar_citas(self):
        with open(get_file_path("citas.csv"), "w") as f:
            for c in self.__citas[:self.__nroCitas]:
                f.write(f"{c.cita_id},{c.fecha},{c.hora},{c.motivo},{c.estado},{c.mascota_id},{c.vet_id}\n")
    
