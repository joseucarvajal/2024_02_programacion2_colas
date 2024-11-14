from datetime import datetime
from models.cliente import Cliente
from listas.lista_producto import ListaProducto

class VentaDetallada:
    def __init__(self, cliente, lista_productos=None):
        self.cliente = cliente
        self.lista_productos = lista_productos if lista_productos else ListaProducto()
        self.total = 0
        self.fecha = datetime.now()
        self.estado = "pendiente"  # pendiente, procesada, cancelada
        self.numero_venta = None  # Se puede asignar un número único de venta
        self.calcular_total()
    
    def calcular_total(self):
        actual = self.lista_productos.cabeza
        subtotal = 0
        cantidad_items = 0
        
        while actual:
            subtotal += actual.producto.precio
            cantidad_items += 1
            actual = actual.siguiente
            
        self.total = subtotal
        self.cantidad_items = cantidad_items
    
    def agregar_producto(self, producto):
        self.lista_productos.agregar(producto)
        self.calcular_total()
    
    def procesar_venta(self):
        self.estado = "procesada"
        
    def cancelar_venta(self):
        self.estado = "cancelada"
    
    def obtener_resumen(self):
        return {
            "cliente": self.cliente.nombre,
            "cedula": self.cliente.cedula,
            "fecha": self.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "total": self.total,
            "cantidad_items": self.cantidad_items,
            "estado": self.estado
        }
    
    def __str__(self):
        return f"Venta de {self.cliente.nombre} - Total: ${self.total:.2f} - Estado: {self.estado}" 