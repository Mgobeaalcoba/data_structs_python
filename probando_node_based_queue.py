from node_based_queue import Queue

food = Queue()
food.enqueue("eggs")
food.enqueue("ham")
food.enqueue("spam")

# Veamos ahora que tenemos en nuestro head de la Queue:

print(food.head.data) # eggs

# ¿Como puedo acceder al proximo elemento de mi lista de nodos? 
# Recordemos que no existen indices en las listas enlazadas de nodos.
# Facil:

print(food.head.next.data) # ham

# ¿Y al tercer elemento?

print(food.head.next.next.data) # spam

# Y si la recorremos para atras? 

print(food.tail.data) # spam

print(food.tail.previous.data) # ham

print(food.tail.previous.previous.data) # eggs

# contemos cuantos elementos hay:

print(food.count) # 3

# Y si removemos un elemento cual debería salir? "eggs" porque fue el primero en ingresar:

# print(food.dequeue())

# Iterando mi queue de nodos de forma completa:
count = 1
for item in food.iter():
    print(f"{count}: {item}")
    count += 1
