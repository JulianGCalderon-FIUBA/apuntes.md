## Circuitos Compuestos

Cuando tenemos circuitos con más de un componente, vamos a tener que realizar operaciones entre *cosenos* para hallar una expresión para la corriente del circuito.

Vamos a querer hallar los valores instantáneos del circuito: $i(t), v_q(t)$.

$$
v_q(t) = i(t) R + \frac 1C \int i(t) dt +  L\cdot \frac{di(t)}{dt}
$$

$$
i(t) = I_0 \cdot \cos(wt + \phi_v+ \phi_{iv})
$$

Como la expresión es una ecuación integro-diferencial, vamos a utilizar el campo complejo para resolverlo. $j = \sqrt{-1}$

$$
\tilde V_q(t) = V_0 \cdot e^{j\cdot(wt + \phi_v)}
$$

$$
\tilde I(t) = I_0 \cdot e^{j\cdot(wt + \phi_v + \phi_{iv})}
$$

Podemos transformar el fasor de voltaje en su parte trigonométrica, y relacionarlo el voltaje de la fuente. (podemos hacer lo mismo con el fasor de la corriente)

$$
\tilde V_q(t) = V_0 \cdot \Big[ \cos(wt + \phi_v) + j \sin(wt + \phi_v)\Big]
$$

$$
\mathbb{R} e(\tilde V_q(t)) = v_q(t)
$$

$$
\tilde I_q(t) = I_0 \cdot \Big[ \cos(wt + \phi_i) + j \sin(wt + \phi_i)\Big]
$$

$$
\mathbb{R} e(\tilde I(t)) = i(t)
$$

También, podemos integrar y derivar el fasor de la corriente.

$$
\int \tilde I(t) dt = \frac{-j\tilde I(t)}{w}
$$

$$
\frac{d\tilde I(t)}{dt} = \tilde I(t) \cdot j\ w
$$

Una vez hecho esto, podemos transformar nuestra ecuación integro-diferencial en una ecuación algebraica.

$$
\tilde V_q(t) = \tilde I(t) \cdot\underbrace{\Big[R + j(X_L - X_C)\Big]}_\text{ $\mathbb{Z}:$ Impedancia del Circuito}
$$

$$
\tilde V_q(t) = \tilde I(t)\cdot \mathbb{Z}
$$

### Pseudo - Ley de Ohm

Si desarrollamos los fasores, llegamos a la **Pseudo - Ley de Ohm**

$$
V_0\ e^{j\phi_v} = I_0\ e^{j\phi_i} \cdot \mathbb{Z}
$$

$$
\boxed{\Bbb V = \Bbb I \cdot \mathbb{Z}}
$$

Reescribimos la impedancia del circuito como un número complejo, así obtenemos una relación entre las amplitudes y las faces del circuito.

$$
|z| = \sqrt{R^2 + (X_L - X_C)^2}
$$

$$
\tan(\phi_z)  = \frac{X_L - X_C}{R}
$$

$$
\text{Amplitud}: V_0 = I_0 \cdot |z|
$$

$$
\text{Fase}: \phi_{iv} = -\phi_z
$$

$$
\text{Impedancias}:X_L = wL \quad X_c = \frac {1}{wC}
$$

También podemos definir las amplitudes en su forma eficaz, este determina el valor cuadrático medio de las funciones $v_q(t)$, $i(t)$. Esto es útil, ya que cuando medimos el voltaje y la corriente con un instrumento, obtendremos los valores eficaces.

$$
V_{ef} = \frac{V_0}{\sqrt 2}
$$

$$
I_{ef} = \frac{I_0}{\sqrt 2}
$$

> [!note]
> En Argentina, la red domiciliaria tiene un voltaje efectivo de $220\ V$, y una frecuencia de $50\ Hz$.
> 
> La amplitud pico es aproximadamente $311\ V$.

### Impedancia Inductiva

Podemos separar la impedancia inductiva en los distintos componentes

$$
\mathbb{Z} = \mathbb{Z}_r + \mathbb{Z}_i + \mathbb{Z}_c \implies

\begin{cases}\mathbb{Z}_r = R \\
\mathbb{Z}_i = j X_L\\
\mathbb{Z}_c = -j X_c\end{cases}
$$

De esta forma, podemos aplicar estas definiciones a cualquier circuito alterno, conectado en serie.

> [!note]
> Si $X_L > X_C$, $\phi_{iv} < 0$ el circuito tiene un comportamiento inductivo. En el caso contrario, el comportamiento es capacitivo. Si las reactancias son iguales, tiene un comportamiento resistivo.

## Diagramas

### Diagrama de Impedancias

El diagrama de impedancias grafica las tres impedancias: $\mathbb{Z}_r$, $\mathbb{Z}_i$, $\mathbb{Z}_c$. Dependiendo de hacia donde apunta la impedancia total, determina el tipo de circuito que se trata. Circuito inductivo si la impedancia inductiva está por encima de la impedancia resistiva.

### Diagrama Fasorial

El diagrama fasorial es un diagrama que representa los fasores en un determinado tiempo $t$. Los fasores que se graficaran serán: $\Bbb V_R(t)$, $\Bbb V_L(t)$, $\Bbb V_C(t)$, $\Bbb I(t)$.

Luego podemos sumar los fasores asociados a la caída de potencial $\tilde V$, si su ángulo es mayor al de la corriente, significa que están adelantados a la corriente (la corriente se atrasa), por lo que es un circuito inductivo.
