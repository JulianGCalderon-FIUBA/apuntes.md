## Constantes

$$
\begin{align*}
&\text{Constante Magnetica}: K_m = \frac{\mu_0}{4\pi} = 10^{-7} N  / A^2
\\
&\text{Permmeabilidad Magnetica del Vacio}: \mu_0 = 4\pi \cdot 10^{-7} N/A^2
\end{align*}

$$

$$
\begin{align*}
\text{Ampere}: [I]\\
\text{Ohmio}: [\Omega]\\
\text{Vatio}: [W]\\
\text{Tesla}: [T]
\end{align*}
$$

## Corriente Continua

$$
\vec v_a = \mu\cdot E
$$

Siendo $\mu$ la movilidad de las partículas

$$
\mu = \frac{q\ \tau}{m}
$$

$$
I = \frac{dq}{dt}
$$

$$
I = q\cdot n\cdot A \cdot \vec v_a
$$

Siendo $n$ la densidad de portadores de carga de un conductor

La unidad de la corriente es $A$

### Densidades

$$
I = \iint\limits_A \vec j(\vec r) \ dA
$$

$$
{\subset\!\supset} \llap{\iint}_S \vec J \cdot ds = 0
$$

Se define $j$ como la densidad volumetrica de corriente

$$
\vec J = \sigma \cdot \vec E
$$

$$
\sigma = \frac{q^2n\tau}{m}
$$

Siendo $\sigma$ la conductividad eléctrica

$$
I = \int \vec k \cdot d\vec l
$$

Se define $k$ como la densidad superficial de corriente

## Ley de Ohm

$$
\Delta V = I\ R
$$

$$
R = \eta\ \frac{l}{A}
$$

Se define $\eta$ como la resistividad eléctrica del material $[\Omega m]$

La unidad de la resistencia es de $\Omega$.

## Circuitos Eléctricos

$$
\sum_{i=1}^n I_i = 0\\
\small\color{Gray}\text{Ley de Nodo}
$$

$$
\sum_{i=1}^n V_i = 0\\
\small\color{Gray}\text{Ley de malla}
$$

$$
\text{Serie: }\quad R_{eq} = \sum_{i=1}^n R_i
$$

$$
\text{Paralelo: }\quad\frac{1}{R_{eq}} = \sum_{i=1}^n \frac{1}{R_i}
$$

### Potencia

$$
P = I \cdot \Delta V
$$

$$
P_{\text{entregada}} = P_{\text{abosrbida}} + P_{\text{disipada}}
$$

La unidad de la potencia es $W$. Se define como la energía consumida por segundo.

## Campo Magnético

La unidad del campo magnético es de $T$

### Fuerza Magnética sobre Carga

$$
\vec F_M = q\cdot \vec v \times \vec B
$$

$$
\vec F_\text{Lorentz} = q\vec E +  q\cdot \vec v \times \vec B
$$

### $\vec v \perp \vec B$

$$
R = \frac{m\cdot v}{|q|\cdot\|\vec B\|}
$$

$$
w = \frac{v}{R} = \frac{|q|\cdot \|\vec B\|}{m}
$$

### $\vec v \not\perp \vec B$

$$
h = v_\parallel\cdot T = \frac{v_\parallel\cdot 2\pi \cdot m}{|q|\cdot \|\vec V\|}
$$

## Fuerza Magnética

$$
\vec F_m = I\int_{\vec r_1}^{\vec r_2} \vec{dl} \times \vec B
$$

### Campo Uniforme

$$
\vec F_m = I\cdot \big(\vec r_2 - \vec r_1\big) \times \vec B
$$

### Torque

Recordando la definición de torque. $T = \vec r \times \vec F$

$$
T = \vec \mu \times \vec B
$$

$$
T = I\vec A \times B
$$

Llamamos $\mu$ al momento dipolar magnético. $\vec \mu = I\vec A$

## Ley de Biot y Savalt

$$
\vec B = K_m \cdot \frac{q\cdot \vec v \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}
$$

$$
\vec B = \frac{\mu_0}{4\pi} \int\frac{I\cdot  d\vec l' \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}
$$

$$
\vec B = \frac{\mu_0}{4\pi} \iint\frac{\vec k\cdot  dS \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}
$$

$$
\vec B = \frac{\mu_0}{4\pi} \iiint\frac{\vec j\cdot  dV \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}
$$

## Ley de Ampere

$$
\text{Forma Integral}:\oint\limits_{\lambda} \vec B \cdot d\vec l = \mu_0 \cdot I_{S(\lambda)}
$$

$$
\text{Forma Diferencial}:\vec \nabla \times \vec B= \mu_0 \cdot \vec j
$$

$$
I_{S(\lambda)} =\sum I_{i\ S(\mathfrak{c)}}
$$

## Campos Conocidos

$$
\vec{B}\text{ Hilo}: \frac{\mu_0\cdot I}{4\pi r} \cdot

\Bigg[ \frac{z + \frac L2}{\sqrt{r^2 + (z + \frac L2)^2}} - \frac{z - \frac L2}{\sqrt{r^2 + (z - \frac L2)^2}}{}\Bigg]

\cdot \hat \theta

$$

$$
\vec{B}\text{ Espira Circular (eje): }\frac{\mu_0IR^2}{ 2\sqrt{z^2 + R^2}^3}\hat z
$$

$$
\vec B \text{ Plano Infinito}: \frac{\mu_0 K_0}{2}
$$

$$
\vec{B}\text{ Solenoide: }\mu_0\frac{ N.I}{L}
$$

$$
\vec{B}\text{ Hilo Infinito: }\frac{\mu_0 I}{2\pi r}
$$

$$
\vec{B}\text{ Cilindro Vacio Infinito: }\frac{\mu_0 I}{2\pi r}\hat{\varphi} \iff r > a
$$

$$
\vec{B}\text{ Dos Cilindros: } (a,b,c)\large\begin{cases}

\frac{\mu_0 I_1 r}{2\pi\cdot a^2}(\hat\varphi)&\iff r<a \\\\

\frac{\mu_0 I_1}{2\pi r}(\hat\varphi)&\iff a<r<b \\\\

\frac{\mu_0\big[I_1 + \frac{I_2(r^2 - b^2)}{c^2 - b^2}\big]}{2\pi r}(\hat\varphi)&\iff b<r<c \\\\

\frac{\mu_0 \big[I_1 + I_2\big]}{2\pi r}(\hat\varphi)&\iff a<r<b

\end{cases}
$$
