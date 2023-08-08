Dado un grafo no dirigido $(G,E)$, con un conjunto $V$ de vertices y $E$ de aristas. Un coloreo valido de $G$ se corresponde a una partición de $V$ en $K$ conjuntos independientes, donde dos elementos adyacentes no pertenecen al mismo conjunto. El objetivo es minimizar $K$. Donde $\min K = \chi(G)$ es el numero cromatico del grafo.

Un Conjunto independiente en un grafo es un conjunto de vértices tal que ninguno de
los vértices es adyacente a otro. Un conjunto independiente máximo es un conjunto tal que al agregarle un vértice más, deja de ser independiente.

Definimos $L_{ij}$ como verdadero si el nodo $i$ es adyacente al nodo $j$. Esta es una constante en nuestro problema. Tambien definimos $Y_{ij}$ como verdadera si el nodo $i$ tiene el color $j$. Por ultimo $Y_j$ indica que usamos el color $j$.

El objetivo será minimizar la cantidad de colores, por lo que:

$$
Z_{\min} = \sum_{j=1}^V Y_J
$$

Cada vértice debe tener un solo color, por lo que:

$$
\sum_{i=1}^V Y_{ij} = 1, \quad \forall j
$$

Si dos vértices son adyacentes, no pueden tener el mismo color

$$
Y_{ij} + Y_{kj} \leq Y_j, \quad \text{si } [i,k] \in E,\  \forall j
$$

# Modelo por Conjuntos Independientes

Colorear es determinar a que conjunto independiente pertenece cada vértice, cada conjunto luego se colorea de un mismo color. Para este modelo, debemos determinar todos los conjuntos independientes del grafo. Sea $S$ el conjunto de todos los conjuntos independientes

Definimos $Y_{S_i} = 1$ si todos los vertices de $S_i$ son coloreados con un mismo color, y $0$ en caso contrario. 

Debemos minimizar la cantidad de conjuntos independientes seleccionados

$$
Z_{\min} = \sum_{i} Y_{S_i}
$$

Cada vértice debe pertenecer a exactamente uno de los conjuntos independientes usados

$$
\sum_{i:v\in S_i}Y_{S_i} = 1,\quad \forall v \in V
$$

# Modelo por conjuntos independientes maximal

Para reducir la cantidad de variables, solo se modelan los conjuntos independientes maximales (conjuntos independientes a los que no se les puede agregar ningún vértice y que sigan siendo independientes). Sea $M$ el conjunto de todos los conjuntos independientes maximales, ahora permitimos que un vertice pertenezca a mas de un conjunto (luego es a arbitrario el color que se le asigna)

$$
\sum_{i:v\in M_i}Y_{M_i} \geq 1, \quad\forall v \in V
$$

# Relajación Lineal

Si se quita la restricciones de las variables enteras, entonces el modelo usara únicamente dos colores, pintando cada vértice de dos colores. Esta solución es factible y por lo tanto, la técnica de relajación lineal no es útil.

# Simetría

Cuando se resuelve de manera exacta un problema de coloreo de grafos, aparecen muchas soluciones alternativas. Este es el problema de la simetría.

$$
w_j \leq \sum_{i \in V} Y_{ij},\quad \forall j=1, \cdots, n
$$

$$
w_j \geq w_{j+1},\quad \forall j=1, \cdots, n -1
$$

Con estas dos restricciones, obligamos a los colores a realizarse de forma ordenada. Donde el grupo con mayor cantidad de nodos tomará el primer color, el segundo con mayor cantidad de nodos tomará el segundo color y así sucesivamente. Podemos agrupar estas dos restricciones de la siguiente forma:

$$
\sum_{i=1}^n x_{ij} \geq \sum_{i=1}^n x_{i{j+1}}
$$