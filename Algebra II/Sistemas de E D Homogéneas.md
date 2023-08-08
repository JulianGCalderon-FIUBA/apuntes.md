Vamos a resolver sistemas que se escriban de la siguiente manera

$$
AY  = Y'
$$

Para resolver esto, vamos a encontrar los autovalores y autovectores de la matriz asociada al sistema. Si $v$ es autovector de $A$ de autovalor $\lambda$, entonces $Y(t) = v\cdot e^{\lambda t}$ es solución del sistema.

Todas las soluciones se escribirán como combinación lineal de las soluciones del sistema

$$
\text{gen}\{v_1 e^{\lambda_1t},\ v_2 e^{\lambda_2t},\ \cdots,\ v_n e^{\lambda_nt}\}
$$

Si una matriz tiene autovalores complejos, algunas de las funciones de la base de soluciones de la ecuación serán complejas. Sin embargo, podemos construir una base de soluciones que contenga únicamente funciones reales.

# Autovalores Complejos

Sean $\lambda = a + bi,\ \lambda = a - bi$, autovalores de $A$. En tal caso, $v, \overline v$ serán autovectores de $A$. Representados de la forma $v = w + ir$

Tenemos entonces, dos soluciones del sistema

$$
Y_1(t) = e^{\lambda t}v \qquad Y_2(t) = e^{\overline{\lambda} t} \overline v
$$

$$
Y_1(t) = e^{at}\cdot\Big(\cos(bx) + i\sin(bx)\Big)\cdot(w+ir)
$$

Podemos buscar dos combinaciones lineales reales, de estas dos funciones:

$$
Re(Y_1(t)) = \frac{Y_1 + Y_2}{2} \qquad Im(Y_1(t)) = \frac{Y_1 - Y_2}{2i}
$$

$$
Re(Y_1(t)) = e^{at} \cdot \Big[\cos(bx)w - \sin(bx)r\Big]
$$

$$
Im(Y_1(t)) = e^{at} \cdot \Big[\cos(bx)r + \sin(bx)w\Big]
$$

# Propiedades

**Si el autovalor es real**

Si $\lambda > 0$, tendremos soluciones divergentes

Si $\lambda < 0$, tendremos soluciones que convergen en $0$

Si $\lambda = 0$, La solución sera constante.

**Si el autovalor es complejo**

$a < 0 \to \lim_{y \to \infty} e^{(a+ib)t}v = 0$

$a > 0 \to \lim_{y \to \infty} e^{(a+ib)t}v = \text{No Acotado}$

# Matrices de Jordan

Si una matriz $A \in \Bbb C^{3 \times 3}$ no es diagonalizable, podemos encontrar matrices de jordan similares a una matriz diagonal, tal que $A \sim J_i$

Llamamos $V_1, V_2, V_3$ las columnas de $Q$

## Caso 1

Si $A$ tiene un autovalor de multiplicidad algebraica $2$ y multiplicidad geometrica $1$. Llamamos $\lambda_1$ al autovalor de multiplicidad algebraica $2$, y $\lambda_2$ al autovalor de multiplicidad algebraica $1$.

$$
\text{gen}\{e^{\lambda t}v_1, e^{\lambda t}(v_2+tv_1), e^{\eta t}v_3\}
$$

## Caso 2

Si $A$ tiene un autovalor de multiplicidad algebraica $3$ y multiplicidad geométrica $1$. Llamamos $\lambda$ al único autovalor

$$
\{e^{\lambda t}v_1, e^{\lambda t}(tv_1+v_2), e^{\lambda t}({t^2}/2 \ v_1 + tv_2 + v_3)\}
$$

## Caso 3

Si $A$ tiene un autovalor de multiplicidad algebraica $3$ y multiplicidad geométrica $2$. Llamamos $\lambda$ al único autovalor

$$
\{e^{\lambda t}v_1, e^{\lambda t}(v_2+tv_1), e^{\lambda t}v_3\}
$$