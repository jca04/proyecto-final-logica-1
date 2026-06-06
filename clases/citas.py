
from utils.citas import existe_cita_para_mascota, obtener_veterinarios_disponibles


class Citas:

    def __init__(self, mascota_id: str, vet_id: str, fecha: str, hora: str, motivo: str, estado: str = "agendada", cita_id = None):
        self.__cita_id = cita_id
        self.__mascota_id = mascota_id
        self.__vet_id = vet_id
        self.__fecha = fecha
        self.__hora = hora
        self.__motivo = motivo
        self.__estado = estado

    def marcar_atendida(self):
        self.__estado = "atendida"
    
    def cancelar(self):
        self.__estado = "cancelada"


    @property
    def cita_id(self): return self.__cita_id

    @property
    def mascota_id(self): return self.__mascota_id

    @property
    def vet_id(self): return self.__vet_id

    @property
    def fecha(self): return self.__fecha

    @property
    def hora(self): return self.__hora

    @property
    def motivo(self): return self.__motivo

    @property
    def estado(self): return self.__estado

    def registrar_cita(self, fecha: str, hora: str, motivo: str, especialidad: str, mascota_id: str):

        if existe_cita_para_mascota(mascota_id, fecha, hora):
            print("La mascota ya tiene una cita agendada en ese horario.")
            return
        
        veterinarios_disponibles = obtener_veterinarios_disponibles(fecha, hora, especialidad)

        if len(veterinarios_disponibles) == 0:
            print("No hay veterinarios disponibles en ese horario para la especialidad seleccionada.")
            return
        
        veterinario_asignado = veterinarios_disponibles[0]

        with open("bd/citas.csv", "a") as file:
            file.write(f"{self.cita_id},{fecha},{hora},{motivo},agendada,{mascota_id},{veterinario_asignado['veterinario_id']}\n")
            return (f"Cita registrada con éxito. Veterinario asignado: {veterinario_asignado['nombre']} (Teléfono: {veterinario_asignado['telefono']})")
            