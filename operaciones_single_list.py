from node import Node

# Armo una serie de nodos encadenados uno dentro del otro en la variable head:
head = None
for count in range(1, 6):
    head = Node(count, head)

"""
while head != None:
    print(head.data) # Reminder: data es un atributo de la clase Node()
    head = head.next # Con esto y sabiendo que los nodos siempre apuntan a un lugar diferente evitamos el infinite loop.
"""

"""
Output: 

12:30:04 👽 with 🤖 mgobea 🐶 in develop/python/data_structs_python …
➜ python3 operaciones_single_list.py
5
4
3
2
1
"""

"""
# Replicamos lo hecho con head pero para con probe
probe = head
while probe != None:
    print(probe.data)
    probe = probe.next
"""

"""
Aquí no nos imprimé nada porque es una copia de head que ya se recorrio por completo.
Y porque probe va a tener otro uso que es ser una variable temporal que nos permite recorrer.
"""

# Codigo para encontrar un item en nuestra secuencia de nodos encadenados: 

probe = head # Para asegurarnos de que nuestra variable no apunte a ningún lugar.

target_item = 2

while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f"Taget item {target_item} has been found")
else:
    print(f"Target item {target_item} is not in the linked list")

"""
Output:

Target item 2 is not in the linked list
"""

# Codigo para reemplazar un item en nuestra secuencia de nodos encadenados:

probe = head
target_item = 3
new_item = "Z"

while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f"{new_item} replaced the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")

"""
Output:

The target item 3 is not in the linked list
"""

# Insertar un nuevo elemento o un nuevo nodo al principio (head) de nuestra cadena de nodos.

# Sabemos que el primer nodo es head, por lo que vamos a cargar allí el nuevo...
head = Node("F",head)

# Insertar un nuevo elemento o nodo al final de nuestra cadena de nodos:

new_node = Node("K") 
# Validamos que ya no tengamos valores en la lista y colocamos allí el nuevo nodo:
if head is None:
    head = new_node
# Y si los tenemos recorremos la cadena de nodos hasta encontrar el None y ahí guardar el nuevo elemento:
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = new_node 

# Imprimo mi cadena de nodos nuevamente: 
"""
while head != None:
    print(head.data) # Reminder: data es un atributo de la clase Node()
    head = head.next 
"""

"""
Output:

F
K
"""

# Eliminamos un elemento de nuestra cadena de nodos del principio: 

"""
removed_item = head.data
head = head.next
print(removed_item) # Eliminé la F de mi cadena de nodos.
"""

"""
Output:

F
"""

# Eliminamos un elemento de nuestra cadena de nodos del final:

"""
removed_item = head.data
if head.next == None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next.data
    probe.next = None
print(removed_item) # Eliminé la K de mi cadena de nodos.
"""

"""
Output:

K
"""

# Añadir un nodo en una posición determinada, ya no al principio ni al final:

"""
new_item = input("Enter new item: ")
index = int(input("Enter de position to insert the new item: "))

if head == None or index < 0:
    head = Node("Py", head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)

# Imprimo mi cadena para ver lo que agregué: 
while head != None:
    print(head.data) # Reminder: data es un atributo de la clase Node()
    head = head.next 
"""

"""
Va a servir para agregar en cualquier posición menos al principio. Para ello debemos usar
el metodo que está mas arriba para tales fines. 
"""

# Eliminar un nodo en una posición determinada:

index = int(input("Enter de position to delete the item: "))
if index <= 0 or head.next == None:
    removed_item = head.data
    head = head.next
    print(removed_item)
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removed_item = probe.next.data
    probe.next = probe.next.next
    print(f"The removed item was: {removed_item}")
    print()

# Imprimo mi cadena para ver la linked list sin ese elemento: 
while head != None:
    print(head.data) # Reminder: data es un atributo de la clase Node()
    head = head.next 












