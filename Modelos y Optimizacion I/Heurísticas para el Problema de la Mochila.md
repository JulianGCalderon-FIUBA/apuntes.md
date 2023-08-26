## Aproximación a través de coeficiente de rendimiento

Un ejemplo simple de **heurística** puede ser:

1. Ordenar los elementos por el índice precio/peso, de mayor a menor. En caso de empate, el de menor peso. En caso de empate, por orden alfabético.
2. Mientras queden elementos en la lista:
	1. Tomo el primer elemento de la lista y lo quito de la lista:
	2. Si entra en la mochila, lo agrego y recalculo el espacio disponible

### Evaluación de la Heurística

Debemos encontrar una forma de evaluar la heurística, para eso, la analizaremos en el peor caso. Definiendo a $z$ como el valor de la solución óptima, y $z'$ como el valor de la solución obtenida tras la aplicación de una heurística, entonces hallamos el índice de performance de la heurística como

$$
\text{Performance} =\frac{z'}z
$$

La aproximación definida anteriormente tiene un índice de performance tendiendo a $0$, en el peor caso.

### Mejoramiento a través de la comparación con el elemento crítico

Para esta mejora, definimos el elemento crítico $s$ como el primer elemento que, en caso de incluirlo, se excede de la capacidad permitida. La heurística se puede mejorar agregando un paso posterior que consiste en comparar al resultado obtenido con el beneficio del elemento crítico, $p_s$. El resultado obtenido sería

$$
z'' = \max\Big(\sum_{i=1}^{s-1}p_i;p_s\Big)
$$

Esta mejora causa que el peor índice de performance sea igual a:

$$
\lim_{k\to\infty}\frac{z''}{z} = \frac 12
$$

## Análisis de Cotas

Para la aproximación anterior, evaluamos las heurísticas utilizando su valor óptimo, pero este valor no siempre es conocido. Para eso, debemos hallar alguna cota superior para nuestro problema.

### Relajación Lineal

Si resolvemos el problema con relajación lineal, obtendremos una solución óptima que será siempre mayor o igual a la solución obtenida con variables enteras.

Definimos $\overline c$ como la capacidad restante luego de introducir todos los elementos previos al elemento crítico

$$
\overline c = c - \sum_{i=1}^{s-1}w_i
$$

Debemos introducir todos los elementos previos, el elemento crítico, y luego introducir tanto elemento crítico como podamos (fraccionándolo)

$$
U_0 = CP(KP) = \sum_{i=1}^{s-1}p_i + \overline c\frac{p_s}{w_s}
$$

### Dantzig

A la solución anterior, Dantzig le aplicó una condición de integralidad. La cota superior será el entero menor más cercano a la cota resuelta por relajación lineal, ya que nunca podremos encontrar un valor de óptimo no entero.

$$
U_1 = \lfloor CP(KP) \rfloor = \sum_{i=1}^{s-1}p_i + \bigg\lfloor \overline c\frac{p_s}{w_s} \bigg\rfloor
$$

### Martello & Toth

Ellos superaron la cota de Dantzig, estableciendo la integridad del elemento crítico. Es decir, plantean dos cotas, una si se ingresa el elemento crítico, y otra si no se ingresa el elemento crítico.

Si no se ingresa el elemento crítico, entonces el término es igual al de Dantzig, pero fraccionando el elemento siguiente al elemento crítico.

$$
W_0 = \sum_{i=1}^{s-1}p_i + \bigg\lfloor \overline c\frac{p_{s+1}}{w_{s+1}} \bigg\rfloor
$$

Para ingresar el elemento crítico, debemos quitar obligatoriamente uno de los elementos del intervalo. Para esto, fraccionamos el último elemento antes del crítico, retirando tanto de este elemento como sea necesario para poder ingresar el elemento crítico.

$$

W_0 = \sum_{i=1}^{s-1}p_i + \bigg\lfloor p_s -(w_s-\overline c)\frac{p_{s+1}}{w_{s+1}} \bigg\rfloor

$$

Finalmente, la cota real estará dada por el máximo de estas dos cotas, como:

$$
U_2 = \max (W_1;W_2)
$$
