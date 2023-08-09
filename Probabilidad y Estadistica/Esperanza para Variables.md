## Esperanza de una Variable Aleatoria

Es el promedio ponderado de los valores que puede tomar una variable aleatoria ("centro de masa"), no necesariamente es un valor del rango. Tambien se lo denomina $\mu_X$

Sea $X$ una V.A.D. Entonces el valor esperado (o media) de $X$ es:

$$
E(X) =\sum_{x \in R_x} x \cdot p_X(x)
$$

Para el caso de $X$ una V.A.C. Entonces el valor esperado (o media) de $X$ es:

$$
E(X) = \int_{-\infty}^{\infty} x \cdot f_X(x)
$$

### Función de Variable Aleatoria

El valor de la esperanza de una función $h(X)$ se calcula como

$$
E(h(x)) = \sum_{x \in R_X} h(x) \cdot P_X(x)
$$

Para el caso de variables continuas, se calcula como

$$
E(h(X)) = \int_{-\infty}^{\infty} h(x) \cdot f_X(x)
$$

**Propiedad: La esperanza de** $X$ "**es lineal"**

Sea $X$ una V.A. con esperanza $\mu$, si $h(X) = aX + b$, entonces $E(h(X)) = a\mu + b$

### Caso General

Sea $X$una variable aleatoria con función de distribución $F_X(x) = P(X \leq x)$, Si $h(X)$ es una función cualquiera de $X$, si definimos $A$ como el conjunto de átomos, entonces

$$
E[h(X)] = \sum_{x \in A} h(x) P(X = x) + \int\limits_{\mathbb{R} \setminus A} h(x) \cdot F_X'(x) dx
$$

**Esperanza Parcial:** Es la esperanza de una parte de $X$, se denota como $E[X  \cdot \mathbf{1} \{x \in A\}$. Encontramos que

$$
E[X | X \in A] = \frac{E[X  \cdot \mathbf{1} \{X \in A\}}{P(X \in A)}
$$

Puedo despejar y pensar en particiones, obtengo

$$
E(X) = E[X | X \in A] P(X \in A) + E[X | X \in \overline A]P(X \in \overline A)
$$

**Propiedad de Areas:** La esperanza de una variable se puede pensar como el area por encima de la función para todos los valores positivos, menos el area por debajo de la función para todos los valores negativos.

$$
E(X) = \int_0^\infty [1 - F_X(x)] dx - \int_{-\infty}^0 F_X(x)dx
$$

## Varianza de una Variable Aleatoria

Sea $X$ una variable aleatoria, Entonces podemos encontrar que tan dispersa se encuentre la variable, como:

$$
\text{Var}(X) = E[(X-E(x))^2]
$$

 Como la esperanza es lineal, entonces

$$
\text{Var}(X) = E(X^2) - E(X)^2
$$

El **Desvío Estándar:** El valor de la varianza no es significativo, ya que estamos calculando la distancia al cuadrado. Debido a esto, definimos el desvío estándar.

$$
\sigma_X = \sqrt{\text{Var}(X)}
$$

La **Mediana:** Es el valor de $X$ que acumula una probabilidad de $0.5$, (es el cuantil $0.5$)

La **Moda:** Es el valor de $X$ con mayor probabilidad.
