Un estimador es un estadístico cuyos valores se consideran medidas experimentales de un parámetro desconocido

Es una funcion delestadistico que provee un valor aproximado de un paraametro o caracteristica desconocida.

Por ejemplo, podemos aproximar el parametro de una Bernoulli a partir de la frecuencia relativa del experimento.

## Estimador de Maxima Verosimilitud

Consiste en encotrar el valor del parametro para el cual la probabilidad es maxima. Esto se encuentra buscando el maximo de la funcion de versimilitud.

Si la distribucion pertenece a una **familia regular**, entonces como $\log$ es una funcion monotona creciente, entonces encontrar el maximo de $L$ equivale a buscar el maximo de $\log L$.

$$
\frac{d}{d\theta} \log(L(\theta)) = 0
$$

Podemos despejar $\theta$ y en contrar una funcion del parametro en funcion de los datos, evaluamos la funcion en las variables aleatorias y encontramos el estimador $\hat \theta(\underline X)$,

Si evaluamos en los datos obtenidos $\hat \theta (\underline x)$ y obtenemos un valor estimado para el parametro de la distribucion.

Para el caso de **familias no regulares**, debemos hallar el maximo a mano, analizando la funcion.

## Principio de Invarianza

Supongamos que $\lambda = q(\theta)$ es una funcion biunívoca de $\theta$, Si $\hat \theta$ es el EMV de $\theta$, entonces $\hat \lambda = q(\hat \theta)$ sera el EMV de $\lambda$.

## Bondad de los Estimadores

El riesgo de estimar el parametro de una distribucion a partir de su EMV se mide con el error cuadratico medio

$$
ECM(\hat \theta) = E[(\theta - \hat \theta)^2]
$$

Un estimador es **optimo** es el estimador de menor error cuadratico medio.

Un estimador es **insesgado** si el promedio del estimador se encuentra en el parametro que quiero estimar, es decir.

$$
E(\hat \theta) = \theta
$$

Si el estimador es **sesgado**, podemos definir el sesgo como

$$
B(\hat \theta) = E(\hat \theta) - \theta
$$

## Consistencia

Dada una sucesión de estimadores de $\hat \theta_n$ de $\theta$, decimos que $T = \hat \theta$ es (debilmente) **consistente** si, para todo $\varepsilon > 0$, entonces

$$
P_\theta(|T - \theta| > \varepsilon ) \stackrel{n \to \infty}\to 0
$$

Si $\Bbb V(\hat \theta) \to 0$ y $\Bbb E(\theta) \to \theta$, entonces $\hat \theta_n$ es debilmente consistente

## Estimadores Asintóticamente normales

Se dice que $\hat \theta_n$ es una sucesión de estimadores asintóticamente normales si $\sqrt n (\hat \theta_n - q(\theta))$ converge en distribución normal con medio 0 y varianza $q'(\theta)^2 / I(\theta)$.

Definimos $I(\theta)$ como el número de informacion de Fisher

$$
I(\theta) = E\Big[\frac{d}{d\theta} \ln(f_\theta(X))^2\Big] = - E\Big[\frac{d^2}{d \theta^2} \ln(f_\theta(X))\Big]
$$

### Teorema de Slutsky

Bajo ciertas condiciones generales, sea, sea $\hat \theta$ un estimador de maxima verosimlitud de $\theta$ consistente. Sea $q(\theta)$ derivable con $q'(\theta) \neq 0, \forall \theta$, entonces $q(\hat \theta)$ es asintoticamente normal para estimar a $q(\theta)$

Luego, si $\sqrt{n}\sqrt{I(\theta)}(\hat\theta_n-\theta) \sim^a \mathcal N(0,1)$. Entonces vale que:

$$
\sqrt{n}\sqrt{I(\hat\theta_n)}(\hat\theta_n-\theta)\sim \mathcal N(0,1)
$$

## Bootstrap

A partir de un conjunto de $n$ muestra puedo obtener un estimador, si consigo mas muestras, puedo obtener el promedio de estos estimadores y asi encontrar la esperanza del estimador.

Para encontrar mas muestras, puedo extraer con reposicion datos de la muestra original. y de esta forma construir nuevas muestras.

Una vez extraidos $N$ conjuntos de $n$ muestras de la muestra original, hallo sus estimadores correspondientes y calculo el promedio.
