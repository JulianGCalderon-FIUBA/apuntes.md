## Derivacion de Funciones Escritas Implicitamente

**Funcion escrita Implicitamente:** No hay una variable despejada

### Teorema de la Funcion Implicita

Sea $f(x,y,z)$ una funcion diferenciable en un entorno del punto $(x_0, y_0, z_0)$ donde $F(x_0, y_0, z_0) = 0$ **(*)***. Entonces, si $f'_z(x_0, y_0, z_0) \neq 0$, la expresion* **(*)** define $z=f(x,y)$ en un entorno de $(x_0, y_0)$. (Pero no se puede despejar)

Ademas, $f$ es diferenciable en $(x_0, y_0)$ y

$$
\begin{align*}f'_x(x_0,  y_0) = -\frac{F'_x(x_0, y_0, z_0)}{F'_z(x_0, y_0, z_0)}&&f'_y(x_0,  y_0) = -\frac{F'_y(x_0, y_0, z_0)}{F'_z(x_0, y_0, z_0)}\end{align*}
$$

#### Condiciones

- $f$ debe ser diferenciable en un entorno de $(x_0, y_0, z_0)$
- $F(x_0, y_0, z_0) = k$
- $f'_x(x_0, y_0, z_0) \neq 0$

### Generalizacion para $m$ Ecuaciones con $n$ Variables

$(n>m)$

- $F_1, F_2, \cdots, F_m$ son funciones simultaneamente $C^1$ en un entorno del punto
- $\displaystyle \begin{cases}F_1(\vec x_0) = 0 \\F_2(\vec x_0) = 0\\\cdots\\F_m(\vec x_0) = 0\end{cases}$
- $\displaystyle\Delta\bigg(\frac{\partial(f_1, f_2, \cdots, f_m)}{\partial(x_1, x_2, \cdots, x_m)}\bigg)\neq 0$ (Determinante jacobiano de las funciones con respecta a las variables dependientes.

Si se cumplen estas condiciones, las $m$ variables se pueden definir como funciones de $(n-m)$ variables

$$
\begin{align*}x_1 = f_1(x_{m+1}, x_{m+2}, &\cdots, x_n)\\x_2 = f_2(x_{m+1}, x_{m+2}, &\cdots, x_n)\\&\cdots\\x_m = f_m(x_{m+1}, x_{m+2}, &\cdots, x_n)\end{align*}
$$

Ademas las funciones $f$ resultan $C^1$ en cercanias del punto, siendo

$$
\frac{\partial f_i}{\partial j}(\vec x_{n\to m}) = -\frac{\Delta\Big(\frac{\partial(F_1, \cdots, F_i, \cdots, F_m)}{\partial(x_1, \cdots, x_j, \cdots, x_m)}\Big)}{\Delta\Big(\frac{\partial(f_1, f_2, \cdots, f_m)}{\partial(x_1, x_2, \cdots, x_m)}\Big)}, \text{Remplazo }x_i \text{ con } x_j
$$

La matriz superior es casi identica a la matriz inferior, remplazando las derivadas respecto de $i$ (Variable que estamos definiendo como funcion) con las derivadas respecto $j$ (Variable respecto a la cual estamos derivando)
