$$
\text{Curva }\gamma(t):\mathbb{R}\to\mathbb{R}^3
$$

Si la derivada de la curva existe para todo punto y es continua, se dice que es una parametrización **suave**.

$$
ds = \|\gamma'\| dt
$$

Entonces la longitud $L$ de la curva es la suma de todos los $ds$, fragmentos de curva.

$$
\boxed{long(C) = \int_a^b \|\gamma'\|dt}
$$

> [!note]
> La integral no depende de la parametrización elegida

## Integral de Campos Escalares sobre Curvas

### Masa

$$
\text{densidad lineal }\delta = \frac {dM}{dL},\quad M = \delta\cdot ds
$$

$$
\text{masa }M = \int \delta ds
$$

Tomando estas definiciones, llegamos a que:

$$
\boxed{M = \int_a^b \delta\big(\gamma(t)\big) \cdot \|\gamma'(t)\|\cdot dt}
$$

### Centro de Masa

$$
r_{cm} = \frac{\sum m_i \cdot \vec r_i}{\sum m_i}
$$

Si aplicamos las definiciones anteriores:

$$
\boxed{r_{cm} = \frac{\int_a^b \gamma(t) \cdot \delta\big(\gamma(t)\big) \cdot \|\gamma'(t)\|\cdot dt}{\int_a^b \delta\big(\gamma(t)\big) \cdot \|\gamma'(t)\|\cdot dt }}
$$

### Momento de Inercia

$$
I_x = \sum m_i \cdot x_i^2
$$

Con integrales:

$$
\boxed{I_x = \int_a^b \delta\big(\gamma(t)\big)\cdot\gamma_x^2(t)\cdot\|\gamma'(t)\|\cdot dt}
$$

> [!note]
> Se calcula de forma análoga para los otros ejes

## Integral de Campos Vectoriales sobre Curvas

### Trabajo de Fuerza

Cuando trabajamos con una partícula en un campo de fuerzas, sea $\gamma$ su trayectoria y $f$ el campo de fuerzas.

$$
W_c(\vec f) =\int \vec f\cdot d\vec s
$$

$$
d \vec s = \vec\gamma'(t)dt
$$

Entonces, el trabajo de una fuerza es (circulación de $f$ sobre $c$):

$$
\boxed{W_c(\vec f) = \int_a^b \vec f\big(\vec\gamma(t)\big)\cdot\vec\gamma'(t)\cdot dt}
$$

> [!note]
> La integral no depende de la parametrización elegida, pero si del sentido.

> [!note]
> En general, el trabajo entre $P$ y $Q$ depende de la trayectoria, a menos que se trate de campos conservativos. Para los cuales la integral es independiente de la trayectoria.

$$
\underbrace{\oint_C}_{\substack{
\text{Integral sobre}\\
\text{sobre curva}\\
\text{cerrada}}}
\vec f\cdot d\vec s \neq 0 \implies \text{campo no conservativo}
$$

Si $\vec f$ es un campo conservativo, entonces es el gradiente de una función potencial $\varphi$

$$
\vec f = \nabla\varphi
$$

$$
\int_a^b \vec f(\vec \gamma\big(t)\big)\cdot\vec\gamma'(t)\cdot dt= \int \underbrace{\nabla\varphi\big(\vec\gamma(t)\big)\cdot\vec\gamma'(t)}_{\Big(\varphi\big(\vec\gamma(t)\big)\Big)'}\cdot dt
$$

$$
W_f = \underbrace{\varphi\big(\vec\gamma(b)\big)}_\text{Punto Final} - \underbrace{\varphi\big(\vec\gamma(a)\big)}_\text{Punto Inicial}
$$

> [!note]
> La matriz jacobiana de un campo conservativo debe ser simétrica

$$
J_f = \begin{pmatrix}f'_{1_x} & f'_{1_y} & f'_{1_z}\\f'_{2_x} & f'_{2_y} & f'_{2_z}\\f'_{3_x} & f'_{3_y} & f'_{3_z}\end{pmatrix} = \begin{pmatrix}Q''_{xx} & Q''_{xy} & Q''_{xz}\\Q''_{yx} & Q''_{yy} & Q''_{yz}\\Q''_{zx} & Q''_{zy} & Q''_{zz}\end{pmatrix} 
$$

### Encontrar Función Potencial $\varphi$

$$
\begin{cases}f_1 = \varphi'_x\\f_2 = \varphi'_y\\f_3 = \varphi'_z\end{cases}\quad\text{Sist. de ED en derivadas parciales}
$$

Se resuelve integrando y derivando respecto de $x,y,z$.

### Condición Necesaria Y Suficiente para Campo Conservativo

Sea $F$ un campo de fuerzas, entonces es conservativo en $D$ si $J_F$ es simétrico y continuo en $D$, y $D$ es simplemente conexo.

**Simplemente conexo:**

Un conjunto es simplemente conexo si para toda curva cerrada contenida en $D$, la puedo contraer hasta tener un solo punto, tambien incluido en $D$.
