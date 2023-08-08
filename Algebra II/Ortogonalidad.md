## Descomposición Ortogonal

Sea $w$ un vector de $\Bbb V$, siempre se va a poder descomponer en componentes ortogonales como $u = kv + w$, siendo $v\perp w$.

$$
k = \frac{\langle u,v\rangle}{\|v\|^2} \qquad w = u-kv
$$

## Conjuntos Ortogonales

Se dice que $\{v_1, v_2, \cdots, v_k\} \in \Bbb V$ es un conjunto **ortogonal**, si $\langle v_i, v_j\rangle = 0 \quad\forall\ i\neq j$.

Se dice que $\{v_1, v_2, \cdots, v_k\} \in \Bbb V$ es un conjunto **ortonormal**, si $\langle v_i, v_j\rangle = 0 \quad\forall\ i\neq j$. y $\|v_i\|^2 = 1 \quad \forall\ i = 1, \cdots, k$

Si un conjunto ortogonal no contiene el vector nulo, entonces este conjunto es linealmente independiente.

## Complemento Ortogonal

Sea $A \subset \Bbb V,\ A \neq \emptyset$, se llama **complemento ortogonal de** $A$, al conjunto $A^\perp$ formado por todos los vectores de $\Bbb V$ que son ortogonales a cada elemento de $A$.

**Propiedades:**

- $A^\perp$ es un subespacio de $\Bbb V$
- $\{0_{\Bbb V}\}^\perp = \Bbb V$
- $\Bbb V^\perp = \{0_{\Bbb V}\}$
- Sea $S,T \subseteq \Bbb V$, entonces $S\subseteq T \implies T^\perp \subseteq S^\perp$
- Sea $S \subseteq \Bbb V$, entonces $S \cap S^\perp = \{0_{\Bbb V}\}$

## Proyección Ortogonal

### Propiedades

La proyección ortogonal de $v$ en $S$, es igual al punto de $S$ mas cercano a $v$, lo llamamos $v'$, es una transformacion lineal.

$$
P_S(v) = v'
$$

$$
v' \in S
$$

Además, el vector que va de $v$ a $v'$ $(v'{-}v)$ es ortogonal a $S$

$$
v' - v \in S^\perp
$$

- $v - P_S(v) = P_{S^\perp}(v)$
- $v = P_S(v) + P_{S^\perp}(v),\ \forall\ v\in \Bbb V$
- $\Bbb V= S \oplus S^\perp$
- $Im(P_S) = S,\ Nu(P_S) = S^\perp$

### Formula

Sea $S \subset\Bbb V$, $v \in \Bbb V$, y $B_S = \{v_1, v_2, \cdots, v_k\}$ una base ortogonal de $S$

$$
P_S(v) = \frac{\langle v, v_1\rangle} {\|v_1\|^2} v_1 + \frac{\langle v, v_2\rangle} {\|v_2\|^2} v_2 + \cdots + \frac{\langle v, v_k\rangle} {\|v_k\|^2} v_k
$$

### Matriz

Recordando que el producto interno canónico en $\Bbb C^n$es $\langle x,y \rangle = \overline y^T x$, podemos escribir la formula anterior como un producto matricial.

$$
P_S(v) = \begin{bmatrix}
\frac{v_1}{\|v_1\|}  & \frac{v_2}{\|v_2\|} & \cdots & \frac{v_k}{\|v_k\|} 
\end{bmatrix} \cdot
\begin{pmatrix}
\frac{\overline{v_1}^T}{\|v_1\|} \\[1em]
\frac{\overline{v_2}^T}{\|v_2\|} \\[1em]
\vdots \\[1em]
\frac{\overline{v_k}^T}{\|v_k\|}
\end{pmatrix} \cdot v
$$

Como es una transformación lineal, el subespacio formado por combinación lineal de las columnas de la matriz es la imagen de la función, $Col(P) = S$.

Una matriz $P \in \Bbb C^{n\times n}$ o $P \in \Bbb R^{n\times n}$ es una proyección ortogonal si cumple que:

- $P = \overline P^T$ (es una matriz hermética)
- $P^2 = P$ (es una matriz idempotente)

## Cuadrados Minimos

Si $X \in \Bbb V$ y $S \subseteq \Bbb V$, entonces la distancia entre el punto y el conjunto es igual a:

$$
dist(X,S) = min\{dist(X, v_S), v_S \in S\} = \|X -P_s(X)\| = \|P_{S^\perp}(X)\|
$$

Para resolver el problema de cuadrados mínimos y encontrar el punto $b$ mas cercano de $S$ al punto $x$, podemos resolver las ecuaciones normales:

$$
\overline A^T A\ \hat x = \overline A^T b
$$

Este problema tiene solución única siempre y cuando $rg(A) = n$ (rango columna máximo) y podemos despejar la incognita. Se le llama seudoinversa de $A$ a la matriz

$$
A^\# = (\overline A^T A)^{-1} \overline A^T
$$

Si el problema tiene infinitas soluciones, la solución de menor norma es aquella que pertenezca al subespacio $\text{fil}(A)$

**Propiedades:**

- $A^\# A = I_n$
- $A A^\# = P_{Col(A)} \to$ Matriz de la proyección ortogonal sobre el subespacio columna

### Regresión Lineal

Si tenemos un conjunto de datos $(x_1, y_1), (x_2, y_2), \cdots, (x_n, y_n)$. Si suponemos que hay una relación lineal entre las variables $(y = mx + b)$, podemos buscar la ecuación que mejor se ajusta

$$
\begin{bmatrix}
x_1 & 1 \\
x_2 & 1 \\
\vdots & \vdots \\
x_n & 1 \\
\end{bmatrix}
\begin{bmatrix}
m \\
b
\end{bmatrix} =
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{bmatrix}
$$

En el caso de que el sistema sea incompatible (medidas imprecisas) podemos resolverlo el sistema con el método de cuadrados mínimos.

Si en lugar de proponer una relación lineal proponemos una relación cuadrático, podemos seguir el mismo procedimiento anterior $(y = ax^2 + bx + c)$

$$
\begin{bmatrix}
x_1^2 & x_1 & 1 \\
x_2^2 & x_2 & 1 \\
\vdots & \vdots & \vdots\\
x_n^2 & x_n & 1 \\
\end{bmatrix}
\begin{bmatrix}
a \\
b \\
c
\end{bmatrix} =
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{bmatrix}
$$
