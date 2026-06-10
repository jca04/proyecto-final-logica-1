from datetime import datetime

class RegistroMedico:

    def __init__(
        self,
        diagnostico,
        tratamiento,
        observaciones
    ):

        self.__fecha = datetime.now()

        self.__diagnostico = diagnostico
        self.__tratamiento = tratamiento
        self.__observaciones = observaciones

    @property
    def fecha(self):
        return self.__fecha

    @property
    def diagnostico(self):
        return self.__diagnostico

    @property
    def tratamiento(self):
        return self.__tratamiento

    @property
    def observaciones(self):
        return self.__observaciones