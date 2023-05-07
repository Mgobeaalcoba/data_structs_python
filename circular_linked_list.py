# Vamos a recrear el comportamiento de una circular_linked_list
# pero con la interacción de los nodos y sin crear la lista aún

from node import Node

# Creamos un solo nodo que se apunta a si mismo. Es decir, 
# tiene un comportamiento circular: 

index = 1
new_item = "ham"
head = Node(None, None)
head.next = head
probe = head

while index > 0 and probe.next != head:
    probe = probe.next
    index -= 1

probe.next = Node(new_item, probe.next)

print(probe.next.data)

"""
Output: 

13:21:08 👽 with 🤖 mgobea 🐶 in develop/python/data_structs_python took 5.3s …
➜ python3 circular_linked_list.py
ham
"""

# La clave es que el ultimo nodo apunte al primero siempre. 