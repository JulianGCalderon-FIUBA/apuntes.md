# Regiones Rectangulares

Una integral doble busca el area debajo de una función de dos variables. Se puede pensar como la suma de muchos rectángulos, con los lados tendiendo a $0$. Tambien como la suma de muchas integrales de Análisis I.

$$
\begin{align*}\iint f(x,y)dxdy &= \int dx\bigg(\int f(x,y)dy\bigg)\\
&=\int dy\bigg( \int f(x,y)dx\bigg)\end{align*}
$$

# Regiones Simples

Las regiones simples son aquellas que, no son rectángulos, pero se parecen a estos. Un lado de la region es fijo, mientras que el otro varia. Se pone afuera el limite fijo, y adentro los limites variables.

$$
\int_a^bdx\bigg(\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)dy\bigg)
$$

$$
\int_a^bdy\bigg(\int_{\Psi_1(x)}^{\Psi_2(x)}f(x,y)dx\bigg)
$$

![[Integrales Dobles 1.png|Integrales%20Dobles%201e415a8cc5c641f19fcba33db477bb15/Untitled.png]]

> [!note]
> Para regiones mas complejas, se puede pensar la integral como la suma de distintas regiones simples, con limites variables conocidos.


# Cambio de variable

Para facilitar la integración, se puede transformar la region para llegar a una mas simple, Cambiando las coordenadas.

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


Esto permite que los limites de la integración sean mas simples.

# Regiones Circulares

En regiones circulares, es mas fácil resolver las integrales dobles en coordenadas polares

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

![[Integrales Dobles 2.png|Integrales%20Dobles%201e415a8cc5c641f19fcba33db477bb15/Untitled%201.png]]