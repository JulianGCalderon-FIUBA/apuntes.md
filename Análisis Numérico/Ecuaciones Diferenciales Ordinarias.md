---
title: Ecuaciones Diferenciales Ordinarias
---

Se dice que una función $f(t,y)$ satisface una condición de Lipschitz en la variable $y$ en un conjunto $D \subset \mathbb{R}^2$ si existe una constante positiva $L$ tal que

$$
\|f(t,y_1) - f(t,y_2)\| \leq L\|y_1 - y_2\|; \qquad (t,y_1), (t,y_2) \in D
$$

**Teorema Condición:** Sea $f(t,y)$ definida en el conjunto $D$ conexo, entonces si existe una constante positiva $L$ tal que:

$$
\Big\|\frac{\partial f}{\partial y}(t,y)\Big\| \leq L, \quad \forall(t,y) \in D
$$

Entonces $f$ satisface una condición de Lipschitz en $D$ en la variable $y$.

**Teorema Unicidad:** Sea $D = \{(t,y): a \leq t \leq b; -\infty \leq y \leq \infty\}$ y la función $f(t,y)$ continua en $D$, entonces si $f$ satisface la condición de Lipschitz en $D$ en la variable $y$, entonces el problema de valores iniciales

$$
\text{PVI:}\begin{cases}
y'(t) = f(t,y) \qquad a \leq t \leq b \\
y(a) = y_0
\end{cases} \tag{1}
$$

tiene solución única en $y(t)$ para $a \leq t \leq b$

**Teorema Bien Planteado:** Sea $D = \{(t,y): a \leq t \leq b; -\infty \leq y \leq \infty\}$. Si $f$ es continua y satisface la condición de Lipschitz en la variable $y$ en el dominio $D$, entonces el problema de valores iniciales $(1)$ está bien planteado.

## Método de Euler

Este método genera aproximaciones a la solución $y(t)$ en distintos valores, llamados **puntos de red** en el intervalo $[a,b]$. Estos puntos se seleccionan de la forma $t_i = a + ih,\ \forall i = 0, 1, 2, \cdots, N$

La distancia $h$ entre los puntos recibe el nombre de paso.

Planteamos un polinomio de Taylor centrado en $t_i$, para hallar una aproximación para la solución de $y(t_{i+1}) \approx y_{i+1}$, despreciando el término del error.

$$
y_{i+1} = y_i + hf(t_i, y_i); \quad y(a) = y_0
$$

**Cota de Error:** La sucesión de los $y_i$ generada por el método de Euler produce la acotación

$$
\|y(t_i) - y_i\| \leq \frac{hM}{2L}\Big[e^{L(t_i - a)} - 1\Big]
$$

Este método es muy inefectivo a medida que incrementamos la distancia entre el $t_0$ y $t_n$. Para aproximaciones lejanas es conveniente usar el método de Runge-Kutta.

## Método de Runge-Kutta

Este método es similar al método de Euler, pero utiliza una función $\varphi$ que permite corregir el error que se va cometiendo.

$$
y_{i+1} = y_i + \phi(t_i, y_i, h) \cdot h
$$

Definimos $\varphi(t_i, y_i, h) =  a_1k_1 + a_2k_2 + \cdots + a_nk_n$. Donde las constantes $k_i$ se definen como:

$$
\begin{align}
&k_1 = f(t_i, y_i) \\
&k_2 = f(t_i + p_1h, y_i +q_{11} k_1 h) \\
&k_3 = f(t_i + p_2h, y_i +q_{21}k_1h + q_{22} k_2h) \\
&k_4 = f(t_i + p_{n-1}h, y_i +q_{{n-1},1}k_1h + \cdots + q_{n-1,n-1}k_{n-1}h)
\end{align}
$$

Donde $p_i, q_{ij}$ son constantes a determinar

### Runge-Kutta de Orden 1

Para el orden $1$, no es necesario encontrar ninguna constante. De esta forma,

$$
\varphi(t_i, y_i, h) = a_1 f(t_i, y_i)
$$

Por lo que si $a_1 = 0$, entonces tenemos el método de Euler.

### Runge-Kutta de Orden 2

Para el orden $2$. Se puede demostrar que las contantes respetan el sistema de ecuaciones

$$
\begin{cases}
a_1 + a_2 = 1 \\
2a_2p_1 = 1 \\
2a_2q_{11} = 1

\end{cases}
$$

Si tomamos $a_2 = 1$, entonces tenemos el método de Runge-Kutta del punto medio:

$$
\text{RK2:}\begin{cases}
y_{i+1} = y_i + k_2h \\
k_1 = f(t_i, y_i) \\
k_2 = f(t_i + \frac h2, y_i + \frac{k_1h}{2})
\end{cases}
$$

### Runge-Kutta del Orden 3

Para el orden $3$, se generan seis ecuaciones con ocho incógnitas. La versión más común de este método es:

$$
\begin{cases}
y_{i+1} = y_i + \frac h6 (k_1 + 4k_2 + k_3) \\
k_1 = f(t_i, y_i)\\
k_2 = f(t_i + \frac h2, y_i + \frac {k_1h}2)\\
k_3 = f(t_i + h, y_i - k_1h + 2k_2h)

\end{cases}
$$

### Runge-Kutta del Orden 4

Para el orden $3$, se generan seis ecuaciones con ocho incógnitas. La versión más común de este método es:

$$
\begin{cases}
y_{i+1} = y_i + \frac h6 (k_1 + 2k_2 + 2k_3 + k_4) \\
k_1 = f(t_i, y_i) \\
k_2 = f(t_i + \frac h2, y_i + \frac {k_1h}2)\\
k_3 = f(t_i + \frac h2, y_i + \frac {k_2h}2)\\
k_4 = f(t_i + h, y_i + k_3h)

\end{cases}
$$
