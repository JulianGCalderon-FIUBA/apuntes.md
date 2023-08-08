Si $\Bbb V$ es un $\Bbb K$ espacio vectorial, entonces se dice que $S \subset \Bbb V$ es un subespacio de $\Bbb V$ si se cumplen las siguientes propiedades $(S \neq \emptyset)$

- $\Bbb O_{\Bbb V} \in S$
- Si $u,v\in S$, se cumple $u + v \in S$. Cerrado para la suma
- Si $u\in S$, $\lambda \in \Bbb K$, se cumple $\lambda u \in S$. Cerrado para producto por escalar

Al estar incluido en un espacio vectorial $\Bbb V$, se cumplen las mismas propiedades.

Un subespacio se puede anotar como el conjunto de todas las combinaciones lineales entre $n$vectores $v_i$, $S =gen(v_1, v_2, \cdots, v_n)$. El conjunto generador de $S$ no es único

Todos los elementos del subespacio se pueden formar como combinación lineal de los elementos del generador de $S$.

$$
\forall w \in S, w = \sum_{i = 1}^n \lambda_iv_i
$$

**¿Como pruebo que dos conjuntos generan el mismo subespacio?**

Se debe demostrar la doble inclusion, es decir, se deben poder formar los elementos del generador de $S_1$ a partir de los elementos de $S_2$ y viceversa. $S \subseteq T, T\subseteq S$

**¿Como demuestro que dos conjuntos generan un espacio vectorial?**

Para esto, tengo que buscar la expresión mas general del espacio vectorial, y verificar que el sistema sea compatible para todos los casos

# Independencia Lineal

Se dice que un generador es linealmente independiente si ninguno de sus componentes se puede formar como combinación lineal del resto de componentes.

**Equivalencia:** Es linealmente independiente si la solución para formar el elemento neutro es única, es decir con todos los escalares nulos.

$$
\sum_{i = 1}^n \lambda_iv_i = 0 \implies \lambda_i = 0\,\forall\,i
$$

Se dice que un generador es una **base** si  es linealmente independiente. Todas las bases de $S$ tienen la misma cantidad de elementos**.** A **l**a cantidad de elementos de la base de se le llama dimension de $S$.

El subespacio nulo $\{\Bbb O_{\Bbb V}\}$ tiene dimension 0, no tiene base.

Si dos subespacios $S,T$ tienen la misma dimension, solo es necesario demostrar que $S\subseteq T$ para concluir que son equivalentes. 

## Independencia Lineal de Funciones en $C^n$

Para demostrar que son linealmente independientes, igualamos una combinación lineal al elemento neutro, y recordando la propiedad de las derivadas, podemos derivar la ecuación respecto a la variable independiente cuantas veces nos permita el conjunto. ($n-1$) veces.

Se le llama Wronskiano al determinante de la matriz de funciones.

$$
\begin{pmatrix}
\phi_1(x) &\phi_2(x) & \cdots & \phi_m(x)\\
\phi_1'(x) &\phi_2'(x) & \cdots & \phi_m'(x)\\
\vdots & \vdots & \vdots & \vdots\\
\phi_1^{(n-1)} &\phi_2^{(n-1)} &\cdots &\phi_m^{(n-1)}
\end{pmatrix}

\times

\begin{pmatrix}
\lambda_1\\
\lambda_2\\
\vdots\\
\lambda_n\\
\end{pmatrix}

=

\begin{pmatrix}
0\\
0\\
\vdots\\
0\\
\end{pmatrix}
$$

**Teorema del Wronskiano:**

Si para algún $x_0 \in I$ se cumple que el Wronskiano $≠$ de 0, entonces el conjunto de funciones es linealmente independiente.

(El reciproco del teorema no es verdadero)