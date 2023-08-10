Cualquier vector perteneciente a un subespacio $S$ puede representarse como una única combinación lineal de los elementos de una base $B$ del subespacio.

Se le llama coordenadas de $v$ con respecto a la base $B$ a la $n$-upla en $\Bbb K^n$ formada por los escalares $a_0, a_1, \cdots, a_n$ que participan en la combinación lineal del elemento $v$.

Así podemos definir la función $[v]^B: \Bbb V \to \Bbb K^n$, que dado un vector $v$ y una base $B$, nos devuelve el conjunto de escalares que forman $v$.

## Matriz de Cambio de Base

Sean $B = \{v_i: i\in I_n\}$ y $B' = \{w_i:i\in I_n\}$ dos bases del espacio vectorial $\Bbb V$. Entonces cada vector del subespacio lo puedo anotar como

$$
[v]^B = \begin{bmatrix}\alpha_1\\\alpha_2\\\vdots\\\alpha_n\end{bmatrix}\implies v = \alpha_1v_1 + \alpha_2v_2 + \cdots + \alpha_nv_n
$$

$$
\begin{align*}
[v]^{B'} &= [\alpha_1v_1 + \alpha_2v_2 + \cdots + \alpha_nv_n]^{B'}\\
[v]^{B'} &= \underbrace{\begin{bmatrix}[v_1]^{B'} & [v_2]^{B'} & \cdots & [v_n]^{B'}\end{bmatrix}}_{M^{n\times n}}
\begin{bmatrix}\alpha_1\\\alpha_2\\\vdots\\\alpha_n\end{bmatrix}
= M_B^{B'}[v]^B
\end{align*}
$$

A esta matriz se le llama, matriz de cambio de base de $B$ a $B'$. Y sirve para justamente, encontrar las coordenadas de cualquier vector respecto de $B'$, usando sus coordenadas respecto a $B$. Si multiplico la matriz por una coordenada en la base $B$, me devuelve la misma coordenada en la base $B’$

$$
M_B^e = \begin{bmatrix}
v_1 | v_2 | \cdots | v_n
\end{bmatrix} = (M_e^B)^{-1}
$$

$$
M_B^{B'} = M_e^{B'}M_B^e
$$
