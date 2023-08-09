A partir de una muestra nunca vamos a poder encontrar nuestro parametro $\mu$. Por lo que vamos a intentar encontar un intervalo $\mu \in [A, B]$ tal que la probabilidad de que el parametro perteneza a ese intervalo sea de $1{-}\alpha$. Donde $1{-}\alpha$ es el nivel de confianza, siendo $\alpha$ el nivel de riesgo

## Metodo del Pivote

Un pivote $U$ es una variable aleatoria que es funcion de la muestra aleatoria y del parametro a encontrar, pero que su distribucion no depende de ningun parametro desconocido

$$
P(a \leq U \leq b) = 1 - \alpha
$$

Debido a que tenemos la distribucion de $U$, podemos encontrar $a, b$ facilmente tras calcular sus quantiles. Notese que debemos hallar el intervalo mas corto posible que acumule esa probabilidad (hay infinitos)

Una vez hallado $a, b$, despejamos el parametro desconocido y hallamos su intervalo de confianza.

Para encontrar nuestro pivote $U$, partiremos del estimador de maxima verosimilitud. Si no funciona, podemos modificarlo hasta encontrar el pivote adecuado.

## Intervalos de Confianza de Nivel Asintotico

Sea $X_1, \cdots, X_n$ una muestra aleatoria de una poblacion con distribucion $F_\theta(x), \theta \in \varTheta$, se dice que $S_n(\underline X)$ es una sucesión de regiones de confianza para $\theta$ de nivel asintotico $1{-}\alpha$ si

$$
\lim_{n \to \infty} P(\theta \in S_n(\underline X)) = 1{-}\alpha,\ \theta \in \varTheta
$$

## Relación entre Regiones de Confianza y Test

Sea $X$ una variable aleatoria con distribución $F_\theta(x), \theta \in \varTheta$, y que para cada $\theta_0$ se tiene un test de nivel $\alpha$ para $H_0: \theta = \theta_0 \text{ vs. } H_1: \theta \not= \theta_0$

Se puede definir una región de confianza de nivel $1{-}\alpha$ para $\theta$ como

$$
S(\underline X) = \Big\{\theta: \delta(\underline X) = 0\Big\}
$$
