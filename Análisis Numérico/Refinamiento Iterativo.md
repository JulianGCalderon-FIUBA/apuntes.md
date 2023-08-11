Sea $\widetilde x$ una aproximación de la solución $x$ del sistema $Ax = b$, con la propiedad de que la norma del vector residual $r = b - A\widetilde x$ es pequeña, entonces es intuitivo pensar que la norma de $\| x - \widetilde x \|$ también lo será. Esto no es necesariamente así.

**Teorema:** Supongamos que $\widetilde x$ es una aproximación a la solución del sistema $Ax = b$, siendo $A$ una no singular y que $r$ es el vector residual

1. $\|x - \widetilde x\| \leq \|r\|\|A^{-1}\|$
2. $\frac{\|x - \widetilde x\|}{\|x\|} \leq \|A\| \|A^{-1}\|\frac{\|r\|}{\|b\|}$

## Número de Condición $K$

Llamamos $K(A)$ al número de condición de la matriz $A$, se puede calcular como $K(A) =\|A\|\|A^{-1}\|$. El número de condición de una matriz es siempre mayor a $1$.

Se dice que una matriz está mal condicionada, si su número de condición es significativamente mayor que $1$.

Para aproximar el número de condición de una matriz, debo encontrar a la solución del sistema en el vector residual

$$
Ay = (b - A\widetilde x) \implies x = \widetilde x + \widetilde y 
$$

Puedo utilizar la fórmula de error residual para aritmética de $t$ cifras significativas.

$$
\|r\| \approx 10^{-t}\|A\| \|\widetilde x\|
$$

Luego, podemos aproximar el número de condición como:

$$
K(A) \approx 10^t \frac{\|\widetilde y\|}{\|\widetilde x\|}
$$

## Refinamiento Iterativo

El refinamiento iterativo consiste en, a cada iteración de un método iterativo, sumarle la solución del sistema para el vector residual.

1. Encontramops aproximación $\widetilde x^{(1)}$, para $Ax = b$
2. Encontrar la  aproximación $\widetilde y^{(1)}$, para $Ay = r$, siendo $r = b-A\widetilde x^{(1)}$
3. Luego encontramos la siguiente aproximación $\widetilde x^{(2)} = \widetilde x^{(1)} + \widetilde y^{(1)}$
4. Repetir este algoritmo hasta llegar a la cota de error deseada
