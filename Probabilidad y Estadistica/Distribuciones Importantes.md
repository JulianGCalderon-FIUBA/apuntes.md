## Chi-Cuadrado $\chi^2$

la variable aleatiroa $X$ tiene distribucion $\chi^2$ de $\nu$ grados de libertar si su densidad esta dada por

$$
f_X(x) = \frac{1}{\Gamma(\nu / 2)} \Big(\frac{1}{2}\Big)^{\nu/2} x^{\nu/2 - 1} e^{-x/2} \cdot \mathbb I\{x > 0\}
$$

Se puede observar que conicide con la distribucion $\Gamma(\nu/2, 1/2)$. De ahi, decducimos facilmente su esperanza y su varianza

Sea $Z$ un normal estandar, entonces la variable aleatoria $X = Z^2 \sim \chi^2_1$

La suma de variables independientes de distribucion $\chi^2$ de $\nu_i$ grados de libertad nos da una nueva variable aleatoria $\chi^2$ de $\sum \nu_i$ grados de libertad. (al igual que con una Gamma)

**Corolario:** Se llama distribución $\chi^2$ con $\nu$ grados de libertad a la distribucion $U = \sum_{i=1}^\nu Z_i^2$, donde $Z_i, \cdots, Z_n \sim \mathscr N(0,1)$

## T de Student

Sean $Z \sim \mathscr N(0,1)$ y $U \sim \chi_n^2$ dos variables aleatorias independientes, entonces definimos

$$
\frac{Z}{\sqrt{U /N}} = T \sim t_n
$$

A medida que aumentan los grados de liberta, la funcion tiende a una normal estandar.

## F de Fisher-Snedecor

Sean $U,V$ dons variables aleatorias independientes con distribución $\chi^2$ de $\nu_1, \nu_2$ grados de livertad respectivamente, entonces

$$
F = \frac{U/\nu_1}{V/\nu_2} \sim \mathscr F_{\nu_1, \nu_2}
$$

## Teorema

Sean $X_1, \cdots, X_n \stackrel{iid}{\sim} \mathscr N(\mu, \sigma^2)$

$$
Z = \sqrt{n} \cdot \frac{\overline X - \mu}{\sigma} \sim \mathscr N(0,1) \tag{1}
$$

$$
W = \sum_{I=1}^n \frac{(X_i - \overline X)^2}{\sigma^2} \tag{2} \sim \chi^2_{n-1}
$$

$$
Z, W \text{ son independientes} \tag 3
$$

$$
\text{Si: } S^2 = \sum_{i=1}^{n}\frac{(X_i - \overline X)^2}{n-1}, \\ \text{Entonces: } T = \sqrt{n} \cdot \frac{\overline X - \mu}{S} \sim t_{n-1} \tag 4
$$
