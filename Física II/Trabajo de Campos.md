---
title: Trabajo de Campos
---

$$
W_{\vec F}^{AB} = \int_A^B \vec F\cdot d\vec l = q_0\int_A^B \vec E\cdot d\vec l
$$

Si usando una fuerza externa $\vec F_e$ desplazo la partícula de $A$ a $B$ como un movimiento cuasi estacionario, entonces la velocidad es constante a lo largo del trayecto y la sumatoria de fuerzas es, por lo tanto, nula.

Entonces podemos definir le trabajo de este fuerza externa como inverso al trabajo del campo eléctrico.

$$
\boxed{W_{F_\text{ext}} = -q_0\int_A^B\vec E\cdot d\vec l}
$$

Además, como el rotor del campo eléctrico es nulo, entonces el campo es conservativo. Por lo que no depende de la trayectoria, y el trabajo vale es nulo para toda curva cerrada.

$$
\text{Forma Integral}:\Delta V^{AB} = V_B - V_A = -\int_A^B \vec E \cdot d \vec l
$$

$$
\text{Forma Diferencial}\implies E = -\nabla V
$$

**Conjunto Equipotencial**: Conjunto de puntos que tienen exactamente el mismo potencial. Desplazarte por un conjunto equipotencial no cuesta trabajo.

## Carga Puntual

En el caso de una carga puntual, solo calculamos la integral de ese campo de $A$ a $B$

$$
\vec E(\vec r) = \frac{q}{4\pi\epsilon_0}\cdot\frac{\hat r}{r^2}
$$

$$
\Delta V^{AB} = -\int_A^B \vec E(\vec r)\cdot d\vec l
$$

$$
\Delta V^{AB} = \frac{q}{4\pi\epsilon_0}\bigg(\frac{1}{r_b} - \frac{1}{r_a}\bigg)
$$

$$
W_{F_\text{ext}} = q_0 \cdot \Delta V^{AB}
$$

> [!note]
> Como el campo solo tiene componente radial, solo nos importa esa componente entre $A$ y $B$, las otras componentes se cancelan

## N.º Cargas

Al ser distribuible la integral, podemos simplemente sumar las diferencias del potencial.

$$
\Delta V^{AB} = \frac{1}{4\pi\epsilon_0}\cdot\sum_{i }^n q_i\cdot\bigg[\frac{1}{|\vec r_B - \vec r_i|} - \frac{1}{|\vec r_A - \vec r_i|}\bigg]
$$

$$
W_{F_\text{ext}} = q_0 \cdot \Delta V^{AB}
$$

## Distribución Continua

Podemos simplemente remplazar la suma por una integral, con su diferencial de carga.

$$
\Delta V^{AB} = \frac{1}{4\pi\epsilon_0}\cdot\int dq'\cdot\bigg[\frac{1}{|\vec r_B - \vec r'|} - \frac{1}{|\vec r_A - \vec r'|}\bigg]
$$

Nótese que la distribución debe ser acotada, porque la integral es indefinida cerca del infinito.

Para distribuciones no acotadas, podemos remitirnos a la definición integral

$$
W_{F_{ext}} = -q_0\int_A^B \vec E\cdot d\vec l
$$
