## Simulación con Distribución Uniforme

"Imitar o fingir que se está realizando una acción cuando en realidad no se está llevando a cabo"

Para simular eventos, asigno a cada evento un segmento entre $[0,1)$. Luego, al obtener un número aleatorio entre $0,1$ con una calculadora/computadora, puedo saber que evento hubiese ocurrido.

> [!example] Ejemplo
> Tirar una moneda. $[0, \frac 12)$ es cara, $[\frac 12, 1)$ es ceca.

## Simulación con Distribución Particular

Dada una función $F(x)$, quiero encontrar una variable aleatoria cuya función de distribución coincide con $F$.

Sean $X$ y $U$ dos variables aleatorias con distribuciones distintas, diremos que dos eventos son equivalentes si acumulan la misma probabilidad. Para hacer esto, planteamos las dos funciones de distribución y buscamos los valores $x_1, x_2, x_3$ que acumulan la misma probabilidad $a_1, a_2, a_3$ que $u_1, u_2, u_3$. Sin embargo, no siempre va a ser tan fácil igualar las probabilidades acumuladas.

Se puede ver que estamos buscando cuantiles para $X$. Buscamos $x_i$ tal que la función de distribución $F_U$ haya acumulado $a_i$. Es decir, el cuantil $a_i$ de $X$.

### Inversa Generalizada

$$
F_X^{-1}(u) = \min \{x \in \mathbb{R}: F_X(x) \geq u\}, u \in (0, 1)
$$

Sea $F$ una función de distribución, exista una variable aleatoria $X$ tal que $F_X(x) = P(X \leq x)$

> [!note]
> Para encontrar todas las equivalencias, divido el intervalo $[0,1]$ en tramos donde cambia la distribución que quiero simular

### Teorema

Sea $F$ una función de distribución, entonces si defino $X = F^{-1}(U)$, con $U \sim \mathcal U(0,1)$. Se tiene que $X$ es una variable aleatoria cuya función de distribución es la función $F$ dada.
