from node import Node, TwoWayNode

head = TwoWayNode(1)
tail = head

# Necesitamos mas nodos para que esto funcione: 
for data in range(2,6):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next

# Usemos probe para hacer el recorrido y saber que hay en estos nodos:
probe = tail

# Iteramos para mostrar los datos:
while probe != None:
    print(probe.data)
    probe = probe.previous

# De la forma anterior estamos recorriendo el nodo de forma inversa. Es decir
# Lo recorremos iterando el nodo previo. 

"""
C:\Users\mgobea\Documents\develop\Python\estructuras_de_datos(main -> origin)
(venv) λ python3 armando_nodos_dobles.py
5
4
3
2
1
"""
