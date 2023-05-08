# Vamos a crear nuestra clase Node():

class Node():
    # Constructor, recibe la data del node y donde lleva el mismo.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Clase que hereda de Node:
class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        # Paso los parametros repetidos a su padre Node()
        # Poner super() o poner el nombre de la clase es lo mismo
        # Si ponemos el nombre de la clase padre, debemos poner el self tambien.
        # Si ponemos super puede ir sin self
        super().__init__(data, next=next)
        self.previous = previous
