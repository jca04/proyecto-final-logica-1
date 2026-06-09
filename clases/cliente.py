import csv
import numpy as np
from clases.mascota import Mascota
from utils.obtener_bd import get_file_path

class Cliente:

    __TAM_MASCOTAS = 200

    def __init__(self, cliente_id: int, nombre: str, telefono: str, cedula: str):
        self.__cliente_id = cliente_id
        self.__nombre = nombre
        self.__telefono = telefono
        self.__cedula = cedula
        self.__mascotas = np.full(self.__TAM_MASCOTAS, fill_value=None, dtype=Mascota)
        self.__nroMascotas = 0

        self.__cargar_mascotas()

    def __cargar_mascotas(self):
        with open(get_file_path("mascotas.csv"), "r") as f:
            lector = csv.DictReader(f)
            for linea in lector:
                m = Mascota(
                    linea["nombre"],
                    linea["especie"],
                    linea["raza"],
                    int(linea["edad"]),
                    int(linea["cliente_id"]),
                    int(linea["mascota_id"])
                )
                self.__mascotas[self.__nroMascotas] = m
                self.__nroMascotas += 1

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

    def agregarMascota(self, nombre, especie, raza, edad, cliente_id):

        mascota_id = self.__siguiente_id_mascota()
        self.__mascotas[self.__nroMascotas] = Mascota(nombre, especie, raza, edad, cliente_id, mascota_id)
        self.__nroMascotas = self.__nroMascotas + 1
        self.__guardar_mascotas()


        # if self.__nroMascotas < len(self.__mascotas):
        #     self.__mascotas[self.__nroMascotas] = Mascota(nombre, especie, raza, edad, cliente_id, mascota_id)
        #     self.__nroMascotas = self.__nroMascotas + 1
        # else: 
        #     print(f"El cliente {self.__nombre} no puede registrar a su mascotas.")

    def listar_mascotas(self, cliente_id):            
            mascotas = self.__mascotas[:self.__nroMascotas]
            for m in mascotas:
                if m is not None and m.cliente_id == cliente_id:
                    print(f"\nID  - {m.mascota_id}")
                    print(f"Nombre: {m.n}")
                    print(f"Especie: {m.especie}")
                    print(f"Raza: {m.raza}")
                    print(f"Edad: {m.edad} años")


    def __siguiente_id_mascota(self):
        if self.nroMascotas == 0:
            return 1
        
        ids = np.array([], dtype=int)

        for m in self.__mascotas[:self.__nroMascotas]:
            ids = np.append(ids, int(m.mascota_id))

        return max(ids) + 1

    def __guardar_mascotas(self):
        with open(get_file_path("mascotas.csv"), "w") as f:
            campos = ["mascota_id", "nombre", "especie", "raza", "edad", "cliente_id"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()

            for m in self.__mascotas[:self.__nroMascotas]:
                escritor.writerow({
                    "mascota_id": m.mascota_id,
                    "nombre": m.n,
                    "especie": m.especie,
                    "raza": m.raza,
                    "edad": m.edad,
                    "cliente_id": m.cliente_id
                })
