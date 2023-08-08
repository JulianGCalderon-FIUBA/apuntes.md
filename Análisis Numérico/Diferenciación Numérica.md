# Aproximacion por 2 puntos

Son aproximaciones simples que se realizan a partir de utilizar dos puntos de la funcion original. Se deducen a partir del teorema de Taylor, despejando la derivada primera e ignorando las derivadas siguientes.

## Diferencias Progresivas (adelanto) y Regresivas (atraso)

Se realizan a partir de evaluar en un punto y a una distancia $h$ del punto

$$
f'(x) = \frac{f(x + h) - f(x)}{h}
$$

$$
f'(x) = \frac{f(x) - f(x-h)}{h}
$$

El error de estos metodos es del orden $O(h)$

## Diferencias Centrales

Se realiza a partir de evaluar a una distancia $h$ del punto (esta aproximacion es igual a la de la derivada centrada en tres puntos, de ahi su orden de error)

$$
f'(x) = \frac{f(x+h) - f(x-h)}{2h}
$$

El error de este metodo es del orden $O(h^2)$.

# Aproximacion por $n$ puntos

A partir de realizar una aproximacion por lagrange, podemos aproximar la derivada usando mas puntos.

1. Escribo el polinomio de lagrange $P$ con mis $n$ puntos. Si tomo los puntos delante del punto sera una diferencia progresiva, si tomo puntos detras del punto sera una diferencia regresiva.
2. Busco la derivada $P'$ del polinomio de lagrange
3. Evaluo la derivada en el punto que estoy buscando

El orden del error de este método es de $O(h^{n-1})$

## Cota de Error

La cota de error se encuentra a partir del error de derivar el termino del error del polinomio de Lagrange, Si escribimos los puntos en funcion de $h$, podemos observar el orden del error.

## Algunas Derivadas Usadas

$$
f'(x) \approx \frac{-3f(x) + 4f(x+h) - f(x+2h)}{2h} + \frac{f^{(3)}(\xi)}{3}h^2,\quad\text{$3$ Nodos, Progresiva}
$$

$$
f'(x) \approx \frac{ f(x+h) - f(x-h)}{2h} + \frac{f^{(3)}(\xi)}{6}h^2,\quad\text{$3$ Nodos, Centrada}
$$

## Derivada de Ordenes Superiores

A partir de este metodo, podemos volver a derivar las expresiones para obtener aproximaciones de derivadas de orden superior.

# Extrapolación de Richardson

La extrapolación de richardson consiste en aproximar una derivada a partir de evaluar la funcion en puntos cada vez mas cercanos al punto

1. Planteamos un $h$ inicial, evaluamos la función en los puntos de la sucesión $\{h/2^k\}_{k=0, {n-1}}$
2. Encontramos las aproximaciones $R^{(0)}$ para cada uno de puntos
    
    $$
    R^{(0)}(h) = \frac{f(x+h) - f(x-h)}{2h}
    $$
    
3. A partir de un proceso similar al de las diferencias divididas, encontramos el termino $R^{(n-1)}$ a partir de la ecuación
    
    $$
    R^{(k)}(h) = \frac{4^kR^{(k-1)}(h/2) - R^{(k-1)}(h)}{4^k-1}
    $$
    

Nuestro arbol de diferencias divididas se vera de la siguiente forma

![[Diferenciación Numérica 1.png|Untitled]]

Podemos encontrar que el orden de este metodo es del orden $O(h^{2k+2})$