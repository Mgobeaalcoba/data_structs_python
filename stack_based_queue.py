# Clase para Queue basado en dos Stacks que a su vez van a estar basados en listas

class Queue:
    # Metodo constructor:
    def __init__(self): 
        # Primer stack basado en listas:
        self.inbound_stack: list = []
        self.obtbound_stack: list = []

    # Metodo para agregar datos: 
    def enqueue(self, data):
        self.inbound_stack.append(data)

    # Metodo para remover data de nuestros stacks
    def dequeue(self):
        # Proceso: los elementos que entraron a inbound stack los vamos a 
        # pasar a outbound stack. Pero respetando el principio de los queues
        # Si nuestro outbound stack no está vacio:
        if not self.obtbound_stack:
            # Mientras self.inbound_stack tenga elementos:
            while self.inbound_stack:
                # Va a ir recibiendo el ultimo elemento del stack:
                self.obtbound_stack.append(self.inbound_stack.pop())
        # Por ultimo queremos que nos retorne aquellos datos que se están extrayendo:
        return self.obtbound_stack.pop()
        # Una vez que del inbound stack pase todos los elementos al outbound stack le
        # voy a hacer pop para que retorne el elemento expulsado. 
        