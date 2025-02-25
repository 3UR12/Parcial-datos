# Simula un sistema de atención en una tienda donde los clientes son atendidos 
# en orden de llegada (FIFO). Implementa la cola para manejar la fila de clientes. 

from collections import deque

class ColaClientes:
    def __init__(self):
        self.cola = deque()

    def agregar_cliente(self, nombre):
        self.cola.append(nombre)
        print(f"Cliente {nombre} ha ingresado a la fila.")

    def atender_cliente(self):
        if self.esta_vacia():
            print("No hay clientes en la fila.")
            return None
        cliente = self.cola.popleft() 
        print(f"Atendiendo a {cliente}.")
        return cliente

    def siguiente_cliente(self):
        if self.esta_vacia():
            print("No hay clientes en la fila.")
            return None
        return self.cola[0]

    def esta_vacia(self):
        return len(self.cola) == 0

if __name__ == "__main__":
    tienda = ColaClientes()
    
    # Clientes llegan a la tienda
    tienda.agregar_cliente("jose")
    tienda.agregar_cliente("Ana")
    tienda.agregar_cliente("Sofia")

    print(f"Siguiente cliente a ser atendido: {tienda.siguiente_cliente()}") 

    # Atender clientes en orden de llegada
    tienda.atender_cliente()  
    tienda.atender_cliente() 

    print(f"Siguiente cliente a ser atendido: {tienda.siguiente_cliente()}") 

    tienda.atender_cliente() 
    tienda.atender_cliente() 
