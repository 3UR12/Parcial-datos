# Implementa una cola utilizando una estructura de datos basada en arreglos y 
# escribe funciones para: 
# • enqueue(x): Agregar un elemento. 
# • dequeue(): Sacar un elemento. 
# • front(): Obtener el elemento en la parte frontal sin eliminarlo.

class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, x):
        self.elementos.append(x)
        print(f"Se ha encolado {x}.")

    def dequeue(self):
        if self.esta_vacia():
            print("Error: La cola está vacía, no se puede desencolar.")
            return None
        x = self.elementos.pop(0)  # Elimina el primer elemento
        print(f"Se ha desencolado {x}.")
        return x

    def front(self):
        if self.esta_vacia():
            print("La cola está vacía, no hay frente.")
            return None
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

if __name__ == "__main__":
    cola = Cola()
    cola.enqueue(10)
    cola.enqueue(20)
    cola.enqueue(30)
    
    print("Elemento en el frente:", cola.front())  #10
    cola.dequeue()  # Elimina 10
    print("Elemento en el frente después del dequeue:", cola.front())  #20
