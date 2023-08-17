---
title: FFT
---

## DFT

Para una señal periódica cuya función no conocemos, podemos escribir la transformada discreta de Fourier como

$$
X_N(k) = X^{(N)}(k) = \sum_{n=0}^{N-1}x(n) e^{-i \frac{2\pi k n}{N}} \qquad \text{para }k = 0, \cdots, N -1
$$

### Implementación Matricial

Es posible representar la ecuación anterior como un producto matricial, de modo que $X = W_n x$, donde $X, x$ son vectores columna y $W_N$ es una matriz de $N\times N$

Llamamos entonces $W_N^{kn} = e^{-i\frac{2\pi kn}{N}}$ al elemento $(k,n)$ de la matriz $W_N$

$$
\begin{pmatrix}
X(0)\\
\vdots\\
X(N-1)
\end{pmatrix}
=
\begin{pmatrix}
W_N^{1\cdot1} & \cdots & W_N^{1\cdot(N-1)}\\
\vdots & \ddots & \vdots\\
W_N^{(N-1)\cdot1} & \cdots & W_N^{(N-1)\cdot(N-1)}
\end{pmatrix}

\begin{pmatrix}
x(0)\\
\vdots\\
x(N-1)
\end{pmatrix}
$$

Para calcular la matriz. Nos ayudamos de las siguientes propiedades:

$$
W_N^{k+N} = W_{N}^k
$$

$$
W_N^{k+N/2} = -W_{N}^k
$$

## FFT

La transformada rápida de Fourier es un método mucho más rápido para calcular la DFT, su velocidad proviene de la utilización de resultados previos para el cálculo de la misma

Para implementarlo, descomponemos una $DFT$ como la suma de dos $NFT$ de la mitad de puntos, lo que reduce la complejidad numérica a casi la mitad. Separamos los puntos impares de los puntos pares.

Definimos $x_0, x_1$ como

$$
x_0 = x(2m)
$$

$$
x_1 = x(2m+1)
$$

$$
X^{(n)}(k) = X_0^{(N/2)} + e^{-i2\pi k/ N} X_1^{(N/2)}(k)  \qquad \text{para }k = 0, \cdots, N -1
$$

Podemos simplificar aún más esta expresión, ya que $X_0, X_1$ son periódicas cada $N/2$, por lo que obtenemos que

$$
X^{(N)}(k) = X_0^{(N/2)}(k) + W_{N}^kX_1^{(N/2)}(k)
$$

$$
X^{(N)}(k + N/2) = X_0^{(N/2)}(k) - W_{N}^kX_1^{(N/2)}(k)
$$

Para $k=0, \cdots, \frac N2 - 1$
