## Método de Variables Separables

$$
y' = f(x)\cdot g(y)
$$

Este método se usa cuando se puede escribir la ecuación diferencial como el producto de dos funciones, con una variable distinta en cada una.

$$
\begin{align*}y'&=f(x)\cdot g(y)\\\frac 1{g(y)}\cdot y' &= f(x)\\\int\frac 1{g(y)}\cdot \overbrace{y'dx}^{dy} &= \int f(x)dx\\\int\frac{dy}{g(y)} &= \int f(x)dx\end{align*}
$$

Si $f$ no se puede separar entre $x$ e $y$, pero se puede escribir como $f(kx,ky) = f(x,y)$. Entonces es una función homogénea de grado $0$, y se puede realizar un cambio de variable para resolver la ecuación diferencial.

$$
\begin{cases} y = xz \\ y' = z + z'x\end{cases}
$$

## Método de Ecuaciones Lineales

### Definición

$$
a_n(x) \cdot y^{(n)} + a_{n-1}(x) \cdot y^{(n-1)} + \cdots + a_1(x) \cdot y= g(x)
$$

Si $g(x) = 0$, entonces la ecuación diferencial lineal es **homogénea**

#### Homogéneas

$$
a(x)\cdot y' = b(x) \cdot y = 0
$$

La combinación lineal de soluciones de las lineales homogéneas (de cualquier orden), es solución de la homogénea

#### No Homogénea

$$
a(x)\cdot y' = b(x) \cdot y = c(x)
$$

La diferencia entre soluciones de la no homogénea es solución de la homogénea.

La solución general (SG) de la no homogénea se obtiene como suma de la solución general de la homogénea asociada, con una solución particular (SP) de la no homogénea.

1. Resolver la homogénea asociada (variables separables)
2. Encontrar una SP de la no homogénea
	1. Proponemos como solución la de la homogénea, pero dejamos que la constante sea en función de $x$
	2. La remplazamos en la ecuación diferencial y la forzamos a que la cumpla.
	3. Resolvemos la ecuación y tomamos la solución particular más simple
3. Buscamos la SG de la no homogénea

	$$
	SG_{NH} = SG_{H} + SP_{NH}
	$$

## ED. de tipo Homogéneo

Este método se aplica cuando la EDO no es lineal, ni de variables separables, pero sí es homogénea,

Se llama **homogénea** de grado $0$ a la toda función que satisfaga que $f(tx,ty) = f(x,y)$.

Se llama EDO de tipo homogéneo siempre que se pueda escribir como $y' = f(x,y)$, siendo $f$ una función homogénea de grado 0.

Podemos entonces aplicar el cambio de variable $y = xz$

$$

(xz)' = f(x,xz) = f(1,z)

$$

Entonces, si resolvemos llegamos a una EDO de variables separables ($x,z$)

$$

z + xz' = f(1,z)

$$

$$

\frac{z'}{f(1,z)-z} = \frac 1x

$$

$$

\frac{1}{f(1,z)-z}\cdot dz = \frac{1}{x}\cdot dx
$$

Una vez resuelta, volvemos a las variables originales. $z = y/x$
