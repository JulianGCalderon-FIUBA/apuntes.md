Si queremos encontrar la función potencial, y no pensarla solo como una diferencia entre dos puntos, entonces tengo que encontrar un valor de referencia. Como cuando calculamos la fuerza potencial gravitatoria, que depende de un valor de referencia.

## Distribuciones Acotadas

En el caso de distribuciones acotadas, podemos analizar el potencial en el infinito. Esto hará que tienda a 0.

A este método se le llama: *integración directa.*

$$
\Delta V^{\infty A} = V(A) - \underbrace{V(\infty)}_{\to 0} = V(A) = -\int \frac{dq'}{4\pi\epsilon_0}\Bigg[\frac{1}{|\vec r_A - \vec r'|} - \frac{1}{\infty}\Bigg]
$$

$$
V(A) = -\int\frac{dq'}{4\pi\epsilon_0}\cdot\frac{1}{\vec r_A - \vec r'}
$$

## Distribuciones no Acotadas

En el caso de distribuciones no acotadas, nuestra integral no está definida. Por lo que no podemos usar esta definición. Sin embargo, podemos elegir un punto arbitrario $P$ y forzarlo a valer $0$

$$
\Delta V^{PA} = V(A) - \underbrace{V(P)}_0 = V(A) =-\int_A^P \vec E d\vec l
$$

De esta forma, si resuelvo esta integral, encuentro la función potencial.
