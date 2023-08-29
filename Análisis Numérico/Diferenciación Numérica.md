## Aproximación por 2 puntos

Son aproximaciones simples que se realizan a partir de utilizar dos puntos de la función original. Se deducen a partir del teorema de Taylor, despejando la derivada primera e ignorando las derivadas siguientes.

### Diferencias Progresivas (adelanto) y Regresivas (atraso)

Se realizan a partir de evaluar en un punto y a una distancia $h$ del punto

$$
f'(x) = \frac{f(x + h) - f(x)}{h}
$$

$$
f'(x) = \frac{f(x) - f(x-h)}{h}
$$

El error de estos métodos es del orden $O(h)$

### Diferencias Centrales

Se realiza a partir de evaluar a una distancia $h$ del punto (esta aproximación es igual a la de la derivada centrada en tres puntos, de ahí su orden de error)

$$
f'(x) = \frac{f(x+h) - f(x-h)}{2h}
$$

El error de este método es del orden $O(h^2)$.

## Aproximación por $n$ puntos

A partir de realizar una aproximación por Lagrange, podemos aproximar la derivada usando más puntos.

1. Escribo el polinomio de Lagrange $P$ con mis $n$ puntos. Si tomo los puntos delante del punto será una diferencia progresiva, si tomo puntos detrás del punto será una diferencia regresiva.
2. Busco la derivada $P'$ del polinomio de Lagrange
3. Evaluó la derivada en el punto que estoy buscando

El orden del error de este método es de $O(h^{n-1})$

### Cota de Error

La cota de error se encuentra a partir del error de derivar el término del error del polinomio de Lagrange, Si escribimos los puntos en función de $h$, podemos observar el orden del error.

### Algunas Derivadas Usadas

$$
f'(x) \approx \frac{-3f(x) + 4f(x+h) - f(x+2h)}{2h} + \frac{f^{(3)}(\xi)}{3}h^2,\quad\text{$3$ Nodos, Progresiva}
$$

$$
f'(x) \approx \frac{ f(x+h) - f(x-h)}{2h} + \frac{f^{(3)}(\xi)}{6}h^2,\quad\text{$3$ Nodos, Centrada}
$$

### Derivada de Órdenes Superiores

A partir de este método, podemos volver a derivar las expresiones para obtener aproximaciones de derivadas de orden superior.

## Extrapolación de Richardson

La extrapolación de Richardson consiste en aproximar una derivada a partir de evaluar la función en puntos cada vez más cercanos al punto

1. Planteamos un $h$ inicial, evaluamos la función en los puntos de la sucesión $\{h/2^k\}_{k=0, {n-1}}$
2. Encontramos las aproximaciones $R^{(0)}$ para cada uno de puntos

	$$
    R^{(0)}(h) = \frac{f(x+h) - f(x-h)}{2h}
    $$

3. A partir de un proceso similar al de las diferencias divididas, encontramos el término $R^{(n-1)}$ a partir de la ecuación

	$$
    R^{(k)}(h) = \frac{4^kR^{(k-1)}(h/2) - R^{(k-1)}(h)}{4^k-1}
    $$

Nuestro árbol de diferencias divididas se verá de la siguiente forma

![[Diferenciacion Numerica 1.png|450]]

Podemos encontrar que el orden de este método es del orden $O(h^{2k+2})$
