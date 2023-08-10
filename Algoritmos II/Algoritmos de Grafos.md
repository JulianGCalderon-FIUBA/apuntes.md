## Recorridos

Es una forma de atravesar el grafo, visitando cada vértice del mismo. El orden en el cual los vértices son visitados determina el tipo de recorrido.

### Breadth First Search

Primero se visitan todos los nodos vecinos antes de visitar los nodos más lejanos. Para su implementación, se utiliza una cola.

1. Encolar un vértice
2. Desencolar un vértice (visitarlo)
3. Encolar los vértices adyacentes al actual
4. Repetir desde (2) hasta terminar

### Depth First Search

Se visita un nodo vecino primero, avanzando hasta que no se puede continuar. Luego se vuelve hasta donde se tenían más caminos y se realiza la misma lógica. Para su implementación, se utiliza una pila.

1. Apilar un Vértice
2. Quitar un Vértice de la pila (visitarlo)
3. Apilar los vértices adyacentes al actual
4. Repetir desde (2) hasta terminar

### **Orden Topológico**

La idea del orden topológico es la de no visitar un vértice hasta haber visitado todos los vértices que conectan a él. De esta forma, devuelve un conjunto de vértices ordenado.

Para esto, utiliza la matriz de incidencia. Recorre todos los vértices cuyo grado de incidencia sea cero, luego "elimino" esos vértices y vuelve a recorrer los nuevos vértices cuyo grado de incidencia sea cero. (número de vértices entrantes)

Una vez que me quedo sin elementos, habremos recorrido el grafo en orden topológico.

## Dijkstra

Es un algoritmo para determinar el camino más corto dado un vértice origen, hacia el resto de los vértices en un grafo con pesos.

1. Se elige el vértice **V** sobre el cual se aplicara el algoritmo.
2. Se crean dos listas de nodos, una de nodos visitados, y otra de nodos no visitados. Esta contiene todos los nodos del grafo.
3. Se crea una tabla con tres columnas: Vértice, Distancia mínima V, y el nodo anterior por el cual se llegó.
4. Se toma el vértice **V** como vértice inicial, su distancia a sí mismo es cero.
5. Se actualiza la tabla, en la cual todas las distancias de los demás vértices se marcan como infinito.
6. Se visita el vértice no visitado con menor distancia conocida desde el primer vértice V, que es el vértice con el que comenzamos, ya que la distancia a ese es 0 y las demás infinito.
7. Se calcula la distancia entre los vértices sumando los pesos de cada uno con la distancia de V
8. Si la distancia calculada de los vértices conocidos es menor a la que está en la tabla se actualiza y también los vértices de donde se llegó.
9. Se pasa el vértice V a la lista de vértices visitados.
10. Se continúa con el vértice no visitado con menor distancia desde ese.

## Floyd

El algoritmo de Floyd consiste en encontrar el camino mínimo entre todos los pares de vértices.

Empezamos por crear la matriz de adyacencia, la que nos muestra la distancia entre los vértices

Para realizar esto, parto de un vértice $v_0$, y luego para cada par de vértices $v_1, v_2$, calculo el mínimo entre los caminos $[v_1 → v_2\;\ v_1 \to v_0 \to v_2]$. Actualizo con la menor de las distancias en la matriz.

Una vez hayamos iterado todos los vértices, tendremos una matriz que indica la mínima distancia entre todos los vértices.

Luego, si queremos reconstruir los caminos, debemos almacenar qué recorrido se tomó para cada valor actualizado (cuál fue el vértice intermedio).

La complejidad de este algoritmo es de $O(n^3)$

## Prim

Este algoritmo permite encontrar un subconjunto de aristas que forman un árbol con todos los vértices, donde el peso total es el mínimo posible. Se puede encontrar siempre y cuando el grafo sea conexo, no dirigido. Si no es pesado, entonces el camino que elija será completamente arbitrario.

Para esto, parte con un árbol con únicamente el nodo inicial. Luego, agrega un vértice no perteneciente al árbol (pero vecino a alguno de sus nodos) cuya arista tenga el menor peso posible.

El algoritmo continúa hasta que no pueda agregar más vértices.

## Kruskal

Este algoritmo hace lo mismo que el algoritmo de Prim

Para esto, comienza con un árbol para cada vértice del grafo. Luego busca la menor arista y une los dos árboles que conecta. Si los vértices pertenecen al mismo árbol, entonces no lo une. (esto generaría un ciclo)

El algoritmo continúa hasta que no pueda unir más árboles.
