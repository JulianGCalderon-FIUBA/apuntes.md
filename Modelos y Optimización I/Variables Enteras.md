Introduciremos al modelado, dos nuevos tipos de variables:

- **Variables discretas:** Utilizadas para representar productos o recursos de valor entero (no divisibles)
- **Variables bivalentes:** También conocidas como variables binarias:
    - *De decisión:* Señalan alternativas posibles, el modelo erigirá un valor para determinar cierto comportamiento
    - *Indicativas:* Marcan el estado de una variable asociada

Usualmente, se acostumbra a notar las variables bivalentes con $Y_\alpha$

# Relaciones Lógicas

Podemos simular relaciones lógicas a partir de variables bivalentes, utilizando algunas técnicas comunes

Definamos una proposición $r$ tal que $p + q = r$. Podemos representar esto en programación lineal de la siguiente forma:

$$
Y_r \le Y_p + Y_q \le 2Y_r
$$

En el caso genérico tendremos que si $p_1 + p_2 + \cdots + p_n = q$. Entonces:

$$
Y_q \le Y_{p_1} + Y_{p_2} + \dots + Y_{p_n} \le nY_q
$$

También, podemos simular una compuesto lógica ***and*** para la variable $r$ tal que $pq = r$ de la siguiente forma:

$$
2Y_r \leq Y_p + Y_q  \leq 1 + Y_r
$$

En el caso genérico, tendremos que si $q = p_1p_2\cdots p_n = q$. Entonces:

$$
nY_q \leq Y_{p_1} + Y_{p_2} + \cdots + Y_{p_n} \leq n-1+Y_q
$$

## Variables Indicativas

Definamos una variable $Y$ tal que $Y = 1 \iff X > 0$. Entonces podemos definir

$$
mY \leq X \leq MY
$$

Para que dos variables no puedan tomar simultáneamente el valor uno $(Y_1Y_2 = 0)$, podremos definir la siguiente restricción:

$$
Y_1 + Y_2 \leq 1
$$

A partir de esto, podremos definir programación de metas para casos donde el funcional no es de ayuda.

$$
X - \lim = \text{Exceso} - \text{Defecto}
$$

$$
mY_D \leq \text{Defecto} \leq MY_D
$$

$$
mY_E \leq \text{Exceso} \leq MY_E
$$

$$
Y_D + Y_E \leq 1
$$

También podremos utilizar esta técnica para definir si dos variables $X_1, X_2$ son iguales

$$
X_1 - X_2= \text{Exceso} - \text{Defecto}
$$

$$
mY_D \leq \text{Defecto} \leq MY_D
$$

$$
mY_E \leq \text{Exceso} \leq MY_E
$$

$$
Y_D + Y_E + Y_= = 1
$$

Entonces, $Y_=$ tomara el valor uno únicamente si son iguales.

Similarmente, podemos forzar ambas variables a ser iguales (o distintas) utilizando

$$
Y_D + Y_E = 0
$$

$$
Y_D + Y_E = 1
$$

Para indicar si una variable se encuentra en el rango $[0,a]$, podemos declarar:

$$
aY \leq X \leq a+ MY
$$

# Eliminación de Restricciones

Podemos declarar restricciones que únicamente serán validas bajo cierta condición $Y = 0$.

$$
g_1(X) \leq b_2 + MY_1
$$

$$
\cdots
$$

$$
g_n(X) \geq b_n - MY_n
$$

Luego, podemos restringir a que únicamente una de las restricciones pueda estar  habilitada a la vez.

$$
Y_1 + \cdots + Y_n = n-1
$$

# Costo Diferencial Por Intervalo

Tendremos una variable $X$, la cual queremos separar en $n$ intervalos, entonces debemos plantear ecuaciones para determinar cuando se encuentra en cada uno de los intervalos.

$$
M_{n-1}Y_n \leq X_n \leq M_nYn
$$

Si $Y_n = 0$, forzará a $X_n$ a valer cero. En caso contrario, $X$ pertenecerá al intervalo $(M_{n-1}, M_n)$, con $X_n = X$.

$$
Y_1 + \cdots + Y_n = 1
$$

$$
X_1 + \cdots + X_n = X
$$

# Función Cóncava Seccionalmente Lineal

En esta situación, crearemos una estructura del tipo ***represa*** tal que cuando se llena el primer ***dique***, se habilita el segundo. De esa forma, si $X$ pertenece al intervalo $(M_{i-1}, M_i)$. Entonces todos los $X_j$ previos a $X_i$ estarán completos. Con el valor de $X_i$ relativo a los otros *diques*.

De esta forma, declararemos la variable $Y_i$ que valdrá uno únicamente si el intervalo apropiado esta completo.

$$
M_1Y_2 \leq X_1 \leq M_1
$$

$$
(M_2-M_1)Y_3 \leq X_2 \leq (M_2-M_1)Y_2
$$

$$
(M_3-M_2-M_1)Y_4 \leq X_3 \leq (M_3-M_2-M_1)Y_3
$$

$$
\cdots
$$

$$
X_n \leq MY_n
$$

$$
X_1 + \cdots + X_n = X
$$

# Función de $n$ valores posibles

Puedo definir una bivalente para cada valor posible de $X$. Únicamente valido si $X$ tiene un número finito de valores posibles

$$
X = aY_a+ bY_b + cY_c
$$

$$
Y_a + Y_b + Y_c = 1
$$

# Redondeo

Si queremos redondear una variable continua X, a una variable entera $E$ tendremos tres posibilidades.

- Round: Al entero más cercano
    
    $$
    X - 0.5 + m \le E \le X + 0.5
    $$
    
- Floor: Al entero menor más cercano
    
    $$
    X - 1 + m \le E \le X
    $$
    
- Ceiling: Al entero mayor más cercano
    
    $$
    X + 1 - m \le E \le X
    $$