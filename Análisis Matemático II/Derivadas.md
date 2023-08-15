## Funciones vectoriales

$$
f(t) = (x, y, \cdots)
$$

La derivada de una función vectorial se hace componente a componente, aplicando la definición de Análisis 1

## Campos escalares

$$
f(x,y) = \cdots
$$

La derivada en un campo escalar depende de la dirección por la cual me aproximo al punto, por lo que se calcula según un vector director

$$
f'(\vec x_0, \hat v) = \lim_{h\to 0} \frac{f(\vec x_0 + h\vec v) - f(\vec x_0)}{h}
$$

La derivada direccional es un número real que representa la pendiente de la recta tangente trazada en $(x_0, y_0, f(x_0, y_0)$ a la curva que se obtiene cortando la gráfica de $f$ con una curva cuya traza en el plano $xy$ es la recta $(x,y) = (x_0, y_0) + h\vec v$, con $h \in R$.

> [!warning] Atención
> Una función no tiene por qué ser continua en $x,y$ para ser derivable. En cálculos de varias variables, estos conceptos son independientes entre sí.

## Derivadas parciales

Cuando $\displaystyle\vec v = \vec e_k$ (vector canónico) la derivada se llama parcial $\displaystyle \frac{\partial f}{\partial e_k}(\vec x)$

La derivada parcial $\partial$ se calcula derivando una sola variable y dejando a la otra como constante.

Si el dominio es más delicado, se analiza por definición

### Teorema de Schwarz

Si las derivadas (cruzadas) $f''_{xy}, f''_{yx}$ existen y son continuas, coinciden

$$
f'''''_{xyyxy} = f'''''_{xxyyy}= \frac{\partial^5f(x,y)}{\partial x^2\partial y^3}
$$

## Gradiente

Es un vector que indica la dirección en la cual el campo varía más rápidamente.

Si $f$ es diferenciable en $\vec r$, entonces:

$$
\nabla f(\vec r) = \Big(f'_{r_1}(\vec r),\cdots,f'_{r_n}(\vec r)\Big )
$$

$$
\begin{align*}f'(\vec r, \hat v) &= \nabla f(\vec r)\cdot \hat v\\&=\|\nabla f(\vec r)\|\cdot\underbrace{\|\hat v\|}_{=1}\cdot\cos\theta\end{align*}
$$

**La derivada es:**

- Máxima $\|\nabla f(\vec r)\|$ en $\theta = 0$
- Mínima $\|\nabla f(\vec r)\|$ en $\theta = \pi$
- Nula en $\displaystyle\theta = \frac\pi 2$
