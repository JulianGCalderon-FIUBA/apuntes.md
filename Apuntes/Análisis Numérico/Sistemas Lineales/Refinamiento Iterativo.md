Sea $\widetilde x$ una aproximacion de la solución $x$ del sistema $Ax = b$, con la propiedad de que la norma del vector residual $r = b - A\widetilde x$ es pequeña, entonces es intuitivo pensar que la norma de $\| x - \widetilde x \|$ tambien lo sera. Esto no es necesariamenet así.

**Teorema:** Supongamos que $\widetilde x$ es una aproximacion a la solucion del sistema $Ax = b$, siendo $A$ una no singular y que $r$ es el vector residual

1. $\|x - \widetilde x\| \leq \|r\|\|A^{-1}\|$
2. $\frac{\|x - \widetilde x\|}{\|x\|} \leq \|A\| \|A^{-1}\|\frac{\|r\|}{\|b\|}$

# Numero de Condicion $K$

Llamamos $K(A)$ al numero de condicion de la matriz $A$, se puede calcular como  $K(A) =\|A\|\|A^{-1}\|$. El numero de condicion de una matriz es siempre mayor a $1$.

Se dice que una matriz esta mal condicionada, si su numero de condicion es significativamente mayor que $1$.

Para aproximar el numero de condicion de una matriz, debo encontrar a la solucion del sistema en el vector residual

$$
Ay = (b - A\widetilde x) \implies x = \widetilde x + \widetilde y 
$$

, puedo utilizar la formula de error residual para aritmetica de $t$ cifras significativas.

$$
\|r\| \approx 10^{-t}\|A\| \|\widetilde x\|
$$

Luego, podemos aproximar el numero de condicion como:

$$
K(A) \approx 10^t \frac{\|\widetilde y\|}{\|\widetilde x\|}
$$

# Refinamiento Iterativo

El refinamiento iterativo consiste en, a cada iteración de un metodo iterativo, sumarle la solucion del sistema para el vector residual.

1. Encontrar aproximación $\widetilde x^{(1)}$, para $Ax = b$
2. Encontar aproximación $\widetilde y^{(1)}$, para $Ay = r$, siendo $r = b-A\widetilde x^{(1)}$
3. Luego encontramos la siguiente aproximacion $\widetilde x^{(2)} = \widetilde x^{(1)} + \widetilde y^{(1)}$
4. Repetir este algoritmo hasta llegar a la cota de error deseada