from models.producto import Producto
from models.venta import Venta
from models.cliente import Cliente
from listas.lista_producto import ListaProducto
from colas.cola_ventas import ColaVentas

lista_productos = ListaProducto()
cola_ventas = ColaVentas()

def mostrar_menu():
    print("1. Adicionar producto")
    print("2. Mostrar productos creados")
    print("3. Encolar venta")
    print("4. Desencolar venta")
    print("5. Salir")
    print("Ingrese una opción: ")

    try:
        opc = int(input())
        if opc > 5 or opc < 1:
            print("ERROR: La opción ingresada no es válida. Por favor ingrese una opción válida")
            return
        
        return opc

    except ValueError:
        print("ERROR: La opción ingresada no es válida. Por favor ingrese una opción válida")
        return

def agregar_producto():
    print("Ingrese la categoria del producto: ")
    categoria = input()
    print("Ingrese el nombre del producto: ")
    nombre = input()
    print("Ingrese el precio del producto: ")
    precio = input()
    print("Ingrese la cantidad de existencias del producto: ")
    cantidad_existencias = input()
    producto = Producto(categoria, nombre, precio, cantidad_existencias)
    lista_productos.agregar_producto(producto)

def mostrar_productos_creados():
    lista_productos.mostrar_productos()

def encolar_venta():
    print("Ingrese el nombre del cliente: ")
    nombre_cliente = input()
    print("Ingrese el documento del cliente: ")
    documento_cliente = input()
    
    cliente = Cliente(nombre_cliente, documento_cliente)
    productos_venta = ListaProducto()
    productos_agregados = 0  # Contador manual de productos
    
    while True:
        print("\n¿Desea agregar un producto a la venta? (s/n): ")
        respuesta = input().lower()
        if respuesta != 's':
            break
            
        lista_productos.mostrar_productos()
        print("\nIngrese el nombre del producto que desea agregar: ")
        nombre_producto = input()
        
        producto = lista_productos.buscar_producto(nombre_producto)
        if producto:
            productos_venta.agregar_producto(producto)
            productos_agregados += 1  # Incrementamos el contador
            print("Producto agregado a la venta exitosamente")
        else:
            print("Producto no encontrado")
    
    if productos_agregados > 0:  # Usamos el contador en lugar de acceder al atributo
        venta = Venta(cliente, productos_venta)
        cola_ventas.encolar(venta)
        print("Venta agregada exitosamente a la cola")
    else:
        print("No se puede crear una venta sin productos")

def desencolar_venta():
    if cola_ventas.esta_vacia():
        print("No hay ventas pendientes para procesar")
        return
        
    venta = cola_ventas.desencolar()
    print("\nProcesando venta:")
    print(f"Cliente: {venta.cliente.nombre}")
    print("Productos:")
    venta.lista_productos.mostrar_productos()
    print("\nVenta procesada exitosamente")

def main():
    while True:
        opc = mostrar_menu()

        if opc == 1:
            agregar_producto()
        elif opc == 2:
            mostrar_productos_creados()
        elif opc == 3:
            encolar_venta()
        elif opc == 4:
            desencolar_venta()
        elif opc == 5:
            break

if __name__ == "__main__":
    main()
