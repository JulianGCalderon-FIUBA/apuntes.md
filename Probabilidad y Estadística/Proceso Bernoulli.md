Supongamos que defino una variable aleatoria que valga $1$ si sale un $1$ en el tiro $i$ de un dado, $0$ en otro caso.

Esta variable aleatoria tendrá distribución Bernoulli de parámetro $1/6$. Si tiro el dado una y otra vez, observo.

- Sale el $1$, o no (dicotomía)
- $P(X_i= 1) = \frac 16 \quad\forall i$ ($p$ constante)
- Los tiros (experimentos) son independientes entre sí

Estas observaciones se denominan Proceso Bernoulli. Nos referimos al caso $X_i = 1$ como un éxito.

Bajo este experimento, podemos definir distintas cosas

- Cuantas veces obtengo éxito en $n$ experimentos
- Si busco observar $n$ éxitos, cuantas veces debo realizar el experimento

## Binomial de parámetros $n, p$

La distribución geométrica nos indica la probabilidad de la cantidad de éxitos en $n$ experimentos

$$
P_Y(y) = \binom{n}{y} p^y (1-p)^{n-y}
$$

Se puede considerar como una suma de $n$ variables de Bernoulli, independientes

## Pascal de parámetros $k, p$

La distribución Pascal nos indica la probabilidad de la cantidad de experimentos necesarios hasta obtener $k$ éxitos.

$$
P_W(w) = \binom{w-1}{k-1} p^k(1-p)^{w-k}
$$

## Geométrica de parámetro $p$

La distribución Geométrica nos indica la probabilidad de cantidad de experimentos necesarios hasta obtener un éxito

$$
P_N(n) = p (1-p)^{n-1}
$$

Se puede relacionar $N$ con $W$ a partir de

$$
W = \sum_{i=1}^k N_i
$$

Una distribución pascal es una suma de distribuciones geométricas independientes.
