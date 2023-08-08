El enfoque bayesiano consiste en utilizar informacion previa del parametro para realizar una mejor aproximacion. 

A priori, nosotros conoceremos la distribucion $\Theta$ y la distribucion de muestra $X | \Theta = \theta$. A partir de bayes para mezclas, podemos hallar la distribucion de $\Theta | \underline X = \underline x$ (distribucion a posteriori del parametro)

$$
f_{\Theta| \underline X = x}(\theta) = 
\frac
{
f_{\underline X | \Theta = \theta}(\underline x) f_\Theta(\theta)
}{
\int_{-\infty}^{\infty} 
f_{\underline X | \Theta = \theta}(\underline x) f_\Theta(\theta)\,  d\theta
}
$$

Definiremos funcion de perdida $l(\theta, d)$ como el costo de estimar $\theta$ con $d$. Definiremos la perdida de bayes como la perdida esperada.

Definiremos el estimador de Bayes como aquel que minimice la perdida de bayes. Si consideramos la funcion de perdida cuadratica, luego el estimador de Bayes es la media de la funcion a posteriori.

Muchas veces no es necesario evaluar todos los elementos de la ecuacion de Bayes para mezclas. Como sabemos que es una funcion de densidad, podremos simplemente buscar a que distribucion se parece.

$$
f_{\Theta| \underline X = x}(\theta) = 
K \cdot f_{\underline X | \Theta = \theta}(\underline x) f_\Theta(\theta)

$$

# Calculo de Probabilidad

Si buscamos calcular la probabilidad de un evento a partir de la estimacion, utilizaremos la formula de probabilidad total.

$$
P(X_2 = x_2 | \underline X = \underline x) = \int_{-\infty}^\infty f_{X | \Theta = \theta}(x)\cdot f_{\Theta | \underline X = x}(\theta) \cdot d\theta
$$

Esta ecuación sirve para tanto distribuciones continuas como discretas.

$$
P(X_2 \leq a | \underline X = \underline x) = \int_{-\infty}^a\int_{-\infty}^\infty f_{X | \Theta = \theta}(x)\cdot f_{\Theta | \underline X = x}(\theta) \cdot d\theta dx
$$

# MAP

Se deonimina moda a posteriori. En algunos casos a $\theta$ con la moda de la distribucion (punto donde se alcanza el maximo de la densidad)