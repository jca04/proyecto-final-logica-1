import numpy as np

from clases.registro_medico import RegistroMedico

class Mascota:

    __TAM_REGISTRO_MEDICO = 200

    def __init__(self, nombre: str, especie: str, raza: str, edad: int, cliente_id: int, mascota_id = None):
        self.__mascota_id = mascota_id
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__cliente_id = cliente_id
        self.__registro_medico = np.full(self.__TAM_REGISTRO_MEDICO, fill_value=None, dtype=RegistroMedico)
        self.__nroRegistros = 0