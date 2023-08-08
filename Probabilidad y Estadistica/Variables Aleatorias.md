Una variable aleatoria *V.A. es una función* $X$ que le asigna a cada uno de los elementos de $\Omega$ un numera real $X(\omega)$. Para definir $X$, usamos un texto que relacione el espacio muestral con los números reales.

Sea $(\Omega, \mathscr A, P)$ un *E.P.* y $X: \Omega \to \mathbb{R}$ una función, diremos que $X$ es una variable aleatoria si $X^{-1} (x) \in \mathscr A$. Es decir, el dominio de la función es el algebra de eventos.

# Función de Distribución

Sea $(\Omega, \mathscr A, P)$ un *E.P. y* $X$ una *V.A.*, definimos su función de distribución $F_X: \mathbb{R} \to [0,1]$ dada por 

$$
F_X(x) = P(X \leq x), \quad \forall x \in \mathbb{R}
$$

**Propiedades:**

1. $F_X(x) \in [0, 1], \quad \forall x \in \mathbb{R}$
2. $F_X(x)$ es monótona no decreciente.
3. $F_X(x)$ es continua a derecha.
4. $\lim\limits_{x \to -\infty} F_X(x) = 0, \text{ y } \lim\limits_{x\to +\infty} F_X(x) = 1$

# Variable Aleatoria Discreta

Sea $(\Omega, \mathscr A, P)$ un *E.P.* y $X$ una *V.A.*, diremos que $X$ es una *V.A.D.* cuando existe $A \in \mathbb{R}$ finito o infinito numerable tal que $P_X(A) = 1$, donde $P_X(A) = P(X \in A)$.

## Rango de *V.A.D*

$$
R_X = \{x \in \mathbb{R}: P_X(x) > 0\}
$$

El rango de la variable aleatoria son los puntos donde la variable tiene probabilidad.

## Función de Probabilidad

Sea $X$ una *V.A.D.*, se llama función de probabilidad de $X$ a una función $P_X: \mathbb{R} \to [0, 1]$ tal que $P_X(x) = P(X = x)$. Con cada resultado posible $x_i$ asociamos un número $P_x(x_i)$

**Propiedades:**

1. $P_X(x_i) \geq 0, \quad \forall x_i$
2. $\sum\limits_{x \in R_x} P_X(x) = 1$

El grafico de esta función se ve como un conjunto de puntitos.

## Función de Distribución

Si la variable aleatoria es discreta, entonces la función de distribución sera escalonada y continua a derecha. Los saltos de la función de distribución representan los cambios en la probabilidad de los casos en ese salto.

$$
P_X(x_j) = P(X = x_j) = F_X(x_j) - F_X(x_{j-1})
$$

## Variable Aleatoria de Bernoulli

Una V.A tiene una distribución de **Bernoulli** si sus  valores posibles son $0$ y $1$ y le asigna $P(x=1) = p$. Es decir, $X$ es una *V.A.D*, $R_X = \{0, 1\}$ y $P_X(0) = 1 - p$

$$
X \sim Ber(p)
$$

**Función Indicadora**

Es un caso particular de la función indicadora donde $p = 1$ . Su forma compacta es la siguiente:

$$
\mathbf{1}\{x \in A\} = \begin{cases}
0 \text{ Si } X \notin A \\
1 \text{ Si } X \in A
\end{cases}
$$

# Variable Aleatoria Continua

Una *V.A.* es continua si se cumplen las siguientes condiciones.

1. Su conjunto de valores posibles se compone de todos los números que hay en un solo intervalo, o en una union excluyente de intervalos
2. Ningún valor posible tiene probabilidad positiva, es decir, $P(X = c) = 0 \quad \forall c \in R$

## Función de Densidad de Probabilidad

Debe existir una función de densidad de probabilidad $f_x: \mathbb{R} \to \mathbb{R}$ tal que:

1. $f_X(x) \geq 0, \quad \forall x \in \mathbb{R}$
2. $\displaystyle \int_{-\infty}^\infty f_X(x) dx = 1$
3. Para cualquier $a, b$ tal que $a < b$, tenemos que $P(a < X < b) = \int_a^b f_X(x)dx$

Esta función solo existe para variables aleatorias continuas.

## Función de Distribución

Para variables aleatorias continuas, tenemos que la probabilidad de distribución se calcula como

$$
F_X(x) = P(X \leq x) = \int_{-\infty}^x f_X(x) dx
$$

Esta función siempre va a ser continua. No puede contener saltos ya que eso implicaría que la probabilidad se acumule en un punto, lo cual es imposible.

**Teorema:**

Sea $F_X(x)$ la función de distribución de una *V.A.C*, luego $f_X(x) = \frac{d}{dx}F_x(x)$

# Tipos de Variable Aleatoria

**Atomos:** Diremos que $a \in \mathbb{R}$ es un átomo de $F_X(x)$ si su peso es positivo, es decir, la probabilidad cumple que $P(X = a) > 0$

El conjunto de todos los átomos de $F_X(x)$ coincide con los puntos de discontinuidad de $F_X(x)$. Podemos definir:

1. La *V.A.* $X$ sera discreta si la suma de las probabilidades de todos sus átomos es $1$
2. La *V.A.* $X$ sera continua si no tiene átomos. (continua)
3. La *V.A.* $X$ sera **MIXTA** si no cumple ninguna de las dos condiciones anteriores.

**Soporte:** Conjunto de puntos donde la función salta (átomos) o su derivada es distinta de $0$ (crece)

# Variable Aleatoria Mixta

Cuando tratamos con variables mixtas, entonces para calcular probabilidad de intervalos debemos usar la siguiente expresión. Esta formula es valida para cualquier tipo de variable aleatoria.

$$
P(A < X \leq B) = F_X(B) - F_X(A)
$$