from node import Node

head = None

print("Antes del for: ")
print(f"head es de tipo: {type(head)}")

# Estoy metiendo un nodo adentro del otro. Es fantastico... Todos quedan guardados dentro de head:
for count in range(1,5):
    head = Node(count, head)

print("Despues del for pero antes del while: ")
print(f"head es de tipo: {type(head)}")

# Imprimo todos los nodos anidados uno dentro del otro: 
while head != None:
    print(f"head.data: {head.data}")
    print(f"head.next: {head.next}")
    try:
        print(f"head.next.data: {head.next.data}")
    except AttributeError as error:
        print(error)
    head = head.next

# Al recorrer el while hasta el None vacío mi nodo y deja de ser una variable tipo nodo para ser nuevamente una variable tipo None
print("Despues del while: ")
print(f"head es de tipo: {type(head)}")

"""
Output: 

22:21:24 👽 with 🤖 mgobea 🐶 in develop/python/data_structs_python …
➜ python3 nodos_2.py
Antes del for:
head es de tipo: <class 'NoneType'>
Despues del for pero antes del while:
head es de tipo: <class 'node.Node'>
head.data: 4
head.next: <node.Node object at 0x7f4135e40640>
head.next.data: 3
head.data: 3
head.next: <node.Node object at 0x7f4135e40490>
head.next.data: 2
head.data: 2
head.next: <node.Node object at 0x7f4135e406d0>
head.next.data: 1
head.data: 1
head.next: None
'NoneType' object has no attribute 'data'
Despues del while:
head es de tipo: <class 'NoneType'>
"""
