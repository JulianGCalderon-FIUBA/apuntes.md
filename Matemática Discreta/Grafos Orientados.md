En los grafos orientados, sus aristas son orientadas. Esto es, una arista del vértice $u$ al vértice $v$, no indica un camino del vértice $v$ hacia el vértice $u$. Para los grafos orientados, valen las mismas definiciones que para los grafos vistos anteriormente, con las salvedades que esta definición causa.

Para la matriz de adyacencia, diremos que $u$ es adyacente a $v$ únicamente si existe una arista orientada de $u$ hacia $v$.

Para la matriz de incidencia, definiremos con un $1$ si la arista parte del vértice, y con un $-1$ si la arista llega al vértice.

Para los grados de un grafo, tendremos el grado entrante $d^+$ *(indeg)* y el grado saliente $d^-$ *(outdeg)*. Esto es, el número de aristas que salen o entran a un vértice. De igual forma, definimos las sucesiones $d^+, d^-$. Estas, al igual que antes, se definen en orden no creciente.

Por el conocido *handshaking di-lemma*, la suma de grados entrantes debe ser igual a la suma de grados salientes, y cada suma, a su vez, equivale a la cantidad de aristas.

## Conectividad

Un grafo orientado se llama conexo si su subgrafo adyacente (sin orientar) se llama conexo. Un grafo se llama fuertemente conexo si para todo par de vértices $u,v$, existe un camino que los une.

Un grafo se llama orientable, si puede introducirse una orientación que lo convierta en un grafo fuertemente conexo.

1. Si un grafo tiene un puente, no es orientable (por definición de puente)
2. Si un grafo es orientable, no tiene puentes. Su recíproca es verdadera:
3. Si un grafo no tiene puentes, es orientable.

Recordemos que un puente es un vértice que une dos componentes conexas, de modo que si eliminamos el vértice, el grafo se vuelve disconexo.

La demostración de la tercera afirmación, se realiza a través de un algoritmo:

1. Elegimos una arista inicial
2. Orientamos un ciclo al que pertenezca la arista, como no hay puentes, existe al menos uno.
3. Seleccionamos alguna arista incidente sobre el ciclo, un ciclo orientada
4. Orientamos el ciclo al que pertenece la arista, teniendo en cuenta el sentido de la orientación del ciclo adyacente.
5. Continuamos hasta que nos quedamos sin aristas, sabemos que en algún momento pasara esto, ya que es un grafo finito.

A partir de esta construcción, podremos movernos entre todos los ciclos, a partir de sus adyacencias. Debido a que toda arista pertenece a un ciclo, entonces podremos visitar todas las aristas y, por lo tanto, todos los vértices.

## Torneo

Un torneo es un grafo completo orientado. Se denomina así, ya que podemos considerar las aristas como el resultado de los partidos entre cada vértice.

Se dice que un grafo es euleriano si para todos los vértices, su grado entrante es igual a su grado saliente.

Se dice que un grado es semi-euleriano si para todos los vértices, su grado entrante es igual a su grado saliente, excepto dos. Uno de ellos tendrá una arista entraste más, y el otro tendrá una arista saliente más.

### Transitividad

Se dice que un torneo es transitivo, si $\forall u,v,w \in V(G): (uv, vw \in E(G)) \to uw \in E(G)$. Esta definición es similar a la transitividad en relaciones de orden. Un torneo es transitivo si y solo si no tiene ciclos.

Para demostrarlo, podemos inicialmente demostrar que todo torneo con al menos un ciclo, tendrá un ciclo de longitud tres. Luego, el ciclo de longitud tres contradice la transitividad.

### Teorema de Rédei

El teorema de Rédei, dice. Sea $G$ un torneo, entonces $G$ es semihamiltoniano. Existe un camino hamiltoniano (no necesariamente un ciclo).

Recordemos, para la demostración, el teorema de Bolzano. Sea $f$ una función continua en el intervalo $[a, b]$, Si $f(a)f(b) \leq 0$, entonces existe un $c \in [a,b]$ tal que $f(c) = 0$.

Sea $v_1, v_2, \cdots, v_m$ un camino maximal en un torneo, y $u$ un vértice aislado, no perteneciente al camino. Deben existir las aristas $v_1u$ y $uv_m$, ya que si no se podría agregar al torneo. De la misma forma, deben existir aristas entre los vértices del camino y el vértice $u$. Luego, en algún punto del camino existirá un vértice $v_i$ tal que $v_iu \in E(G)$, y $uv_{i+1} \in E(G)$. Luego, podremos aumentar el camino para incluir el vértice $u$. Entonces, el camino maximal de un torneo incluye todos los vértices, por lo que es semihamiltoniano.
