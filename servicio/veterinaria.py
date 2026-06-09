import numpy as np
import csv
from clases.cliente import Cliente
from clases.mascota import Mascota
from clases.producto import Producto   # import de angel
from clases.citas import Citas
from clases.veterinario import Veterinario
from utils.citas import existe_cita_para_mascota, obtener_veterinarios_disponibles
from utils.obtener_bd import get_file_path

class Veterinaria:


    def __init__(self, nombre, direccion, telefono):

        self.__TAM = 200 # tamaño que vamos a usar para llenar los arreglos

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
        self.__cargar_citas()
        self.__cargar_productos() 
        self.__cargar_veterinarios()

    
    def __cargar_clientes(self):
        with open(get_file_path("clientes.csv"), "r") as f:
            lector = csv.DictReader(f)
            for linea in lector:
                c = Cliente(
                    int(linea["cliente_id"]),
                    linea["nombre"],
                    linea["telefono"],
                    linea["cedula"]
                )
                self.__clientes[self.__nroClientes] = c
                self.__nroClientes += 1

    def __cargar_citas(self):
        with open(get_file_path("citas.csv"), "r") as f:
            lector = csv.DictReader(f)
            for linea in lector:
                ci = Citas(
                    int(linea["mascota_id"]),
                    int(linea["vet_id"]),
                    linea["fecha"],
                    linea["hora"],
                    linea["motivo"],
                    linea["estado"],
                )
                self.__citas[self.__nroCitas] = ci
                self.__nroCitas += 1
    
    def __cargar_veterinarios(self):
        with open(get_file_path("veterinarios.csv"), "r") as f:
            lector = csv.DictReader(f)
            for linea in lector:
                v = Veterinario(
                    int(linea["vet_id"]),
                    linea["nombre"],
                    linea["telefono"],
                    linea["especialidad"]
                )
                self.__veterinarios[self.__nroVeterinarios] = v
                self.__nroVeterinarios += 1

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

#--- metodos productos

    def __cargar_productos(self):
        with open(get_file_path("productos.csv"), "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                p = Producto(
                    int(fila["producto_id"]),
                    fila["nombre"],
                    int(fila["cantidad"]),
                    float(fila["precio"]),
                    fila["categoria"],
                    int(fila["stock_minimo"])
                )
                self.__productos[self.__nroProductos] = p
                self.__nroProductos += 1
    
    def __siguiente_id_producto(self):
        if self.__nroProductos == 0:
            return 1

        ids = np.array([], dtype=int)

        for p in self.__productos[:self.__nroProductos]:
            ids = np.append(ids, int(p.producto_id))

        return max(ids) + 1
    
    def __guardar_productos(self):
        ruta = get_file_path("productos.csv")

        with open(ruta, "w", newline="", encoding="utf-8") as f:
            campos = ["producto_id", "nombre", "cantidad", "precio", "categoria", "stock_minimo"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()

            for p in self.__productos[:self.__nroProductos]:
                escritor.writerow({
                    "producto_id":  p.producto_id,
                    "nombre":       p.nombre,
                    "cantidad":     p.cantidad,
                    "precio":       p.precio,
                    "categoria":    p.categoria,
                    "stock_minimo": p.stock_minimo
                })


    def crear_producto(self):
        if self.__nroProductos == self.__TAM:
            print("No hay espacio para más productos.")
            return

        print("\nREGISTRAR PRODUCTO")
        nombre      = input("Nombre: ")
        cantidad    = int(input("Cantidad inicial: "))
        precio      = float(input("Precio unitario: "))
        categoria   = input("Categoría: ")
        stock_min   = int(input("stock mínimo: "))

        producto_id = self.__siguiente_id_producto()

        nuevo = Producto(producto_id, nombre, cantidad, precio, categoria, stock_min)
        self.__productos[self.__nroProductos] = nuevo
        self.__nroProductos += 1

        self.__guardar_productos()
        print(f"Producto '{nombre}' registrado con ID {producto_id}.")


    def actualizar_stock(self):
        print("\nACTUALIZAR STOCK")
        id_buscar = int(input("ingrese el ID del producto: "))

        pos = -1
        for i in range(self.__nroProductos):
            if self.__productos[i].producto_id == id_buscar:
                pos = i

        if pos == -1:
            print("producto no encontrado.")
            return

        print(f"Producto: {self.__productos[pos].nombre}")
        print(f"Stock actual: {self.__productos[pos].cantidad}")
        cambio = int(input("cantidad a sumar (+) o restar (-): "))
        self.__productos[pos].actualizar_stock(cambio)

        self.__guardar_productos()
        print(f"stock actualizado. Nuevo stock: {self.__productos[pos].cantidad}")

    def productos_bajo_stock(self):
        print("\nPRODUCTOS CON POCO STOCK")
        encontrados = 0

        for i in range(self.__nroProductos):
            if self.__productos[i].tiene_poco_stock():
                self.__productos[i].mostrar()
                print("  Stock bajo")
                print("-" * 30)
                encontrados += 1

        if encontrados == 0:
            print("todos los productos tienen stock suficiente.")

    def ver_productos(self):
        print("\nINVENTARIO COMPLETO")

        if self.__nroProductos == 0:
            print("no hay productos registrados.")
            return

        for i in range(self.__nroProductos):
            print(f"\nProducto #{i + 1}")
            self.__productos[i].mostrar()
            print("-" * 30)
                
#fin metodos productos-----------------------------------------------------------------------------------------------

#Métodos Alejo
    def registrar_cliente(self, nombre: str, telefono: str, cedula: str) -> Cliente | None:

        clientes = self.__clientes[:self.__nroClientes] # aqui obtengo solo los clientes que ya están registrados, no todo el arreglo

        for cliente in clientes:
            if cliente.cedula == cedula:
                print("El cliente ya está registrado.")
                return
        
        cliente_id = self.__siguiente_id_cliente()
        self.__clientes[self.__nroClientes] = Cliente(cliente_id, nombre, telefono, cedula)
        self.__nroClientes = self.__nroClientes + 1
        self.__guardar_clientes()

        print(f"El cliente {nombre} ha sido registrado con éxito.")

        return self.__clientes[self.__nroClientes - 1] # retorno el cliente que acabo de registrar

        # if self.__nroClientes < len(self.__clientes):
        #     self.__clientes[self.__nroClientes] = Cliente(cliente_id, nombre, telefono, cedula)
        #     self.__nroClientes = self.__nroClientes + 1
        #     print(f"El cliente {nombre} ha sido registrado con éxito.")
        # else:
        #    print("No hay espacio para más clientes.")

    def consultar_cliente(self, cliente_id = None, cedula = None) -> Cliente | None:
        for i in range(0, self.__nroClientes, 1):
            if cliente_id is not None and self.__clientes[i].cliente_id == cliente_id:
                return self.__clientes[i]

            if cedula is not None and self.__clientes[i].cedula == cedula:
                return self.__clientes[i]
            
        return None

    def registrar_mascota(self, cliente_id: int, nombre: str, especie: str, raza: str, edad: int) -> Mascota | None:
        cliente = self.consultar_cliente(cliente_id)
        if cliente is None:
            print(f"El cliente con id {cliente_id} no está registrado.")
        else:
            cliente.agregarMascota(nombre, especie, raza, edad, cliente_id)
            print(f"\nLa mascota {nombre} se registro al cliente {cliente.nombre}.")

            return cliente.mascotas[cliente.nroMascotas - 1] # retorno la mascota que acabo de registrar

    def listar_mascotas(self, cliente_id: int):
        cliente = self.consultar_cliente(cliente_id)
        if cliente is None:
            print(f"El cliente con id {cliente_id} no está registrado.")
        else:
            print(f"\nMascotas de {cliente.nombre}:")
            cliente.listar_mascotas(cliente_id)

    def __guardar_clientes(self):
        with open(get_file_path("clientes.csv"), mode="w") as f:
            campos = ["cliente_id", "nombre", "telefono", "cedula"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()

            for c in self.__clientes[:self.__nroClientes]:
                escritor.writerow({
                    "cliente_id": c.cliente_id,
                    "nombre": c.nombre,
                    "telefono": c.telefono,
                    "cedula": c.cedula
                })
    

    ## Metodos para las citas

    def consultar_veterinario(self, vet_id: int) -> Veterinario | None:
        for i in range(0, self.__nroVeterinarios, 1):
            if self.__veterinarios[i].vet_id == vet_id:
                return self.__veterinarios[i]
            
        return None


    def crear_cita(self, fecha, hora, motivo, especialidad, mascota_id) -> Citas | None:
        
        citas_activas = self.__citas[:self.__nroCitas] # aqui obtengo solo las citas que ya están registradas, no todo el arreglo

        cita_duplicada = False

        for c in citas_activas:
            if c.mascota_id == mascota_id and c.fecha == fecha and c.hora == hora:
                cita_duplicada = True
                break

        if cita_duplicada:
            print("\nLa mascota ya tiene una cita agendada en ese horario.")
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
        self.__citas[self.__nroCitas] = Citas(mascota_id, veterinario_asignado.vet_id, fecha, hora, motivo, especialidad, "agendada", cita_id)
        self.__nroCitas = self.__nroCitas + 1
        self.__guardar_citas()

        return self.__citas[self.__nroCitas - 1] # retorno la cita que acabo de registrar y el veterinario asignado a esa cita

    
    def listar_citas_mascota(self, mascota_id: int):
        citas_activas = self.__citas[:self.__nroCitas]

        print(f"\nCitas agendadas para la mascota con ID {mascota_id}:")

        for c in citas_activas:
            if c.mascota_id == mascota_id:
                print(f"\nFecha: {c.fecha}")
                print(f"Hora: {c.hora}")
                print(f"Motivo: {c.motivo}")
                print(f"Especialidad: {c.especialidad}")
                vet = self.consultar_veterinario(c.vet_id)
                if vet is not None:
                    print(f"Veterinario asignado: {vet.nombre}")
                print("-" * 30)


    def __guardar_citas(self):
        with open(get_file_path("citas.csv"), "w") as f:
            campos = ["cita_id", "fecha", "hora", "motivo", "estado", "mascota_id", "vet_id"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            
            for c in self.__citas[:self.__nroCitas]:
                escritor.writerow({
                    "cita_id": c.cita_id,
                    "fecha": c.fecha,
                    "hora": c.hora,
                    "motivo": c.motivo,
                    "estado": c.estado,
                    "mascota_id": c.mascota_id,
                    "vet_id": c.vet_id
                })
    
