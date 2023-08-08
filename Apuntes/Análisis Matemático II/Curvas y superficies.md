Una curva es la imagen de una función vectorial $\vec f(t)$ continua en A, donde A es un intervalo de la recta real

![[Apuntes/Análisis Matemático II/Attachments/Curvas y superficies 1.png|$\displaystyle x^3 + y^3 - 3xy = 0$]]

$\displaystyle x^3 + y^3 - 3xy = 0$

$$
\boxed {\vec X(t) = \Big(\frac{3\cos^2t\cdot\sin t}{\cos^3 + sen^3},\frac{3\cos t\cdot\sin^2t}{\cos^3 + sen^3}\Big)}
$$

# Curva plana

Esta totalmente contenida en un plano

# Curva cerrada simple

Tambien llamadas *curvas de Jordan, solo tienen en común el punto inicial y el final*

# Tangente a la curva (Regular)

Si existe la derivada en un punto, se puede construir una recta tangente en ese punto. Si se puede derivar en todo el dominio, entonces la curva es regular.

Si se cambia la parametrización de una curva, pueden cambiar las propiedades de su parametrización (tener derivada en un punto que antes no tenia)

Se dice que es **regular a trozos** si deja de ser regular en un numero finito de puntos del intervalo $[a,b]$

# Plano normal a la curva

El plano perpendicular a la tangente de la curva y que contiene el punto de la misma

$$
\Pi: \Big[(x,y,z) -\vec f(x_0)\Big]\cdot \vec f'(x_0) = 0 \\\vec f'(x_0) = N_\pi\quad\vec f(x_0) = P
$$

# Superficies

Una superficie es la imagen de una función vectorial $\vec f(x,y):\mathbb{R}^2 \to \mathbb{R}$. continua en $A \subset \mathbb{R}^2$

Si dejo constante una de las variables y vario la otra, se genera una *curva coordenada*

$$
g(x):\mathbb{R} \to \mathbb{R} \quad h(y):\mathbb{R} \to \mathbb{R} 
$$

El producto vectorial de los vectores tangentes de 2 curvas coordenadas en un punto en común, te da un vector normal a la superficie

Con el vector normal a la superficie y el punto, puedo encontrar el plano tangente a la superficie

![[Apuntes/Análisis Matemático II/Attachments/Curvas y superficies 2.png|Curvas%20y%20superficies%20154986f6fd1d4db9973f7e4b5cd92fa1/Untitled%201.png]]

Una superficie es normal si en cada punto de la superficie, se puede encontrar un plano normal a la misma.

## Vector normal a la superficie:

$$
\sigma'_u(u,v)\times\sigma'_v(u,v) = \begin{vmatrix}\hat i & \hat j & \hat k\\x'_u & y'_u & z'_u \\ x'_v & y'_v & z'_v\end{vmatrix}
$$