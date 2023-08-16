---
title: Ecuaciones Diferenciales de Frontera
---

## Definición

Si tenemos un problema de ecuación diferencial con valores en la frontera de siguiente forma, podemos encontrar una aproximación para los valores de $y$.

$$
\begin{cases}
y'' = f(x, y, y')\qquad a \leq x \leq b\\
y(a) = \alpha \\
y(b) = \beta 
\end{cases}
$$

A diferencia que los problemas de valores iniciales de segundo orden, este problema no requiere escribir la ecuación diferencial como un sistema de ecuaciones diferenciales de primer orden.

## Aproximación por Diferencias Finitas

Definimos $h = (b - a)/n$, donde $x_i = a + ih, \ \forall i = 0,1, \cdots, n$

Podemos reescribir el problema como:

$$
y'' + P(x)y' + Q(x)y = f(x)
$$

Luego, a partir de aproximar $y''$ y $y'$ con el polinomio de Taylor centrado, podemos simplificar la expresión para obtener un sistema de ecuaciones

$$
y_{i+1}\Big[1 + P_i \frac h2\Big] + y_i\Big[1Q_ih^2 - 2\Big] + y_{i-1}\Big[1 - P_i \frac h2\Big] = h^2f_i
$$

A partir de resolver el sistema de ecuaciones, evaluando la expresión en $i=1, 2, \cdots, n{-}1$. Encontramos una aproximación de $y$ para los puntos de red dentro del intervalo $[a,b]$.
