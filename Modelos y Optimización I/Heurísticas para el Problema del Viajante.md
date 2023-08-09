El problema del viajante requiere, por fuerza bruta, verificar $n!$ posibles configuraciones, siendo $n$ la cantidad de ciudades. Para grandes cantidades de ciudades, esto se vuelve insostenible. Debido a esto, se utilizan heurísticas.

## Heurística del Vecino mas Proximo

1. Se empieza por un vértice inicial cualquiera, se puede utilizar una heurística para elegirla
2. Mientras que queden ciudades sin visitar, se agrega la ciudad mas cercana a la ciudad actual.
3. Cuando no queden mas ciudades, se une la ultima ciudad con la primera

Este algoritmo parece dar buenas soluciones inicialmente, pero su desempeño empeora cuantas menos ciudades queden por elegir

## Heurística del Emparchamiento mas Cercano

1. Elegir la arista con menor costo, si hay mas de uno, elegir por orden alfabético.
2. Mientras que queden ciudades sin agregar al tour, elegir la arista restante con menor costo que no genere subtours y que incida en alguno de los extremos. (se debe mantener un camino)
3. Cuando no queden mas ciudades, se une la ultima ciudad con la primera.

Esta heurística es similar a la del vecino mas proximo, pero permite analizar las aristas desde ambos extremos.

## Heurística de la Inserción mas Cercana

1. Se empieza por una ciudad inicial cualquiera.
2. Mientras que queden ciudades sin agregar, y para cada una, se evalúa agregarla al final del recorrido. Se elige la alternativa de menor costo.

## Heurística del Árbol Generador Mínimo

Requiere que se respete la desigualdad triangular entre las ciudades, es decir

$$
\forall u,v,w \in V(G): d(u,v) + d (v,w) \geq d(u,w)
$$

1. Se arma un árbol de costo mínimo *(prim* o *kruskal)*
2. Definimos la raíz como un vértice arbitrario
3. Se duplican las aristas y se halla un camino euleriano. ***(DFS)***
4. Se toman los vertices de este camino, ignorando los repetidos.
5. El camino encontrando será un camino ***hamiltoniano***.

## Heurística de $k$-intercambios

Es una heurística de mejora, parte de una solución factible inicial. Esta puede ser la trivial, dada por el orden alfabético de las ciudades. Opera bajo una propiedad importante de los grafos:

> Si un ciclo *hamiltoniano* se cruza a si mismo, puede ser fácilmente mejorado eliminando las aristas que se cruzan y volviendo a unir los caminos con aristas que no se unan.
>

1. Se eliminan $k$ aristas del grafo
2. Se reúnen los caminos con $k$ aristas nuevas
3. Si el costo del nuevo camino es mejor al anterior, entonces se actualiza la solución optimo

Estos algoritmos no prueban todos los posibles cambios, sino que buscan alternativas durante un tiempo determinado y si no lo encuentran, finalizan.

## Heurística de Lin y Kerninghan

Es una variación de la heurística de $k$-intercambios. Busca decidir en cada momento, el valor de $k$ apropiado. Al igual que la la heurística de los intercambios, es una heurística muy costosa, por lo que no se suele realizar de forma completa.

1. Se define marca como verdadero
2. Mientras que marca sea verdadero
	1. Se define marca como falso y se etiquetan todos los nodos como no explorados
	2. Mientras que queden nodos sin explorar:
		1. Seleccionar un nodo $i$ no explorado y caminar todos los movimientos (**2-opt, inserción)** que incluyan la arista $i$ y a su sucesor. Luego, se marca como explorado
		2. Si alguno de los movimientos reduce la longitud del tour, establecer como solución actual y definir marca como uno.
