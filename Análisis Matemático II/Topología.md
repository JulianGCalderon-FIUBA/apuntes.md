## Distancia en $\mathbb{R}^n$

$$
d(\vec{x},\vec{y}) = \|\vec{x}-\vec{y}\| = \sqrt{(x_1-y_2)^2 + (x_2-y_2)^2 + \text{... } + (x_n-y_n)^2}
$$

## Bolas en $\mathbb{R}^n$

Existen tres tipos de $n$-bolas

- **n-bola abierta:**

	$$
	B(\vec x_0, r) = \{\vec x \in \mathbb{R}^n / d(\vec x ,\vec x_0 ) < r\}
	$$

- **n-bola cerrada:**

	$$
	B(\vec x_0, r) = \{\vec x \in \mathbb{R}^n / d(\vec x ,\vec x_0 ) \leq r\}
	$$

- **n-bola abierta reducida:**

	$$
	B(\vec x_0, r) = \{\vec x \in \mathbb{R}^n /0 < d(\vec x ,\vec x_0 ) < r\}
	$$

## Topología en $\mathbb{R}^n$

### Puntos

- $\vec x$ es un **punto interior** de $A$ si existe $r > 0$ tal que $B(\vec x, r) \subset A$
- $\vec x$ es un **punto exterior** de $A$ si existe $r > 0$ tal que $B(\vec x, r) \subset A^c$
- $\vec x$ es un **punto frontera** de $A$ si para todo $r > 0$, $B(\vec x, r)$ contiene puntos de $A$ y de $A^c$
- $\vec x$ es un **punto de acumulación** de $A$ si para todo $r > 0$, $B(\vec x, r) \subset$ infinitos puntos de $A$
- $\vec x$ es un **punto aislado** de $A$ si existe $r > 0$ tal que $B(\vec x, r) \cap A = \{\vec x\}$

### Conjuntos

- $A^0$ es el conjunto de **puntos interiores** de $A$
- $Ext(A)$ es el **conjunto de *puntos exteriores* de $A$
- $\partial A$ es el conjunto de **puntos frontera** de $A$
- $A^´$ es el conjunto de **puntos de acumulación** de $A$, se denomina conjunto **derivado** de $A$
- $I(A)$ es el conjunto de **puntos aislados** de $A$
- $\bar A$ es el conjunto $A \cup A^´$. Se denomina **clausura** de $A$

### Tipos de conjuntos:

- $A$ es **abierto** si $A = A^0$
- $A$ es **cerrado** si su complemento es abierto
- $A$ es **acotado** si existe $r > 0$ tal que $A \subset B(\vec 0,r)$
- $A$ es **compacto** si es cerrado y acotado

### Según su conectividad:

- $A$ es **convexo** si con cada par de puntos de $A$, el segmento que los une también pertenece a $A$
- $A$ es **conexo** si está formado por una sola parte
- $A$ es **arco conexo** si para cada par de puntos de $A$ existe una curva contenida en $A$ que los une
- Si $A$ es conexo, también es **simplemente conexo** si toda curva cerrada contenida en $A$, forma un conjunto contenido en $A$
