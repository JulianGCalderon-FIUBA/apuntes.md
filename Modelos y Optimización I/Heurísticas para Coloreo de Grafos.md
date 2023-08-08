Inicialmente se resuelve el modelo con relajación lineal. Recordemos que la solución obtenida no servirá, ya que siempre encontrará que la solución óptima será la utilización de dos colores. Todos los nodos del grafos se colorean a la mitad, con ambos colores.

> ***Teorema de Appel-Hanke:*** Un grafo planar es al menos **4-**coloreable. Este teorema fue demostrado con la ayuda de una computadora, categorizando los grafos planares en clases (con una cantidad finita de clases) y demostrando (por fuerza bruta) la condición para cada clase.
> 

## Heurística Greedy

Un ejemplo de ***heurística golosa*** podría ser el siguiente:

1. Construyo una lista de vertices no pintados y parto de un color inicial.
2. Pinto vertices de la lista con el color seleccionado hasta llegar a un vértice que no puedo pintar con dicho color.
3. Selecciono un nuevo color y vuelvo al paso anterior.
4. Una vez pinte todos los vertices, habré formado un coloreo valido

Esta heurística puede fallar, por ejemplo, al pintar un grafo bipartito completo ordenando los vertices de forma intercalada entre ambas clases. Cada vértice se deberá pintar con un color nuevo, alcanzando el máximo de colores posibles (todos los vertices de un color distinto). Si en cambio, se ordenan los vértices colocando todos los vertices de una clase primero, entonces la solución óptima sera la correcta (dos colores)

### Heurística DSATUR

La heurística ***largest saturation degree (don satur)*** parte de pintar los tres vertices de mayor grado de tres colores distintos.

### Heurística RLF

Similar a la anterior ***heurística***, pero tiene un algoritmo más complejo, y recursivo.

# Meta-heurística MACOL

Trabaja sobre un algoritmo memético (un tipo de algoritmo genético). Se usa un algoritmo genético combinando ***Tabu Search***.

Se busca un $k$-coloreo valido, en caso de encontrarlo, se busca un $k'$-coloreo valido mejor. A medida que disminuye $k$, el problema se vuelve mas difícil.

Se define una solución de evaluación $f$ que mide la cantidad de conflictos que tiene una solución 

## Algoritmo

1. Se define una población inicial $P$ utilizando `initial_population()`.
2. A cada solución obtenida, se le aplica `tabu_search()`.
3. Se toma la solución óptima actual $S^*$ como la de menor conflictos.
4. Hasta que se cumpla la condición de corte:
    1. Se eligen $m$ individuos de la población.
    2. Se aplica `adaptive_multi_parent_crossover()` para los individuos seleccionados.
    3. A la solución obtenida, se le aplica `tabu_search()`.
    4. Si la solución actual es mejor que la optima (tiene menos errores), se actualiza,
    5. Se aplica `pool_updating()` para todos los individuos seleccionados, incluyendo el generado por el crossover y se actualizan en la población.

## Initial Population

Se utiliza una versión aleatorizada de la heurística ***DANGER***. El proximo vértice a colorear se elige en base a su índice de riesgo. El color a asignar se toma con el mismo criterio. Los valores de riesgo se toan como una probabilidad de elección del color o vértice.

Si el nuevo $k$-coloreo obtenido es muy parecido a los ya obtenidos, se lo descarta y se busca uno nuevo. Para esto, se toma una función de distancia entre dos coloreos, a partir de la cual se deriva una función de distancia entre un coloreo y una población.

## Tabu Search

Se define una función de evaluación $f$ como la suma de los vertices en conflicto. Luego, se obtiene un vecino de un coloreo dado cambiando el color de un vértice en conflicto.

Una vez que se efectúa el movimiento, se prohíbe al vértice a volver al color anterior por una cantidad determinada de iteraciones.

Esto se repite, y la condición de corte es la cantidad de iteraciones.

## Adaptive Multi-Parent Crossover

*AMPaX* Es una extensión del algoritmo ***GPX (Greedy Partition Crossover)***. Toma como entrada dos particiones, y devolverá una nueva partición mejorada.

## Pool Updating

Se toma un conjunto de soluciones y se busca mejorarlas a partir de calcular una puntuación de solución. Esta puntuación busca equilibrar calidad con variedad de soluciones. A medida que se mejoran las soluciones, la diversidad disminuye

## Conclusión

El éxito de MACOL frente a otras heurísticas de coloreo de grafos resalta el papel fundamental de los mecanismos de generación de diversidad para evitar la convergencia prematura y permitir explorar el espacio de soluciones