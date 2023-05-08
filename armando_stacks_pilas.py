from stack import Stack

food = Stack()
food.push('egg')
food.push('ham')
food.push('spam')

# Voy a usar el metodo pop para sacar uno de ellos. Recordemos que también los devuelve: 
delete_item = food.pop()
print(delete_item)

# Voy a consultar que está arriba de mi stack: 
top_stack = food.peek()
print(top_stack)

# Voy a limpiar mi pila:
food.clear()

# Vuelvo a consultar el Top que se que está vacio:
top_stack = food.peek()
print(top_stack)

"""
C:\Users\mgobea\Documents\develop\Python\estructuras_de_datos(main -> origin)
(venv) λ python3 armando_stacks_pilas.py
spam
ham
The stack is empty
"""