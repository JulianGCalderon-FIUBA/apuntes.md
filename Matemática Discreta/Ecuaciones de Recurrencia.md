Sea $x_{n+k} =f(x_n, x_n+1, x_n+2, \cdots, x_n+k-1)$ con conocidos $x_0, x_1, \cdots, x_{k-1}$. Es un PVI (problema de valor inicial) de orden $k$.

Una función $x$ con dominio en $\mathbb{N}$ es una sucesión $(x: \mathbb{N} \to C)$ habitualmente denotada $x(n)$, aunque para abreviar, se puede definir $x_n \stackrel{\text{def}}{=} x(n)$.

Si $f$ es lineal, la ecuación de recurrencia también es lineal. En esta materia, únicamente trabajaremos con ecuaciones de recurrencia lineales.

## Ecuación de Primer Orden

Sea $x_{n+1} = ax_{n} + b$, con $x_0, a, b$ constantes, entonces podemos llegar a una solución de forma artesanal de la forma

$$
x_{n+1} = x_0a^n + b\frac{a^n-1}{a-1}  ,\quad a \neq 1
$$

Podemos llegar a una expresión equivalente, definiendo $x^*$ como el punto de equilibrio:

$$
x_{n+1} = \begin{cases}
(x-x^*)a^n + x^*,\quad x^* = \frac{b}{1-a},a\neq1\\
x_0 + bn,\quad a=1
\end{cases}
$$

Observamos que se cumple:

- Si $x_0 = x^*$, entonces $x_n = x^*$ para cualquier $n$.
- El punto de equilibrio es un atractor global si $|a| < 1$:

	$$
    \lim_{n \to \inf} x_n = x^*
    $$

- El punto de equilibrio es un repulsor global si $|a| > 1$:

	$$
    \nexists\lim_{n \to \inf} x_n
    $$

- Si $a = 1$, tiene un comportamiento lineal (como se define en la expresión general)
- Si $a = -1$, entonces $x_n$ oscila infinitamente alrededor de $x_*$

Si $b$ ya no es constante, tendremos $x_{n+1} = ax_{n} + b_n$, en donde encontramos la solución general

$$
 x_0a^n + \sum_{k=0}^{n-1}a^kb_{n-1-k}
$$

### Solución General

Sea $a$ constante, entonces la ecuación de recurrencia de la forma

$$
x_{n+1} = ax_{n} + b_n
$$

Podemos obtener la solución general como suma de solución de la homogénea más una solución particular.

1. Definimos la ecuación homogénea $x_{n+1} - ax_n = 0$ y la ecuación característica $\lambda -a = 0$. De aquí, obtenemos el espectro $\sigma = \{\lambda_1 = a\}$. Luego, la solución de la homogénea será de la forma

	$$
    X_{h_n} = C_1a^n
    $$

2. Proponemos una solución particular $x_{p_n}$ cuya forma dependerá de $b_n$.
	1. Si $b_n$ es un polinomio: $x_{p_n}$ será un polinomio del mismo grado si $a \neq 1$, multiplicado por $n$ si $a = 1$.
	2. Si $b_n$ es una exponencial del tipo $\alpha^n$, se propone otra exponencial del mismo tipo cuando $\alpha \neq \lambda$, multiplicada por $n$ si $\alpha = \lambda$.
	3. Si $b_n$ es una combinación lineal de los casos anteriores, se propone una combinación lineal de las reglas anteriores
	4. Si $b_n$ es un producto de las reglas anteriores, se propone un producto de las reglas anteriores si $\alpha \neq \lambda$, multiplicado por $n$ si $\alpha = \lambda$.

	Para hallar los coeficientes, reemplazamos la solución planeada en la ecuación de recurrencia

3. Hallamos la solución general como suma de ambas

	$$
    X_n = X_{h_n} + X_{p_n}
    $$

4. Imponemos la condición inicial para hallar las constantes apropiadas

## Ecuación de Segundo Orden, Homogénea

Sea $a, b$ constantes, entonces la ecuación de recurrencia de la forma

$$
x_{n+2} + ax_{n+1} +bx_n = 0
$$

Podemos obtener la solución general como suma de solución de la homogénea más una solución particular.

1. Definimos la ecuación homogénea $x_{n+2} + ax_{n+1} +bx_n = 0$ y la ecuación característica $\lambda^2 + a\lambda +b= 0$. De aquí, obtenemos el espectro $\sigma = \{\lambda_1, \lambda_2\}$. Luego, la solución de la homogénea será de la forma:
	1. Si $\lambda_1 \neq \lambda_2 \in \mathbb{R}$, entonces proponemos como solución $x_n = C_1\lambda_1^n + C_2\lambda_2^n$
	2. Si $\lambda_1 = \lambda_2 \in \mathbb{R}$, entonces proponemos como solución $x_n = C_1\lambda_1^n + C_2n\lambda_1^n$
	3. Si $\lambda_1 = \overline\lambda_2 \in \mathbb{C}$ con $\lambda_{1,2} = re^{\pm i\theta}$, entonces proponemos como solución a:

		 $x_n = C_1r^n\cos(n\theta) + C_2r^n\sin(n\theta)$

2. Debido a que es homogénea, únicamente debemos hallar las constantes a partir de la condición inicial.

## Ecuación de Orden Superior Homogénea

Si la ecuación de recurrencia es de orden $q$, para la construcción de la solución de la homogénea se utilizan las mismas reglas que para las de orden 2. Por ejemplo, si una ecuación de recurrencia tiene el espectro.

Es decir, la solución es una sumatoria de los términos correspondientes a cada raíz de la ecuación característica. Si una raíz es de multiplicidad $m$, entonces se suma un término por cada multiplicidad, cada vez multiplicando por $n$ una vez más.

## Ecuación de Orden Superior Completa

Proponemos una solución particular, cuya forma dependerá del término independiente $f_n$.

1. Si $f_n$ es un polinomio de orden $q$, se propone un polinomio de orden $q$ si $1$ no pertenece al espectro, multiplicado por $n$ elevado a su multiplicidad de la raíz.
2. Si $f_n$ es exponencial, se propone otra del mismo tipo si $\alpha$ no pertenece al espectro, multiplicada por $n$ elevado a su multiplicidad si lo hace.
3. Si $f_n$ es una combinación lineal de ambas reglas, se propone una combinación lineal de las propuestas
4. Si $f_n$ es de la forma $a\cos(n\alpha) + b\sin(n \alpha)$, entonces se propone ecuación del mismo tipo si $e^{i\alpha}$ no pertenece al espectro, multiplicada por $n$ elevado a su multiplicidad si lo hace.

## Análisis Cualitativo de las Soluciones

Sea la ecuación característica $x_{n+2} + ax_{n+1} + bx_n = c$, entonces debemos analizar la convergencia de $x_n$ para cualquier condición inicial.

### Si $\lambda_1 \neq \lambda_2$ con $\lambda_1, \lambda_2 \neq 1$

La solución particular será $x_{np} = k$. Luego, reemplazando la solución en la ecuación, encontramos que $k = \frac{c}{1 + a + b}$. Como $1$ no es raíz de la ecuación característica, sabemos que el denominador nunca podrá valer cero. Debido a que 1 no pertenece al espectro, la solución de la homogénea será $x_{hn} = C_1\lambda_1^n + C_2\lambda_2^n$ Definimos entonces la solución general, como:

$$
x_n = C_1\lambda_1^n + C_2\lambda_2^n + \frac{c}{1 + a + b}
$$

Vemos que si las raíces son de módulo mayor a uno, entonces la serie diverge debido a la exponenciación.

$$
\lim_{n\to\infty} x_n = \frac{c}{1+a+b}, \forall x_0, x_1 \iff |\lambda_1|,|\lambda_2| <1
$$

$$
\begin{cases}
1 + a + b \neq 0\\
a^2 \neq 4b
\end{cases}
$$

### Si $\lambda_1 = \lambda_2 = 1$

Sabemos que tanto la ecuación de característica como su derivada se anulan en $\lambda = 1$. Luego, encontramos que $a=-2$ y $b=1$. Proponemos como solución de la ecuación particular $x_{np} = kn$ debido a que $1$ pertenece al espectro. Sustituyendo en la ecuación de recurrencia, encontramos que $k_1 = c/2$. Como conocemos la raíz, definimos, la solución homogénea como $x_{hn} = C_1 + C_2n$. Definimos como solución general.

$$
x_n = C_1 + C_2n + \frac{c}{2}n^2
$$

Vemos que el término puede divergir debido al crecimiento lineal dado por la condición inicial $C_2$.

$$
\exists x_0, x_1: \nexists\lim_{n \to \infty} x_n
$$

Este caso se encuentra cuando:

$$
\begin{cases}a=-2\\
b = 1

\end{cases}
$$

### Si $\lambda_1 \neq \lambda_2, \lambda_1 = 1$

Nuevamente, tendremos que $1 + a + b = 0$. Debido a que las raíces no pueden ser complejas, con la fórmula resolvente obtenemos que $a^2 > 4b$. Debido a que la raíz no es doble, también obtenemos $a \neq -2$. La solución homogénea tendrá la forma $x_{hn} = C_1 + C_2\lambda_2^n$. Proponemos la solución particular $x_{pn} = k_1n$, y a partir de sustituir en la ecuación de recurrencia, obtenemos que $k_1 = \frac{c}{2 + a}$. Como $a \neq 2$, siempre podremos despejar $k_1$. La solución general entonces será

$$
x_n = C_1 + C_2\lambda_2^n + \frac{c}{2+ a}n
$$

Vemos que el término únicamente converge si anulamos tanto el crecimiento exponencial como el crecimiento lineal.

$$
\lim_{n\to\infty} x_n = C_1, \forall x_0, x_1 \iff |\lambda_2| <1,\, c = 0
$$

Este caso se encuentra cuando:

$$
\begin{cases}1 +a+b=0\\
a \neq 2\\
a^2 > 4b

\end{cases}
$$

### Si $\lambda_1 = \lambda_2 = \lambda \neq 1$

Entonces tendremos que $1 + a + b \neq 0$. Proponemos como solución general $x_{hn} = C_1\lambda_1^n + C_2\lambda_2^n$. Para la solución particular, propondremos (como 1 no pertenece al espectro) $x_{pn} = k_1$. Si sustituimos en la ecuación de recurrencia, obtenemos que $k_1 = \frac{c}{1+a+b}$. Sabemos que el denominador no puede valer cero. Definimos entonces la solución general

$$
x_n = C_1\lambda^n + C_2n\lambda^n + \frac{c}{1 + a + b}
$$

Vemos que el término únicamente converge si anulamos el crecimiento exponencial. Como la exponenciación converge más rápido que la linealidad, esto también anula el segundo término.

$$
\lim_{n\to\infty} x_n = \frac{c}{1 + a + b}, \forall x_0, x_1 \iff |\lambda| <1
$$

Este caso se encuentra cuando:

$$
\begin{cases}1 +a+b\neq0\\
a^2 > 4b
\end{cases}
$$

Vemos que si los módulos $\lambda_1, \lambda_2$ son menores a cero, entonces la solución converge siempre (si no tomamos la solución trivial $c = 0$).

## Espacio de Coeficientes

El espacio de coeficientes consiste en hallar todos los $a, b$ tales que la solución siempre converge. Para hacerlo, podemos ayudarnos de las identidades:

$$
\lambda_1 + \lambda_2 = -a
$$

$$
\lambda_1\lambda_2 = b
$$
