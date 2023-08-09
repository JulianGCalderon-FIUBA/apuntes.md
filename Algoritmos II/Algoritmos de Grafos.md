## Recorridos

Es una forma de atravesar el grafo, visitando cada vértice del mismo. El orden en el cual los vertices son visitados determina el tipo de recorrido.

### Breadth First Search

Primero se visitan todos los nodos vecinos antes de visitar los nodos mas lejanos. Para su implementación, se utiliza un cola.

1. Encolar un vértice
2. Desencolar un vértice (visitarlo)
3. Encolar los vertices adyacentes al actual
4. Repetir desde (2) hasta terminar

### Depth First Search

Se visita un nodo vecino primero, avanzando hasta que no se puede continuar. Luego se vuelve hasta donde se tenían mas caminos y se realiza la misma lógica. Para su implementación, se utiliza una pila.

1. Apilar un Vértice
2. Quitar un Vértice de la pila (visitarlo)
3. Apilar los vertices adyacentes al actual
4. Repetir desde (2) hasta terminar

### **Orden Topológico**

La idea del orden topológico es la de no visitar un vértice hasta haber visitado todos los vertices que conectan a el. De esta forma, devuelve un conjunto de vertices ordenado.

Para esto, utiliza la matriz de incidencia. Recorre todos los vertices cuyo grado de incidencia sea cero, luego "elimino" esos vertices y vuelve a recorrer los nuevos vertices cuyo grado de incidencia sea cero. (numero de vertices entrantes)

Una vez que me quedo sin elementos, habremos recorrido el grafo en orden topológico.

## Dijkstra

Es un algoritmo para determinar el camino mas corto dado un vértice origen, hacia el resto de los vertices en un grafo con pesos.

1. Se elige el vértice **V** sobre el cual se aplicara el algoritmo.
2. Se crean dos listas de nodos, una de nodos visitados, y otra de nodos no visitados. Esta contiene todos los nodos del grafo.
3. Se crea una tabla con tres columnas: Vértice, Distancia Minima V, y el nodo anterior por el cual se llego.
4. Se toma el vértice **V** como vértice inicial, su distancia a si mismo es cero.
5. Se actualiza la tabla, en la cual todas las distancias de los demás vertices se marcan como infinito.
6. Se visita el vértice no visitado con menor distancia conocida desde el primer vértice V, que es el vértice con el que comenzamos ya que la distancia a ese es 0 y las demás infinito.
7. Se calcula la distancia entre los vertices sumando los pesos de cada uno con la distancia de V
8. Si la distancia calculada de los vertices conocidos es menor a la que esta en la tabla se actualiza y también los vertices de donde se llegó.
9. Se pasa el vértice V a la lista de vertices visitados.
10. Se continua con el vértice no visitado con menor distancia desde ese.

## Floyd

El algoritmo de Floyd consiste en encontrar el camino mínimo entre todos los pares de vertices.

Empezamos por crear la matriz de adyacencia, la que nos muestra la distancia entre los vertices

Para realizar esto, parto de un vértice $v_0$, y luego para cada par de vertices $v_1, v_2$, calculo el mínimo entre los caminos $[v_1 → v_2\;\ v_1 \to v_0 \to v_2]$. Actualizo con la menor de las distancias en la matriz.

Una vez hayamos iterado todos los vertices, tendremos una matriz que indica la minima distancia entre todos los vertices.

Luego, si queremos reconstruir los caminos, debemos almacenar que recorrido se tomo para cada valor actualizado (cual fue el vértice intermedio).

La complejidad de este algoritmo es de $O(n^3)$

## Prim

Este algoritmo permite encontrar un subconjunto de aristas que forman un árbol con todos los vertices, donde el peso total es el mínimo posible. Se puede encontrar siempre y cuando el grafo sea conexo, no dirigido. Si no es pesado, entonces el camino que elija sera completamente arbitrario.

Para esto, parte con un árbol con únicamente el nodo inicial. Luego, agrega un vértice no perteneciente al árbol (pero vecino a alguno de sus nodos) cuya arista tenga el menor peso posible.

El algoritmo continua hasta que no pueda agregar mas vertices.

## Kruskal

Este algoritmo hace lo mismo que el algoritmo de Prim

Para esto, comienza con un árbol para cada vértice del grafo. Luego busca la menor arista y une los dos arboles que conecta. Si los vertices pertenecen al mismo árbol, entonces no lo une. (esto generaría un ciclo)

El algoritmo continua hasta que no pueda unir mas arboles.
