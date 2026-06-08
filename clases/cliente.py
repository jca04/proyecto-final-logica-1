import numpy as np
from clases.mascota import Mascota

class Cliente:

    __TAM_MASCOTAS = 200

    def __init__(self, cliente_id: int, nombre: str, telefono: str, cedula: str):
        self.__cliente_id = cliente_id
        self.__nombre = nombre
        self.__telefono = telefono
        self.__cedula = cedula
        self.__mascotas = np.full(self.__TAM_MASCOTAS, fill_value=None, dtype=Mascota)
        self.__nroMascotas = 0

    @property
    def cliente_id(self):
        return self.__cliente_id
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def cedula(self):
        return self.__cedula
    
    @property
    def mascotas(self):
        return self.__mascotas

    @property
    def nroMascotas(self):
        return self.__nroMascotas

    def agregarMascota(self, nombre, especie, raza, edad, cliente_id, mascota_id = None):
        if self.__nroMascotas < len(self.__mascotas):
            self.__mascotas[self.__nroMascotas] = Mascota(nombre, especie, raza, edad, cliente_id, mascota_id)
            self.__nroMascotas = self.__nroMascotas + 1
        else: 
            print(f"El cliente {self.__nombre} no puede registrar a su mascotas.")
