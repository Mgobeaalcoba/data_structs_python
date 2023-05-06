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

- Arrays:

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