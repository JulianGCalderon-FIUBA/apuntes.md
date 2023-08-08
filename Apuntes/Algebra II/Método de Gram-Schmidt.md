Es un método que nos permite encontrar una base ortogonal de cualquier subespacio, a partir de la aplicación de un mismo algoritmo de forma recursiva.

Si tenemos una base $B = \{v_1, v_2, \cdots, v_n\}$, podemos construir una nueva base $B' = \{w_1, w_2, \cdots, w_n\}$, siendo $w_1, w_2, \cdots, w_n$ vectores ortogonales entre si. De forma tal que

$$
S_1 = gen(v_1) = gen(w_1)\\S_2 = gen(v_1, v_2) = gen(w_1, w_2)\\
\vdots = \vdots\\
S_n = gen(v_1, v_2, \cdots, v_n) = gen(w_1, w_2, \cdots, w_n)
$$

Definimos entonces el primer vector de la base original

$$
w_1 = v_1
$$

Luego, encontramos el siguiente a partir de la proyección

$$
w_2 = v_2 - P_{S_1}(v_2) = v_2 - \frac{\langle v_2, w_1\rangle}{\|w_1\|^2} w_1
$$

Por propiedades de la proyección, $w_2$ es un vector ortogonal a $v_1,\ (w_1)$

Repetimos la misma lógica para el próximo elemento

$$
w_3 =v_3 - P_{S_2}(v_3) = v_3 - \Bigg(\frac{\langle v_3, w_1\rangle}{\|w_1\|^2} w_1 + \frac{\langle v_3, w_2\rangle}{\|w_2\|^2} w_2\Bigg)
$$

Continuamos hasta el ultimo vector de la nueva base

$$
w_n = v_n - \Bigg(\frac{\langle v_n, w_1\rangle}{\|w_1\|^2} w_1 + \frac{\langle v_n, w_2\rangle}{\|w_2\|^2} w_2 + \cdots +\frac{\langle v_n, w_{n-1}\rangle}{\|w_{n-1}\|^2} w_{n-1}\Bigg)
$$

Si en lugar de buscar un base ortogonal, buscamos una base ortonormal, entonces debemos dividir cada vector por su norma

$$
w_n' := \frac{w_n}{\|w_n\|}
$$

# Descomposición $QR$ de una matriz $A$

Con el algoritmo de Gram-Schmidt teníamos una forma de encontrar vectores $w_i$ ortogonales entre si. En lugar de los vectores $w$, podemos despejar los vectores $v$.

Podemos entonces definir una matriz

$$
A = \begin{bmatrix}|v_1| & |v_2|  & \cdots & |v_n|\end{bmatrix} = \begin{bmatrix}|w_1| & |w_2|  &\cdots & |w_n|\end{bmatrix} \cdot R^{n\times n}
$$

El subespacio columna de la matriz es el subespacio en cuestión, siendo $B' = \{w_1, w_2, \cdots, w_n\}$ una base ortogonal de $Col(A)$

Por propiedades de las columnas del producto matricial, encontramos la matriz $R^{k \times k}$

$$
R = \begin{bmatrix}
1 & \alpha_{12} & \cdots &\alpha_{1k} \\
0 & 1 & \cdots & \alpha_{2k} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 &\cdots &\alpha_{(k-1)k}\\
0 & 0 & \cdots & 1
\end{bmatrix} \to\alpha_{ij} = \langle v_j,w_i \rangle
$$

Dada una matriz $A \in \mathbb{R}^{m\times k}$ $Rg(A) = k$, una descomposición $QR$ de $A$ es una factorización de la forma $A = QR \to Q \in \mathbb{R}^{m \times k},  R \in \mathbb{R}^{k\times k}$

Además, se cumple que $Q^T Q = I_k$

# Teorema de Representación de Riesz

Sea $\Bbb V$ un $\Bbb K$-espacio vectorial de dimensión finita con **P.I.**, ***Si $\phi : \Bbb V \to \Bbb K$ es cualquier función lineal no nula, existe un único $w \in \Bbb V$ tal que $\langle X, w \rangle = \phi(X),\ \forall X \in \Bbb V$