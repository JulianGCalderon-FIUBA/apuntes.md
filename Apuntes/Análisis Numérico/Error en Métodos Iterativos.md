Si existen constantes positivas $\alpha$ y $\lambda$ tal que se cumple la siguiente expresión, entonces podemos decir la convergencia del método es de orden $\alpha$ con constante asintótica $\alpha$

$$
\lim_{n\to\infty} \frac{|p_{n+1} - p |}{{|p_n - p|}^\alpha} = \lambda
$$

# Punto Fijo

El método del punto fijo converge linealmente. Se cumple que

$$
\lim_{n\to\infty} \frac{|p_{n+1} - p |}{|p_n - p|} = |g'(p)|
$$

# Newton-Raphson

Este método converge cuadráticamente únicamente cuando la raíz es simple, si la raíz es multiple, debo realizar una modificación del método para obtener una convergencia cuadrática.

$$
\lim_{n\to\infty} \frac{|p_{n+1} - p |}{|p_n - p|^2} = \frac{|g''(p)|}{2}
$$

Además, para valores suficientemente grandes, se cumple la siguiente expresión, siendo $M$ la cota de $g''(x)$ en el intervalo abierto del teorema.

$$
|p_{n+1} - p| < \frac M2 |p_n - p|^2
$$

Cuando $g'(p) = 0$, tendremos que los métodos convergen cuadráticamente, por lo que el método de newton consiste en multiplicar $f(x)$ por otra función $\phi(x)$, tal que $x -\phi(x)f(x)$ sea un punto máximo en $p$. 

De esta forma, obtenemos el método de **Newton-Raphson** a partir del método de punto fijo. $\phi(x) = 1/f'(x)$. Nótese que esto es solo valido si $f'(p) \neq 0$