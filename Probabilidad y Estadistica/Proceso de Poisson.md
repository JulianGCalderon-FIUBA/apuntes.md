---
title: Proceso de Poisson
---

Un proceso puntual aleatorio es un conjunto enumerado de puntos aleatorios ubicados sobre una recta real. Si el proceso es de Poisson, se denota como $PP(\lambda)$

Llamaremos $N(t)$ al número de eventos en un intervalo específico $[0, t]$

1. El número de eventos durante intervalos de tiempo no superpuestos son variables aleatorias independientes.
2. La probabilidad de cada evento en particular es la misma para todos los intervalos de longitud $t$, independientemente de la ubicación y de la historia del sistema
3. La probabilidad de obtener $2$ o más eventos en un intervalo lo suficientemente pequeño es despreciable

La función de probabilidad de $N$ está dada por la siguiente expresión, donde $\lambda > 0$ y tiene distribución de Poisson de parámetro $\mu = \lambda t$

$$
p_N(n) = \frac{(\lambda t)^n}{n!} e^{-\lambda t}, \qquad n \in \mathbb{N}_0
$$

la constante $\lambda$ será la intensidad o tasa de ocurrencia, y $t$ será la longitud del intervalo que voy a estudiar

## Propiedades

- La variable aleatoria $N(t)$ tiene distribución de Poisson si y solo si la variable aleatoria $T$ "Tiempo entre 2 eventos consecutivos" tiene distribución exponencial, de parámetro $\lambda$.
- Si definimos $G$ como el tiempo hasta el $k$-ésimo evento de Poisson, entonces $G$ se define como la suma de variables exponenciales independientes de parámetro $\lambda$, por lo que $G \sim \Gamma(k, \lambda)$
