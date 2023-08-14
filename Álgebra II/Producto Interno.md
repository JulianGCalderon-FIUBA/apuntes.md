## Definición

Si $\Bbb V$ es un $\Bbb K$-espacio vectorial, se dice que una función $\langle *,* \rangle: \Bbb V \times \Bbb V \to \Bbb K$ es un producto interno **(P.I.),** si cumple:

- $\langle \alpha u + \beta v, w\rangle = \alpha \langle u, w\rangle + \beta \langle v, w\rangle \impliedby \forall u,v,w \in \Bbb V \ \land\  \forall \alpha, \beta \in \Bbb K$
- $\langle u,v\rangle = \overline{\langle v,u\rangle } \impliedby \forall u,v \in V \text{Conjugado}$
- $\langle u,u\rangle > 0 \iff u \in \Bbb V \neq 0_V$
- $\langle u,u\rangle = 0 \iff u \in \Bbb V = 0_V$

### Consecuencias Inmediatas

1. $\langle u,u\rangle \in \mathbb{R} \impliedby \forall u \in \Bbb V$
2. $\langle u, \alpha v + \beta w\rangle = \overline{\alpha}\langle u,v\rangle + \overline{\beta}\langle u,w\rangle \impliedby \forall u,v,w \in \Bbb V$
3. $\langle0,u\rangle = 0 \impliedby \forall u \in \Bbb V$

### Nociones del Producto Interno

#### Norma

Es inducida por el producto interno

$$
\|u\| = \sqrt{\langle u,u\rangle}
$$

Cumple las siguientes propiedades:

- $||u|| > 0$
- $||\lambda u|| = |\lambda|.||u||$
- $|| u || = 0 \iff u = 0_V$

#### Distancia

Sean $u,v \in \Bbb V$, definimos la distancia entre $u,v$ como

$$
d(u,v) = \|u - v\| = \|v - u\|
$$

#### Ortogonalidad

Sean $u, v \in \Bbb V$, se dice que son ortogonales si

$$
\langle u,v \rangle = 0 \iff u \perp v
$$

### Ejemplos Básicos

- **Producto Interno canónico en** $\mathbb{R}^n$, Se cumple la siguiente igualdad para $X, Y \in \mathbb{R}^n$

	$$
    \langle X,Y\rangle = Y^TX
    $$

- **Producto Interno canónico en** $C^n$, Se cumple la siguiente igualdad para $X, Y \in \Bbb C^n$

	$$
    \langle X, Y\rangle = \overline{Y}^TX
    $$

- Si tomamos $\Bbb V$ = $C([0,1])$, entonces para $f, g$ funciones continuas en el intervalo $[0,1]$

	$$
    \langle f,g \rangle  = \int_0^1 f(t)g(t)dt
    $$

	> [!note]
	> Este producto interno nos permite calcular la norma y la distancia entre funciones continuas.

- Si tomamos $\Bbb V = \mathbb{R}^2$, entonces para $X, Y \in \Bbb V$, podemos definir el producto interno

	$$
    \langle X,Y\rangle = X\begin{pmatrix} 4 & -1 \\ -1 & 2\end{pmatrix} Y^T
    $$

	Lo que es equivalente a la siguiente expresión

	$$
    \langle (x_1,x_2)^T, (y_1,y_2)^T\rangle = (x_1, x_2)\begin{pmatrix} 4 & -1 \\ -1 & 2\end{pmatrix}\begin{pmatrix}y_1 \\ y_2\end{pmatrix}
	$$

	$$
    \langle (x_1,x_2)^T, (y_1,y_2)^T\rangle = (4x_1y_1 -x_2y_1 -x_1y_2+ 2x_2y_2)
    $$

## Base de Producto Interno

Si $\Bbb V$ es un espacio vectorial de dimensión finita, todo **P.I.** queda definido sobre una base de $\Bbb V$. Más aún, si $B = \{v_1,...,v_n\}$ todo **P.I**. puede escribirse como:

$$
\langle u,v\rangle = \overline{[v]^B}^T G_B[u]^B = [u]^{B^T}G_B\overline{[v]^B}
$$

$$
\langle u, v\rangle = [x_1,x_2,...,x_n]
\begin{bmatrix}

\langle v_1, v_1\rangle & \langle v_1, v_2\rangle & \cdots &  \langle v_1, v_n\rangle \\  \langle v_2, v_1\rangle &  \langle v_2, v_2\rangle & \cdots &  \langle v_2, v_n\rangle \\ \vdots & \vdots & \ddots & \vdots \\  \langle v_n, v_1\rangle &  \langle v_n, v_2\rangle & \cdots &  \langle v_n, v_n\rangle

\end{bmatrix}

\begin{bmatrix}\overline{y_1} \\ \overline{y_2} \\ \vdots \\ \overline{y_n}\end{bmatrix}
$$

Con $G_B \in K^{n\times n}$ una matriz hermética y definida positiva.

- $G_B \in K^{n\times n}$ es una matriz **hermética** si y solo si $G_B = \overline{G_B}^T$, Las matrices herméticas son un subconjunto de las matrices simétricas, extendida a las matrices con coeficientes reales.
- $G_B \in K^{n\times n}$ es definida **positiva** si y solo si $X^TG_BX > 0 \impliedby \forall X \in K^n \neq \{0_{\Bbb K^n}\}$

## Propiedades

### Desigualdad de Cauchy-Bunyakovsky-Schwarz:

$$
| \langle u,v \rangle | \leq \|u\| \|v\| \impliedby \forall u,v \in \Bbb V
$$

$$
\text{Mas aun:}
\begin{cases}
| \langle u,v \rangle | = \|u\| \|v\| \iff u,v \text{ son L.D} \\
| \langle u,v \rangle | < \|u\| \|v\| \iff u,v \text{ son L.I} \\
\end{cases}
$$

### Desigualdad Triangular:

$$
\|u + v\| \leq \|u\| + \|v\| \impliedby \forall u,c \in \Bbb V
$$

### Teorema de Pitágoras:

Si $\langle u,v \rangle = 0 \iff u \perp v$ (es decir, si trabajamos con vectores perpendiculares) se cumple que

$$
\|u + v\|^2 = \|u\|^2 + \|v\|^2
$$

### Ángulo entre $u, v$:

Como consecuencia la desigualdad de *Cauchy-Bunyakovsky-Schwarz*, llegamos a la siguiente expresión

$$
-1 \leq \frac{\langle u,v \rangle}{\|u\| \|v\|}\leq 1
$$

Extendemos entonces la definición de ángulo, para cualquier $\mathbb{R}$-espacio vectorial

$$
\cos(\theta) = \frac{\langle u,v \rangle}{\|u\| \|v\|} \impliedby \theta \in [0, \pi]
$$

$$
\alpha(u,v) = \theta
$$

### Área de un triángulo

Sea $\triangle$ un triángulo de vértices $(0, e_1, e_2)$, entonces el área de este triángulo se calcula con la siguiente fórmula

$$
A(\triangle) = \frac 12 \cdot \sqrt{\|e_1\|^2\|e_2\|^2 - \langle e_1, e_2\rangle^2}
$$

### Área de un paralelogramo

Se puede dividir el paralelogramo en dos triángulos y usar la fórmula anterior para encontrar su área.

$$
A(\triangle) = \sqrt{\|e_1\|^2\|e_2\|^2 - \langle e_1, e_2\rangle^2}
$$
