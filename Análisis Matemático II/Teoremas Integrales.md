## Divergencia

La divergencia se calcula con el producto escalar entre el operador nabla $\nabla$ y una función vectorial $f$, el resultado sería la traza de la jacobiana de $f$

$$
\text{Div}(f) = \nabla\cdot \vec f = f'_{1_x} + f'_{2_y}+ f'_{3_z}
$$

Representa la cantidad de líquido saliente en un punto (fuente). Si es negativa, el líquido está entrando. (sumidero)

Si la divergencia es nula, entonces el campo es **solenoidal**.

## Rotor

El rotor se calcula con el producto vectorial entre el operador nabla $\nabla$ y una función vectorial $f$.

$$
\text{Rot}(f) = \nabla\times\vec f =
\begin{vmatrix}
\hat i & \hat j &\hat k \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} &\frac{\partial}{\partial z} \\
f_1 & f_2 & f_3
\end{vmatrix} =
\bigg(
\frac{\partial f_3}{\partial y} - \frac{\partial f_2}{\partial z},\,
\frac{\partial f_1}{\partial z} - \frac{\partial f_3}{\partial x},\,
\frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y}
\bigg)
$$

Si el rotor es distinto de 0, esto indica que en ese punto se genera un vórtice, o un torbellino. En caso contrario, el campo en ese punto está tranquilo. Es **irrotacional.** Si el rotor es nulo en todo el campo, entonces es un campo conservativo

El rotor y la Divergencia se anulan entre sí.

$$
\begin{gathered}
\nabla\cdot(\nabla \times f) ) = 0\\
\nabla\times (\nabla \cdot f) ) = 0
\end{gathered}
$$

## Teoremas Integrales

Relacionan entre sí, integrales.

- $\text{Gauss}$: Relaciona Flujo con una integral triple
- $\text{Stokes}$: Relaciona Circulación con un flujo
- $\text{Green}$: Relaciona Circulación con una integral doble (Stokes en 2D)

## Teorema de Gauss

Sí se cumple que

- $f \in C^1(D), D\subset \mathbb{R}^3\to \mathbb{R}^3$
- $V \subset D,\quad\text{Volumen Compacto}$
- $\partial V,\quad\text{Superficie frontera cerrada es suave a trozos, orientada hacia afuera}$

Entonces podemos aplicar el **teorema de Gauss.**

$$
\boxed{{\subset\!\supset} \llap{\iint}_{\partial V} \vec f \cdot d\vec\sigma = \iiint\limits_{V}\nabla\cdot\vec f\cdot dxdydz}
$$

Este teorema permite calcular el flujo de superficies cerradas, con más facilidad. El resultado de la integral devuelve la cantidad de líquido saliente del sólido.

Si la superficie no es cerrada, se puede usar el teorema cerrando la superficie, pero restándole el flujo de la superficie agregada.

## Teorema de Stokes

Sí se cumple que

- $f \in C^1(D), D\in R^3$
- $S \subset D,\quad\text{Superficie abierta, orientable, suave (a trozos)}$
- $C,\,\text{Borde orientado respecto de la normal de S (mano derecha)}$

> [!note]
> Una superficie orientable si tiene dos caras. Un ejemplo de una superficie no orientable es la Banda de Möbius

Entonces podemos aplicar el **teorema de Stokes.**

$$
\boxed{\oint\limits_{C} \vec f \cdot d\vec s = \iint\limits_{S}\nabla\times\vec f\cdot d\vec\sigma}
$$

Este teorema permite calcular la circulación de curvas cerradas, con más facilidad. El resultado de la integral es independiente de la superficie, solo depende de sus bordes. Debido a esto, se calcula la circulación con la superficie más simple posible.

## Teorema de Green

Sea $\vec f:D\subset \mathbb{R}^2\to\mathbb{R}^2$, y $C$ una curva cerrada, plana, suave o suave a trozos, orientada en sentido contrario a las agujas del reloj (positivo), perteneciente a $D$. Entonces podemos aplicar el **teorema de Green**.

El teorema de Green se utiliza para calcular la circulación en entornos de dos dimensiones. Aplicando lo mismo, pero usando una superficie que sea totalmente parte del plano. La normal en este caso sería perpendicular al plano

$$
\begin{gathered}
\vec F = \Big(f_1(x,y),\,f_2(x,y),\,0\Big)
\\ \, \\
\vec N = \big(0,\,0,\,1\big)
\\ \, \\
\nabla\times\vec F = \bigg(0,\,0,\,\frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y}\bigg)
\end{gathered}
$$

A partir del teorema de Stokes, llegamos al teorema de Green

$$
\oint\limits_{C^+} \vec f\cdot d\vec s = \iint\limits_S \nabla\times \vec F\cdot d\vec\sigma
$$

Simplificando los vectores, llegamos a que

$$
\boxed{W_{c^+}(f) = \iint\limits_S \frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y}\,\cdot dxdy}
$$
