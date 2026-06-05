import uuid
class Producto:

    def __init__(self):
        self.__producto_id = uuid.uuid4()
    
    # @property
    # def producto_id(self):
    #     return self.__producto_id

    # @property
    # def nombre(self):
    #     return self.__nombre

    # @property
    # def cantidad(self):
    #     return self.__cantidad

    # @property
    # def precio(self):
    #     return self.__precio

    # @property
    # def categoria(self):
    #     return self.__categoria

    # @property
    # def stock_minimo(self):
    #     return self.__stock_minimo

    # def actualizar_stock(self, cantidad):
    #     self.__cantidad = self.__cantidad + cantidad

    # def tiene_poco_stock(self):
    #     return self.__cantidad <= self.__stock_minimo

    # def mostrar(self):
    #     print(f"ID: {self.__producto_id}")
    #     print(f"Nombre: {self.__nombre}")
    #     print(f"Cantidad: {self.__cantidad}")
    #     print(f"Precio: {self.__precio}")
    #     print(f"Categoría: {self.__categoria}")
    #     print(f"Stock mínimo: {self.__stock_minimo}")

    def registrar_producto(self, nombre, cantidad, precio, categoria, stock_minimo):
        # w -> write escribir
        # r -> read -> solo para leer el archivo
        # a -> append ->
        with open("bd/productos.csv", "a") as file:
            file.write(f"{self.__producto_id},{nombre},{cantidad},{precio},{categoria},{stock_minimo}\n")
            return "Producto registrado con éxito."