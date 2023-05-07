"""
Reto:
Crear un array unidimensional.
Tranferir los datos a una linked structure sencilla
"""

from my_array import Array
from linked_list import SinglyLinkedList

# Creo mi Array
my_array = Array(10, 0)
# Imprimo mi array para verificar que esté creado.
# Al imprimir el objeto recurre a su metodo __str__
print(my_array)
print()
# Asigno valores random a mi array:
my_array.__randomitem__()
# Vuelvo a imprimir mi array con valores random
print(my_array)
print()

# Creo mi linked list:
my_linked = SinglyLinkedList()

# Cargo mi linked list con los valores del array:
for value in my_array.__iter__():
    my_linked.append(value)

# Imprimo los valores de mi linked list ya cargada:
for value in my_linked.iter():
    print(value)

print()

"""
23:36:12 👽 with 🤖 mgobea 🐶 in develop/python/data_structs_python …
➜ python3 challenge_single.py
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

[6, 15, 10, 53, 50, 34, 90, 76, 32, 85]

6
15
10
53
50
34
90
76
32
85
"""