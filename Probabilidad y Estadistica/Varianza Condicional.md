---
title: Varianza Condicional
---

Sean $X$ e $Y$ variables aleatorias con $\text{var}(Y)$ finita, la varianza de $Y|X=x$ será

$$
\text{var}(Y| X= x) =E[(Y - E(Y |X=x)^2|X=x]
$$

Llamaremos $\tau(x) = \text{var}(Y|X=x], \tau: \text{sop}(X) \to R$. Así llamaremos varianza condicional de $Y$ dado $X$ a la variable aleatoria

$$
\tau(X) = var(Y|X) = E[(Y - E[Y|X])^2|X]
$$

Si desarrollamos la expresión, encontramos que

$$
\text{var}(Y|X) = E[Y^2|X] - E[Y|X]^2
$$

> [!tip] Propiedad de Pitágoras
> Proviene de aplicar el teorema de Pitágoras
> 
> $$
> \text{var}(Y) = E[\text{var}(Y|X)] + \text{var}(E[Y|X])
> $$
