
import uuid
from utils.citas import existe_cita_para_mascota, obtener_veterinarios_disponibles


class Citas:

    def __init__(self):
        self.cita_id = uuid.uuid4()

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
            