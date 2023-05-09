from node import TwoWayNode

class Queue:
    def __init__(self) -> None:
        self.head= None
        self.tail= None
        # Tamaño entendido como "conteo de nodos en nuestra lista":
        self.count = 0

    # 1° metodo enqueue para añadir datos
    def enqueue(self, data):
        new_node = TwoWayNode(data, None, None)
        # Definimos los parametros next y previous del nodo instanciado:
        # Si es el primer nodo, o lo que es igual, si head is None:
        if self.head is None:
            # Entonces head apunta al nodo creado y tail apunta a head,
            # dado que son nodos de doble vía:
            self.head = new_node
            self.tail = self.head
        # Si por el contrarío hay nodos en nuestro Queue:
        else:
            # entonces atamos el previos del nuevo nodo a self.tail
            new_node.previous = self.tail
            # y el tail del siguiente nodo lo atamos al new node:
            self.tail.next = new_node
            # Ademas self.tail va a ser el nuevo nodo:
            self.tail = new_node
        
        # Por ultimo aumentamos en 1 unidad el tamaño de nuestro count:
        self.count += 1

    # 2° metodo para remover elemento con criterio FIFO de queue o cola: 
    def dequeue(self):
        # Creamos una variable auxiliar que retenga cual es el head:
        current = self.head.data

        # Validamos si tenemos 1 elemento en nuestra queue:
        if self.count == 1:
            # Reduzco en 1 el tamaño y situo nuevamente a head y tail en None
            self.count -= 1
            self.head = None
            self.tail = None
        # otro caso: si hay mas de un nodo:
        if self.count > 1:
            # el head va a apuntar al siguiente y el previos de ese mismo head va a ser None
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        # Que nos va a indicar cual fue el elemento eliminado de mi queue. El primero en ingresar.
        return current
    
    # Challenge: metodo para recorrer la lista de nodos: 
        # 3° un metodo para iterar y recorrer sus valores.
    def iter(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            # yield genera valores "on the flight" o sobre
            # la marcha que no son almacenados en memoría:
            yield value
            

