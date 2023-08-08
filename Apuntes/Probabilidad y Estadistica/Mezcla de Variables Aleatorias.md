Diremos que $X$ es una variable aleatoria **“mezcla”** si es una mezcla de variables aleatorias, dados distintos eventos. Si $A_1, \cdots, A_n$ es una partición de $\Omega$ y $X$ una variable aleatoria de manera que conozco las distribuciones  de $X|A_i$, entonces podemos aplicar la propiedad de probabilidad total.

$$
F_X(x) = P(X \leq x) = \sum_{i=1}^n F_{X | A_i} (x) P(A_i)
$$

Si definimos una variable aleatoria que indique la partición de $\Omega$ en la que nos encontremos, entonces esta sera la variable **“mezcladora”**. Es una variable aleatoria discreta, por lo tanto, conocemos las distribuciones de $X | M = m$.

$$
F_X(x) = \sum_{i=1}^n F_{X | M = m} (x) P(M = m)
$$

Esta misma expresión es valida para las funciones de distribución y de probabilidad, dependiendo del tipo de variable aleatoria.

# Bayes para Mezclas

Sea $M$ una variable aleatoria discreta con soporte finito y $X$ una variable aleatoria continua, de manera que conozco la función de probabilidad de $M$ y la función de probabilidad de densidad de las variables aleatorias $X | M = m$. La funcion de probabilidad de $M$ dado que $X = x$ sera

$$
P_{M | X = x}(m) = \frac{f_{X | M = m}(x)P(M = m)}{\sum f_{X | M = i}(x) P(M = i)} 
$$