---
title: Estimadores
---

Un estimador es un estadístico cuyos valores se consideran medidas experimentales de un parámetro desconocido

Es una función del estadístico que provee un valor aproximado de un parámetro o característica desconocida.

Por ejemplo, podemos aproximar el parámetro de una Bernoulli a partir de la frecuencia relativa del experimento.

## Estimador de Máxima Verosimilitud

Consiste en encontrar el valor del parámetro para el cual la probabilidad es máxima. Esto se encuentra buscando el máximo de la función de verosimilitud.

Si la distribución pertenece a una **familia regular**, entonces como $\log$ es una función monótona creciente, entonces encontrar el máximo de $L$ equivale a buscar el máximo de $\log L$.

$$
\frac{d}{d\theta} \log(L(\theta)) = 0
$$

Podemos despejar $\theta$ y encontrar una función del parámetro en función de los datos, evaluamos la función en las variables aleatorias y encontramos el estimador $\hat \theta(\underline X)$,

Si evaluamos en los datos obtenidos $\hat \theta (\underline x)$ y obtenemos un valor estimado para el parámetro de la distribución.

Para el caso de **familias no regulares**, debemos hallar el máximo a mano, analizando la función.

## Principio de Invarianza

Supongamos que $\lambda = q(\theta)$ es una función biunívoca de $\theta$, Si $\hat \theta$ es el EMV de $\theta$, entonces $\hat \lambda = q(\hat \theta)$ será el EMV de $\lambda$.

## Bondad de los Estimadores

El riesgo de estimar el parámetro de una distribución a partir de su EMV se mide con el error cuadrático medio

$$
ECM(\hat \theta) = E[(\theta - \hat \theta)^2]
$$

Un estimador es **óptimo** es el estimador de menor error cuadrático medio.

Un estimador es **insesgado** si el promedio del estimador se encuentra en el parámetro que quiero estimar, es decir.

$$
E(\hat \theta) = \theta
$$

Si el estimador es **sesgado**, podemos definir el sesgo como

$$
B(\hat \theta) = E(\hat \theta) - \theta
$$

## Consistencia

Dada una sucesión de estimadores de $\hat \theta_n$ de $\theta$, decimos que $T = \hat \theta$ es (débilmente) **consistente** si, para todo $\varepsilon > 0$, entonces

$$
P_\theta(|T - \theta| > \varepsilon ) \stackrel{n \to \infty}\to 0
$$

Si $\Bbb V(\hat \theta) \to 0$ y $\Bbb E(\theta) \to \theta$, entonces $\hat \theta_n$ es débilmente consistente

## Estimadores Asintóticamente normales

Se dice que $\hat \theta_n$ es una sucesión de estimadores asintóticamente normales si $\sqrt n (\hat \theta_n - q(\theta))$ converge en distribución normal con medio 0 y varianza $q'(\theta)^2 / I(\theta)$.

Definimos $I(\theta)$ como el número de información de Fisher

$$
I(\theta) = E\Big[\frac{d}{d\theta} \ln(f_\theta(X))^2\Big] = - E\Big[\frac{d^2}{d \theta^2} \ln(f_\theta(X))\Big]
$$

### Teorema de Slutsky

Bajo ciertas condiciones generales, sea, sea $\hat \theta$ un estimador de máxima verosimilitud de $\theta$ consistente. Sea $q(\theta)$ derivable con $q'(\theta) \neq 0, \forall \theta$, entonces $q(\hat \theta)$ es asintóticamente normal para estimar a $q(\theta)$

Luego, si $\sqrt{n}\sqrt{I(\theta)}(\hat\theta_n-\theta) \sim^a \mathcal N(0,1)$. Entonces vale que:

$$
\sqrt{n}\sqrt{I(\hat\theta_n)}(\hat\theta_n-\theta)\sim \mathcal N(0,1)
$$

## Bootstrap

A partir de un conjunto de $n$ muestra puedo obtener un estimador, si consigo más muestras, puedo obtener el promedio de estos estimadores y así encontrar la esperanza del estimador.

Para encontrar más muestras, puedo extraer con reposición datos de la muestra original, y de esta forma construir nuevas muestras.

Una vez extraídos $N$ conjuntos de $n$ muestras de la muestra original, hallo sus estimadores correspondientes y calculo el promedio.
