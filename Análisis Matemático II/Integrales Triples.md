Similar a las integrales dobles, las integrales triples calculan el área a partir de pequeños cubos.

$$
\iiint_V f(x,y,z)\cdot dxdydz
$$

Si $f(x,y,z) = 0$, entonces de esta manera se calcula el volumen de un espacio tridimensional.

Si $f$ representa la densidad $\delta$ del cuerpo en el punto, entonces la integral triple representa la **masa** del cuerpo.

$f$ debe ser continua en la región, (o continua salvo por una porción nula de volumen).

## Regiones Simples

Se dice que una región es simple cuando se puede proyectar sobre uno de los planos coordenados. Para que un cuerpo sea proyectable, al trazar una recta perpendicular al plano, debe atravesar la región solo dos veces la región.

Si un cuerpo es proyectable, entonces puedo calcular su volumen utilizando dos campos escalares, que sean función de las variables del plano. $\Big(z = \varphi_1(x,y),\,z=\varphi_2(x,y)\Big)$

Podemos reducir la integral triple, a la suma de varillas infinitesimales de dirección $z$, en toda la proyección.

$$
\iint_{P_{xy}(V)}dxdy\underbrace{\int_{\varphi_1}^{\varphi_2}f(x,y,z)dz}_{g(x,y)}
$$

## Cambio de coordenadas

En integrales triples, puedo hacer un cambio de coordenadas parcial, Cambiando dos coordenadas, y dejando constante la otra. O puedo cambiar las tres variables.

$$
\begin{cases}x = x(u,v,w)\\
y = y(u,v,w)\\
z = z(u,v,w)\end{cases}\implies \boxed{dxdydz = K\cdot dudvdw}
$$

$$
K = \begin{vmatrix}x'_u && x'_v && x'_w\\
y'_u && y'_v && y'_w\\
z'_u && z'_v && z'_w\end{vmatrix}\quad\text{Factor de transformacion}
$$

## Coordenadas Esféricas

$$
\text{Variables}\begin{cases}
\theta:\text{ Longitud}\\
\varphi:\text{ Latitud}\\
\rho:\text{Distancia al origen}
\end{cases}\\\quad\\
\text{Diccionario}\begin{cases}
x = \rho\sin(\varphi)\cos(\theta)\\
y = \rho\sin(\varphi)\sin(\theta)\\
z = \rho\cos(\varphi)
\end{cases}
$$

$$
K = \rho^2\sin(\varphi)\cdot  d\varphi d\theta d\rho
$$

![[Integrales Triples 1693351678.png]]

En la imagen, los parámetros varían según:

$$\theta\in[0,2\pi],\,\varphi\in[0,\pi],\,\rho\in\mathbb{R}^+$$
