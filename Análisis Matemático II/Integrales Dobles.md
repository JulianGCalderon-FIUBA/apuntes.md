---
title: Integrales Dobles
---

## Regiones Rectangulares

Una integral doble busca el área debajo de una función de dos variables. Se puede pensar como la suma de muchos rectángulos, con los lados tendiendo a $0$. También como la suma de muchas integrales de Análisis I.

$$
\begin{align*}\iint f(x,y)dxdy &= \int dx\bigg(\int f(x,y)dy\bigg)\\
&=\int dy\bigg( \int f(x,y)dx\bigg)\end{align*}
$$

## Regiones Simples

Las regiones simples son aquellas que, no son rectángulos, pero se parecen a estos. Un lado de la región es fijo, mientras que el otro varía. Se pone afuera el límite fijo, y adentro los límites variables.

$$
\int_a^bdx\bigg(\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)dy\bigg)
$$

$$
\int_a^bdy\bigg(\int_{\Psi_1(x)}^{\Psi_2(x)}f(x,y)dx\bigg)
$$

![[Integrales Dobles 1.png|475]]

> [!note]
> Para regiones más complejas, se puede pensar la integral como la suma de distintas regiones simples, con límites variables conocidos.

## Cambio de variable

Para facilitar la integración, se puede transformar la región para llegar a una más simple, Cambiando las coordenadas.

$$
\begin{cases}x = x(u,v)\\
y = y(u,v)\end{cases}\implies \boxed{dxdy = K\cdot dudv}
$$

$$
K = \begin{vmatrix}x'_u && x'_v\\
y'_u && y'_v\end{vmatrix}\quad\text{Factor de transformacion}
$$

> [!note]
> El factor de transformación es siempre positivo

Esto permite que los límites de la integración sean más simples.

## Regiones Circulares

En regiones circulares, es más fácil resolver las integrales dobles en coordenadas polares

$$
\text{Variables}\begin{cases}
\theta:\text{ Angulo}\\
r:\text{ Distancia al origen}\\
\end{cases}\\\quad\\
\text{Diccionario}\begin{cases}
x = r\cdot\cos\theta\\
y = r\cdot\sin\theta\\
r = \sqrt{x^2+y^2}
\end{cases}
$$

$$
K = r\cdot drd\theta
$$

![[Integrales Dobles 2.png|260]]
