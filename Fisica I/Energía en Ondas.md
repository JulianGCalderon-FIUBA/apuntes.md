## Potencia

La **potencia** $P$ de una onda se puede calcular como la derivada del trabajo respecto del tiempo, o la fuerza por la velocidad.

$$
P = \xi^2\cdot F\cdot k\cdot w\cdot\cos^2(kx \pm wt)
$$

Si calculo el promedio de la potencia por unidad de area, llegamos a que

$$
⟨P⟩ = \frac12\cdot\Big[\rho\cdot\text{Sección}\Big]\cdot v\cdot w^2\cdot A^2
$$

En el caso de las cuerdas, $\mu = \rho\cdot\text{Sección}$

$$
⟨P⟩ =\frac 12\cdot\mu\cdot v\cdot w^2\cdot A^2
$$

## Intensidad

La intensidad de una cuerda esta relacionada con la potencia que tiene la cuerda, por unidad de area.

$$
⟨I⟩ =
\frac{\text{⟨Potencia⟩}}{\text{Sección}}\implies[I] = \frac{\text{Watt}}{m^2}
$$

$$
⟨I⟩ = \frac 12\cdot\rho\cdot v\cdot w^2\cdot A^2
$$

Si la onda se propaga en tres dimensiones, entonces el area vale $4\pi R^2$

$$
I = \frac{⟨P⟩}{4\pi R^2}
$$

## Energía Cinética

En modelo de partículas, se da que

$$
E_c = \frac 12m\cdot v^2
$$

Si tomamos que la velocidad es la derivada temporal de la perturbación, entonces podemos calcular la densidad de energía cinética de una onda

$$
dE_c = \frac 12\rho\cdot v^2 = \frac 12\rho\cdot A^2\cdot w^2\cdot\cos^2(\ldots)
$$

Si calculamos su valor medio, se simplifica y llegamos a que

$$
⟨dE_c⟩ = \frac 14\rho\cdot A^2\cdot w^2
$$

## **Energía Potencial**

En modelo de partículas, se da que

$$
E_{Pel} = \frac 12K\cdot\Delta x^2
$$

Asociamos la constante elástica $K$ al modulo de *Young* $Y$, y la velocidad de la partícula a la derivada espacial de la perturbación. Así podemos calcular la densidad de energía potencial

$$
dE_{Pel} = \frac 12v_p^2\cdot\rho
=\frac 12v_p^2\cdot\rho\cdot A^2\cdot K^2\cdot\cos^2(\ldots) 
$$

Si calculamos su valor medio, se simplifica y llegamos a que

$$
⟨dE_{Pel}⟩ = \frac 14\rho\cdot A^2\cdot w^2
$$

## Energía Mecánica

Como el valor medio de la energía potencial y el de la energía cinética son iguales, entonces

$$
⟨dE⟩ = ⟨dE_{c_m}⟩ + ⟨dE_{Pel_m}⟩
$$

$$
⟨dE⟩ = \frac 12\cdot\rho\cdot w^2\cdot A^2
$$
