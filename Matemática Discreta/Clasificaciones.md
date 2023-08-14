## Particiones

$G$ es $k$-partito si $V(G) = \bigcup_{i = 1}^k V_i$, con conjuntos disjuntos $\bigcap_{i=1}^k V_i = \emptyset$ tal que si $uv \in E(G)$, entonces $u,v$ no pertenecen ambos al mismo $V_i$.

El $k$-partito se llama completo si esta saturado de aristas permitidas. Estos pueden ser denotados según el tamaño de sus conjuntos, con $K_{n, m, \cdots}$

Ademas, puede ser definido a partir de operaciones entre grafos, como:

$$
K_{n,m, \cdots} = N_n * N_m * \cdots
$$

Un grafo es **bi**partito $(k{=}2)$ si y solo si tiene ciclos impares

## Cactus

El grafo $G$ es un cactus si el numero ciclomático coincide con la cantidad de aristas de ciclos.

El numero ciclomático de un grafo es la cantidad minima de aristas que debo eliminar para convertir el grafo en acíclico

Denotamos $\nu(G)$ como el numero de ciclos de un grafo, y $\mu(G)$ como el numero ciclomático de un grafo

## Trazabilidad

### Grafo Euleriano - Explorador

Se dice que un grafo es Euleriano si existe un ciclo que recorra todas las aristas exactamente una sola vez. Es decir, si existe un circuito Euleriano.

**Teorema:** Un grafo conexo es Euleriano si y solo si el grado de todos sus vertices es par.

Se dice que un grafo es semi Euleriano si existe un camino no cerrado que recorra todas las aristas exactamente una sola vez.

**Teorema:** Un grafo conexo es semi Euleriano si y solo si exactamente dos vertices tienen grado par.

### Grafo Hamiltoniano - Viajante

Se dice que un grafo es Hamiltoniano si existe un ciclo que recorra todos los vertices exactamente una sola vez.

Este grafo es un problema no resuelto. No conocemos ninguna implicancia de si solo si, pero conocemos condiciones suficientes

**Teorema de Direc:** Un grafo simple conexo es Hamiltoneano si se cumple que $2d(v) \geq n(G)$ para todos los vertices

**Teorema de Orec:** Un grafo simple conexo es Hamiltoneano si se cumple que $d(u) + d(v) \geq n(G)$ para todos los vertices no adyacentes.

Podremos demostrar fácilmente que el teorema de *Direc* implica el teorema de *Orec*.

## Arboles

Un grafo $G$ es un bosque si y solo si es acíclico. Las componentes conexas de los bosques son arboles. Por definición, un árbol es un bosque de una sola componente conexa.

Cualquiera de las siguientes definiciones de árbol son equivalentes. El grafo $T$ es un árbol si y solo si:

- Es conexo acíclico.
- Es acíclico y $m = n-1$
- Es conexo y $m = n-1$
- Es conexo minimal
- Es acíclico, pero $T+e$ no.
- Cualquier par de vertices tiene exactamente un camino que los une.

Un árbol generador de un grafo $G$ es un subgrafo que contiene todos los vertices del grafo original y es un árbol.

**Propiedad:** Si a un árbol se le quita una hoja (vértice de grado 1), el grafo resultante es un árbol. Esto se debe a que no se generan ciclos ni se pierde la conexidad.

> [!proof]- **Demostración de $m = n-1$:**
>
> Para demostrar que en un árbol, $m = n-1$, utilizaremos inducción. Sea $G$ un árbol de tamaño $n$:
>
> - $n = 1$. Al ser simple, $m=0$.
> - $n \geq 1$. Si $h$ es una hoja de $G$, con orden $m=n-1$, entonces $G - h$ es un árbol de tamaño $n-1$ y, por hipotesis inductiva, de tamaño $n-2$. Al agregar nuevamente $h$ no generamos ningun ciclo, y generamos un árbol de orden $n$ y tamaño $n-1$.

> [!proof]- Demostración de conexo minimal:
> Sea $G$ un árbol, y se supone falso que es un conexo minimal. Luego, existe una arista $e$ que al retirarla, el grafo sigue siendo conexo. Si el grafo es acíclico, entonces existe un único camino entre dos vertices, ya que si no lo fuese existiría un ciclo. Luego, al eliminar la arista $e$, se desconecta los vertices en los que incide y separa el grafo, volviéndolo disconexo. Luego, el grafo era conexo minimal.

> [!proof]- Demostración de acíclico
> Sea $G$ un árbol, se supone falso que es aciclico. Luego, existe una arista $e$ perteneciente al ciclo tal que al eliminarla el grafo continua siendo conexo, pero como un grafo es conexo minimal, entonces esto es un absurdo. Todo árbol es acíclico.

## Inmersión

Un grafo $G$ es planar si y solo si puede representarse en un plano (inmersión), tal que sus aristas no tengan puntos de cruce.

La planeidad es un concepto particular de cuando la inmersión se exige en un plano, pero puede exigirse en otras formas (como un toroide, o una esfera.

Si un grafo no es planar, hablamos de su espesor. Esta es la cantidad mínima de capas que son necesarias para representarlo (en un circuito, por ejemplo).

Ver [[Operaciones entre Grafos#Grafo Dual|Grafo Dual]]

### Formula de Euler

Definimos una cara de una inmersión planar de un grafo como una región acotada del mismo. Una inmersión es dividida en $f$ caras, todas excluyentes y completas. Toda inmersión tiene la cara externa, que rodea el grafo.

Toda curva cerrada divide el espacio el plano en dos secciones, de la misma forma, definimos caras como secciones del plano, delimitadas por aristas. La frontera de una cara es el ciclo que recorre todos los vertices que la delimitan. Se observa que si una arista no separa dos caras, sino que esta contenida en una, el camino debe recorrerla dos veces. Se define el grado de una cara, $d(f)$, como la longitud de su frontera.

Para todos las inmersiones, se cumple la formula de Euler

$$
n - m + f = 2 \tag{Euler}
$$

> [!proof]- Demostración:
> Todo grafo conexo admite un árbol generador, esto es un subgrafo que contiene todos los vertices y es un árbol.
>
> Sea $T$ un grafo generador de $G$, entonces:
>
> $$
> \begin{gathered}
> n(T) - m(T) + f(T) = 12\\
> n(G) - (n(G)-1) + 1 = 12
> \end{gathered}
> $$
>
> Se añade a ese árbol generador una a una las aristas hasta completar $G$, por cada arista agregada, crearemos un circulo y entonces, crearemos una cara
>
> $$
> n(T) + (n(G) -1 - k) + f + k = 2
> $$

Por definición de grado de una cara, cada arista que separa dos caras contribuye a la suma de grados de las caras en dos unidades. Cada arista que no separa caras también contribuye en dos. Luego, tendremos que:

$$
\sum_{k=1}^{f} d(f_k) = 2m \tag{FSL}
$$

Si $G$ es un primo conexo con $n(G) ≥ 3$, entonces podremos demostrar el criterio de rechazo tal que si no se cumple, descartamos la posibilidad de que el grafo sea planar:

$$

m \leq 3(n-2)

$$

A partir de este criterio, podemos demostrar por fuerza bruta que $K_5$ es el primer grafo completo no planar. Además, todos los grafos siguientes tampoco lo son.

> [!proof]- Demostración
>
>
>
> Por inducción podemos probar que para todos los grafos de orden mayor a dos, se cumple que:
>
> $$
> d(f_k) \geq 3, \forall k \in 0,\cdots, f
> $$
>
> Intuitivamente, se puede pensar como que toda cara esta delimitada por una frontera. La curva de frontera de menor longitud que podemos formar es el triangulo, de longitud tres.
> Si utilizamos *FSL*, tendremos que $3f \leq 2m$. Si combinamos esta > propiedad con el teorema de *Euler*, tendremos un criterio de rechazo para la planáridad de un grafo
>
> $$
> m \leq 3(n-2)
> $$
>
> Si no se cumple esta prioridad, entonces podemos asegurar que el grafo conexo de grado mayor a dos no es planar.

Si $G$ es un primo conexo sin ciclos de longitud tres, con $n(G) \geq 3$, entonces podremos demostrar análogamente criterio similar. Si no se permiten ciclos impares, entonces la minima longitud de frontera ya no será tres, sino cuatro.

$$
m \leq 2(n-2)
$$

A partir de este criterio, podemos demostrar por fuerza bruta que $K_{3,3}$ es el primer grafo bipartito completo no planar. Además, todos los grafos siguientes tampoco lo son.

## Coloración

Una $k$-coloración es una asignación al conjunto de vertices tal que dos vertices adyacentes no son del mismo color. Notemos que por la propia definición, los grafos no deben tener lazos.

El numero cromático de un grafo, designado con $\chi(G)$, es el mínimo $k$ para el cual es posible una coloración. Es decir, existe una $\chi$-coloración y para toda $k$-coloración, entonces $\chi \leq k$. Los grafos con un número cromático de uno, son solo los grafos nulos $N_n$.

Una cota inferior del número cromático de $G$ es el número $p$ si $K_p$ es un subgrafo de $G$, notemos que la reciproca es falsa.

Una cota superior del número cromático de $G$ es $\Delta(G) + 1$. Recordemos que se denota con $\Delta(G)$ al máximo grado. La prueba de esto es por inducción.

> [!proof]- Demostración
>
> Buscamos probar que la cota superior del número cromático de $G$ es $\Delta(G) + 1$, para un grafo de cualquier orden. Esto es:
>
> $$
> p(n): \forall G \text{ simple de orden $n$},\chi(G)\leq \Delta(G) + 1
> $$
>
> Para $n = 1$, sea $G$ el grafo de orden $1$, entonces existira la coloración trivial de un color, siendo $\chi(G) = 1 \leq \Delta(G) + 1 = 1$.
>
> Para $n> 1$, sea $G$ un grafo simple de orden $n$, y sea $v$ un vértice cualquiera del grafo. Luego, definimos $H = Gv$. El grafo $H$ es simple ya que eliminar aristas no introduce vertices. $\Delta(H) \leq \Delta(G)$ ya que tomamos cualquier vértice $v$, por lo que el grado máximo puede mantenerse igual. Debido a que no introducimos aristas, este nunca podrá ser mayor. Por la hipótesis inductiva, sabremos que existe al menos una coloración $H$ con a lo sumo, $\Delta(H) + 1 \leq\Delta(G) + 1$. Luego, existirá esa misma coloración para $G$, pero aún sin colorear el vértice eliminado $v$. Debido a que el vértice eliminado tiene, por definición, a lo sumo $\Delta(G)$ vecinos y tenemos un total de $\Delta(G) +1$ colores, siempre tendremos un color para utilizar.

Se llama el índice cromático $\chi’(G)$ de un grafo al cardinal de una coloración mínima de aristas. Se consideran dos aristas adyacentes si inciden sobre el mismo vértice. Para las aristas, tendremos cotas mucho mas poderosas, con el teorema de **Vizing**.

$$
\Delta(G) \leq \chi'(G) \leq \Delta(G) + 1
$$
