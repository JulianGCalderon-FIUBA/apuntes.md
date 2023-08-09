Por la experiencia, se encontró que los campos magnéticos son generados por cargas en movimiento (corrientes). Además, se encontraron las siguientes relaciones.

- $\vec B \perp I\cdot d\vec l$
- $\vec B \perp (\vec r - \vec r')$
- $\displaystyle\|\vec B\| \propto \frac{1}{\|\vec r - \vec r'\|^2}$

A partir de estas relaciones, se formalizo la ley del campo magnético para una carga puntual en movimiento.

$$
\vec B = K_m \cdot \frac{q\cdot \vec v \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}
$$

$$
\begin{gathered}
\text{Constante Magnetica}: K_m = \frac{\mu_0}{4\pi} \\
\text{Permmeabilidad Magnetica del Vacio}: \mu_0 = 4\pi \cdot 10^{-7} N/A^2
\end{gathered}
$$

Si extendemos esta formula para una corriente en lugar de una carga puntual, llegamos a la **Ley de Biot y Savalt** para una corriente estacionaria.

$$
\vec B = \frac{\mu_0}{4\pi} \int\frac{I\cdot  d\vec l' \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}
$$

## Campo Magnético Generado por un Hilo

Si planteamos una integral recta, y resolvemos la ley del campo magnético, llegamos a la siguiente expresión

$$
\vec B = \frac{\mu_0\cdot I}{4\pi r} \cdot

\Bigg[ \frac{z + \frac L2}{\sqrt{r^2 + (z + \frac L2)^2}} - \frac{z - \frac L2}{\sqrt{r^2 + (z - \frac L2)^2}}{}\Bigg]

\cdot \hat \theta

$$

Si extendemos el hilo hacia el infinito, entonces llegamos a un campo mas simple

$$
\vec B = \frac{\mu_0\cdot I}{2\pi r} \cdot \hat \theta

$$

## Distribución de Corriente

Así como teníamos densidades volumétricas de corriente, también tenemos densidades superficiales de corriente.

$$
I = \int \vec k \cdot d\vec l = \iint \vec j \cdot d\vec S
$$

De esta forma, podemos encontrar el campo magnético a partir de una densidad superficial de corriente, y una volumetrica.

$$
\vec B = \frac{\mu_0}{4\pi} \iint\frac{\vec k\cdot  dS \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}
$$

$$
\vec B = \frac{\mu_0}{4\pi} \iiint\frac{\vec j\cdot  dV \times (\vec r - \vec r')}{\|\vec r - \vec r'\|^3}
$$

> [!note]
> En estos casos, el carácter vectorial lo tiene la distribución de corriente, en lugar del diferencial.
