from .nodo_producto import NodoProducto

class ListaProducto:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, producto):
        nuevo_nodo_producto = NodoProducto(producto)

        if self.cabeza == None:
            self.cabeza = nuevo_nodo_producto
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo_producto

    def mostrar_productos(self):
        nodo_actual = self.cabeza
        while nodo_actual != None:
            print(f"Nombre: {nodo_actual.producto.nombre}")
            nodo_actual = nodo_actual.siguiente

    def buscar_producto(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.producto.nombre.lower() == nombre.lower():
                return actual.producto
            actual = actual.siguiente
        return None
