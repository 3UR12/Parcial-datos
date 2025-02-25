# Dada una lista doblemente enlazada de números enteros, escribe una función que 
# la invierta en orden. 

class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.prev = None
        self.next = None

class ListaDobleEnlazada:
    def __init__(self):
        self.head = None

#funcion para agregar al final
    def agregar_final(self, valor):
        nuevo = NodoDoble(valor)
        if self.head is None:
            self.head = nuevo
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo
        nuevo.prev = actual

#funcion par imprimir lista
    def imprimir_lista(self):
        actual = self.head
        valores = []
        while actual:
            valores.append(str(actual.valor))
            actual = actual.next
        print(" <-> ".join(valores))

#funcion para invertir la lista
    def invertir(self):
        actual = self.head
        temp = None
        while actual:
            temp = actual.prev
            actual.prev = actual.next
            actual.next = temp
            actual = actual.prev
        if temp:
            self.head = temp.prev

if __name__ == "__main__":
    lista = ListaDobleEnlazada()
    
# Agregar los elementos a la lista.
    for valor in [10, 20, 30, 40, 50]:
        lista.agregar_final(valor)
    
    print("Lista original:")
    lista.imprimir_lista()  # Salida: 10 <-> 20 <-> 30 <-> 40 <-> 50
    
    # funcion para I+nvertir la lista.
    lista.invertir()
    print("Lista invertida:")
    lista.imprimir_lista()  #deberia salir esto, 50 <-> 40 <-> 30 <-> 20 <-> 10
