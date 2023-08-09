Un proceso puntual aleatorio es un conjunto enumerado de puntos aleatorios ubicados sobre una recta real. Si el proceso de es Poisson, se denota como $PP(\lambda)$

Llamaremos $N(t)$ al numero de eventos en un intervalo especifico $[0, t]$

1. El numero de eventos durante intervalos de tiempo no superpuestos son variables aleatorias independientes.
2. La probabilidad de cada evento en particular es la misma para todos los intervalos de longitud $t$, independientemente de la ubicacion y de la historia del sistema
3. La probabilidad de obtener $2$ o mas eventos en un intervalo lo suficientemente pequeño es despreciable

La funcion de probabilidad de $N$ esta dada por la siguiente expresion, donde $\lambda > 0$ y tiene distribucion de Poisson de parametro $\mu = \lambda t$

$$
p_N(n) = \frac{(\lambda t)^n}{n!} e^{-\lambda t}, \qquad n \in \mathbb{N}_0
$$

la constante $\lambda$ sera la intensidad o tasa de ocurrencia, y $t$ sera la longitud del intervalo que voy a estudiar

## Propiedades

- La variable aleatoria $N(t)$ tiene distribucion de Poisson si y solo si la variable aleatoria $T$ "Tiempo entre 2 eventos consecutivos" tiene distribución exponencial, de parametro $\lambda$.
- Si definimos $G$ como el tiempo hasta el $k$-ésimo evento de Poisson, entonces $G$ se define como la suma de variables exponenciales independientes de parametro $\lambda$, por lo que $G \sim \Gamma(k, \lambda)$
