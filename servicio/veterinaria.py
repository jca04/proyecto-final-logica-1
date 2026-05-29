from clases.citas import Citas
class Veterinaria:


    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self._citas = Citas()
        

    def mostrar_informacion(self):
        print(f"Veterinaria: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")

    
    def crear_cita(self, fecha: str, hora: str, motivo: str, especialidad: str, mascota_id: str):
        return self._citas.registrar_cita(fecha, hora, motivo, especialidad, mascota_id)

    def cancelar_cita(self, cita_id: str):
        pass