'''
Descripción: 
Una empresa de entregas tiene un sistema donde recibe pedidos de clientes y 
los asigna a repartidores. Los pedidos pueden ser normales o urgentes. 
• Los pedidos urgentes deben ser atendidos primero. 
• Los pedidos normales se atienden en el orden en que llegan. 
• Cada repartidor solo puede llevar un pedido a la vez. 
• Se debe permitir agregar y procesar pedidos de manera eficiente. 

Requisitos: 
• Diseñar una estructura de datos eficiente para gestionar los pedidos. 
• Implementar funciones para agregar un pedido, asignar un pedido a un 
repartidor y mostrar los pedidos pendientes. 
• El sistema debe permitir múltiples repartidores. 

Para resolverlo, deberá responder las siguientes preguntas: 
1. ¿Qué estructura de datos permite manejar prioridades? 
2. ¿Cómo se podría organizar la cola para que los pedidos urgentes sean 
atendidos primero? 
3. ¿Cómo se asignan pedidos a los repartidores de manera eficiente?
'''
'''
Respuestas de las preguntas:
¿Qué estructura de datos permite manejar prioridades?
Una cola de prioridad (heap) permite manejar pedidos  de manera urgente antes que los normales.

¿Cómo se podría organizar la cola para que los pedidos urgentes sean atendidos primero?
Se puede usar una cola de prioridad donde los pedidos urgentes tienen mayor prioridad.

¿Cómo se asignan pedidos a los repartidores de manera eficiente?
Se mantiene una lista de repartidores disponibles.
Cuando un repartidor queda libre, se le asigna el pedido de mayor prioridad.
Una estructura heap permite obtener el pedido más urgente.

'''


import heapq

class Pedido:
    def __init__(self, id_pedido, cliente, prioridad):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.prioridad = prioridad  

    def __lt__(self, otro):
        return self.prioridad < otro.prioridad

class SistemaPedidos:
    def __init__(self):
        self.cola_pedidos = []  
        self.repartidores_disponibles = set()  # Conjunto de repartidores disponibles

    def agregar_pedido(self, id_pedido, cliente, urgente=False):
        prioridad = 0 if urgente else 1  # Urgentes tienen prioridad 0
        pedido = Pedido(id_pedido, cliente, prioridad)
        heapq.heappush(self.cola_pedidos, pedido)
        print(f"Pedido {id_pedido} agregado {'URGENTE' if urgente else 'NORMAL'}.")

    def agregar_repartidor(self, id_repartidor):
        self.repartidores_disponibles.add(id_repartidor)
        print(f"Repartidor {id_repartidor} disponible.")

    def asignar_pedido(self):
        if not self.cola_pedidos:
            print("No hay pedidos pendientes.")
            return

        if not self.repartidores_disponibles:
            print("No hay repartidores disponibles.")
            return

        pedido = heapq.heappop(self.cola_pedidos)        

        repartidor = self.repartidores_disponibles.pop()  
        print(f"Pedido {pedido.id_pedido} asignado al repartidor {repartidor}.")

    def mostrar_pedidos_pendientes(self):
        if not self.cola_pedidos:
            print("No hay pedidos pendientes.")
            return

        print("Pedidos pendientes:")
        for pedido in sorted(self.cola_pedidos, key=lambda p: p.prioridad):
            tipo = "URGENTE" if pedido.prioridad == 0 else "NORMAL"
            print(f"- Pedido {pedido.id_pedido} ({tipo}) de {pedido.cliente}")

# Prueba
if __name__ == "__main__":
    sistema = SistemaPedidos()

    # Agregar pedidos
    sistema.agregar_pedido(101, "Cliente A", urgente=True)
    sistema.agregar_pedido(102, "Cliente B", urgente=False)
    sistema.agregar_pedido(103, "Cliente C", urgente=True)

    # Agregar repartidores
    sistema.agregar_repartidor("R1")
    sistema.agregar_repartidor("R2")

    # Asignar pedidos
    sistema.asignar_pedido()
    sistema.asignar_pedido()

    # Mostrar pedidos pendientes
    sistema.mostrar_pedidos_pendientes()
