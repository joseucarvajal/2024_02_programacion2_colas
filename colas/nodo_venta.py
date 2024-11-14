from .venta import Venta

class NodoVenta:
    def __init__(self, venta: Venta):
        self.venta = venta
        self.siguiente = None 