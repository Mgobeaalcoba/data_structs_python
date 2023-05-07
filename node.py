# Vamos a crear nuestra clase Node():

class Node():
    # Constructor, recibe la data del node y donde lleva el mismo.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next