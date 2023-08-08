# Predicción

Sea $Y$ una V.A., $\Bbb X = (X_1, \cdots, X_n)$ un vector aleatorio, existirá alguna función $g(x)$ que nos sirve para predecir a $Y$. Para encontrar dicha función se calcula el error cuadrático medio

$$
\text{ECM} = E[(Y-g(\Bbb X))^2]
$$

Si $g(X) = c$, busco $c$ tal que el error cuadrático medio sea mínimo.

$$
c = E[Y]
$$

Si $g(X) = a + bX$, busco $c$ tal que el error cuadrático medio sea mínimo.

$$
a = E(Y)  + bE(X)
$$

$$
b = \frac{\text{Cov}(X,Y)}{\text{Var}(X)}
$$

$$
g(X) = \hat Y = \frac{\text{Cov} (X,Y)}{\text{Var}(X)} (X - E(X)) + E(Y)
$$

# Desigualdades

**Desigualdad de Markov:**

Sea $h: \mathbb{R} \to \mathbb{R}^+$ tal que $h$ es par, y restringida a $\mathbb{R}^+$ es creciente, y sea $X$ una V.A. tal que $E(h(x))$ existe, entonces $\forall t \in \mathbb{R}$

$$
P(|X| \geq t) \leq \frac{E[h(x)]}{h(t)}
$$

Si además, $X$ es no negativa, $\forall a > 0$

$$
P(X \geq a) \leq \frac{E(x)}{a}
$$

**Desigualdad de Tchevychev:**

Sea $X$ una V.A. con varianza finita, $\forall k > 0$

$$
P(|X - E(X)| \geq k) \leq \frac{\text{Var}(X)}{k^2}
$$

> [!note]
> esta es la desigualdad de Markov si $Y = X - E(X)$ y $h(t) = t^2$
