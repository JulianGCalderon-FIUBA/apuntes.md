# Energía Cinética

Para un sistema de partículas, se cumple que:

$$
E_c = \overbrace{\frac M2v_{cm}^2}^{E_c^{\text{cm}}} + \overbrace{\sum \frac {m_i}2v^2_{i/cm}}^{E_c^{\text{Sist/cm}}}
$$

$$
\text{Rígidez: }\quad\begin{align*}\vec v_{i/cm} &= \vec\Omega \times \vec r_{i/cm}\\\vec v_{cm} &= \vec\Omega \times \vec r_{cm/cir}\end{align*}
$$

Si aplicamos esto, llegamos a que:

$$
E_c = \frac 12Mv^2_{cm} + \frac 12I_{cm}\Omega^2
$$

$$
\boxed{E_c = \frac 12I_{cir}\Omega^2}
$$

# Energía Potencial

$$
E_p^{Sist} = \sum M_igh_i
$$

$$
\boxed{E_p = Mgh_{cm}}
$$

# Trabajo

En el calculo de trabajo, el procedimiento es el mismo que en un cuerpo puntual, pero se debe considerar el desplazamiento del punto del cuerpo rígido donde se aplica la fuerza

### Calculo de $\Delta x$ en $A$

![[Apuntes/Fisica I/Attachments/Energia CR 1.png|Energia%20CR%200f59974032d54fb393f89c6d7179bf35/Untitled.png]]

$$
W^F = \int F\cdot dx_A
$$

$$
v_{cm} = \Omega\times r_{cm/cir} \implies v_{cm} = \Omega.R \implies dx_{cm} = d\theta.R
$$

$$
v_a = \Omega\times r_{a/cir} \implies v_a = \Omega.(R+r) \implies dx_a = d\theta.(R+r)
$$

$$
dx_a = dx_{cm}\cdot\frac{R+r}{R}
$$

$$
\boxed{W^F = \int_0^dF\cdot\frac{R+r}Rdx_{cm} = F\cdot\frac{R+r}R\cdot d }
$$