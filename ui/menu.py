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

        while True:

            print("\n============= MENÚ CLIENTES =============")
            print("1. Registrar cliente")
            print("2. Consultar clientes")
            print("3. Volver")

            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Debe ingresar un número.")
                continue

            if opcion == 1:
                nombre = input("Nombre del cliente: ")
                telefono = input("Teléfono: ")
                cedula = input("Cédula: ")

                self.veterinaria.registrar_cliente(
                    nombre,
                    telefono,
                    cedula
                )

            elif opcion == 2:
                self.veterinaria.listar_clientes()

            elif opcion == 3:
                break

            else:
                print("Opción no válida.")

    def __menu_mascotas(self):

        while True:

            print("\n============= MENÚ MASCOTAS =============")
            print("1. Registrar mascota")
            print("2. Listar mascotas de un cliente")
            print("3. Volver")

            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Debe ingresar un número.")
                continue

            if opcion == 1:

                self.veterinaria.listar_clientes()

                cliente_id = int(input("ID del cliente: "))
                nombre = input("Nombre de la mascota: ")
                especie = input("Especie: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))

                self.veterinaria.registrar_mascota(
                    cliente_id,
                    nombre,
                    especie,
                    raza,
                    edad
                )

            elif opcion == 2:

                self.veterinaria.listar_clientes()

                cliente_id = int(input("ID del cliente: "))

                self.veterinaria.listar_mascotas(cliente_id)

            elif opcion == 3:

                print("Volviendo al menú principal...")
                break

            else:
                print("Opción no válida.")   

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

                    cliente = self.veterinaria.consultar_cliente(None, cedula_cliente) # -> esto deberia retornar un diccionario con la información del cliente incluyendo su id si no existe retornar None
                    if cliente is None:
                        print("Cliente no encontrado. Procediendo a registrar nuevo cliente.")
                        nombre_cliente = input("Ingrese el nombre del cliente: ")
                        telefono_cliente = input("Ingrese el teléfono del cliente: ")

                        cliente = self.veterinaria.registrar_cliente(nombre_cliente, telefono_cliente, cedula_cliente)

                    print("\n --- Identificación de la mascota ---")

                    if cliente is not None:
                        self.veterinaria.listar_mascotas(cliente.cliente_id) # -> esto deberia mostrar por pantalla en una lista las mascotas del cliente respectivo con su id, nombre, especie y raza

                    while True:
                        opcion_mascota = input("\n¿La mascota para la cita ya está registrada? (s/n): ").lower()
                        if opcion_mascota in ["s", "n"]:
                            break
                        else:
                            print("Opción no válida. Por favor, ingrese 's' para sí o 'n' para no.")

                    if opcion_mascota == "s":
                        mascota_id = int(input("Ingrese el ID  de la mascota que asistirá a la cita: "))
                    else:
                        print(f"\nRegistrando nueva mascota para el cliente {cliente.nombre if cliente is not None else 'desconocido'}:")
                        nombre_mascota = input("Nombre de la mascota: ")
                        edad_mascota = int(input("Edad de la mascota: "))
                        especie_mascota = input("Especie (Perro, Gato, etc.): ")
                        raza_mascota = input("Raza: ")

                        if cliente is not None:
                            nueva_mascota = self.veterinaria.registrar_mascota(
                                cliente.cliente_id, nombre_mascota, especie_mascota, raza_mascota, edad_mascota
                            )

                            if nueva_mascota is not None:
                                mascota_id = nueva_mascota.mascota_id   

                    print("\n--- Datos de la cita ---")
                    fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
                    hora = input("Ingrese la hora de la cita (HH:MM): ")
                    motivo = input("Ingrese el motivo de la cita: ")
                    especialidad = input("Ingrese la especialidad requerida: ").lower()

                    if mascota_id is None:
                        print("No se pudo identificar la mascota para la cita. Por favor, intente nuevamente.")
                        continue

                    cita = self.veterinaria.crear_cita(fecha, hora, motivo, especialidad, mascota_id)

                    if cita is not None:
                        print("\n¡Cita agendada con éxito! Detalles de la cita:")
                        print(f"\nFecha: {cita.fecha}")
                        print(f"Hora: {cita.hora}")
                        print(f"Motivo: {cita.motivo}")
                        print(f"Especialidad: {cita.especialidad}")

                case "2":
                        print("\n--- Ver citas de una mascota ---")
                        self.veterinaria.listar_mascotas_completo()

                        mascota_id = int(input("\nIngrese el ID de la mascota para ver sus citas: "))

                        self.veterinaria.listar_citas_de_mascota(mascota_id)
                
                case "3":
                    
                    print("\n--- Cancelar una cita ---")
                    cedula_cliente = int(input("Ingrese la cédula del cliente: "))

                    cliente = self.veterinaria.consultar_cliente(cedula=cedula_cliente)

                    if not cliente:
                        print("Cliente no encontrado.")
                        return
                    
                    cliente.listar_mascotas(cliente.cliente_id)

                    mascota_id = int(input("\nIngrese el ID de la mascota para ver sus citas: "))

                    self.veterinaria.listar_citas_de_mascota(mascota_id)

                    cita_id = int(input("\nIngrese el ID de la cita que desea cancelar: "))

                    self.veterinaria.cancelar_cita(cita_id)
                    print("\nCita cancelada con éxito.")

                case "4":

                    print("\n--- Crear registro médico para una cita ---")

                    self.veterinaria.listar_mascotas_completo()
                    
                    mascota_id = int(input("\nIngrese el ID de la mascota para crear un registro médico: "))

                    diagnostico = input("\nIngrese el diagnóstico: ")
                    tratamiento = input("Ingrese el tratamiento recomendado: ")
                    observaciones = input("Ingrese cualquier observación adicional: ")

                    self.veterinaria.crear_registro_medico(mascota_id, diagnostico, tratamiento, observaciones)

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
                    self.veterinaria.crear_producto()

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
