# Array es un tipo de lista pero las listas no son arrays: 

import random

# Clase Array que será la representación de un array per si
class Array:
    # Metodo constructor de la clase. Define sus atributos luego
    # del self. capacity es la capacidad del array. fill_value es
    # el valor con el que lo vamos a rellenar. 
    def __init__(self, capacity, fill_value=None):
        # ¿Donde guardamos estos elementos? En un lista, nos apoyamos
        # en este tipo de colección pero le vamos a crear sus propios
        # metodos. 
        self.items = list()
        # Agregamos el valor como elemento de nuestro array. 
        for i in range(capacity):
            self.items.append(fill_value)

    # Metodo len del array para conocer su tamaño será un metodo
    # privado dado que es de consulta y no modifica al array: 
    def __len__(self):
        return len(self.items)
    
    # Metodo para definir como un string a los elementos de mi array:
    def __str__(self):
        return str(self.items)
    
    # Metodo iterador:
    def __iter__(self):
        return iter(self.items)
    
    # Metodo para obtener un elemento: 
    def __getitem__(self, index):
        return self.items[index]
    
    # Metodo para reemplazar un elemento:
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    # Podríamos sumar los metodos que deseemos... 
    # Reto: metodo para poblar sus slots con numeros aleatorios
    # Reto_2: metodo para sumar todos los valores del array.

    def __randomitem__(self):
        for i in range(self.items.__len__()):
            self.items[i] = random.randint(0,100)

    def __sumitems__(self):
        sum = 0
        for i in range(self.items.__len__()):
            sum += self.items[i]
        return sum
    
    