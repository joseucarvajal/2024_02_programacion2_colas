from models.nodo_venta import NodoVenta

class ColaVentas:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def encolar(self, venta):
        nuevo_nodo = NodoVenta(venta)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        
        self.tamanio += 1
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        
        venta = self.cabeza.venta
        self.cabeza = self.cabeza.siguiente
        self.tamanio -= 1
        
        if self.cabeza is None:
            self.cola = None
            
        return venta
    
    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.cabeza.venta
    
    def obtener_tamanio(self):
        return self.tamanio 