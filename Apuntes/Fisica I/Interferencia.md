Ocurre cuando tomas dos ondas armónicas de la misma *frecuencia*, misma *longitud*, pero con diferente *fase.* Cada onda recorre caminos distintos $x_1, x_2$. 

Estas ondas se denominan **coherentes** porque su diferencia de fase es constante en el tiempo. Si no trabajamos con fuentes coherentes, entonces el factor de interferencia se anula.

$$
\xi_1(x,t) = A_1\sin(kx_1-wt+\varphi_1)
$$

$$
\xi_2(x,t) = A_2\sin(kx_2-wt+\varphi_2)
$$

Si asumimos que ambas ondas tienen la misma amplitud, llegamos a la ecuación de onda de interferencia.

$$
\boxed{\xi(x,t) = 2A
\cdot
\cos\bigg[kx_p - wt +\varphi_p\bigg]
\cdot
\cos\bigg[\frac{k\cdot\Delta x}{2}+\frac{\Delta\varphi}{2}\bigg]}
$$

**Interferencia Constructiva:** Ocurre cuando las dos ondas se complementan y la amplitud de la onda resultante es maxima

**Interferencia Destructiva:** Ocurre cuando las dos ondas se anulan y la amplitud de la onda resultante es nula.

# Experiencia de Young

Las fuentes $S_1,\,S_2$ son puntuales y monocromáticas. al provenir de la misma fuente, asumimos que $\Delta \varphi = 0$

![[Apuntes/Fisica I/Attachments/Interferencia 1.png|Interferencia%204de3b4bba5014045a549249d7f66e2be/Untitled.png]]

$$
\Delta x = \Delta r = d\sin\theta
$$

$$
\delta = k\cdot\Delta x+\Delta\varphi
$$

$$
\theta\ll\sin\theta\approx\tan\theta=\frac yD
$$

## Interferencia Constructiva

$$
\cos(\delta/2) = 1
$$

$$
\frac{2\pi\cdot d\cdot\sin\theta}{2\lambda} = n\cdot\pi
$$

$$
\sin\theta = n\cdot\frac{\lambda}{d}
$$

$$
\boxed{y_{max} = n\cdot\frac{\lambda\cdot D}d}
$$

$n = \pm0,1,2,\cdots$

## Interferencia Destructiva

$$
\cos(\delta/2) = 0
$$

$$
\frac{2\pi\cdot d\cdot\sin\theta}{2\lambda} = (2n+1)\cdot\frac\pi2
$$

$$
\sin\theta = \frac{(2n+1)}{2}\cdot\frac{\lambda}{d}
$$

$$
\boxed{y_{min} = \frac{2n-1}2\cdot\frac{\lambda\cdot D}d}
$$

$n = \pm1,2,3\cdots$

# Diagrama Fasorial

Le asignamos a cada onda un fasor, y calculamos la suma de las ondas para llegar a la onda resultante.

![[Apuntes/Fisica I/Attachments/Interferencia 2.png|Interferencia%204de3b4bba5014045a549249d7f66e2be/Untitled%201.png]]

![[Apuntes/Fisica I/Attachments/Interferencia 3.png|Interferencia%204de3b4bba5014045a549249d7f66e2be/Untitled%202.png]]

$$
\xi_0 = \xi_{01} + \xi_{02}\\
A^2 = (A_1 + A_2)^2

$$

La intensidad de una onda es proporcional a su amplitud al cuadrado. $I \propto A^2$

$$
I = I_1 + I_2 + 2\sqrt{I_1\cdot I_2}\cdot\cos\delta
$$

Suponemos que ambas ondas tienen la misma amplitud

$$
I = 2I_0\cdot (1 + \cos\delta)
$$

Si aplicamos las siguientes identidades trigonométricas

$$
\begin{align*}&\cos\beta = \cos\bigg(\frac\delta2 + \frac\delta2\bigg) = \cos^2\bigg(\frac\delta2\bigg) - \sin^2\bigg(\frac\delta2\bigg)
\\
&\sin^2\bigg(\frac\delta2\bigg) = 1-cos^2\bigg(\frac\delta2\bigg)\end{align*}
$$

Llegamos a las siguientes expresiones

$$
\boxed{I = 4I_0\cdot \cos^2\bigg(\frac\delta2\bigg)}
$$

$$
⟨I⟩ = 2I_0
$$

# Interferencia en $N$ rendijas

Por el método fasorial, podemos deducir que los puntos de interferencia críticos.

A medida que aumenta $N$, el ancho angular del pico principal disminuye y los máximos secundarios se vuelve cada vez mas chicos. La cantidad de máximos relativos que hay entre los máximos principales es de $[N-2]$

## Máximos Principales

Los máximos principales se encuentran cuando no hay variación de ángulo entre los fasores $:\cos(\delta/2) = 1$

$$
\delta = n\cdot2\pi
$$

$$
\boxed{y_{max} = n\cdot\frac{\lambda\cdot D}d}
$$

## Mínimos

En este tipo de interferencia, la cantidad de ceros en un intervalo de $2\pi$ es de $[N-1]$.

$n$ no es múltiplo de $N$

$$
\delta =2\pi\cdot \frac nN
$$

$$
\boxed{y_{min} = \frac nN\cdot\frac{\lambda\cdot D}d}
$$

## Amplitud

La amplitud inicial de la onda resultante por la suma de las $N$ ondas esta dada por la siguiente formula:

$$
A = A_0\frac{\sin\Big(\frac{N\cdot k\cdot\Delta x}2\Big)}
{\sin\Big(\frac{ k\cdot\Delta x}2\Big)}
$$

## Intensidad

La intensidad de cada punto, para la interferencia de $N$ rendijas esta dada por la siguiente formula:

$$
I = I_0\frac{\sin^2\Big(\frac{N\cdot k\cdot\Delta x}2\Big)}{\sin^2\Big(\frac{k\cdot\Delta x}2\Big)}
$$