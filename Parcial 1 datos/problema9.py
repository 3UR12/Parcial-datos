# Implementa una pila con un arreglo dinámico y realiza las siguientes operaciones: 
# • push(x): Agregar un elemento. 
# • pop(): Eliminar el elemento en el tope. 
# • top(): Obtener el elemento en el tope sin eliminarlo. 


class Pila:
        def __init__(self):
            self.elementos = []

        def push(self, x):
            self.elementos.append(x)
            print(f"Se ha insertado {x} en la pila.")

        def pop(self):
            if self.esta_vacia():
                print("Error: La pila está vacía, no se puede hacer pop.")
                return None
            x = self.elementos.pop()
            print(f"Se ha eliminado {x} del tope de la pila.")
            return x

        def top(self):
            if self.esta_vacia():
                print("La pila está vacía, no hay tope.")
                return None
            return self.elementos[-1]

        def esta_vacia(self):
            return len(self.elementos) == 0

if __name__ == "__main__":
        pila = Pila()
        pila.push(10)
        pila.push(20)
        pila.push(30)
        print("Elemento en el tope:", pila.top())  # Debería mostrar 30
        pila.pop()  # Elimina 30
        print("Elemento en el tope después del pop:", pila.top())  # Debería mostrar 20
        pila.pop()  # Elimina 20
        print("Elemento en el tope después del pop:", pila.top())  # Debería mostrar 20
        pila.pop()  # Elimina 10
        print("Elemento en el tope después del pop:", pila.top())  # Debería mostrar 20
