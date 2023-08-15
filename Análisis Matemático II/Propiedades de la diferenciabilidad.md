
- Una suma de funciones $C^1$ es $C^1$
- Un producto de función $C^1$ es $C^1$
- Un cociente de funciones $C^1$ es $C^1$, (con denominador no nulo)

## Regla de la Cadena

Sea $\vec f: D\subset\mathbb{R}^n\to\mathbb{R}^m,\vec g: D\subset\mathbb{R}^m\to\mathbb{R}^p$. Si $\vec f$ es diferenciable en $\vec x_0$ y $\vec g$ es diferenciable en $\vec y_0 =\vec f(\vec x_0)$, entonces la composición $\vec h = \vec g \circ\vec f$, resulta diferenciable en $\vec x_0$, sí existe $\vec h$.

$\vec h$ existe si $\text{Img}(f) \subset Dom(g)$

$$
D_{\vec h}(\vec x_0) = D_{\vec g}(\vec f(\vec x_0))\times D_{\vec f}(\vec x_0)
$$

Donde $D_{\vec f}$ es la matriz Jacobiana de $\vec f$

## Árbol de derivación

![[Propiedades de la diferenciabiliad 1.png|450]]

$$
h'_x = g'_u f'_x + g'_vf'_x
$$

$$
h'_y = g'_u f'_y + g'_vf'_y
$$

$$
h'_z = g'_u f'_z + g'_vf'_z
$$
