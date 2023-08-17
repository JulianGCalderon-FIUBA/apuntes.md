---
title: Distribuciones Continuas
---

## Uniforme

Una variable aleatoria tiene función de densidad uniforme, si todo punto tiene la misma probabilidad, su densidad está dada por:

$$
\displaystyle{f_X(x) = \begin{cases}\frac{1}{b-a} &\iff x \in [a, b] \\
0 &\iff x \notin [a,b] \end{cases}}
$$

$$
P(x \in [c, d]) = \frac{d-c}{b-a}
$$

## Exponencial

Una variable aleatoria tiene distribución exponencial de parámetro $\lambda > 0$ si su función de densidad está dada por:

$$
f_X(x) = \begin{cases}\lambda e^{-\lambda x} &\iff x \geq 0 \\
0 &\iff x <0\end{cases}
$$

$$
F_X(x) = \begin{cases}1 - e^{-\lambda x} &\iff x \geq 0\\
0 &\iff x < 0
\end{cases} 
$$

$$
P(X >x) = e^{-\lambda x}
$$

### Propiedades

1. Si $x \backsim \varepsilon(\lambda)$, entonces $P(x > t+s | x > t) = P(x > s)$
2. Además, si se cumple la propiedad anterior para una variable aleatoria, sabemos que tiene distribución exponencial

### Función Intensidad de Fallas

Esta función se relaciona la probabilidad de un punto inmediatamente después de $t$, dado que $P(x > t)$

$$
\lambda(t) = \frac{f_T(t)}{1 - F_T(t)}
$$

$$
F_T(t) = 1-e^{-\int_0^t \lambda(s) ds}
$$

## Gamma

Se dice que una V.A. $X$ tiene distribución Gamma de parámetros $\lambda$ y $k$, si su función de densidad es

$$
f_X(x) = \frac{\lambda^k}{\varGamma(k)} x^{k-1} e^{-\lambda x} \cdot \mathfrak{1}\{x > 0\}
$$

Para obtener la función $\varGamma$, debo usar la tabla de resumen de la cátedra.

## Normal

Se dice que una V.A. $X$ que toma valores $-\infty < x < \infty$ tiene una distribución normal estándar si su función de densidad es de la forma

$$
f_x(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
$$
