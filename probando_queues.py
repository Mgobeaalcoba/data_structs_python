from list_based_queue import ListQueue

my_queue = ListQueue()
print(my_queue.items) # []
print(my_queue.size) # 0

my_queue.enqueue("Mariano")
my_queue.enqueue("Nicole")
my_queue.enqueue("Lisandro")
my_queue.enqueue("Lautaro")

print(my_queue.items) # ['Lautaro', 'Lisandro', 'Nicole', 'Mariano']
print(my_queue.size) # 4

my_queue.traverse

print(my_queue.dequeue()) # Mariano
print(my_queue.items) # ['Lautaro', 'Lisandro', 'Nicole']
print(my_queue.size) # 3
