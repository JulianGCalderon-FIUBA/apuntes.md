Si tenemos un conjunto de datos y queremos encontrar una función que aproxime el conjunto de datos, entonces buscamos una función cuyo error cuadrático medio sea el mínimo posible. Buscamos la recta de mínimos cuadrados que aproxima los datos.

Desde un punto de vista algebraica, buscamos un vector que minimiza la norma del error. A partir de una proyección sobre el subespacio de funciones.

$$
Ax = b
$$

$$
A^T A x = A^T b
$$

## Lineal

Si creemos que nuestros datos se asemejan a una función lineal, entonces aplicamos lo visto anteriormente para encontrar la mejor recta que aproxime.

$$
y = a + bx
$$

$$
\begin{pmatrix}
1 & x_1 \\
\vdots & \vdots\\
1 & x_n
\end{pmatrix}
\begin{pmatrix}
a \\b
\end{pmatrix}
=
\begin{pmatrix}
y_1\\
\vdots\\
y_n
\end{pmatrix}
$$

Por mínimos cuadrados, resolvemos la expresión anterior

## Exponencial

Si el modelo es de la forma exponencial, entonces trataremos de modificar la expresión para llegar a una relación lineal y aplicar la técnica anterior.

$$
y = ae^{bx}
$$

$$
\ln (y) = \ln(a) + bx
$$

$$
\begin{pmatrix}
1 & x_1 \\
\vdots & \vdots\\
1 & x_n
\end{pmatrix}
\begin{pmatrix}
\ln a \\b
\end{pmatrix}
=
\begin{pmatrix}
 \ln y_1\\
\vdots\\
 \ln y_n
\end{pmatrix}
$$

## Potencial

Si el modelo es de la forma potencial, lo resolveremos de forma similar

$$
y = ax^b
$$

$$
\log(y) = \log(a) + b\log(x)
$$

$$
\begin{pmatrix}
1 & \log x_1 \\
\vdots & \vdots\\
1 & \log x_n
\end{pmatrix}
\begin{pmatrix}
\log a \\b
\end{pmatrix}
=
\begin{pmatrix}
 \log y_1\\
\vdots\\
 \log y_n
\end{pmatrix}
$$

## Racional

El modelo racional es un poco más complejo, sin embargo, se resuelve da la misma forma

$$
y = \frac{ax}{b + x}
$$

$$
\frac 1y = \frac ba \frac 1x + \frac 1a
$$

$$
\begin{pmatrix}
1 & \frac 1{x_1} \\
\vdots & \vdots\\
1 & \frac 1{x_n}
\end{pmatrix}
\begin{pmatrix}
\frac 1a\\ \frac ba
\end{pmatrix}
=
\begin{pmatrix}
 \frac 1{y_0}\\
\vdots\\
 \frac 1{y_n}
\end{pmatrix}
$$

## Regresión por Polinomios

El procedimiento es fácilmente extensible al ajuste de datos con un polinomio de orden superior.
