class Client:
    
    __name: str
    __phone: str
    __nroPets: int

    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone
        self.__pets = np.full(TAM, fill_value=None, dtype=Pet)
        self.__nroPets = 0

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone
    
    @property
    def pets(self):
        return self.__pets

    @property
    def nroPets(self):
        return self.__nroPets

    def agregarMascota(self, petName, species, age):
        self.__pets[self.__nroPets] = Pet(petName, species, age)
        self.__nroPets = self.__nroPets + 1
