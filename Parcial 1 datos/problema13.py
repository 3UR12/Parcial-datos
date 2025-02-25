# Implementa una cola con dos pilas. Es decir, simula el comportamiento de una 
# cola utilizando únicamente dos pilas. 

class ColaConDosPilas:
    def __init__(self):
        self.pila_entrada = [] 
        self.pila_salida = []   
    def enqueue(self, x):
        self.pila_entrada.append(x)
        print(f"Encolado: {x}")

    def dequeue(self):
        if self.esta_vacia():
            print("La cola está vacía, no se puede desencolar.")
            return None
        
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())

        return self.pila_salida.pop()

    def front(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return None
        
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())

        return self.pila_salida[-1]

    def esta_vacia(self):
        return not self.pila_entrada and not self.pila_salida


if __name__ == "__main__":
    cola = ColaConDosPilas()
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)

    print("Frente de la cola:", cola.front())  # Debe ser 1
    print("Desencolado:", cola.dequeue())  # Debe ser 1
    print("Frente de la cola:", cola.front())  # Debe ser 2
    print("Desencolado:", cola.dequeue())  # Debe ser 2
    print("Desencolado:", cola.dequeue())  # Debe ser 3
    print("Desencolado:", cola.dequeue())  # La cola está vacía
