## Frecuencia Angular de Resonancia

Yo puedo variar la pulsación de un generador de corriente alterna. Si quiero maximizar la amplitud de la corriente, entonces debo tender la frecuencia hacia un valor

$$
w_r = \frac{1}{\sqrt{LC}}
$$

A este valor, se lo llamara frecuencia angular (o pulsación) de resonancia.

Cuando un circuito se encuentra en resonancia, entonces $I_0 = V_0 / R$. Sera un circuito resistivo puro, ya que la diferencia entre las reactancias es $0$.

Debido a eso, la potencia media es maxima. $cos(\phi_z) = 1$

$$
P = \frac{v_{ef}^2}{R}
$$

Cuando $w < w_r$, entonces la reactancia capacitiva sera mayor a la inductiva, por lo que el circuito sera capacitivo. Cuando $w > w_r$, entonces la reactancia inductiva sera mayor a la capacitiva, por lo que el circuito sera inductivo.

Si vario la resistencia del circuito, entonces varia la corriente maxima del circuito. A mayor resistencia, menor corriente maxima.

Si analizamos la potencia activa, llegamos a que la potencia maxima también se encuentra cuando el circuito esta en resonancia. Por otro lado, la potencia reactiva es nula.

## Frecuencia Angular de Corte

Se define la frecuencia angular de corte como la que causa que la potencia activa sea exactamente la mitad de la maxima. Entonces se define como:

Nos quedan 4 soluciones, pero debemos descartar las soluciones negativas (no podemos tener pulsación negativa)

$$
w_c = \frac{\pm CR + \sqrt{C^2R^2 + 4LC}}{2CL}
$$

Si calculamos la diferencia entre ambas pulsaciones, tenemos que

$$
\Delta w = w_2 - w_1 = R/L
$$

## Factor de Calidad

Definimos factor de calidad o merito al siguiente valor, determina que tan estrecha es la campana (ancho de banda) de la potencia en función de la pulsación.

$$
q = \frac{w_r}{\Delta w} = w_r \cdot \frac{L}{R}
$$

Cuanto mayor es el factor de calidad, mas fácil es sintonizar con la resonancia. Hablamos de un buen sintonizador cuando el factor de calidad es mayor a $1000$.

Para sintonizar, podremos usar un capacitor variable para encontrar el punto de resonancia.
