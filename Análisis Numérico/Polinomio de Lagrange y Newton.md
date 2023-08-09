## Polinomio de Lagrange

La interpolación de Lagrange permite encontrar una polinomio que coincida con la función $f$ en $n+1$ puntos del espacio

$$
P_L(x) = \sum_{k=0}^n f(x_k)L_k(x)
$$

$$
L_k(x) = \prod_{i=0, i\neq k}^n \frac{(x-x_i)}{(x_k - x_i)}
$$

### Teorema del Error

Supongamos $x_0, x_1, \cdots, x_n$ son números distintos en el intervalo $[a,b]$ y que $f \in C^{n+1}[a,b]$. Entonces, para cada $x$ en $[a,b]$ existe un numero $\xi(x)$ en $(a,b)$ con la propiedad:

$$
f(x) = P_n(x) + \frac{f^{(n+1)}(\xi(x))}{(n+1)!}(x - x_0)(x - x_1)\cdots(x - x_n)
$$

> [!note]
> La dificultad práctica con esta interpolación consiste en que el termino de error es difícil de aplicar y generalmente el grado del polinomio necesario para lograr la exactitud deseada no se conoce antes de calcular.

## Polinomio de Newton

Supongamos que $P_L(x)$ es un polinomio de Lagrange de grado $n$, las diferencias divididas $a_i$ de $f$ respecto a $x_0, x_1, \cdots, x_n$ se usan para expresar $P_L(x)$ en la forma:

$$
\begin{align}
P_N(x) &= a_0 + a_1(x - x_0) + a_2(x-x_0)(x-x_1) + \cdots \\&+ a_n(x-x_0)(x-x_1)\cdots(x-x_{n-1})
\end{align}
$$

### Diferencias Divididas

$$
f[x_i] = f(x_i)
$$

$$
f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}
$$

Siguiendo esta lógica, podemos definir la $k$-esima diferencia dividida como

$$
f[x_i, x_{i+1}, \cdots x_{i+k}] =
\frac{f[x_{i+1}, x_{i+2}, \cdots, x_{i+k}] - f[x_{i}, x_{i+1}, \cdots, x_{i+k-1}]}{x_{i+k} - x_i}
$$

### Generalización

Una vez definidas las diferencias divididas, podemos definir el polinomio de Newton como

$$
P_N(x) = f[x_0] + \sum_{k=1}^n f[x_0, x_1, \cdots, x_k](x-x_0)\cdots(x - x_{k-1})
$$

> [!note]
> Podemos ignorar el ultimo termino de la suma, y utilizarlo como su cota de error.

### Cálculo del Error

Sea $f \in C^n[a,b]$ y $x_0, x_1, \cdots, x_n$ números distintos en el intervalo $[a,b]$. Entonces existe un número $\xi \in (a,b)$ tal que

$$
f[x_0, x_1, \cdots, x_n] = \frac{f^{(n)}(\xi)}{n!}
$$

De esta forma, podemos usar el teorema del error del polinomio de Lagrange para calcular el error cometido en la aproximación polinomial. El polinomio de newton es una forma del polinomio de lagrange pero de un grado menor. Sacrificamos un grado del polinomio para obtener la cota del error.

$$
f(x) = P_{n-1} + \frac{f^{(n)}(\xi) }{n!} \cdot (x-x_0)(x-x_1)\cdots(x-x_{n-1})
$$
