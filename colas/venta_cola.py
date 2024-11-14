from datetime import datetime
from models.cliente import Cliente
from listas.lista_producto import ListaProducto

class VentaCola:
    def __init__(self, cliente, lista_productos=None):
        self.cliente = cliente
        self.lista_productos = lista_productos if lista_productos else ListaProducto()
        self.total = 0
        self.fecha_ingreso = datetime.now()
        self.prioridad = self._calcular_prioridad()
        self.calcular_total()

    def _calcular_prioridad(self):
        # Ejemplo simple de prioridad basada en la cantidad de productos
        if self.lista_productos and self.lista_productos.cabeza:
            cantidad = 0
            actual = self.lista_productos.cabeza
            while actual:
                cantidad += 1
                actual = actual.siguiente
            
            if cantidad > 10:
                return "ALTA"
            elif cantidad > 5:
                return "MEDIA"
            return "BAJA"
        return "BAJA"
    
    def calcular_total(self):
        actual = self.lista_productos.cabeza
        total = 0
        while actual:
            total += actual.producto.precio
            actual = actual.siguiente
        self.total = total

    def agregar_producto(self, producto):
        self.lista_productos.agregar(producto)
        self.calcular_total()
        self.prioridad = self._calcular_prioridad()

    def tiempo_en_cola(self):
        tiempo_transcurrido = datetime.now() - self.fecha_ingreso
        return tiempo_transcurrido.total_seconds() / 60  # retorna minutos

    def __str__(self):
        tiempo = self.tiempo_en_cola()
        return (f"Venta en cola - Cliente: {self.cliente.nombre}\n"
                f"Total: ${self.total:.2f}\n"
                f"Prioridad: {self.prioridad}\n"
                f"Tiempo en cola: {tiempo:.1f} minutos") 