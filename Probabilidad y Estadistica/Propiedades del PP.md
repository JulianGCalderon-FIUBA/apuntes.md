## Adelgazamiento

Sea $N(t)$ un proceso de Poisson de intensidad $\lambda$, donde cada evento es del tipo $I, II$ con probabilidad independiente de cada evento $p, 1{-}p$ respectivamente. Entonces podemos dividir el proceso de de Poisson en 2 *Poissonsitos* $N_I(t), N_{II}(t)$, con intensidad $\lambda p, \lambda (1{-}p)$ respectivamente. De esta forma, obtenemos

$$
N(t) = N_I(t) + N_{II}(t)
$$

Estos procesos de Poisson son independientes entre si.

## Superposición de Procesos de Poisson

Sean $N_I(t), N_{II}(t)$ dos procesos de poisson independientes de tasas $\lambda_I,  \lambda_{II}$ respectivamente, entonces podemos definir un proceso de poisson general de intensidad $\lambda = \lambda_I + \lambda_{II}$ que tiene en cuenta las marcas de ambos procesos. Es el camino inverso al teorema de adelgazamiento

$$
N(t) := N_I(t) + N_{II}(t)
$$

## Distribución Condicional de los Tiempos de Llegada

Como el proceso de Poisson es temporalmente homogéneo y tiene incrementos independientes, entonces cada intervalo de igual longitud tiene la misma probabilidad de contener un arribo, de esta forma. Encontramos que, sabiendo que ocurrio un evento en el intervalo $[0, t]$, la posición en el tiempo del evento tiene distribución uniforme en el intervalo $[0, t]$

Si sabemos que ocurrieron exactamente $n$ eventos en el intervalo $[0, t]$, Entonces si definimos $S_i$ como el tiempo exacto en el que ocurrió el evento $i$. Entonces la variable aleatoria $S_i$ tiene distribución uniforme en el intervalo $[0, t]$

Para todo $s < t$, se cumple que $P(S_1 < s | N(t) = 1) = \frac st$

Como cada evento puede, o no, pertenecer a un intervalo de tiempo, podemos usar la distribución binomial

$$
\Big[N(a,b) | N(t) = n\Big] \sim \mathcal B\Big(n, \frac{b-a}{t}\Big)
$$

Esta variable aleatoria representa la cantidad de eventos ocurridos en el intervalo $(a,b)$, dado que ocurrieron $n$ eventos en el intervalo $(0, t)$

Si quiero encontrar la probabilidad de un número de eventos para cada intervalo, entonces podemos definir una multinomial

$$
\Big[\big(N(0, a), N(a, b), \cdots, N(z, t\big)\Big | N(t) = n\Big] \sim \mathcal M\Big(n, \frac at, \frac{b-a}t, \cdots \frac{t-z}t\Big)
$$
