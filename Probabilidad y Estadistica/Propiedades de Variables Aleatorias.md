## Suma de Distribuciones Poisson

Sean $X,Y$ dos distribuciones independientes Poisson de parámetro $\mu,\lambda$. Entonces si definimos la variable aleatoria $W = X+Y$. Podremos ver que la distribución de $W$ sera una Poisson de parámetro $\mu + \lambda$.

## Método del Jacobiano

Sean $Y_1, Y_2$ dos V.A.C tal que para todo $y_1, y_2$ se cumple que $f_{Y_1, Y_2}(y_1, y_2) > 0$, entonces $u_1 = h_1(y_1, y_2)$ y $u_2 = h_2(y_1, y_2)$ Es una transformación $1$ a $1$ de $Y$ a $U$ con inversa $y_1 = h_1^{-1}(u_1, u_2), y_2 = h_2^{-1}(u_1, u_2)$.

Si las inversas tienen derivadas parciales continuas respecto a $u_1, u_2$ con jacobiano $J$, entonces se cumple que

$$
f_{U_1, U_2}(u_1, u_2) =\frac{f_{Y_1, Y_2}(y_1, y_2)}{|J|} \Bigg |_{h_1^{-1}, h_2^{-1}}
$$

## Método del Jacobiano Generalizado

$Si X$ es un vector aleatorio, e $Y = g(X)$. Con $g$ tal que $g | A_i = g_i$ es biyectiva, continua, con derivada continua, donde $A_i \dots A_k$ es una particion del soporte de $X$, entonces

$$
f_Y(y) = \sum_{i=1}^k \frac{f_X(x) \ \mathbf{1}\{x \in A_i\}}{|J_{g_i}(x)|}\Bigg|_{x = g^{-1}_i(y)}
$$

> [!note]
> Si no podemos aplicar el método del jacobiana, tendremos que usar el método de eventos equivalentes.
