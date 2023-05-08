# Estructura de datos en Python 

### Tipos de colecciones

Nos referimos a las estructuras de datos. Una colección es un grupo de cero o más elementos que pueden tratarse como una unidad conceptual.

**Tipos de datos.**

- Non-zeo Value
- Cero
- null
- undefined

Estos tipos de dato también pueden formar parte de una colección. Existen **colecciones** de tipo Dinámicas que son aquelas que pueden variar su tamaño y las Inmutables que no cambian su tamaño.

**Estructuras Lineales**

De forma general encontramos estructuras de datos lineales que están definidas por sus índices. Es decir puedo encotnrarme estrcuturas de datos lineales que sean dinámicas o inmutables, de ello variarán sus propiedades, como poner un elemento al final, (sucesor) o no.

Te encontrarás con Listas, Listas Ordenadas, Cola, Cola de prioridad y más.

Es decir está ordenadas por posición.
Solo el primer elementono no tiene predecesor

Ej:

- Una fila para un concierto
- Una pila de platos por lavar, o una pila de libros por leer.
- Checklist, una lista de mercado, la lista de Schindler
- Estructuras Jerárquicas
- Estructuras basadas en una jerarquia definida.
- Los árboles pueden tener n números de nieleves hacia abajo o adyacentes. Te encotnrarás con árboles Binarios, Montículos.

**Ordendas como árbol invertido (raices)**

Solo el primer nodo no tiene predecesores, pero si sucesores.
Es un sistema de padres e Hijos.

Ej:

- Libros, Capítulos, Temas.
- Abuelos, Madres, Hijos.

**Estructuras Grafos:**

Cada dato puede tener varios predecesores y sucesores, se les llama vecinos
Los elementos se relecionan entre si con n relaciones.

Ej:

- Vuelos aéreos, sistemas de recomendación
- La mismísima internet es un grafo
  
**Estructuras Desordenadas:**

Estructuras como Bolsa, Bolsa ordenada, Conjuntos, DIccionarios, Diccionario ordenados.

No tienen orden en particular

No hay predecesores o sucesores.

Ej:

- Una bolsa de gomitas, no sabe de qué color te va a tocar.
  
**Estructuras Ordenadas:**

Son estructuras que imponen un orden con una regla. Generalmente una regla de orden.
item <= item(i+1) Es decir que el tiem que sigue es el primer elemento +1.

Ej:

- Los directorios telefónicos, los catálogos
  
**Conclusión:**

Suponga que tiene un dataset con muchos datos, una colección de libros, música, fotos, y desea ordenar esta colección, ante esta situación siempre existe el Trade Off entre rapidez/costo/memoria El conocimeinto de las propiedades de las colecciones te facilitará la selección de estructura de datos según sea el caso y velar por un software eficiente

--------------------------------

colecciones de datos incorporadas en python:

- Listas []
- Tuplas ()
- Sets {} o set()
- Diccionarios {key:value}

---------------------------------------------

### Estructuras de datos NO incorporadas en python pero que es posible construir como clases y luego usarlas: 

- **Arrays:**

Es una estructura de datos lineal, las estructuras de datos son representaciones internas de una colección de información, por lo que un array puede representarme de una forma particular y con unas características puntuales.

Elemento: Valor almacenado en las posiciones del array
Indice: Referencia a la posición del elemento.
En a memoria los arrays se almacenan de manera consecutiva, los bits se guardan casilla por casilla consecutivamente.

El array tiene una capacidad de almacenamiento. Puedo tener arrays en 1,2 y/o 3 dimensiones. A mayor complejidad dimensional, es decir, si aumenta la dimensión se hace más complicado acceder a estos datos, se recomienda en python trabajar con dimensiones <2

NOTA: Los arrays son un tipo de listas, pero las listas no son arrays. Los arrays son diferentes y poseen las siguientes restricciones:

No pueden:

- Agregar posiciones
- Remover Posiciones
- Modificar su tamaño
- Su capacidad se define al crearse

Los arrays se usan en los sprites de los videojuegos, o en un menú de opciones. Son opciones definidas.

El módulo array de python solo almacena números y caracteres, está basado en listas. Sin embargo tiene funciones reducidas, pero podemos crear nuestros propios arrays.

----------------------------

- **Nodes y singly linked list**

Las estructuras linked consisten en nodos conectados a otros, los más comunes son sencillos o dobles. No se accede por índice sino por recorrido. Es decir se busca en la lista de nodos hasta encontrar un valor.

- Data: Será el valor albergado en un nodo.
- Next: Es la referencia al siguiente nodo en la lista
- Previous: Será el nodo anterior.
- Head: Hace referencia al primer nodo en la lista
- Tail: Hace referencia al último nodo.

*¿Cómo funciona en memoria los Linked Estructures?*

Estas estructuras de datos hablan de nodos/datos repartidos en memoria, diferentes a los arrays que son contiguos. Los nodos se conectan a diferentes espacios en memoria, podemos acceder a los datos saltando en memoria, siendo mucho más ágil. Los nodos nos sirven para crear otras estructuras más complejas, como Stacks, Queues, las llamadas pilas y colas. Es posible optimizar partes del código usando nodos.

*Double Linked Structure.*

Estos hacen que el nodo haga referencia al siguiente nodo y al anterior, es decir nos va a permitir ir en ambas direcciones. También nos permitirá realizar “formas” y contextos circulares.

El ejemplo clave aquí será función de ctrl+z y ctrl+y Estas opciones nos permiten hacer y deshacer un proceso en Windows.

El historial del navegador también es un buen ejemplo al permitirnos navegar entre el pasado y el presente.

**Nota: Los linked list tienen una desventaja importante, si la lista crece mucho será más costoso computacionalmente recorrer toda la lista.**

Es importante saber cuando usarlas y cuando no.

----------------------------------

Como se puede ver en las practicas realizadas con nodos (nodos_1 y nodos_2) trabajar con nodos puede volverse algo confuso y el codigo volverse poco claro. Puede servirnos para trabajar con pocos datos. Pero con muchos datos ya es mas complejo. Para ello es que viene a solucionar la complejidad de este codigo las **"singly linked list"**

**Lista enlazada lineal simple (singly linked list) – Implementación en Python**

Una lista enlazada (linked list en inglés), es un tipo de estructura de datos compuesta de nodos. Cada nodo contiene los datos de ese nodo y enlaces a otros nodos.

Se pueden implementar distintos tipos de listas enlazadas. En este post vamos a implementar una lista enlazada lineal simple (singly linked list). En este tipo de listas, cada nodo contiene sus datos y un enlace al siguiente nodo. Además la lista tendrá un método para contar el número de elementos de la lista, un método para insertar un elemento en la lista y un método para eliminar un elemento de la lista.

En primer lugar, definimos una clase que va a ser la clase Node. Los objetos de esta contendrán sus propios datos y un enlace al siguiente elemento de la lista:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

A continuación definimos la clase de la lista SinglyLinkedList, que contiene el primer elemento de la lista:

```python
class SinglyLinkedList:
    def __init__(self, head):
        self.head = head
```

El método que cuenta los elementos de la lista, length(), primero comprueba que la lista no esté vacía, y luego recorre todos los elementos de la lista incrementando un contador por cada elemento. Al final devuelve el contador:

```python
    def length(self) -> int: 
        current = self.head
        if current is not None:
            count = 1

            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0
```

El siguiente método, insert(datos, posición), inserta un elemento tras la posición indicada. Si se indica la posición 0, el nuevo elemento pasa a ser la cabecera de la lista. En esta implementación, si la posición que se pasa como argumento excede el tamaño de la lista,el elemento se inserta al final:

```python
   def insert(self, data, position):
       new_node = Node(data)

       if position == 0:
           new_node.next = linked_list.head
           linked_list.head = new_node
       else:
           current = linked_list.head
           k = 1
           while current.next is not None and k < position:
               current = current.next
               k += 1
           new_node.next = current.next
           current.next = new_node
```

El método delete(posición) borra el elemento en la posición pasada como parámetro. Si es el primer elemento la lista de la cabeza pasa a ser el segundo elemento. Si se encuentra el elemento en la lista y se borra devolvemos True, en caso contrario devolvemos False:

```python
    def delete(self, position):
       if position != 1:
           current = self.head
           k = 1
           while current.next is not None and k < position - 1:
               current = current.next
               k += 1
           if current.next is not None:
               current.next = current.next.next
               return True
           else:
               return False
       else:
           self.head = self.head.next
           return True
```

Creamos la lista

```python
linked_list = SinglyLinkedList(Node(1))
```

Rellenamos la lista

```python
 for i in range(2,10):
        linked_list.insert(i, i-1)
```

Insertamos un elemento

```python
    linked_list.insert(999,3)
```

Eliminamos un elemento

```python
    linked_list.delete(6)
```

Mostramos la lista

```python
    current = linked_list.head
    while current is not None:
	print(current.data)
        current = current.next
```

---------------------------------------

**Circular Linked Structure**

A diferencia de las linear linked structure en este caso el tail o ultimo nodo no apunta mas a None sino que apunta nuevamente al head o primer nodo. 

Las listas enlazadas circulares tienen bastantes casos de uso interesantes:
- Dar la vuelta al turno de cada jugador en un juego multijugador
- Gestionar el ciclo de vida de la aplicación de un sistema operativo determinado
- Implementando un montón de Fibonacci

Una de las ventajas de las listas enlazadas circulares es que puede recorrer toda la lista comenzando en cualquier nodo. Dado que el último nodo apunta al headde la lista, debe asegurarse de dejar de atravesar cuando llegue al punto de partida. De lo contrario, terminarás en un bucle infinito.

En términos de implementación, las listas enlazadas circulares son muy similares a la lista enlazada individualmente. La única diferencia es que puede definir el punto de partida cuando recorre la lista:

Para generar el Cirle Linked List solo hay que poner esto y modificar algunas cosas de la clase Single Linked List...

1- Su circular linked list

```python
class CircularLinkedList(LinkedList):
    def __init__(self) -> None:
        super().__init__()

    def append(self, data):
        super().append(data, self.head)
```

2- Modificar las primeras líneas del append así:

```python
def append(self, data, next = None):
        node = Node(data, next)
```

3.- Modificar los whiles en la Linked List original de la siguiente forma:

```python
i = self.size
            while current.next and i>=0:
                current = current.next
                i -= 1
            current.next = node
```

--------------------------------------------------

**listas doblemente enlazadas**

Las listas doblemente enlazadas se diferencian de las listas enlazadas individualmente en que tienen dos referencias:

- El previous campo hace referencia al nodo anterior.
- El next campo hace referencia al siguiente nodo.

Este tipo de implementación le permitiría atravesar una lista en ambas direcciones en lugar de solo atravesar usando next. Puede utilizar next para avanzar y previous retroceder.

--------------------------------------------

**Stacks o pilas**

Las pilas (stacks) son una estructura de datos donde tenemos una colección de elementos, y sólo podemos hacer dos cosas:

- añadir un elemento al final de la pila
- sacar el último elemento de la pila

Una manera común de visualizar una pila es imaginando una torre de panqueques, donde una vez que ponemos un panqueque encima de otro, no podemos sacar el anterior hasta que se hayan sacado todos los que están encima.

A pesar de su simplicidad, las pilas son estructuras relativamente comunes en ciertas áreas de la computación, en especial para implementar o simular evaluación de expresiones, recursión, scope, …

LIFO (Last In First Out)

Las pilas son estructuras de tipo LIFO, lo cual quiere decir que el último elemento añadido es siempre el primero en salir.

De alguna forma, podemos decir que una pila es como si fuera una lista o array, en el sentido que es una colección, pero a diferencia de los arrays y otras colecciones, en las pilas solo accedemos al elemento que esté “encima de la pila”, el último elemento. Nunca manipulamos ni accedemos a valores por debajo del último elemento.


