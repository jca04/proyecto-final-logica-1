class Producto:

    def __init__(self, producto_id, nombre, cantidad, precio, categoria, stock_minimo):
        self.__producto_id  = producto_id
        self.__nombre       = nombre
        self.__cantidad     = cantidad
        self.__precio       = precio
        self.__categoria    = categoria
        self.__stock_minimo = stock_minimo

    #Getters

    @property
    def producto_id(self):
        return self.__producto_id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def precio(self):
        return self.__precio

    @property
    def categoria(self):
        return self.__categoria

    @property
    def stock_minimo(self):
        return self.__stock_minimo

    # métodos principales

    def actualizar_stock(self, cantidad):
        self.__cantidad = self.__cantidad + cantidad

    def tiene_poco_stock(self):
        if self.__cantidad <= self.__stock_minimo:
            return True
        else:
            return False

    def mostrar(self):
        print(f"  ID:         {self.__producto_id}")
        print(f"  Nombre:     {self.__nombre}")
        print(f"  Categoría:  {self.__categoria}")
        print(f"  Cantidad:   {self.__cantidad} unidades")
        print(f"  Precio:     ${self.__precio:.2f}")
        print(f"  Stock mín:  {self.__stock_minimo} unidades")