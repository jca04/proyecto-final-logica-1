from servicio.veterinaria import Veterinaria

class Menu:
    def __init__(self):
        self.veterinaria = Veterinaria("Veterinaria", "Calle 123", "1234")

    
    def mostrar_menu(self):

        while True:
            
            print("\n ============== Bienvenido a la Veterinaria =============")
            print("1. Menú de Clientes")
            print("2. Menú de Mascotas")
            print("3. Menú de Citas")
            print("4. Menú de Productos")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            match opcion:

                case "1":
                    self.__menu_clientes()

                case "2":
                    self.__menu_mascotas()
                
                case "3":
                    self.__menu_citas()
                
                case "4":
                    self.__menu_productos()

                case "0":
                    print("Saliendo del sistemas...")
                    break
                    
                case _:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
     
    def __menu_clientes(self):
        print("Menú de Clientes")
        print("Funcionalidad en desarrollo.")

    def __menu_mascotas(self):
        print("Menú de Mascotas")
        print("Funcionalidad en desarrollo.")       

    def __menu_citas(self):
        
        while True:
            print("\n============= Menú de Citas =============")
            print("1. Crear cita")
            print("2. Ver citas")
            print("3. Cancelar cita")
            print("4. Crear Registro medico")
            print("0. Volver al menú principal")

            opcion = input("\nSeleccione una opción: ")

            match opcion:
                
                case "1":

                    print("\n--- Identificación del cliente ---")
                    cedula_cliente = input("Ingrese la cédula del cliente: ")

                    cliente = self.veterinaria.buscar_cliente(cedula_cliente) # -> esto deberia retornar un diccionario con la información del cliente incluyendo su id si no existe retornar None
                    if not cliente:
                        print("Cliente no encontrado. Procediendo a registrar nuevo cliente.")
                        nombre_cliente = input("Ingrese el nombre del cliente: ")
                        telefono_cliente = input("Ingrese el teléfono del cliente: ")

                        cliente = self.veterinaria.registrar_cliente(nombre_cliente, cedula_cliente, telefono_cliente)

                    print("\n --- Identificación de la mascota ---")

                    cliente.mostrar_mascotas_de_cliente(cliente["cliente_id"]) # -> esto deberia mostrar por pantalla en una lista las mascotas del cliente respectivo con su id, nombre, especie y raza

                    opcion_mascota = input("¿La mascota para la cita ya está registrada? (s/n): ").lower()

                    if opcion_mascota == "s":
                        mascota_id = int(input("Ingrese el ID  de la mascota que asistirá a la cita: "))
                    else:
                        print("\nRegistrando nueva mascota para este cliente:")
                        nombre_mascota = input("Nombre de la mascota: ")
                        edad_mascota = input("Edad de la mascota: ")
                        especie_mascota = input("Especie (Perro, Gato, etc.): ")
                        raza_mascota = input("Raza: ")

                        mascota_id = self.veterinaria.registrar_mascota(
                            nombre_mascota, edad_mascota, especie_mascota, raza_mascota, cliente["cliente_id"]
                        )

                    print("\n--- Datos de la cita ---")
                    fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
                    hora = input("Ingrese la hora de la cita (HH:MM): ")
                    motivo = input("Ingrese el motivo de la cita: ")
                    especialidad = input("Ingrese la especialidad requerida: ").lower()

                    cita = self.veterinaria.crear_cita(fecha, hora, motivo, especialidad, mascota_id)

                    print("\n¡Cita agendada con éxito!")
                    print(cita)

                case "2":
                    pass
                
                case "3":
                    pass

                case "4":
                    pass

                case "0":
                    break

                case _:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
    
    # menu de producto Angel
    def __menu_productos(self):
        while True:
            print("\n============= Menú de Productos =============")
            print("1. Agregar producto")
            print("2. Actualizar stock")
            print("3. Ver productos con poco stock")
            print("4. Ver todos los productos")
            print("0. Volver al menú principal")

            opcion = input("\nSeleccione una opción: ")

            match opcion:
                case "1":

                    print("\n--- REGISTRAR PRODUCTO ---")
                    nombre = input("Nombre: ")
                    cantidad = int(input("Cantidad inicial: "))
                    precio = float(input("Precio unitario: "))
                    categoria = input("Categoría: ")
                    stock_minimo = int(input("Stock mínimo: "))


                    respuesta = self.veterinaria.crear_producto(nombre, cantidad, precio, categoria, stock_minimo)
                    print(respuesta)

                case "2":
                    self.veterinaria.actualizar_stock()

                case "3":
                    self.veterinaria.productos_bajo_stock()

                case "4":
                    self.veterinaria.ver_productos()

                case "0":
                    break

                case _:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")