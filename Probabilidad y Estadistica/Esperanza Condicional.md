---
title: Esperanza Condicional
---

## Función de Regresión

Sea $Y | X = x$ una variable aleatoria discreta, entonces definimos su esperanza como

$$
E[Y | X = x] = \sum_{y \in R_{Y | X = x}} yP_{Y|X=x}(y)
$$

Si es una variable a aleatoria continua, entonces definimos su esperanza como

$$
E[Y | X = x] = \int_{-\infty}^\infty yP_{Y|X=x}(y)
$$

Ambas, son funciones de $x$, las llamamos **funciones de Regresión** $\varphi(x)$**.**

## Esperanza Condicional

Si llamamos $\varphi(x) = E[Y | X = x]$ a la esperanza de la variable condicionada $Y$ dado que $X = x$, luego $\varphi: \text{sop}(X) \to \mathbb{R}$

Vamos a definir una variable aleatoria llamada esperanza condicional de $Y$ dado $X$, denotada por$E[Y | X]$, como $\varphi(X) = E[Y | X]$

> [!tip] Propiedad Útil
> La esperanza de la variable $\varphi$ definida anteriormente es la esperanza de $Y$
> 
> $$
> E[E[Y|X]] = E[Y]
> $$

### Propiedades

1. Sean $X$ e $Y$ variables aleatorias, $r$ y $s$ funciones medibles, tales que las variables aleatorias $r(x)s(y)$, $r(x)$, $s(y)$ tienen esperanza finita, entonces

	$$
    E[r(X)s(Y) | X] = r(X)E[S(Y) |X]
    $$

2. Sean $Y_1, Y_2$ variables aleatorias con esperanza finita, entonces

	$$
    E[aY_1 + bY_2 | X] = aE[Y_1 | X] + bE[Y_2 | X]
    $$

3. Si $X, Y$ son dos variables aleatorias independientes

	$$
    E[Y|X] = E[Y]
    $$

4. Sea $X$ una variable aleatoria, entonces

	$$
    E[r(X) |X] = r(X)
    $$

### Definición Formal

La variable aleatoria **esperanza condicional** de $Y$ dada $X$ se define como $\varphi(X) = E[Y|X]$, con $\varphi$ una función medible tal que $E[(Y - \varphi(X))t(X)) = 0$ para toda función $t$ medible $t: \text{sop}(X) \to \mathbb{R}$. Tal que $Yt(X)$ tiene esperanza finita.

La esperanza condicional siempre existe, y además es única, con probabilidad $1$.

De esta forma, la esperanza condicional de $Y$ dada $X$ es el mejor predictor de $Y$ dado $X$. Si esta función es una recta, entonces va a coincidir con la recta de regresión.

## Esperanza de la Mezcla

Sea $X$ una variable aleatoria "mezcla", y $M$ una variable aleatoria mezcladora. Entonces definimos la esperanza de $X$ como

$$
E[X] = \sum E[X |M = i] P_M(i)
$$
