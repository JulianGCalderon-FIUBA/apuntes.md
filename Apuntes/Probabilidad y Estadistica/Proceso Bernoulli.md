Supongamos que defino una variable aleatoria que valga $1$ si sale un $1$ en el tiro $i$ de un dado, $0$ en otro caso

Esta variable aleatoria tendra distribucion Bernoulli de parametro $1/6$. Si tiro el dado una y otra vez, observo

- Sale el $1$, o no (dicotomia)
- $P(X_i= 1) = \frac 16 \quad\forall i$ ($p$ constante)
- Los tiros (experimentos) son independientes entre si

Estas observaciones se denominan Proceso Bernoulli. Nos referimos al caso $X_i = 1$ como un exito.

Bajo este experimento, podemos definir distintas cosas

- Cuantas veces obtengo exito en $n$ experimentos
- Si busco observar $n$ existos, cuantas veces debo realizar el experimento

# Binomial de parametros $n, p$

La distribucion geometrica nos indica la probabilidad de la cantidad de exitos en $n$ experimentos

$$
P_Y(y) = \binom{n}{y} p^y (1-p)^{n-y}
$$

Se puede considerar como una suma de $n$ variables de Bernoulli, independientes

# Pascal de parametros $k, p$

La distribucion Pascal nos indica la probabilidad de la cantidad de experimentos necesarios hasta obtener $k$ exitos.

$$
P_W(w) = \binom{w-1}{k-1} p^k(1-p)^{w-k}
$$

# Geometrica de parametro $p$

La distribucion Geometrica nos indica la probabilidad de cantidad de experimentos necesarios hasta obtener un exito

$$
P_N(n) = p (1-p)^{n-1}
$$

Se puede relacionar $N$ con $W$ a partir de 

$$
W = \sum_{i=1}^k N_i
$$

Una pascal es una suma de Geometricas independientes.