---
title: Campo Eléctrico
---

El campo eléctrico es una magnitud vectorial que en cada punto $p$ apunta en la dirección de la fuerza eléctrica si pusiéramos en el punto $p$ una carga $q_0 = 1C$

$$
\vec E = \frac{F_0}{q_0}\implies[\vec E] = \frac NC
$$

El campo eléctrico es uniforme si es constante para todo punto $p$.

Así, la fuerza que experimenta una partícula cargada $q$ en cada punto $\vec r$ es de:

$$
\vec F(q, \vec r) = q\cdot \vec E(\vec r)
$$

## Campo Eléctrico de una Carga Puntual

$$
\vec E(\vec r) = qk\cdot\frac{(\vec r-\vec r')}{\|\vec r - \vec r'\|^3}
$$

- Punto Campo: $\vec r: (x,y,z)$
- Punto Fuente: $\vec r': (x,y,z)$
- Carga Puntual: $q$
- Constante: $k = 1/4\pi\epsilon_0$

Si la carga se encuentra en el eje de coordenadas, entonces tenemos:

$$
\vec E(\vec r) = qk\cdot\frac{\hat r}{r^2}
$$

Si la carga puntual es negativa, entonces el sentido del campo se invierte. Entrante a la carga negativa.

## Campo Eléctrico de un conjunto de Cargas

Debido al principio de superposición, podemos sumar los campos eléctricos de cada carga puntual y llegar a la siguiente definición

$$
\vec E(\vec r) = k\sum_{i}^nq_i\cdot\frac{(\vec r - \vec r_i)}{\|\vec r - \vec r_i\|^3}
$$

## Campo Eléctrico en una Distribución Continua

Podemos pensar a este campo eléctrico como una suma de cargas infinitesimales. Es decir, una integral

$$
\vec E(\vec r) = k\int \frac{r-r'}{\|\vec r - \vec r'\|^3}\cdot dq
$$

Si está distribuida en una línea, entonces podemos definir la densidad lineal de carga $\lambda$, y entonces $dq = \lambda dl$.

Si está distribuida en una superficie, podemos definir la densidad superficial de carga $\sigma$, y entonces $dq = \sigma ds$

Si está distribuida en un volumen, podemos definir la densidad volumétrica de carga $\rho$, y entonces $dq = \rho dv$

Tanto $\lambda, \sigma, \rho$ pueden depender de las coordenadas primadas. $\lambda(\vec r'), \sigma(\vec r'), \rho(\vec r')$.

$r$ es el punto campo, y no se integra respecto a esta variable. $r'$ por el otro lado es el punto fuente y varía dentro de la integral

Por lo tanto, definimos el campo eléctrico de una distribución continua de cargas en un volumen como

$$
\vec E(\vec r) = k\iiint_V \rho(x', y', z')\cdot\frac{(\vec r - \vec r')}{\|\vec r - \vec r'\|^3}dx'dy'dz'
$$

## Líneas de Campo Eléctrico

Son curvas imaginarias, de modo que su tangente en todo punto del espacio sea la dirección del campo eléctrico $E$. Al representar la dirección del campo, se pierde la información del módulo.

Para remplazar esta información faltante usamos la densidad de líneas dibujadas, la cual es proporcional a la intensidad del campo. Cuantas más líneas haya alrededor de un punto $p$, mayor es la intensidad del campo en ese punto

Si alrededor de una carga $C$ hay más líneas de campo que alrededor de la carga $D$, entonces podemos afirmar que $\|Q_C\| > \|Q_D\|$

Las líneas de campo son salientes de las cargas positivas (fuentes), y entrantes en las cargas negativas (sumidero).

Las líneas de campo nunca se cruzan, ya que cada punto pertenece a una sola línea de campo.

![[Campo Electrico 1.png|450]]
