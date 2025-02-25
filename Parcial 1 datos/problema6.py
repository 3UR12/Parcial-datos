# Implementa una estructura para manejar un inventario de productos con los 
# siguientes campos: ID, nombre, cantidad y precio. Escribe un programa que 
# permita agregar, modificar y eliminar productos del inventario. 

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        #diccionario.
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos: #un nuevo producto al inventario.
            print(f"Error: Ya existe un producto con ID {producto.id}.")
        else:
            self.productos[producto.id] = producto
            print("Producto agregado exitosamente.")

    
    #Modifica los datos de un producto existente.
    def modificar_producto(self, id, nombre=None, cantidad=None, precio=None):
        if id not in self.productos:
            print("Error: Producto no encontrado.")
        else:
            producto = self.productos[id]
            if nombre is not None:
                producto.nombre = nombre
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto modificado exitosamente.")

    def eliminar_producto(self, id):
        """Elimina un producto del inventario."""
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


if __name__ == "__main__":
    inventario = Inventario()

    # Agregar productos
    cosa1 = Producto(1, "Marcador", 20, 500.00)
    cosa2 = Producto(2, "Gato Hidraulico", 40, 200.00)
    cosa3 = Producto(3, "Macarenas", 10, 20.00)

    inventario.agregar_producto(cosa1)
    inventario.agregar_producto(cosa2)
    inventario.agregar_producto(cosa3)
    
    print("\nInventario inicial:")
    inventario.mostrar_inventario()

    # Modificar un producto
    inventario.modificar_producto(2, cantidad=60, precio=27.50)
    
    print("\nInventario después de modificar el producto con ID 2:")
    inventario.mostrar_inventario()

    # Eliminar un producto
    inventario.eliminar_producto(1)
    
    print("\nInventario después de eliminar el producto con ID 1:")
    inventario.mostrar_inventario()
