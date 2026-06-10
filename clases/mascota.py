import numpy as np
import csv
from clases.registro_medico import RegistroMedico
from utils.obtener_bd import get_file_path

class Mascota:

    __TAM_REGISTRO_MEDICO = 200

    def __init__(self, n: str, especie: str, raza: str, edad: int, cliente_id: int, mascota_id = None):
        self.__mascota_id = mascota_id
        self.__nombre = n
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__cliente_id = cliente_id
        self.__registro_medico = np.full(self.__TAM_REGISTRO_MEDICO, fill_value=None, dtype=RegistroMedico)
        self.__nroRegistros = 0

    @property
    def mascota_id(self):
        return self.__mascota_id

    @property
    def n(self):
        return self.__nombre
    
    @property
    def especie(self):
        return self.__especie
    
    @property
    def raza(self):
        return self.__raza
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def cliente_id(self):
        return self.__cliente_id
    
    def agregar_registro_medico(self, diagnostico: str, tratamiento: str, observaciones: str):
        if self.__nroRegistros < self.__TAM_REGISTRO_MEDICO:
            r = RegistroMedico(diagnostico, tratamiento, observaciones)
            self.__registro_medico[self.__nroRegistros] = r
            self.__nroRegistros += 1
            self.__guardar_registro_medico()
        else:
            print(f"No se pueden agregar más registros médicos para la mascota {self.__nombre}.")

    def __guardar_registro_medico(self):
        with open(get_file_path("registro_medico.csv"), mode="a") as f:
            campos = ["mascota_id", "fecha", "diagnostico", "tratamiento", "observaciones"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()

            for r in self.__registro_medico[:self.__nroRegistros]:
                escritor.writerow({
                    "mascota_id": self.__mascota_id,
                    "fecha": r.fecha,
                    "diagnostico": r.diagnostico,
                    "tratamiento": r.tratamiento,
                    "observaciones": r.observaciones
                })
