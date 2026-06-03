class Pet:
    
    __petName: str
    __species: str
    __age: int

    def __init__(self, petName, species, age):
        self.__petName = petName
        self.__species = species
        self.__age = age

    @property
    def petName(self):
        return self.__petName

    @property
    def species(self):
        return self.__species
        
    @property
    def age(self):
        return self.__age
