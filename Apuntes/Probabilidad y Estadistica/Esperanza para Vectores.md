# Esperanza para Vectores Aleatorios

Sea el vector aleatorio $X, Y$, entonces definimos la esperanza de una función de las variables aleatorias como

$$
E(h(X,Y)) = \sum_{x \in R_X} \sum_{y \in R_Y} h(x,y) p_{X,Y}(x,y)
$$

$$
E(h(X,Y)) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} h(x,y) f_{X,Y}(x,y) dx dy
$$

## Propiedades de Orden

Sea $X$ un vector aleatorio y $g: \mathbb{R}^k \to \mathbb{R}$ una función, tenemos que:

1. Si $X > 0$, entonces $E(X) > 0$
2. Si $g(x) > 0$, entonces $E(g(X)) > 0$
3. Sea $h(x) > g(x)$, entonces $E(h(X)) > E(g(X))$
4. $E(|X|) \geq E(X)$
5. $E(|XY|) \leq \sqrt{E(X^2)E(Y^2)}$

## Propiedades Importantes

1. Linealidad de la esperanza: $E[\sum_{i=1}^n a_i x_i] = \sum_{i=1}^n a_iE(x_i)$ 
2. Si $x_1, \cdots, x_n$ son variables aleatorias independientes, entonces
    
    $$
    E(\Pi_{i=1}^n X_i) = \Pi_{i=1}^n E(X_i)
    $$
    

# Covarianza para Vectores Aleatorios

La covarianza sirve para encontrar una relación entre dos variables aleatorias. Definimos

$$
\text{Cov}(X,Y) = E[(X-E(X)(Y-E(Y))]
$$

Como es una multiplicación, el significado del resultado lo voy a encontrar en su signo, no en su magnitud. Si tenemos una dependencia lineal creciente, entonces la covarianza resultara positiva. En caso contrario, la covarianza resultara negativa.

**Propiedades:**

1. $\text{Cov}(X,Y) = E(XY) - E(X)E(Y)$
2. Si $X,Y$ son independientes, entonces $\text{Cov}(X,Y) = 0$
3. **Propiedad de Colinealidad:** $\text{Cov}(a + bX, c + dY) = bd \cdot \text{Cov}(X,Y)$
4. $\text{Cov}(X + Y, Z) = \text{Cov}(X,Z) + \text{Cov}(Y,Z)$
5. $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$

## Coeficiente de Correlación

Entre las variables aleatorias $X,Y$, está dado por. Toma un valor entre $[-1, 1]$

$$
\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}
$$

Si $\rho_{XY} = \pm1$, entonces $P(aX + b = Y) = 1$