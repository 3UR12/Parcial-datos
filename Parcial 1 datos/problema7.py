
# siguientes operaciones: 
# • Insertar un nodo al inicio. 
# • Insertar un nodo al final. 
# • Buscar un nodo por su valor. 
# • Eliminar un nodo por su valor. 


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"Insertado {valor} al inicio.")

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            print(f"Insertado {valor} al final (lista vacía).")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        print(f"Insertado {valor} al final.")

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                print(f"Nodo con valor {valor} encontrado.")
                return True
            actual = actual.siguiente
        print(f"Nodo con valor {valor} no encontrado.")
        return False

    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print(f"Nodo con valor {valor} no encontrado, no se puede eliminar.")
            return

        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

        print(f"Nodo con valor {valor} eliminado.")

    def mostrar_lista(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        print("Lista: " + " -> ".join(valores))

if __name__ == "__main__":
    lista = ListaEnlazada()

    # Insertar nodos al inicio y al final.
    lista.insertar_inicio(10)
    lista.insertar_final(20)
    lista.insertar_inicio(5)
    lista.insertar_final(30)
    lista.mostrar_lista()  #5 -> 10 -> 20 -> 30

    # Buscar nodos.
    lista.buscar(20)
    lista.buscar(100)

    # Eliminar nodos.
    lista.eliminar(10)  #Eliminar el nodo con valor 10.
    lista.mostrar_lista()  #5 -> 20 -> 30

    lista.eliminar(5)   # Esto deberia Eliminar
    lista.mostrar_lista()  #20 -> 30

    lista.eliminar(30)  #con este se elimina el nodo al final.
    lista.mostrar_lista()  #20
