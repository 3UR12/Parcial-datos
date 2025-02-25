# Dada una lista enlazada con un posible ciclo, escribe un algoritmo que detecte si 
# la lista tiene un ciclo o no (algoritmo de Floyd, "tortuga y liebre"). 

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def tiene_ciclo(head):
    tortuga = liebre = head  
    
    while liebre and liebre.siguiente:
        tortuga = tortuga.siguiente  
        liebre = liebre.siguiente.siguiente  

        if tortuga == liebre:  
            return True
    
    return False  

# Prueba
if __name__ == "__main__":
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4

    print("Tiene ciclo:", tiene_ciclo(nodo1))  

    nodo4.siguiente = nodo2

    print("Tiene ciclo:", tiene_ciclo(nodo1))  
