from stack_based_queue import Queue

numbers = Queue()

numbers.enqueue(5)
numbers.enqueue(6)
numbers.enqueue(7)

# Veamos que hay en nuestro inbound_stack:

print(numbers.inbound_stack) # [5, 6, 7]

# Saco un numero y debería salir el primero que entró es decir el 5. FIFO

print(numbers.dequeue()) # 5

# Verifico que inbound_stack haya quedado vacia y los datos restantes hayan pasado
# a outbound_stack:

print(numbers.inbound_stack) # []
print(numbers.obtbound_stack) # [7, 6]

# ¿por que quedó al reves que como ingreso. Porque de una stack a la otra lo quite 
# usando pop que es como funcionan las Queues. FIFO. Luego al eliminar con pop 
# estoy eliminando el primero que ingreso, en lugar del ultimo, que es lo hace pop,
# porque al pasar de un stack a otro se invirtió el orden. Pero eliminar el primero,
# o sea el 5 es lo que debe hacerse en una Queue que es lo que tenemos. 
