---
title: Test de Hipótesis
---

El test de hipótesis es una regla de decisión entre $H_0, H_1$, la expresamos como una función de la muestra aleatoria $\delta(\underline X)$, que toma valores entre $0, 1$. Si $\delta = 1$, se rechaza la hipótesis nula. Si $\delta = 0$, no se rechaza.

Debo encontrar tests que minimicen la probabilidad de error, priorizando minimizar el error del tipo 1.

## Definiciones

Sea $\underline X$ una muestra aleatoria de una población con distribución paramétrica. Sean $\varTheta_1, \varTheta_2$ dos particiones de $\varTheta$. Un test para este problema es una regla de decisión basada en $\underline X$ para decidir entre 2 hipótesis.

$$
H_0: \theta \in \varTheta_1
$$

$$
H_1: \theta \in \varTheta_2
$$

De esta forma, definimos la probabilidad de cada error:

$$
P(\text{"Error I"})=P_\theta(\text{"Rechazar $H_0$"}),\ \theta \in \varTheta_1
$$

$$
P(\text{"Error II"})=P_\theta(\text{"No rechazar $H_0$"}),\ \theta \in \varTheta_2
$$

Definimos entonces la potencia del test como

$$
\pi_\delta(\theta) = P_\theta (\delta(\underline X) = 1) = E(\delta(\underline X))
$$

El test perfecto es aquel que tiene como función potencia una función partida con $\pi = 0, \theta \in \varTheta_1$, y $\pi = 1, \theta \in \varTheta_2$

Llamaremos nivel de significación $\alpha$ a la máxima probabilidad de cometer un error del tipo 1

$$
\alpha(\theta) = P_\theta(\text{"Error I"}) = \pi_\delta(\theta),\  \theta \in \varTheta_1
$$

Llamaremos $\beta$ a la máxima probabilidad de cometer un error del tipo 2

$$
\beta(\theta) = P_\theta(\text{"Error II"}) = 1 -\pi_\delta(\theta),\  \theta \in \varTheta_2
$$

## $P$-Valor

Definimos el $p$-valor como la probabilidad de encontrar otra muestra tan extremo como la hallada, Si $H_0$ fuera verdadero. Proponemos como límite: $p_V \leq 0.05$

## Test del Cociente de Verosimilitud

Dados dos parámetros, buscamos el cociente entre las funciones de verosimilitud de una muestra en cada parámetro. Si el cociente $T$ es mayor a un $k_\alpha$, entonces rechazamos la hipótesis nula. Nuestra constante $k_\alpha$ depende de la probabilidad $\alpha$ que deseamos de realizar un error del tipo 1.

$$
T = \frac{f_{\theta_2}(\underline X)}{f_{\theta_1}(\underline X)}
$$

$$
\delta(\underline X) = \begin{cases}1 \iff T > k_\alpha\\0 \iff T \leq k_\alpha\end{cases}
$$

Para hallar $k_\alpha$, encuentro $\alpha$ y determino la probabilidad del error que estoy buscando. $T$ es el estadístico de

### Propiedad

Sea $\underline X = (X_1, \cdot, X_n)$ una muestra aleatoria con distribución perteneciente a una familia exponencial, luego

- Si $C(\theta)$ es creciente, el test para $H_0: \theta \leq \theta_1, H_1: \theta > \theta_1$

$$
\delta(\underline X) = \begin{cases}
1 \iff T > k_\alpha\\
0 \iff T \leq k_\alpha
\end{cases}
$$

- Si $C(\theta)$ es decreciente, entonces para $H_0: \theta \leq \theta_1, H_1: \theta > \theta_1$.

	$$
    \delta(\underline X) = \begin{cases}
    1 \iff -T > k_\alpha\\
    0 \iff -T \leq k_\alpha
    \end{cases}
    $$

Si $H_0: \theta \geq \theta_1, H_1: \theta < \theta_1$, entonces las desigualdades se invierten.

## Test con Nivel de Significación Asintótico

Sea $\underline X = (X_1, \cdots, X_n)$ una muestra aleatoria de una población con distribución $F_\theta(x), \theta \in \Theta$

Si se quiere testear $H_0: \theta \in \Theta_1, H_1: \theta \in \Theta_2$

Se dirá que una sucesión de tests $\delta_n(\underline X)$ tiene nivel de significación asintótica $\alpha$

$$
\lim_{n\to\infty} \sup_{\theta \in \Theta_1}\Pi_{\delta_n}(\theta) = \alpha
$$

Se utiliza para las variables aleatorias discretas.
