from linked_list import SinglyLinkedList

# Instanceo una SinglyLinkedList
words = SinglyLinkedList()

# Agrego objetos Node() a mi SinglyLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")

# Necesitamos una variable auxiliar "current" que nos ayude
# a entender donde está el tail en nuestra lista
current = words.tail

# Recorro nuestra lista de nodos:
while current:
    print(current.data)
    current = current.next

print()

"""
22:28:09 👽 with 🤖 mgobea 🐶 in develop/python/data_structs_python …
➜ python3 single_linked_list_1.py
egg
ham
spam
"""

# Otra forma de iterar e imprimir los valores de nuestra lista
# de nodos es usando el metodo iter() que construí para tales fines:

for word in words.iter():
    print(word)

print()

"""
23:00:47 👽 with 🤖 mgobea 🐶 in develop/python/data_structs_python …
➜ python3 single_linked_list_1.py
egg
ham
spam

egg
ham
spam
"""

words.search("spam")
print()
words.search("juice")
print()

"""
23:12:20 👽 with 🤖 mgobea 🐶 in develop/python/data_structs_python …
➜ python3 single_linked_list_1.py
egg
ham
spam

egg
ham
spam

Data: spam found!

juice not found in the list!
"""

# Si limpio mi lista y luego reimprimo entonces no me mostrará
# nada dado que tail y head apuntan a None. 

print("Abajo no debería imprimirse nada:")

words.clear()
for word in words.iter():
    print(word)

print()

print("Fin.")

"""
23:12:53 👽 with 🤖 mgobea 🐶 in develop/python/data_structs_python …
➜ python3 single_linked_list_1.py
egg
ham
spam

egg
ham
spam

Data: spam found!

juice not found in the list!

Abajo no debería imprimirse nada:

Fin.
"""
