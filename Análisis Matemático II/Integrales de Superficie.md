Sea $\Sigma$ una superficie parametrizada, entonces una porción infinitesimal de la superficie se puede pensar como:

$$
d\sigma =\|\underbrace{\Sigma'_u\times\Sigma'_v}_N\|dudv
$$

Así podemos calcular el área de una superficie parametrizada.

$$
A(S) = \iint\limits_Sd\sigma = \iint\limits_D\|\Sigma'_u\times\Sigma'_v\|\cdot dudv
$$

## Superficie como Campo Escalar

Si una superficie está escrita como campo escalar, entonces puedo buscar la normal como en las unidades anteriores.

$$
\text{Si }z(x,y):\,\Sigma = (x,y,f(x,y))
$$

$$
\vec N = (-f'_x,\,-f'_y,\,1)
$$

$$
d\vec\sigma = \vec Ndxdy
$$

## Superficie Implícita

Si la superficie está definida implícitamente (como conjunto de nivel de $F$), entonces:

$$
\underbrace{\vec N = \nabla F(x,y,z)}_{\text{F es }\perp \text{ a su } C_k \text{ en } x_0}
$$

Como quiero escribirlo en función de una de las variables, entonces:

$$
\frac{\nabla F}{F'_z} = \bigg(\frac{F'_x}{F'_z},\,\frac{F'_y}{F'_z},\,1\bigg) = \bigg(-f'_x,\,-f'_y,\, 1\bigg)
$$

$$
d\sigma = \bigg\|\frac{\nabla F}{F'_z}\bigg\|
$$

## Flujo

Llamamos **flujo** a la integral de superficie de tipo vectorial.

Sea $S$ una superficie en $\mathbb{R}^3$, y $f$ un campo vectorial que representa la velocidad de un fluido en el espacio.

> [!note]
> ¿Cuanto liquido atraviesa la superficie por unidad de tiempo?

Solo la porción perpendicular de la velocidad atraviesa la superficie. Entonces, si multiplico esta porción por el área infinitesimal, calculo el flujo. También se puede pensar como el área del paralelogramo formado por la base infinitesimal y la velocidad de la partícula en el punto.

$$
\substack{
\text{Flujo}\\
\text{Infinitesimal}} = \Big(\vec f \cdot \Sigma'_u\times\Sigma'_v\Big)dudv
$$

$$
\varPhi_s(\vec f) =\iint\limits_S\vec f\cdot d\vec\sigma = \iint\limits_D\vec f\cdot\Sigma'_u\times\Sigma'_v\cdot dudv
$$
