Sean $X,Y$ variables aleatorias discretas con $p_X(x) > 0$. La función de probabilidad de $Y$ dado que $X = x$ es

$$
p_{Y|X=x}(y) = P(Y=y | X = x) = \frac{P(X = x, Y = y)}{P(X = x)}
$$

$$
p_{Y|X=x}(y) = \frac{p_{XY}(x,y)}{p_X(x)}
$$

De esta forma, encontramos que

$$
p_{X,Y}(x,y) = p_{Y | X = x}(y) p_X(x) = p_{X | Y = y}(x) p_Y(y)
$$

**Propiedad Útil :**

Sean $X,Y$ variables aleatorias discretas tal que $p_{Y | X = x}(y) = p_Y(y)$, entonces podemos decir que $X,Y$ son independientes.

# Vectores Aleatorios Continuos

Sea $(X,Y)$ un vector aleatorio continuo con densidad conjunta $f_{X,Y}(x,y)$ y densidad marginal $f_X(x)$, entonces para cualquier valor de $X$ con el cual $f_X(x) > 0$, la función de densidad de la variable aleatoria condicionada $Y$ dado $X=x$ es

$$
f_{Y | X = x}(y) = \frac{f_{XY}(x,y)}{f_X(x)}
$$

Si $f_X(x) = 0$, entonces la densidad condicional vale $0$. De forma análoga, obtenemos que

$$
f_{X,Y}(x,y) = f_{Y | X = x}(y) f_X(x) = f_{X | Y = y}(x) f_Y(y)
$$