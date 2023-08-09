Es un polinomio interpolador de $f$ en los nodos $x_0, x_1, \cdots, x_n$ y la derivada del polinomio coincide con la derivada primera de la función en dichos nodos.

Para calcularlo, se define la sucesión $z_0, z_1, \cdots z_n$ de la siguiente manera

$$
z_{2i} = z_{2i+1} = x_i
$$

Ahora construimos una tabla con las diferencias divididas a partir de la sucesión $z$. Como algunas diferencias no estarán definidas (no se puede dividir por cero) entonces, tomamos la siguiente igualdad.

$$
f[z_{2i}; z_{2i +1}] = f'[x_i] 
$$

A partir de los datos de la función, definimos un polinomio de newton de grado $2n + 1$

$$
f[z_0] + \sum_{k=1}^{2n+1} f[z_0, \cdots, z_k] (x-z_0) \cdots (x-z_{k-1})
$$

## Fórmula Del Error para El Polinomio de Hermite

Al igual que con el polinomio de Lagrange, se puede aproximar a la función usando el polinomio a partir de la siguiente fórmula

$$
f(x) = H_{2n+1}(x) + \frac{(x-x_0)^2 \cdots (x-x_n)^2}{(2n+2)!} f^{(2n+2)}(\xi(x))
$$
