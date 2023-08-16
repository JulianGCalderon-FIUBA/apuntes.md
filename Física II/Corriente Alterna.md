---
title: Corriente Alterna
---

Vamos a diseñar circuitos que contengan los elementos vistos anteriormente. Además, vamos a conectar circuitos a la corriente alterna, Es decir, una corriente cuya tensión está asociada a una función cosenoidal.

$$
v_q(t) = v_0 \cdot \cos(wt + \phi_v)
$$

Siendo $v_0$ la amplitud (o valor pico), $w$ la frecuencia angular (o pulsación), y $\phi_v$ la fase inicial de la corriente.

## Circuito Resistivo Puro

Planteamos, como con corriente estacionaria, la Ley de Ohm. Llegamos al valor de la corriente en el circuito, que varía en función del tiempo, según la tensión el generador.

$$
v_q(t) = i(t)\ R
$$

$$
i(t) = \frac{v_0}{R} \cdot \cos(wt + \phi_v)
$$

> [!note]
> La corriente del circuito va a estar en fase con la tensión del generador, lo que varía (en función de la resistencia) será la amplitud.

## Circuito Capacitivo Puro

Planteamos, como con corriente estacionaria, la relación entre la diferencia de potencial y las propiedades del capacitor. Como obtenemos la carga del capacitor, podemos derivar la expresión para encontrar la corriente que circula.

$$
v_q(t) = \frac 1C \int i(t) dt
$$

$$
i(t) = C \cdot w\ v_0  \cdot \cos(wt + \phi_v + \frac\pi 2)
$$

> [!note]
> La corriente del circuito va a estar desfasada $\pi/2$ con la tensión del generador. Va a variar la amplitud (en función de la capacidad)

Vamos a definir la reactancia capacitiva $X_c = \frac 1{C\ w}$. La cual tendrá unidades de Ohm. A mayor frecuencia, tendremos menor reactancia (menor corriente). Esto se debe a que no le damos tiempo suficiente al capacitor para cargarse.

## Circuito Inductivo Puro

Si recordamos la $\mathcal E$ de un inductor, y luego integramos en función del tiempo, podemos encontrar la corriente que circula por el mismo.

$$
v_q(t) = L\cdot \frac{di(t)}{dt}
$$

$$
i(t) = \frac{v_0}{w\cdot L} \cdot \cos(wt + \phi_v - \frac \pi 2)
$$

Definimos, entonces, la reactancia inductiva $X_L = w\ L$. A mayor frecuencia, La reactancia inductiva aumentará (menor corriente). Esto se debe a que la variación de flujo será menor.

> [!note]
> La corriente del circuito va a estar desfasada $\pi/2$ con la tensión del generador. Va a variar la amplitud (en función del coeficiente de autoinductancia del material)

## Conclusión

Vemos, entonces, que los tres elementos del circuito no modifican la frecuencia angular de la corriente, sin embargo, Existirán desfasajes en la intensidad de la corriente. Además, la corriente varía según las propiedades de los elementos.

|     | Amplitud $(i_0)$ |   Fase $(\phi_i)$    | Desfasaje $(\phi_{iv})$ |
|:---:|:----------------:|:--------------------:|:-----------------------:|
| $R$ |  $\frac{v_0}R$   |       $\phi_v$       |            0            |
| $C$ |     $v_0wc$      | $\phi_v + \frac\pi2$ |       $\frac\pi2$       |
| $L$ | $\frac{v_0}{wL}$ | $\phi_v - \frac\pi2$ |      -$\frac\pi2$       |

> [!note]
> Si el desfasaje fluctúa entre $0$ y $\pi\over2$, tiene un comportamiento capacitivo. Si fluctúa entre $-{\pi\over2}$ y $0$, tiene un comportamiento inductivo.
