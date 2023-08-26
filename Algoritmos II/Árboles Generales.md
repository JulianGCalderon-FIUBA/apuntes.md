Para cantidades grandes de datos, usamos los árboles. De esta forma, reducimos la complejidad computacional del algoritmo de búsqueda.

Hay distintos **tipos** de árboles:

- Árbol General.
- Árbol Binario.
- Árbol Binario de Búsqueda.
- Árbol AVL.
- Árbol Rojo Negro.
- Árbol B.
- Árbol B+.
- Árbol B*.
- Árbol Splay.

Los árboles tienen las siguientes **características**:

- **Nodo Padre:** Es la raíz del árbol principal
- **Nodo Hijo**: Es la raíz de un subárbol, derivado del árbol principal.
- **Nodo Hoja:** Son aquellos nodos que no contengan hijos
- **Camino:** Se define como la secuencia de nodos que se debe tomar para llegar al elemento deseado a partir del nodo padre.
- **Profundidad:** Cada nodo tiene una profundidad, definida como el número de nodos que hay que atravesar para llegar al nodo en cuestión.

## Iteradores de Árbol

Existe la posibilidad de recorrer el árbol de dos formas:

- Recorrido en profundidad
- Recorrido a lo ancho

Además, el recorrido en profundidad presenta tres caminos principales:

- **In-orden:** Este camino recorre los elementos de menor a mayor **(IND)**
- **Pre-orden:** Este camino es mejor para clonar un árbol **(NID)**
- **Post-orden:** Este camino es mejor para destruir un árbol **(IDN)**

> [!note] **IND** implica: primero izquierda, luego el nodo, por ultimo derecha

## Árbol Binario de Búsqueda

El árbol binario es aquel que cada nodo tiene permitido un máximo de **dos nodos.** Como es un árbol binario de búsqueda, entonces los elementos están ordenados. En el subárbol izquierdo están los nodos menores a la raíz, en el subárbol derecho están los nodos mayores. Esta lógica se cumple para todos los hijos.

## Árboles Binarios Equilibrados

Un árbol binario equilibrado es aquel en el que la altura de los subárboles izquierdo y derecho de cualquier nodo, nunca difiere en más de una unidad. De esta forma, el árbol no se degenera en lista y la complejidad continúa siendo $O(log(n))$

### Factor de Equilibrio

El factor de equilibrio es la diferencia entre las alturas del árbol derecho y el izquierdo

$$
FE = \text{altura arbol derecho} -\text{altura arbol izquierdo}
$$
