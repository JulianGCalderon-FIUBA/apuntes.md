$$
\lim_{x\to x_0} \vec f(\vec x) =
\forall\varepsilon > 0, \exists\delta = \delta(\varepsilon) / 0 < \|\vec x - \vec x_0\| < \delta \implies \|\vec f(\vec x) - \vec L\| < \varepsilon
$$

En el caso de varias variables existe una infinidad de caminos para aproximarse a un punto. Para que exista el límite, por todos esos caminos posibles deberíamos observar que las imágenes de $f$ se aproximan aún el mismo valor.

En los campos y funciones vectoriales, el cálculo de límites se hace componente a componente

## Estrategias

### Para mostrar que un límite no existe

- Límites iterados (Acerco una componente al límite y después el otro)
- Acercarme por curvas del dominio que contengan al límite
	- Rectas: $y = m(x-x_0) + y_0$
	- Parábolas:
		- $y = m(x-x_0)^2 + y_0$
		- $x = m(y - y_0)^2 + x_0$
	- Curva de nivel $K$:
		- Me acerco por una curva de nivel $k$ que contenga el punto al que me quiero acercar

### Para calcular límites

- Infinitésimo por Acotado (Producto de una expresión que tiende a cero y otra acotada)
- Por límites conocidos
	- $\displaystyle \lim_{x\to0}\frac{senx}{x} = 1$
	- $\displaystyle \lim_{x\to0}\frac{1-cosx}{x} = 0$
	- $\displaystyle \lim_{x\to0}\frac{e^x-1}{x} = 1$

## Continuidad

Decimos que $\vec f(\vec x)$ es continua en $\vec x_0$ si:

$$
\begin{gathered}
\exists\vec f(\vec x)\\\exists \lim_{\vec x\to \vec x_0} \vec f(\vec x) = \vec L\\\vec L = \vec f(\vec x_0)
\end{gathered}
$$

Si $\vec f(\vec x)$ es continua todos los puntos de $A$, entonces la función es continua en $A$.
