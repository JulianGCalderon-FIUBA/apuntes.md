Vamos a determinar todas las soluciones de ecuaciones diferenciales de orden $n$ de la forma:

$$
L(y)=y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1 y' + a_0y = f
$$

Ya que $L$ es una transformación lineal, las soluciones del nulo de esta transformación son las soluciones del sistema homogéneo asociado. Si la E.D.O. es de orden $n$, entonces $Nu(L)$ tiene dimensión $n$.

Todas las soluciones de la ecuación se puede anotar como:

$$
v = v_p + v_N
$$

## Solución General

A cada ecuación diferencial de la forma anterior, le podemos asociar un polinomio característico de grado $n$

$$
p(r) = r^{n} + a_{n-1}r^{n-1} + \cdots + a_1 r + a_0
$$

Si $\lambda$ es raíz de $p$, entonces $y(t) = e^{\lambda t}$ es solución de la ecuación homogénea asociada.

### Base del Subespacio

Si el polinomio característico tiene $n$ raíces reales distintas, entonces $\{e^{\lambda_1x},\,e^{\lambda_2x},\,\cdot,\,e^{\lambda_nx}\}$ es una base del subespacio nulo.

Si el polinomio característico tiene alguna raíz real $\beta$ de multiplicidad $k$, entonces vamos a obtener $k$ soluciones linealmente independientes de la forma $\{e^{\beta x},\, xe^{\beta x},\, \cdots,\,x^{k-1}e^{\beta x}\}$.

Si el polinomio característico tiene raíces no reales $(a \pm ib)$, entonces podemos conseguir dos funciones reales linealmente independientes. $\{e^{ax}\cos(bx),\,e^{ax}\sin(bx)\}$

## Solución Particular

Una vez que tenemos las soluciones de la homogénea asociada, es momento de encontrar una solución particular. Para eso, vamos a hacerlo a través del método de coeficientes indeterminados.

Este método consiste en proponer una forma de la función $y_p$ solución para cierto tipo de función $f$, si las raíces del polinomio característico cumplen con las condiciones especificadas.

$$
\def\arraystretch{1.4}\begin{array}{|c|c|c|}\hline
\boldsymbol{f} & \boldsymbol{y_p} & \textbf{Raíces del polinomio caracteristico}
\\\hline
P_n & P_n & r \neq 0
\\\hline
P_n & P_{n+1} & r = 0:\text{Raíz Simple}
\\\hline
P_n & P_{n+k} & r=0:\text{Raiz mult. }k
\\\hline
e^{\lambda x} & ke^{\lambda x} & r \neq \lambda
\\\hline
e^{\lambda x} & P_k e^{\lambda x} & r = \lambda:\text{Raíz mult. } k
\\\hline
\sin(cx) & k_1\sin(cx) + k_2\cos(cx) &  r \neq ci 
\\\hline
\sin(cx) & P_k\sin(cx) + Q_k\cos(cx) & r = ci: \text{Raiz mult. } k 
\\\hline
\cos(cx) & k_1\sin(cx) + k_2\cos(cx) & r \neq ci
\\\hline\end{array}
$$

Si la función $f$ es una suma de las funciones mencionadas, entonces la solución particular es una suma de las soluciones particulares de la ecuación diferencial con cada $f_n$.
