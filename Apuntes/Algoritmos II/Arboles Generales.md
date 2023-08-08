Para cantidades grandes de datos, usamos los arboles. De esta forma, reducimos la complejidad computaicional del algoritmo de busqueda.

Hay distintos **tipos** de arboles:

- Árbol General
- Árbol Binario
- Árbol Binario de Búsqueda
- Árbol AVL
- Árbol Rojo Negro

- Árbol B
- Árbol B+
- Árbol B*
- Árbol Splay

Los arboles tienen las siguientes **características**:

- **Nodo Padre:** Es la raíz del árbol principal
- **Nodo Hijo**: Es la raíz de un sub-árbol, derivado del árbol principal.
- **Nodo Hoja:** Son aquellos nodos que no contengan hijos
- **Camino:** Se define como la secuencia de nodos que se debe tomar para llegar al elemento deseado a partir del nodo padre.
- **Profundidad:** Cada nodo tiene una profundidad, definida como el numero de nodos que hay que atravesar para llegar al nodo en cuestión.

# Iteradores de Árbol

Existe la posibilidad de recorrer el arbol de dos formas:

- Recorrido en profundidad
- Recorrido a lo ancho

Además el recorrido en profundidad presenta tres caminos principales:

- In-orden: Este camino recorre los elementos de menor a mayor **(IND)**
- Pre-orden: Este camino es mejor para clonar un árbol **(NID)**
- Post-orden: Este camino es mejor para destruir un árbol **(IDN)**

# Árbol Binario de Busqueda

El árbol binario es aquel que cada nodo tiene permitido un máximo de **DOS NODOS.** Como es un árbol binario de búsqueda, entonces los elementos están ordenados. En el sub-árbol izquierdo están los nodos menores a la raíz, en el sub-árbol derecho están los nodos mayores. Esta lógica se cumple para todos los hijos.

# Arboles Binarios Equilibrados

Un árbol binario equilibrado es aquel en el que la altura de los subárboles izquierdo y derecho de cualquier nodo, nunca difiere en más de una unidad. De esta forma, el árbol no se degenera en lista y la complejidad continua siendo $O(log(n))$

## Factor de Equilibrio

El factor de equilibrio es la diferencia entre las alturas del árbol derecho y el izquierdo

$$
FE = \text{altura arbol derecho} -\text{altura arbol izquierdo}
$$