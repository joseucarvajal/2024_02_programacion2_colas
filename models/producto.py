class Producto:
    def __init__(self, categoria, nombre, precio, existencias):
        """
        Inicializa un objeto de tipo Producto,
        que debe tener valores validos para cada atributo
        """
        
        if(categoria.strip() == ""):
            raise ValueError("La categoria del producto no puede ser vacia")
        self.categoria = categoria
        
        if(nombre.strip() == ""):
            raise ValueError("El nombre del producto no puede ser vacío")
        self.nombre = nombre

        try:
            precio =  float(precio)
        except ValueError:
            raise ValueError("el precio del producto debe ser un número válido")
        if(precio <= 0):
            raise ValueError("El precio del producto no puede ser un valor negativo")
        self.precio = precio
        
        try:
            existencias = int(existencias)
        except ValueError:
            raise ValueError("La cantidad de existencias debe ser un numero entero válido")
        if(existencias < 0):
            raise ValueError("La cantidad de existencias no puede ser menor a 0 (cero )")
        self.existencias = existencias
        