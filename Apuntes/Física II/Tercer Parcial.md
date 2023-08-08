# Constantes

$$
\begin{align*}
\text{Red Domiciliaria Argentina}:V_{ef} = 220,\ I_{ef} = 50hz
\end{align*}
$$

$$
\begin{align*}
\text{Henrio}:[H]
\end{align*}
$$

# Materiales Magnéticos

$$
\text{Campo de Inducción Magnética}\implies \oint\limits_\lambda \vec B d\vec l = \mu_0 I_\lambda
$$

$$
\text{Campo Magnetización}\implies \oint\limits_\lambda \vec Md\vec l = I_m
$$

$$
\text{Campo Magnético}\implies \oint\limits_\lambda \vec H d\vec l = I_R
$$

El campo magnetización solo existe dentro de los materiales magnéticos. Indica la cantidad de momentos angulares por unidad de volume que tiene el material.

### Relaciones entre Campos

Si definimos la permeabilidad relativa $\mu_r$ y la susceptibilidad magnética $X_M = \mu_r - 1$. Entonces:

$$
\vec M = X_M \cdot H
$$

$$
\vec B = \mu_0 \mu_r \cdot H
$$

# Inducción Electromagnética

$$
\mathcal{E} = -\frac{d\phi}{dt}
$$

### Coeficiente de Autoinducción

$$
L_1 = N_1 \cdot \frac{d\phi_{11}}{di_1} 
$$

$$
\mathcal E_{11} = -L_1 \cdot \frac{di_1}{dt}
$$

La unidad de la inductancia es de $H$

### Coeficiente de Inducción Mutuo

$$
M_{21} =N_2 \cdot \frac{d\varphi_{21}}{di_1} 
$$

$$
\mathcal E_{21} = -M_{21} \cdot \frac{di_1}{dt}
$$

$$
M_{21} = M_{12} = M
$$

### Factor de Acoplamiento

$$
M = k \sqrt{L_1 \cdot L_2}
$$

# Inductores

$$
L = \frac{\mu_0 \mu_r\cdot N_1^2 \cdot S_1}{l_1}
$$

### Bobinado Interno

$$
M_{21} = \frac{\mu_0 \mu_r\cdot  N_1 N_2 \cdot S_2}{l_1} = M_{12}
$$

### Acoplamiento (Material Magnético)

$$
\mathcal E_1 = \mathcal E_{11} \color{red}{\pm}\mathcal E_{12}  = -L_1 \cdot \frac{di_1}{dt} \color{red}{\mp} M_{12} \cdot \frac{di_2}{dt}
$$

### Conexión en Serie

$$
L_{eq} = L_1 + L_2 \color{red}{\pm} 2M
$$

### Energía Almacenada

$$
U = \frac 12 \cdot L \cdot I^2
$$

$$
U = U_1 + U_2 = \frac 12 L_1 I_1^2 + \frac 12 L_2 I_2^2\ \color{red}{\pm}\  MI_1 I_2
$$

### Transformador

$$
\frac{\mathcal E_1}{\mathcal E_2} = \frac{N_1}{N_2\ k}
$$

# Corriente Alterna

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

### Pseudo - Ley de Ohm

$$
\tilde V(t) = \tilde I(t) \cdot \mathbb{Z}
$$

$$
V_0\ e^{j\phi_v} = I_0\ e^{j\phi_i} \cdot \mathbb{Z}
$$

$$
|z| = \sqrt{R^2 + (X_L - X_C)^2}
$$

$$
\tan(\phi_z)  = \frac{X_L - X_C}{R}
$$

$$
\mathbb{Z} = R + j(X_L - X_C)
$$

$$
\text{Amplitud}: V_0 = I_0 \cdot |z| \\
\text{Fase}: \phi_{iv} = -\phi_z
$$

### Valores Eficaces

$$
V_{ef} = \frac{V_0}{\sqrt 2}
$$

$$
I_{ef} = \frac{I_0}{\sqrt 2}
$$

# Potencia Activa y Reactiva

$$
P(t) = v_0\ i_0 \cdot \cos(wt) \cdot \cos(wt +\phi_{iv})
$$

### Activa (Potencia Disipada)

$$
P = v_{ef}\ i_{ef} \cdot \cos(\phi_z)=i_{ef}^2 \cdot R
$$

### Reactiva (Potencia Almacenada)

$$
Q = v_{ef}\ i_{ef} \cdot  \sin(\phi_z) = i_{ef}^2 \cdot (X_L - X_C)
$$

### Triangulo De Potencias

![[Apuntes/Física II/Attachments/Tercer Parcial 1.svg|Tercer%20Parcial%2016944545111d4a8ab9086d0e72a0c894/Diagram.drawio.svg]]

$$
S = v_{ef} \cdot i_{ef}
$$

$$
\cos(\phi_z) = \frac{P}{S}
$$

### Frecuencia Angular de Resonancia

$$
w_r = \frac{1}{\sqrt{LC}}
$$

$$
P = \frac{v_{ef}^2}{R}
$$

### Frecuencia Angular de Corte

$$
w_c = \frac{\pm CR + \sqrt{C^2R^2 + 4LC}}{2CL}
$$

$$
\Delta w = w_2 - w_1 = R/L
$$

### Factor de Calidad

$$
q = \frac{w_r}{\Delta w} = w_r \cdot \frac{L}{R}
$$