---
title: Métodos Iterativos
---

Los métodos iterativos comienzan con una aproximación lineal $x^{(0)}$ y generan una sucesión de vectores que converge a $x$, siendo $x$ la solución del sistema $Ax = b$. Consiste en convertir el sistema en un sistema $Tx + c = x$, con $T$ una matriz fija y $c$ un vector fijo.

## Método de Jacobi

Consiste en despejar $x_i$ de la fila $i$, para cada ecuación del sistema, luego a partir de remplazar los valores de la aproximación lineal en las funciones halladas encontramos el siguiente término de la sucesión.

Para hallar el error relativo, podemos simplemente utilizar la norma infinita, para más fácil cálculo

$$
\frac{||x^{(k)}-x^{(k-1)}||_{\infty}}{||x^{(k)}||_{\infty}} \le \varepsilon
$$

Si descomponemos la matriz $A$ de la forma $A = D - L - U$, entonces podemos encontrar los términos $T, c$ de la siguiente forma:

$$
T_J = D^{-1} (L + U)
$$

$$
c_J = D^{-1}b
$$

## Método de Gauss-Seidel

Este método es idéntico al anterior, pero una vez calculado un valor, lo remplazo en la aproximación actual y lo utilizo en las siguientes ecuaciones. Este método converge más rápido que el anterior, y además diverge más rápido.

Podemos encontrar los términos $T, c$ de la siguiente forma:

$$
T_G = (D-L)^{-1} U
$$

$$
c_G = (D-L)^{-1}b
$$

## Teorema de Convergencia

Para cualquier $x^{(0)} \in \mathbb{R}^n$, los métodos anteriores convergen a la solución de $x = Tx + b$ si y solo si el radio espectral $\rho(T) < 1$

> [!note]
> El radio espectral de una matriz es su mayor autovalor.

Si $\|T\| < 1$ para cualquier norma matricial y $c$ es un vector cualquiera, entonces la sucesión definida converge a la única solución si las siguientes cotas son válidas

$$
\|x - x^{(k)}\| \leq \|T\|^k \|x^{(0)} - x\|
$$

$$
\|x - x^{(k)}\| \leq \frac{\|T\|^k}{1 - \|T\|} \|x^{(1)} - x^{(0)}\|
$$

**Teorema por Diagonal Dominante:** Si $A$ es estrictamente diagonal dominante, entonces para cualquier elección de $x^{(0)}$, la sucesión converge a la única solución del sistema $Ax = b$

**Teorema por Signo:** Si los elementos de la diagonal son los únicos positivos de la matriz $A$, entonces se valida solo una de las siguientes condiciones

1. $0 \leq \rho(T_g) < \rho(T_j) < 1$
2. $1 < \rho(T_g) < \rho(T_j)$
3. $\rho(T_g) = \rho(T_j) = 0$
4. $\rho(T_g) = \rho(T_j) = 1$

> [!definition]- Matriz estrictamente diagonal dominante
> Se dice que la matriz $A$ de $n \times n$ es **estrictamente diagonal dominante por filas** si un elemento de la diagonal es mayor a la suma del resto de los elementos de la fila.
> 
> $$
> |a_{ii}| > \sum_{j=1, j \neq i}^{n} |a_{ij}|
> $$
> 
> Se dice que la matriz $A$ de $n \times n$ es **estrictamente diagonal dominante por columnas** si un elemento de la diagonal es mayor a la suma del resto de los elementos de la fila.
> 
> $$
> |a_{ii}| > \sum_{i=1, j \neq i}^{n} |a_{ij}|
> $$
> 
> Se dice que una matriz es estrictamente diagonal dominante si se cumple alguna de las dos condiciones anteriores.

### Métodos SOR

Los métodos de sobre relajación reciben este nombre porque producen sucesivas relajaciones excesivas. Son útiles para resolver sistemas lineales que ocurren en la solución numérica de ciertas ecuaciones diferenciales en derivadas parciales.

Los métodos consisten en utilizar $\omega$ para modificar las matrices $T, c$

$$
T_\omega = (D - \omega L)^{-1}[(1-\omega)D + \omega U]
$$

$$
c_\omega =\omega(D - \omega L)^{-1}b
$$

$$
x^{(k)} = T_\omega x^{(k-1)} + c_\omega
$$

Si ningún elemento de la diagonal es nulo, entonces el método SOR converge solo si $0 < \omega < 2$

Si la matriz es definida positiva y $0 < \omega < 2$, entonces el método SOR converge para cualquier semilla.

> [!note] Si $\omega = 1$, entonces se reduce al método Gauss-Seidel.
