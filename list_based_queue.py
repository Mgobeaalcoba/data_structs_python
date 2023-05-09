# Clase para queue o cola de listas:

class ListQueue:
    def __init__(self):
        self.items = []
        self.size = len(self.items)

    # Ingresar elementos a la fila:
    def enqueue(self, data):
        # self.items.append(data) Si lo hiciera así lo agrego al final, pero debo agregarlo al principio
        self.items.insert(0, data)
        self.size = len(self.items)

    # Remover elementos de la fila:
    def dequeue(self):
        # No debemos especificar cual, porque siempre va a ser el front o ultimo elemento de la lista:
        data = self.items.pop() # Por default es el ultimo elemento el que elimino 
        self.size = len(self.items)
        return data

    # Metodo para recorrer nuestra queue:
    def traverse(self):
        for item in self.items:
            print(item)
