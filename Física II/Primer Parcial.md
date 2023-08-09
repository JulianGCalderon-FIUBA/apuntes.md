# Constantes

$$
\begin{align*} \text{Carga Elemental}:e&=-1,6\times10^{-19}C\\
\text{Constante de Proporcionalidad}:k&= 9\times10^9 N m^2/C^2\\
\text{Permitividad del Vacio}:\varepsilon_0 &= 8,842\times10^{-12} N m^2/C^2
\end{align*}
$$

$$

\begin{align*}
\text{Coulomb}:[C] \\
\text{Julio}: [J] \\
\text{Newton}: [N] \\
\text{Voltio}: [V] \\
\text{Faraday}: [F] 
\end{align*}
$$

# Ley de Coulomb

$$
\vec F_{ij} = k\cdot q_iq_j\cdot\frac{\vec r_i - \vec r_j}{\|\vec r_i - \vec r_j\|^{3}}
$$

Siendo $F_{ij}$ la fuerza que siente la carga $i$ debido a la carga $j$

# Campo Eléctrico

$$
\vec E(\vec r) \cdot q_0 = F_0
$$

La unidad del campo eléctrico es de $N/C$

### Carga Puntual

$$
\vec E(\vec r) = k\cdot q\cdot\frac{(\vec r-\vec r')}{\|\vec r - \vec r'\|^3}
$$

### Multiples Cargas

$$
\vec E(\vec r) = k\sum_{i}^nq_i\cdot\frac{(\vec r - \vec r_i)}{\|\vec r - \vec r_i\|^3}
$$

### Distribución Continua

$$
\vec E(\vec r) = k\int \frac{r-r'}{\|\vec r - \vec r'\|^3}\cdot dq
$$

# Ley de Gauss

$$
\text{Forma Integral}: {\subset\!\supset} \llap{\iint} \vec Ed\vec s = \frac{Q_\text{enc}}{\varepsilon_0}
$$

$$
\text{Forma Diferencial}:\nabla\cdot\vec E = \frac{\rho}{\varepsilon_0}
$$

# Trabajo

$$
W_{F_\text{ext}} = -q_0\int_A^B\vec E\cdot d\vec l
$$

$$
\text{Forma Integral}:\Delta V^{AB} = -\int_A^B \vec E \cdot d \vec l
$$

$$
\text{Forma Diferencial}:E = -\nabla V
$$

El trabajo se mide en $J$. El potencial se mide en $V$

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

# Conductores

### Campo en el Interior

$$
\vec E = 0
$$

### Campo en las Cercanías

$$
\vec E_p = \frac{\sigma_p}{\varepsilon_0}\hat n_c
$$

# Capacitores

### Capacidad

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

La capacidad se mide en $F$

### Conexión/

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

La energía se mide en $J$, es igual al trabajo necesario para cargar el capacitor

# Aislantes

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

La unidad de los campos desplazamiento y polarización es $Q/m^2$

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

### Cargas de Polarización

$$
\rho_p = \frac{-X_e}{\varepsilon_r}\cdot\rho_{libres}
$$

$$
\sigma_p = \vec P |_S \cdot \hat n_{s}
$$

# Campos Comunes

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

# Integrales Útiles

$$
\bullet\textbf{ 196}: \int \frac{dx}{[x^2 + a^2]^{3/2}} = \frac{x}{a^2\sqrt{x^2 + a^2}}
$$

$$
\bullet\textbf{ 197}: \int \frac{x\ dx}{[x^2 + a^2]^{3/2}} = \frac{-1}{\sqrt{x^2 + a^2}}
$$