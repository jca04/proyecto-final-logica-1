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

    def __menu_mascotas(self):
        print("Menú de Mascotas")

    def __menu_citas(self):
        
        while True:
            print("\n============= Menú de Citas =============")
            print("1. Crear cita")
            print("2. Ver citas")
            print("3. Cancelar cita")
            print("0. Volver al menú principal")

            print("\n")

            opcion = input("Seleccione una opción: ")

            print("\n")

            match opcion:
                
                case "1":
                    fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
                    hora = input("Ingrese la hora de la cita (HH:MM): ")
                    motivo = input("Ingrese el motivo de la cita: ")
                    especialidad = input("Ingrese la especialidad requerida: ").lower()
                    mascota_id = input("Ingrese el ID de la mascota: ")

                    cita = self.veterinaria.crear_cita(fecha, hora, motivo, especialidad, mascota_id)

                    print("\n")
                    print(cita)

                case "2":
                    pass
                
                case "3":
                    pass

                case "0":
                    break

                case _:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
    
    def __menu_productos(self):
        print("Menú de Productos")