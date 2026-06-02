from utils.obtener_bd import get_file_path


def obtener_citas_por_veterinario(veterinario_id: str):
    pass

def obtener_citas_por_mascota(mascota_id: str):
    pass

def obtener_citas_por_fecha_hora(fecha: str, hora: str):
    pass

def obtener_veterinarios_disponibles(fecha: str, hora: str, especialidad: str):
    with open(get_file_path("veterinarios.csv"), "r") as file:
        veterinarios_disponibles = []
        for line in file:
            veterinario_id, nombre, telefono, especialidad_vet = line.strip().split(",")
            if especialidad == especialidad_vet.lower() and not existe_cita_en_horario(veterinario_id, fecha, hora):
                veterinarios_disponibles.append({
                    "veterinario_id": veterinario_id,
                    "nombre": nombre,
                    "telefono": telefono,
                    "especialidad": especialidad
                })
    return veterinarios_disponibles

def existe_cita_en_horario(veterinario_id: str, fecha: str, hora: str):
    with open(get_file_path("citas.csv"), "r") as file:
        for line in file:
            data = line.strip().split(",")
            if (data[5] == veterinario_id and data[1] == fecha and data[2] == hora and data[4] == "agendada"):
                return True
    return False

def existe_cita_para_mascota(mascota_id: str, fecha: str, hora: str):
    with open(get_file_path("citas.csv"), "r") as file:
        for line in file:
            data = line.strip().split(",")
            if (data[5] == mascota_id and data[1] == fecha and data[2] == hora and data[4] == "agendada"):
                return True
    return False

def obtener_cita(cita_id: str):
    with open(get_file_path("citas.csv"), "r") as file:
        for line in file:
            if line.startswith(cita_id):
                cita_id, fecha, hora, motivo, estado, mascota_id, veterinario_id = line.strip().split(",")
                return {
                    "cita_id": cita_id,
                    "fecha": fecha,
                    "hora": hora,
                    "motivo": motivo,
                    "estado": estado,
                    "mascota_id": mascota_id,
                    "veterinario_id": veterinario_id
                }
    return None