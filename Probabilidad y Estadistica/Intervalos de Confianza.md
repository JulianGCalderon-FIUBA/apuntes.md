A partir de una muestra nunca vamos a poder encontrar nuestro parámetro $\mu$. Por lo que vamos a intentar encontrar un intervalo $\mu \in [A, B]$ tal que la probabilidad de que el parámetro pertenezca a ese intervalo sea de $1{-}\alpha$. Donde $1{-}\alpha$ es el nivel de confianza, siendo $\alpha$ el nivel de riesgo

## Método del Pivote

Un pivote $U$ es una variable aleatoria que es función de la muestra aleatoria y del parámetro a encontrar, pero que su distribución no depende de ningún parámetro desconocido

$$
P(a \leq U \leq b) = 1 - \alpha
$$

Debido a que tenemos la distribución de $U$, podemos encontrar $a, b$ fácilmente tras calcular sus cuantiles. Nótese que debemos hallar el intervalo más corto posible que acumule esa probabilidad (hay infinitos)

Una vez hallado $a, b$, despejamos el parámetro desconocido y hallamos su intervalo de confianza.

Para encontrar nuestro pivote $U$, partiremos del estimador de máxima verosimilitud. Si no funciona, podemos modificarlo hasta encontrar el pivote adecuado.

## Intervalos de Confianza de Nivel Asintótico

Sea $X_1, \cdots, X_n$ una muestra aleatoria de una población con distribución $F_\theta(x), \theta \in \varTheta$, se dice que $S_n(\underline X)$ es una sucesión de regiones de confianza para $\theta$ de nivel asintótico $1{-}\alpha$ si

$$
\lim_{n \to \infty} P(\theta \in S_n(\underline X)) = 1{-}\alpha,\ \theta \in \varTheta
$$

## Relación entre Regiones de Confianza y Test

Sea $X$ una variable aleatoria con distribución $F_\theta(x), \theta \in \varTheta$, y que para cada $\theta_0$ se tiene un test de nivel $\alpha$ para $H_0: \theta = \theta_0 \text{ vs. } H_1: \theta \not= \theta_0$

Se puede definir una región de confianza de nivel $1{-}\alpha$ para $\theta$ como

$$
S(\underline X) = \Big\{\theta: \delta(\underline X) = 0\Big\}
$$
