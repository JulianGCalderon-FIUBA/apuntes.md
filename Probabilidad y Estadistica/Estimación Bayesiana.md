---
title: Estimación Bayesiana
---

El enfoque bayesiano consiste en utilizar información previa del parámetro para realizar una mejor aproximación.

A priori, nosotros conoceremos la distribución $\Theta$ y la distribución de muestra $X | \Theta = \theta$. A partir de Bayes para mezclas, podemos hallar la distribución de $\Theta | \underline X = \underline x$ (distribución a posteriori del parámetro)

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

Definiremos función de perdida $l(\theta, d)$ como el costo de estimar $\theta$ con $d$. Definiremos la perdida de Bayes como la perdida esperada.

Definiremos el estimador de Bayes como aquel que minimice la perdida de Bayes. Si consideramos la función de perdida cuadrática, luego el estimador de Bayes es la media de la función a posteriori.

Muchas veces no es necesario evaluar todos los elementos de la ecuación de Bayes para mezclas. Como sabemos que es una función de densidad, podremos simplemente buscar a qué distribución se parece.

$$
f_{\Theta| \underline X = x}(\theta) = 
K \cdot f_{\underline X | \Theta = \theta}(\underline x) f_\Theta(\theta)

$$

## Cálculo de Probabilidad

Si buscamos calcular la probabilidad de un evento a partir de la estimación, utilizaremos la fórmula de probabilidad total.

$$
P(X_2 = x_2 | \underline X = \underline x) = \int_{-\infty}^\infty f_{X | \Theta = \theta}(x)\cdot f_{\Theta | \underline X = x}(\theta) \cdot d\theta
$$

Esta ecuación sirve para tanto distribuciones continuas como discretas.

$$
P(X_2 \leq a | \underline X = \underline x) = \int_{-\infty}^a\int_{-\infty}^\infty f_{X | \Theta = \theta}(x)\cdot f_{\Theta | \underline X = x}(\theta) \cdot d\theta dx
$$

## MAP

Se denomina moda *a posteriori*. En algunos casos a $\theta$ con la moda de la distribución (punto donde se alcanza el máximo de la densidad)
