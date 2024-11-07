from models.producto import Producto

from listas.lista_producto import ListaProducto

lista_productos = ListaProducto()

def mostrar_menu():
    print("1. Adicionar producto")
    print("2. Mostrar productos creados")
    print("3. Salir")
    print("Ingrese una opción: ")

    try:
        opc = int(input())
        if opc > 3 or opc < 1:
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


def main():
    
    while True:
        opc = mostrar_menu()

        if opc == 1:
            agregar_producto()

        elif opc == 2:
            mostrar_productos_creados()

        elif opc == 3:
            break

if __name__ == "__main__":
    main()
