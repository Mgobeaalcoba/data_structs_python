# Lista de nodos... Por lo que necesitamos usar Node()
# No tienen indices como los arrays o las list. Por lo que 
# deben emularlos. 
# Vamos a crear una variable auxiliar "probe" que funciona 
# como un sonda o puntero temporal que recorre la lista 
# consultando los datos. 

from node import Node

class SinglyLinkedList:
    # Metodo constructor con dos atributos que no vienen
    # en la instanciación del objeto:
    def __init__(self):
        # tail o final de la lista
        self.tail = None
        # size o tamaño de la lista
        self.size = 0

    # ¿Que metodos va a necesitar esta clase? 

    # 1° un metodo para añadir nodos
    def append(self, data):
        node = Node(data)

        # Dos escenarios: la lista está vacia o no lo está:
        # 1° escenario con lista vacia:
        if self.tail == None:
            self.tail = node
            self.size += 1
        # 2° escenario con lista que ya tienen nodos:
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
            self.size += 1

    # 2° un metodo que nos diga el tamaño de nuestra lista:
    def size(self):
        return str(self.size)
    
    # 3° un metodo para iterar y recorrer sus valores.
    def iter(self):
        current = self.tail
        while current:
            value = current.data
            current = current.next
            # yield genera valores "on the flight" o sobre
            # la marcha que no son almacenados en memoría:
            yield value

    # 4° un metodo que nos permita eliminar un nodo:
    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    # Retornamos el valor que eliminamos:
                    return current.data
                
            previous = current
            current = current.next

    # 5° un metodo que nos permita buscar nodos en nuestra lista: 
    def search(self, data):
        check = True
        for node in self.iter():
            if data == node:
                check = True
            else:
                check = False
        if check:
            print(f"Data: {data} found!")
        else:
            print(f"{data} not found in the list!")
            

    # 6° y ultimo metodo: "Limpiar" nuestra lista. No es
    # necesario eliminar nuestros nodos sino setear el 
    # tail y head en None y el size en 0
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0


