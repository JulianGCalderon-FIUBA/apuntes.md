## Definición

Definimos un grafo $G = (V(G), E(G), \Psi_G)$ como una terna de un conjunto de vértices $V(G)$, un conjunto de aristas $E(G)$ y una función $\Psi_G$ que relaciona los vértices con las aristas.

- Definimos el orden del grafo $n(G) = |V(G)|$
- Definimos el tamaño de un grafo $m(G) = |E(G)|$

El grafo se puede denominar según su tamaño y orden, de la forma $G(n,m)$

## Aristas

Generalmente, definimos la función de incidencia:

$$
\Psi_G: E(G) \to \mathcal P(V(G))
$$

Para definir $\Psi_G$ utilizamos alguna de las siguientes notaciones:

$$
\Psi_G(e_1) = \{v_1, v_2\}
$$

$$
\Psi_G(e_1) = v_1v_2
$$

$$
e_1 = v_1v_2
$$

- Las aristas que inciden dos veces en el mismo vértice se denominan **lazos**
- Si hay dos aristas que inciden sobre los mismos dos vértices, entonces estas aristas son **múltiples**

El entorno abierto de un vértice es el conjunto de vértices que se conectan con él directamente, y se define

$$
\Gamma(v) = \{x \in V(G), x\neq u: \exists e \in E(G): \Psi_G(e) = \{x, v\}
$$

El entorno cerrado es aquel que incluye al camino trivial propio

$$
\Gamma[v] = \Gamma(v) \cup \{v\}
$$

Un grafo es simple si no tiene lazos ni aristas múltiples. En los grafos simples puede prescindirse de etiquetas en las aristas porque sus extremos las definen inequívocamente.

## Grado de Vértice

El grado de un vértice $d(v)$, del inglés *degree* es la cantidad de aristas que inciden sobre ese vértice. La sucesión de grados $d(G)$ es un vector no decreciente con el grado de cada uno de los vértices.

- Definimos $\delta(G)$ como el grado mínimo del grafo.
- Definimos $\Delta(G)$ como el grado máximo del grafo.
- También denotamos $\overline d(G)$ como el grado promedio del grafo

Si todos los vértices de un grafo tienen el mismo grado, se dice que es regular

Si todos los vértices del grafo $G$ tienen de grado $\delta(G)$, excepto uno de grado $\Delta(G) = \delta(G) + 1$, entonces se dice que es un grafo casi regular.

### Sucesión Gráfica

Se dice que la sucesión $P=(p_1, p_2, \cdots, p_n)$ es gráfica si existe un grafo $G(n,m)$ cuya sucesión de grafos es $P$.

**Teorema:** Si $P$ es una sucesión de naturales cuya suma es par, entones siempre es una sucesión gráfica de algún grafo, posiblemente simple.

#### Algoritmo de Construcción de Grafo

1. Unir todos los vértices de grado impar, siempre podre, ya que hay una cantidad par de ellos
2. Coloco una cantidad de lazos igual al grado de cada vértice restante (este será par) partido por dos.
3. Se formó un grafo no simple con la sucesión dada.

## Formas Matriciales

Se define $A_g$ a la matriz de adyacencia de $G$ tal que $A_g(i,j)$ es la cantidad de aristas que conectan el vértice $v_i$ con el vértice $v_j$. Los lazos cuentan doble.

Se define $M_g$ a la matriz de incidencias de $G$ tal que $A_g(i,j)$ lleva un uno si la arista $j$ incide en $i$, y lleva un dos si es un lazo.

Podemos probar por inducción que $A_G^q(i,j)$ cuenta la cantidad de caminos de longitud $q$ entre $v_i$ y $v_j$.

Por otro lado, a partir de la definición, tendremos que $M_GM_G^T = A_G + D$, con $D$ la matriz diagonal de los grados de los vértices del grafo.

## Complemento de un Grafo Simple

Sea $G$ un grafo simple, entonces definimos su complemento como $G'$, donde:

- $V(G') = V(G)$
- $e \in E(G’) \iff e \notin E(G)$

Observamos que si sumamos $d(G) + d(G')$, obtendremos una sucesión estable, como si fuera la del grafo $K_n$.
