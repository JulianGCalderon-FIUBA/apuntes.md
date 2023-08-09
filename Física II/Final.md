## Constantes

$$
\begin{align*} \text{Carga Elemental}:e&=-1,6\times10^{-19}C\\
\text{Constante de Proporcionalidad}:k&= 9\times10^9 N m^2/C^2\\
\text{Permitividad del Vacio}:\varepsilon_0 &= 8,842\times10^{-12} N m^2/C^2
\end{align*}
$$

$$
\begin{align*}
&\text{Constante Magnetica}: K_m = \frac{\mu_0}{4\pi} = 10^{-7} N  / A^2
\\
&\text{Permmeabilidad Magnetica del Vacio}: \mu_0 = 4\pi \cdot 10^{-7} N/A^2
\end{align*}

$$

$$
\begin{align*}
\text{Red Domiciliaria Argentina}:V_{ef} = 220,\ I_{ef} = 50hz = 100\pi/s
\end{align*}
$$

$$

\begin{align*}
\text{Coulomb}:[C] \\
\text{Joule}: [J] \\
\text{Newton}: [N] \\
\text{Volt}: [V] \\
\text{Faraday}: [F]
\end{align*}
$$

$$
\begin{align*}
\text{Ampere}: [I]\\
\text{Ohm}: [\Omega]\\
\text{Watt}: [W]\\
\text{Tesla}: [T]
\end{align*}
$$

$$
\begin{align*}
\text{Henry}:[H]
\end{align*}
$$

## Integrales Útiles

$$
\bullet\textbf{ 196}: \int \frac{dx}{[x^2 + a^2]^{3/2}} = \frac{x}{a^2\sqrt{x^2 + a^2}}
$$

$$
\bullet\textbf{ 197}: \int \frac{x\ dx}{[x^2 + a^2]^{3/2}} = \frac{-1}{\sqrt{x^2 + a^2}}
$$

## Ley de Coulomb

$$
\vec F_{ij} = k\cdot q_iq_j\cdot\frac{\vec r_i - \vec r_j}{\|\vec r_i - \vec r_j\|^{3}}
$$

Siendo $F_{ij}$ la fuerza que siente la carga $i$ debido a la carga $j$

## Campo Eléctrico

$$
\vec E(\vec r) \cdot q_0 = F_0
$$

La unidad del campo eléctrico es de $N/C$.

Representa numericamente la fuerza que experimentaria una particula de carga $1C$ en ese punto del espacio.

### Carga Puntual

$$
\vec E(\vec r) = k\cdot q\cdot\frac{(\vec r-\vec r')}{\|\vec r - \vec r'\|^3}
$$

### Multiples Cargas

### Distribución Continua

$$
\vec E(\vec r) = k\sum_{i}^nq_i\cdot\frac{(\vec r - \vec r_i)}{\|\vec r - \vec r_i\|^3}
$$

$$
\vec E(\vec r) = k\int \frac{r-r'}{\|\vec r - \vec r'\|^3}\cdot dq
$$

## Ley de Gauss

$$
\text{Integral}: {\subset\!\supset} \llap{\iint} \vec Ed\vec s = \frac{Q_\text{enc}}{\varepsilon_0}
$$

$$
\text{Diferencial}:\nabla\cdot\vec E = \frac{\rho}{\varepsilon_0}
$$

Para utilizar la ley de Gauss, debo utilizar una superficie que sea paralela o perpendicular al campo en cada porción de la misma.

## Trabajo

$$
W_{F_\text{ext}} = -q_0\int_A^B\vec E\cdot d\vec l
$$

$$
\text{Integral}:\Delta V^{AB} = -\int_A^B \vec E \cdot d \vec l
$$

$$
\text{Diferencial}:E = -\nabla V
$$

El trabajo se mide en $J$. El potencial se mide en $V$. Se define como el trabajo que me cuesta llevar una particula de $A, B$ en estado cuasiestacinario. Es opuesto al trabajo del campo electrico.

### Carga Puntual

$$
\Delta V^{AB} = \frac{q}{4\pi\epsilon_0}\bigg(\frac{1}{r_b} - \frac{1}{r_a}\bigg)
$$

### Multiples Cargas

$$
\Delta V^{AB} = \frac{1}{4\pi\epsilon_0}\cdot\sum_{i }^n q_i\cdot\bigg[\frac{1}{|\vec r_B - \vec r_i|} - \frac{1}{|\vec r_A - \vec r_i|}\bigg]
$$

### Distribución Finita Continua

$$
\Delta V^{AB} = \frac{1}{4\pi\epsilon_0}\cdot\int \bigg[\frac{1}{|\vec r_B - \vec r'|} - \frac{1}{|\vec r_A - \vec r'|}\bigg]dq
$$

Para obtener una funcion potencial, colocamos la referencia $A$ en el infinito. En el caso de distribuciones infinitas, lo colocamos en un punto arbitrario

## Conductores

### Campo en las Cercanías

$$
\vec E_p = \frac{\sigma_p}{\varepsilon_0}\hat n_c
$$

El campo en las cercanías se asemeja al de un plano infinito y es por lo tanto, normal a su superficie.

### Capacitor

$$
Q = C \cdot \Delta V
$$

$$
\text{Plano}: C = \varepsilon_0\varepsilon_r \cdot \frac{A}{d}
$$

$$
\text{Cilindrico}:C = \varepsilon_0\varepsilon_r \cdot\frac{2\pi L }{\ln(b/a)}
$$

$$
\text{Esferico}: C = 4\pi\varepsilon_0\varepsilon_r\cdot \frac{ab}{b-a}
$$

La capacidad se mide en $F$. Se define como la carga que puede almacenar un capacitor por unidad de voltaje. Para calcular la capacidad, determinamos la forma del campo electrico y resolvemos la ecuación.

### Conexión de Capacitores

$$
\text{Serie}:\frac 1{C_{eq}} = \frac 1{C_1} + \frac 1{C_2}
$$

$$
\text{Paralelo}: C_{eq} = C_1 + C_2
$$

### Energía

$$
U = \frac 12\cdot \frac{Q^2}{C} =\frac 12\cdot C\Delta V^2 = \frac 12 \cdot Q\Delta V
$$

La energía se mide en $J$, es igual al trabajo necesario para cargar el capacitor.

## Dieléctricos

$$
\begin{align*}

&\overbrace
{{\subset\!\supset} \llap{\iint}_{S} \vec D \cdot   d \vec s = Q_{\text{enc}}^{\text{libres}}
}^{\text{Ley de Gauss Generalizada}}

\implies \vec \nabla \vec D = \delta^{\text{libres}}

\\

&{\subset\!\supset} \llap{\iint}_{S} \vec P \cdot   d \vec s = -Q_{\text{enc}}^{\text{pol}} \implies \vec\nabla \vec P = -\delta^{\text{pol}}

\end{align*}
$$

La unidad de los campos desplazamiento y polarización es $Q/m^2$. El campo desplazamiento esta asociada con las cargas libres del circuito, mientras que el campo polarizacion esta asociado con las cargas polarizadas que se encuentran dentro del dielectrico.

### Relaciones Entre Campos

$$
\vec D = \varepsilon_0 \vec E + \vec P
$$

$$
\vec D = \varepsilon \cdot \vec E
$$

$$
P = \varepsilon_0 \cdot X_E \cdot \vec E
$$

$$
\varepsilon = \varepsilon_0 \cdot \varepsilon_r
$$

$$
X_E =\varepsilon_r - 1
$$

El campo polarización apantalla el campo eléctrico, por lo que lo reduce (disminuyendo la diferencia de potencial entre las placas y aumentando la capacidad)

## Campos Eléctricos Comunes

$$
\text{Hilo Infinito}: E(r) = \frac{\lambda}{2\pi\varepsilon_0} \frac{\hat r}{r}
$$

$$
\text{Plano Infinito}: E(r) = \frac{\sigma}{2\varepsilon_0} \hat z
$$

$$
\text{Esfera Volumetrica}: \begin{dcases}
E(r) = \frac{\rho R^3}{3\varepsilon_0} \frac{\hat r}{r^2} &\impliedby r > R

\\\\

E(r) = \frac{\rho}{3\varepsilon_0} \cdot r\hat r &\impliedby r < R
\end{dcases}
$$

$$
\text{Esfera Superficial}: \begin{dcases}
E(r) = \frac{\sigma R^2}{\varepsilon_0} \frac{\hat r}{r^2} &\impliedby r > R

\\\\

0 &\impliedby r < R
\end{dcases}
$$

$$
\text{Cilindro Volumetrico}: \begin{dcases}
E(r) = \frac{\rho R^2}{2\varepsilon_0} \frac{\hat r}{r} &\impliedby r > R

\\\\

E(r) = \frac{\rho}{2\varepsilon_0} \cdot r\hat r &\impliedby r < R
\end{dcases}
$$

$$
\text{Cilindro Superficial}: \begin{dcases}
E(r) = \frac{\sigma R}{\varepsilon_0} \frac{\hat r}{r} &\impliedby r > R

\\\\

0 &\impliedby r < R
\end{dcases}
$$

## Corriente Continua

$$
\vec v_a = \mu\cdot E
$$

$$
\mu = \frac{q\ \tau}{m}
$$

$$
n = \frac{Nº}{vol}
$$

Siendo $\mu$ la movilidad de las partículas y $n$ la densidad de portadores de carga de un conductor

$$
I = \frac{dq}{dt}
$$

$$
I = q\cdot n\cdot A \cdot \vec v_a
$$

La unidad de la corriente es $A$.

### Densidades

$$
I = \iint\limits_A \vec j(\vec r) \ dA
$$

$$
{\subset\!\supset} \llap{\iint}_S \vec J \cdot ds = 0
$$

$$
I = \int \vec k \cdot d\vec l
$$

Se define $j$ como la densidad volumétrica de corriente, y $k$ como la densidad superficial.

$$
\vec J = \sigma \cdot \vec E
$$

$$
\sigma = \frac{q^2n\tau}{m}
$$

Siendo $\sigma$ la conductividad eléctrica

## Ley de Ohm

$$
\Delta V = I\ R
$$

$$
R = \rho\ \frac{l}{A}
$$

Se define $\rho = 1/\sigma$ como la resistividad eléctrica del material $[\Omega m]$

La unidad de la resistencia es de $\Omega$, y su formula es unicamente para conductores cilindricos.

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

La unidad del campo magnético es de $T$. Este actúa sobre las cargas en movimiento

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

El radio de curvatura y la velocidad angular se calculan usando la velocidad perpendicular

### Fuerza Magnética sobre Corriente

$$
d\vec F_m = I \vec dl \times \vec B
$$

$$
\vec F_m = I\int_{\vec r_1}^{\vec r_2} \vec{dl} \times \vec B
$$

Si el campo magnético es uniforme, entonces la integral no depende de la curva.

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
\underbrace{\vec B = \frac{\mu_0}{4\pi} \int\frac{I\cdot  d\vec l' \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}}_\text{Corriente}
$$

$$
\underbrace{\vec B = \frac{\mu_0}{4\pi} \iiint\frac{\vec j\cdot  dV \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}}_\text{Densidad Volumetrica de Corriente}
$$

$$
\underbrace{\vec B = \frac{\mu_0}{4\pi} \iint\frac{\vec k\cdot  dS \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}}_\text{Densidad Superficial de Corriente}
$$

## Ley de Ampere

$$
\text{Integral}:\oint\limits_{\lambda} \vec B \cdot d\vec l = \mu_0 \cdot I_{S(\lambda)}
$$

$$
\text{Diferencial}:\vec \nabla \times \vec B= \mu_0 \cdot \vec j
$$

La curva de la ley de ampere debe ser perpendicular o paralelo al campo en cada porción de la misma.

## Campos Magnéticos Conocidos

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
\vec{B}\text{ Cilindro Vacio Infinito: }\frac{\mu_0 I}{2\pi r}\hat{\varphi} \\r > a
$$

$$
\vec{B}\text{ Dos Cilindros: } (a,b,c)\large\begin{cases}

\frac{\mu_0 I_1 r}{2\pi\cdot a^2}(\hat\varphi)&\iff r<a \\\\

\frac{\mu_0 I_1}{2\pi r}(\hat\varphi)&\iff a<r<b \\\\

\frac{\mu_0\big[I_1 + \frac{I_2(r^2 - b^2)}{c^2 - b^2}\big]}{2\pi r}(\hat\varphi)&\iff b<r<c \\\\

\frac{\mu_0 \big[I_1 + I_2\big]}{2\pi r}(\hat\varphi)&\iff a<r<b

\end{cases}
$$

## Materiales Magnéticos

$$
\text{Campo de Inducción Magnética}\implies \oint\limits_\lambda \vec B d\vec l = \mu_0 I_\lambda
$$

$$
\text{Campo Magnetización}\\\oint\limits_\lambda \vec Md\vec l = I_m
$$

$$
\text{Campo Magnético}\\\oint\limits_\lambda \vec H d\vec l = I_R
$$

El campo magnetización solo existe dentro de los materiales magnéticos. Indica la cantidad de momentos angulares por unidad de volume que tiene el material. El campo magnético existe siempre y esta relacionado con las corrientes reales

### Relaciones Entre Campos

Si definimos la permeabilidad relativa $\mu_r$ y la susceptibilidad magnética $X_M = \mu_r - 1$. Entonces:

$$
\vec M = X_M \cdot H
$$

$$
\vec B = \mu_0 \mu_r \cdot H
$$

## Inducción Electromagnética

$$
\mathcal{E} = -\frac{d\phi}{dt}
$$

La *fem* inducida sobre un circuito esta relacionada con el cambio de flujo de un campo eléctrico externo sobre el mismo.

### Coeficiente de Autoinducción

$$
L_1 = N_1 \cdot \frac{d\phi_{11}}{di_1}
$$

$$
\mathcal E_{11} = -L_1 \cdot \frac{di_1}{dt}
$$

La unidad de la inductancia es de $H$.

### Coeficiente de Inducción Mutuo

$$
M =N_2 \cdot \frac{d\varphi_{21}}{di_1}
$$

$$
\mathcal E_{21} = -M \cdot \frac{di_1}{dt}
$$

### Factor de Acoplamiento

$$
M = k \sqrt{L_1 \cdot L_2}
$$

El factor de acoplamiento define que porcentaje del flujo de un inductor es concatenado por el segundo.

## Inductores

$$
L = \frac{\mu_0 \mu_r\cdot N_1^2 \cdot S_1}{l_1}
$$

$$
M = \frac{\mu_0 \mu_r\cdot  N_1 N_2 \cdot S}{l_1}
$$

Inductancia mutua para inductores en un toroide.

### Acoplamiento (Material Magnético)

$$
\mathcal E_1 = \mathcal E_{11} \color{Red}{\pm}\mathcal E_{12}  = -L_1 \cdot \frac{di_1}{dt} \color{Red}{\mp} M_{12} \cdot \frac{di_2}{dt}
$$

Si los bornes son homólogos (los flujos son aditivos), entonces las *fem* inducidas también lo son.

### Conexión en Serie

$$
L_{eq} = L_1 + L_2 \color{Red}{\pm} 2M
$$

### Energía Almacenada

$$
U = \frac 12 \cdot L \cdot I^2
$$

$$
U = U_1 + U_2 = \frac 12 L_1 I_1^2 + \frac 12 L_2 I_2^2\ \color{Red}{\pm}\  MI_1 I_2
$$

Se define la energía almacenada en un inductor como el trabajo que me cuesta energizarlo.

### Transformador

$$
\frac{\mathcal E_1}{\mathcal E_2} = \frac{N_1}{N_2\ k}
$$

Un transformador ideal es un toroide que permite cambiar el voltaje entre dos corrientes, a partir de inductores

## Corriente Alterna

$$
v(t) = v_0 \cdot \cos(wt + \phi_v)
$$

### Circuitos Puros

$$
v_r(t) = i(t)\ R
$$

$$
v_c(t) = \frac 1C \int i(t) dt
$$

$$
v_i(t) = L\cdot \frac{di(t)}{dt}
$$

$$
X_L = wL
$$

$$
i(t) = i_0 \cdot \cos(wt + \phi_v + \phi_{iv})
$$

$$
X_C = \frac{1}{wC}
$$

$$
\def\arraystretch{1.4}\begin{array}{|c|c|c|c|}\hline

& \textbf{Amplitud } (i_0)  &
\textbf{Fase } (\phi_i) & \textbf{Desfasaje } (\phi_{iv})

\\\hline

\textbf{R} &
\frac{v_0}{R} &
\phi_v &
0

\\\hline

\textbf{C} &
\frac{v_0}{1/wc} &
\phi_v + \frac{\pi}{2} &
\frac{\pi}{2}

\\\hline

\textbf{L} &
\frac{v_0}{wL} &
\phi_v - \frac{\pi}{2} &
-\frac{\pi}{2}

\\\hline\end{array}
$$

Se define $X_L, X_C$ como las impedancia inductiva y capacitiva, respectivamente.

### Valores Complejos

$$
\tilde V(t) = V_0 \cdot e^{j\cdot(wt + \phi_v)}
$$

$$
\mathbb{R} e(\tilde V(t)) = v(t)
$$

$$
\tilde I(t) = I_0 \cdot e^{j\cdot(wt + \phi_v + \phi_{iv})}
$$

$$
\mathbb{R} e(\tilde I(t)) = i(t)
$$

Se definen los valores complejos para operar de mejor forma con la ecuacion integrodiferencial del voltaje de un circuito RCL.

### Pseudo - Ley de Ohm

$$
\tilde V(t) = \tilde I(t) \cdot \mathbb{Z}
$$

$$
\Bbb V = \Bbb I \cdot \mathbb{Z}
$$

$$
\Bbb V = \Bbb V_R + \Bbb V_L + \Bbb V_C
$$

### Impedancia del Circuito

$$
\mathbb{Z} = R + j(X_L - X_C)
$$

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

Se define $\phi_{iv}$ como el desfasaje entre la corriente y el voltaje. Si es positivo, la corriente se adelanta respecto a la potencia.

Si $X_L > X_C$, entonces el circuito es es inductivo (la corriente se atrasa)

### Valores Eficaces

$$
V_{ef} = \frac{V_0}{\sqrt 2}
$$

$$
I_{ef} = \frac{I_0}{\sqrt 2}
$$

## Potencia

$$
p(t) = v_0\ i_0 \cdot \cos(wt) \cdot \cos(wt +\phi_{iv})
$$

### Activa

$$
P = v_{ef}\ i_{ef} \cdot \cos(\phi_z)=i_{ef}^2 \cdot R
$$

Es la potencia media, también asociada con la potencia disipada por las resistencias

### Reactiva

$$
Q = v_{ef}\ i_{ef} \cdot  \sin(\phi_z) = i_{ef}^2 \cdot (X_L - X_C)
$$

Asociada a la potencia almacenada en los capacitores e inductores.

### Triangulo de Potencias

![[Final 1.png]]

$$
S = v_{ef} \cdot i_{ef}
$$

$$
\cos(\phi_z) = \frac{P}{S}
$$

La potencia aparente $S$ indica la potencia que siente la fuente que deberá entregarle a la corriente.

### Frecuencia angular de Resonancia

$$
w_r = \frac{1}{\sqrt{LC}}
$$

$$
P = \frac{v_{ef}^2}{R}
$$

La frecuencia de resonancia es la que causa que la potencia sea la maxima (circuito resistivo)

### Frecuencia angular de Corte

$$
w_c = \frac{\pm CR + \sqrt{C^2R^2 + 4LC}}{2CL}
$$

$$
\Delta w = w_2 - w_1 = R/L
$$

La frecuencia angular de corte causa que la potencia sea la mitad de la maxima

### Factor de Calidad

$$
q = \frac{w_r}{\Delta w} = w_r \cdot \frac{L}{R}
$$

El factor de calidad determina que tan fácil sera sintonizar con la frecuencia angular de resonancia del circuito. Determina el grosor de la campana de la potencia en función de la pulsación.
