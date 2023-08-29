## Observaciones

1. Las series de Fourier describen señales periódicas como combinación lineal de señales armónicas (senos y cosenos)
2. Con esta herramienta, analizamos señales periódicas en términos de su contenido frecuencial o espectro.
3. Nos permite establecer la dualidad entre tiempo y frecuencia, de forma que operaciones realizadas en el dominio temporal tienen su dual en el dominio frecuencial.

Recordamos la relación entre frecuencia y período:

$$
f = 1/T
$$

Normalmente, hablamos de frecuencia angular

$$
w = 2\pi f
$$

## Teorema de Fourier

Este teorema garantiza que una función periódica que satisface ciertas condiciones de continuidad puede ser expresada como suma de un número infinito de funciones senoidales y de diferentes amplitudes, fases, y periodos.

$$
f(t) = A_0 + \sum A_i \sin(i\omega t + \varphi_i)
$$

Podemos reescribir los términos a partir del teorema de la suma, de la siguiente forma. Donde $a_0 = 2A_0$

$$
\boxed{f(t) = \frac{a_0}2 + \sum a_n \cos(n\omega t) + \sum b_n \sin(n\omega t)}
$$

Esta forma se conoce como el nombre de **Expansión en Serie de Fourier.**

Si definimos la base ortogonal del espacio de funciones periódicas como:

$$
B = \{1, \cos(\omega t), \cos(2\omega t), \cdots, \cos(n\omega t), \sin(\omega t), \sin(2\omega t), \cdots, \sin(n\omega t)\}
$$

Para obtener los **coeficientes**, proyectamos la función sobre esta base

$$
a_n = \frac{2}{T} \int_d^{d+T} f(t) \cos (n\omega t) dt \qquad n=0, 1, 2, \cdots
$$

$$
b_n = \frac{2}{T} \int_d^{d+T} f(t) \cos (n\omega t) dt \qquad n=1, 2, \cdots
$$

## Forma Compleja de la Serie de Fourier

Podemos usar la forma exponencial de los números complejos para encontrar las siguientes equivalencias

$$
\begin{cases}

\sin(nwt) = \Large\frac{e^{in\omega t} - e^{-in\omega t}}{2i}\normalsize

\\\ \\

\cos(nwt) = \Large\frac{e^{in\omega t} + e^{-in\omega t}}{2}\normalsize

\end{cases}
$$

Remplazando en la serie de Fourier, y definiendo $c_{-n}$ como $c^*_n$, y que $c_0 = \frac{a_0}{2}$. Llegamos a la siguiente expresión

$$
f(t) = c_0 +\sum c_n e^{in\omega t} + \sum c_{-n} e^{-in\omega t}
$$

Podemos juntar ambas sumas en una sola integral, desde infinito negativo hasta infinito

$$
\boxed{f(t) = \sum_{n=-\infty}^\infty c_n e^{in\omega t}}
$$

Análogamente, como en el caso anterior, los **coeficientes** se encuentran a partir de la siguiente integral

$$
c_n = \frac{1}{T} \int_d^{d+T} f(t) e^{-in\omega t}dt \qquad n=0, \pm1, \pm2, \cdots
$$

## Teorema de Dirichlet

Si $f(t)$ es una función periódica que en cualquier periodo tiene:

- Un número finito de máximos y mínimos aislados
- Un número finito de puntos de discontinuidad finita

Entonces la expansión en serie de Fourier de $f(t)$ converge a $f(t)$ donde $f$ es continua y al promedio de los límites por derecha y por izquierda donde $f$ es discontinua.
