
class Veterinario:
    def __init__(self, vet_id, nombre, telefono, especialidad):
        self.__vet_id = vet_id
        self.__nombre = nombre
        self.__telefono = telefono
        self.__especialidad = especialidad

    @property
    def vet_id(self):
        return self.__vet_id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def especialidad(self):
        return self.__especialidad