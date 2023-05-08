from node import Node

class Stack: 
    def __init__(self):
        # Cuando lo inicialicemos sabemos que no hay nada arriba entonces:
        self.top = None
        self.size = 0

    # Metodo para ingresar un nodo al stack
    def push(self, data):
        node = Node(data)

        # Si hay algo en la pila entonces lo empujamos abajo así:
        if self.top: 
            node.next = self.top
            self.top = node
        # Si no hay nada en la pila entonces directamente lo metemos:
        else:
            self.top = node

        # Como estamos añadiendo elementos no se nos debe olvidar cambiar el tamaño de nuestro stack:
        self.size += 1

    # Metodo para eliminar el ultimo nodo ingresado del stack: 
    def pop(self):

        # En caso de que haya un elemento arriba del stack:
        if self.top:
            # Tomados el elemento a eliminar para luego devolverlo y mostarlo
            data = self.top.data
            self.size -= 1

            # Si hay algo despues de ese nodo:
            if self.top.next:
                self.top = self.top.next # porque necesitamos reposicionar los valores del stack
            else:
                # Si nuestra stack ya está vacio entonces:
                self.top = None
            
            return data
        # Pero puede que el stack o pila esté vacio. En ese caso:
        else: 
            return "The stack is empty"
        
    # Metodo para conocer el elemento que está en el Top: 
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"
        
    # Metodo para vaciar la pila:
    def clear(self):
        # Mientras haya un elemento en el Top del Stack...
        while self.top: 
            # Vamos a estar llamando al metodo pop que definimos arriba:
            self.pop()