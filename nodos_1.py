from node import Node

node1 = Node("Inicio")
node2 = Node("A", node1)
node3 = Node("B", node2)

print(f"node1: {node1}")
print(f"node1.data: {node1.data}")
print(f"node1.next: {node1.next}")
try:
    print(f"node1.next.data: {node1.next.data}")
except AttributeError as error:
    print(error)
print()
print(f"node2: {node2}")
print(f"node2.data: {node2.data}")
print(f"node2.next: {node2.next}")
try:
    print(f"node2.next.data: {node2.next.data}")
except AttributeError as error:
    print(error)
print()
print(f"node3: {node3}")
print(f"node3.data: {node3.data}")
print(f"node3.next: {node3.next}")
try:
    print(f"node3.next.data: {node3.next.data}")
except AttributeError as error:
    print(error)
print()

