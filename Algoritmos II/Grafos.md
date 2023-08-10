Es un conjunto de vértices y aristas, que determinan conexiones entre los vértices. Es útil al estudiar las relaciones entre unidades que interactúan entre sí. Por ejemplo, una red de computadores puede representarse y estudiarse mediante un grafo.

## Clasificación

**Según su Dirección:**

- **Grafo no Dirigido:** Todas sus aristas son bidireccionales.
- **Grafo Dirigido:** Tiene al menos una arista unidireccional.

**Según su Peso:**

- **Grafo Pesado**: Las aristas tienen asignadas un peso, representa el costo de tomar ese camino.

**Según su complejidad:**

- **Grafo Simple:** Es aquel que no posee aristas múltiples ni lazos. Entre dos vértices, solo hay como máximo un camino posible.
- **Grafo Denso**: Es aquel cuyo número de aristas está muy cerca del valor máximo que puede tener

	Para el caso de un grafo simple, el índice de densidad equivale a

	$$
    D = \frac{2\cdot E}{V \cdot (V - 1)}
    $$

	Siendo $D$ el índice de densidad, $E$ la cantidad de aristas y $V$ la cantidad de vértices.

- **Grafo Completo:** Sí posee todas las aristas posibles $(D = 1)$

## Definiciones

### Ciclos

Un ciclo es un recorrido de aristas adyacentes que empieza y termina en un mismo lugar. No todos los grafos contienen ciclos

![[Grafos 1.svg|550]]

### Camino

Un camino es un recorrido a través de un grafo.

**Definiciones:**

- **Camino Simple:** Es aquel que no recorre dos veces el mismo vértice.
- **Camino Cerrado:** Es aquel que termina en el vértice en el que comenzó.
- **Componente Conexa:** Conjunto de vértices del grafo en el cual existe un camino que conecta todo par de vértices entre sí.

	Si el grado es dirigido *(digrafo)*, entonces surgen dos definiciones más

	- **Fuertemente Conexo:** Todo vértice conecta con cualquier vértice
	- **Débilmente Conexo:** Todo par de vértices está conectado, aunque el camino puede no ser bidireccional

### Arbol

Un grafo es un árbol si es tanto conexo como acíclico.

### Grado de Vértice

El grado de vértice es la cantidad de aristas que tiene un vértice. En el caso de grafos no dirigidos, se diferencia en grado de entrada y grado de salida.

El grado de entrada indica la cantidad de aristas que entran al vértice. El grado de salida indica la cantidad de aristas que salen del vértice.

## Representación de Grafos

### Matriz de Adyacencia

La matriz de adyacencia registra las conexiones entre los vértices. Las filas y columnas representan las vértices, y una posición determinada de la matriz representa, si existe o no, conexión entre esos vértices.

Se coloca un $1$ en las posiciones en las que existe una arista, y un 0 en las que no.

La diagonal de la matriz representa los lazos del grafo. (Aquellos vértices que conectan con ellos mismos)

Si el grafo es pesado, entonces en lugar de colocar un $1$ donde hay una arista, colocamos su peso.

> [!note]
> En un grafo no dirigido, la matriz sera una matriz simétrica.

### Lista de Adyacencia

Cada vértice tiene asociada una lista que contiene los vértices con los que conecta. Si conecta dos veces con el mismo vértice, es recomendable agregar un nuevo elemento a la lista.

Es útil ya que no tenemos posiciones vacías, como en la matriz de adyacencia.

En el caso de grafos pesados, solo debemos incluir el peso en los elementos de la lista.

### Matriz de Incidencia

Las filas de la matriz representan las aristas, las columnas de la matriz representa los vértices.

Colocamos un $1$ si la arista conecta con ese vértice. En el caso de grafos dirigidos, colocamos un $1$ si es entrante, y un $-1$ si es saliente.

En el caso de grafos pesados, colocamos el peso en lugar de un $1$.
