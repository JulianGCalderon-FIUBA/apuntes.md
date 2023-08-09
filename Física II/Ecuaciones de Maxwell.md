Maxwell cambio algunas formulas que vimos en la materia, para que sean mas precisas. Y abarquen el caso dinámico. Considero que las leyes de Gauss ya eran validas en el caso dinámico.

> “La visión unificadora de Maxwell es la mayor alteración en nuestra concepción de la estructura de la realidad desde Newton” ~ Einstein
> 

# Ley de Ampere-Maxwell

$$
\oint\limits_\lambda \vec H \cdot \vec dl = \iint\limits_S\vec j \cdot d\vec A + \color{blue}{\frac d{dt} \iint\limits_S \vec D \cdot d\vec A}
$$

$$
\vec\nabla \times \vec H = \vec j + \color{blue}{\frac{\partial\vec D}{\partial t}}
$$

Maxwell introdujo un termino adicional, que corresponde a las corrientes de desplazamiento. Esto se debe a que cuando trabajamos con corrientes que dependen del tiempo, la ley de ampere es invalida. El flujo de la corriente sobre una superficie cerrada no es nulo (como indica la ley original)

# Ley de Faraday-Maxwell

$$
\mathcal{E} =-\frac d{dt} \iint\limits_S \vec B \cdot d\vec A = \color{blue}{\oint\limits_\lambda \vec E \cdot d\vec l}
$$

$$
\color{blue}{\vec\nabla \times \vec E =  -\frac{\partial\vec B}{\partial t}}
$$

Maxwell reinterpreto la ley de Faraday. Indicando que todo campo variable en el tiempo genera, además de una campo magnético inducido , un campo eléctrico.

Esta nueva interpretación parece cerrar el ciclo del electromagnetismo. Los campos eléctricos ejercen fuerzas sobre las cargas estacionarias, quienes crean campos eléctricos. Por otro lado los campos magnéticos ejercen fuerzas sobre las corrientes, quienes crean campos magnéticos. Gracias a la ley de Ohm, Biot-Savart y Ampere, encontramos que los campos eléctricos generan corrientes y a su vez, campos magnéticos.

Por ultimo, y gracias a Maxwell, encontramos que los campos magnéticos variables crean campos eléctricos (aunque no haya corrientes).