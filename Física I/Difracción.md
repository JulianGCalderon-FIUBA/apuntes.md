---
title: Difracción
---

La difracción ocurre cuando la ranura por la que pasa la luz, no es puntual. Tiene un diámetro similar a la longitud de onda $\lambda$ de la onda. Debido a esto, se puede pensar a la difracción y a la interferencia como conceptos similares, pero varía en la cantidad de ondas que se analizan.

La constante o periodo de red $C$ define la cantidad de ranuras que se encuentran por unidad de longitud

$$
C = \frac 1d
$$

**Principio de Huyggens-Fresnel:** Todo punto sin obstrucción de un frente de onda se puede considerar como un emisor de una onda esférica secundaria (de la misma frecuencia que la primaria). La amplitud del campo óptico en cualquier punto posterior es la superposición de todas esas ondas secundarias

## Difracción por una Rendija

En el eje de simetría, se ubica el máximo principal $(\theta = 0)$. Los ceros y máximos secundarios se ubican hacia los costados del eje, Cada vez con menor intensidad. La cantidad de fuentes tiende al infinito, y la distancia entre las fuentes es despreciable.

![[Difraccion 1.png|400]]

### Mínimos

Para que haya interferencia destructiva, se tiene que cumplir la siguiente condición.

$$
a\cdot\sin\theta = n\lambda
$$

$$
y_{min} = n\cdot\lambda\frac Da
$$

$$
n = \pm\,1,2,3,\cdots
$$

### Intensidad

Para calcular la intensidad, tengo que calcular la suma de la intensidad de todos los fasores.

$$
\beta = \frac{a\pi\sin\theta}\lambda = \frac{ak\sin\theta}2
$$

$$
A = A_0\frac{\sin\beta}{\beta}
$$

$$
I = I_0\frac{\sin^2\beta}{\beta^2}
$$

## Redes de Difracción

Ocurren cuando se superponen los fenómenos de interferencia y de difracción. Es decir, se estudia el comportamiento de ondas al atravesar múltiples $N$ ranuras no puntuales de ancho $a$ equidistantes $d$ entre sí.

$$
\begin{gathered}
\lambda \gg a\\
d > a
\end{gathered}
$$

El gráfico para $N$ rendijas anchas se visualiza como la interferencia para $N$ rendijas puntuales, envuelta por la campana de difracción para una rendija ancha.

La cantidad de mínimos de interferencia que hay entre los máximos de la campana de difracción es de $[N-1]$

La cantidad de máximos de interferencia que hay entre los máximos de la campana depende de la relación $a,d$

### Máximos de interferencia

Los máximos de interferencia se encuentran cuando la diferencia de recorrido es de una longitud de onda $\lambda$

$$
d\sin\theta = m\cdot\lambda
$$

$$
y_M = m\cdot\frac{\lambda D}{d}
$$

### Mínimos de interferencia

Los mínimos de interferencia se encuentran cuando los fasores se anulan entre sí

$$
d\sin\theta = \frac mN\cdot\lambda
$$

$$
y_M = \frac mN\cdot\frac {\lambda D}d
$$

### Mínimos de difracción

Los mínimos de difracción se encuentran cuando cada par de ondas (medio e inferior) se anula entre sí, con una diferencia de recorrido de $\lambda/2$

$$
b\sin\theta = n\lambda
$$

$$
y_n = n\cdot\lambda\cdot\frac{D}{a}
$$

### Relación $a,d$

Si los máximos de interferencia y los mínimos de difracción coinciden en un punto, entonces sus posiciones son iguales. Por lo que puedo igualar las ecuaciones y despejar la relación entre $a,d$

$$
\frac da = \frac mn
$$

Si $d/a = k,\,k\in\mathbb{N}$, entonces se da que el primer mínimo de difracción coincide con el máximo de interferencia $m =k$. Esto implica que dentro de la campana principal de difracción hay $[2k-1]$ máximos.

### Intensidad

La intensidad resultante de esta superposición en la pantalla es

$$
\beta = \frac{a\pi\cdot\sin\theta}\lambda = \frac{ak\cdot\sin\theta}2
$$

$$
\gamma= \frac{\delta}2 =
\frac{dk\cdot\sin\theta}2
$$

$$
I = I_0\cdot
\frac{\sin^2\beta}{\beta^2}\cdot
\frac{\sin^2(N\cdot\gamma)}{\sin^2\gamma}
$$
