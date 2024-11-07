from models.producto import Producto

class NodoProducto:
    def __init__(self, producto: Producto):
        self.producto = producto
        self.siguiente = None