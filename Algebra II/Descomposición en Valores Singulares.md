A partir de la descomposición en valores singulares (D.V.S), podemos encontrar que toda matriz puede ser factorizada de forma que quede de forma explicita los subespacios fundamentales de la matriz.

**Recordamos:**

- $A^* A = \overline A^T A \implies$Es una matriz hermítica, semi definida positiva.
- $\text{Nul}(A^* A) = \text{Nul}(A) = \text{Rg}(A)$
- Para toda matriz hermítica, se cumple que:
	- Todos sus autovalores son reales.
	- Los autovectores son ortogonales.
	- Es siempre diagonalizable.
- Si además es semi definida positiva, no tiene autovalores negativos.
- Sea $\text{Rg}(A^* A) = k$, los primeros $k$ autovalores son estrictamente positivos, mientras que el resto valen cero. (los autovalores se ordenan de mayor a menor)

## Valor Singular

Se dice que $\sigma$ es un valor singular de $A$ si $\sigma = \sqrt \lambda$, con $\lambda$ autovalor de $A^* A$.

Por observaciones anteriores, si $\text{Rg}(A) = k$, los primeros $k$ autovalores (y valores singulares) son estrictamente positivos, mientras que el resto valen cero.

$$
\|Av_i\| = \sqrt \lambda_i = \sigma_i
$$

Los valores singulares de una matriz no dicen cuanto cambia la norma de los autovectores de $A^* A$ al ser multiplicados por $A$

> [!note]
> Los autovectores de $A^*A$ deben ser ortonormales

## Subespacios Fundamentales

Sea $\Lambda$ el conjunto de autovalores asociados a la matriz $A^*A$, entonces podemos encontrar los subespacios asociados a la matriz $A$.

$$
\Lambda = \Big\{\underbrace{\lambda_1,\, \lambda_2,\, \cdots,\, \lambda_k}_\text{Autovalores Positivos},\ \underbrace{\lambda{_k+1},\  \cdots,\ \lambda_n}_\text{Autovalores Nulos}\Big\}
$$

Podemos a partir de este conjunto, definir el subespacio columna, fila, y nulo de $A$. Todos estos conjuntos son ortonormales.

$$
\text{Col}(A) = \Big\{ \frac{Av_1}{\sigma_1},\ \frac{Av_2}{\sigma_2},\ \cdots,\ \frac{Av_k}{\sigma_k}\Big\}
$$

$$
\text{Fil}(A) = \Big\{v_1,\ v_2,\ \cdots ,\ v_k\Big\}
$$

$$
\text{Nul}(A) = \Big\{v_{k+1},\ \cdots ,\ v_n\Big\}
$$

$$
\text{Nul}(A^T) = \Big\{ \frac{Av_{k+1}}{\sigma_{k+1}},\ \frac{Av_{k+2}}{\sigma_{k+2}},\ \cdots,\ \frac{Av_n}{\sigma_n}\Big\}
$$

## Descomposición en V.S.

Sea $A$ una matriz $\Bbb C^{m \times n}$, Puedo factorizarla de la forma

$$
A = U \Sigma V^*
$$

$$
A = AVV^* \implies AV = U\Sigma
$$

$$
D_k= \begin{bmatrix}\sigma_1 & 0 & \cdots & 0 \\
0 & \sigma_2 &\cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \sigma_k
\end{bmatrix}

$$

$$
\Sigma = \begin{bmatrix}D_k & 0_{k\times(n{-}k)} \\ 0_{(m{-}k)\times k} & 0_{(m{-}k)\times(m{-}k)}\end{bmatrix}
$$

> [!note]
> Los valores singulares entre $[k{+}1: n]$ valen $0$

Siendo $U$, $V$, matrices unitarias e $\Bbb C^{m \times m}$ y $\Bbb C^{n \times n}$ respectivamente.

$$
U = \Big[|u_1|, \ |u_2|,\ \cdots ,\ |u_k|\Big] \\u_i = \frac{Av_i}{\sigma_i}
$$

$$
V = \Big[|v_1|, \ |v_2|,\ \cdots ,\ |v_n|\Big]
$$

Si el rango de la matriz es menor a $m$, entonces las columnas restantes de $U$ se deben calcular a mano, teniendo en cuenta que debe ser un conjunto ortonormal.

## D.V.S Reducida

Si $A\in\Bbb C^{m \times n}$ y $\text{Rg(A)} = k$. Podemos escribir la D.V.S. de $A$ como

$$
A = 
\begin{bmatrix}
|U_k| & |U_{n{-}k}|
\end{bmatrix}
\begin{bmatrix}D_k & 0_{k\times(n{-}k)} \\ 0_{(m{-}k)\times k} & 0_{(m{-}k)\times(n{-}k)}\end{bmatrix}
\begin{bmatrix}
V_k^* \\
\hline
V_{m{-}k}^*
\end{bmatrix}
$$

Por lo que su forma reducida, se vera de la siguiente manera:

$$
A = U_k D_k V_k^*
$$

## Pseudo-inversa de Moore-penrose

Se le llama así a la matriz $A^\dagger = V_K D_K^{-1} U_K^*$. Se define para toda matriz de $m \times n$.

Si la matriz $A$ es de rango máximo, entonces coincide con la matriz pseudo-inversa definida anteriormente. $A^\dagger = A^\# \impliedby \text{Rg}(A) = m$

**Propiedades:**

- $A A^\dagger = P_{\text{Col}(A)}$
- $A^\dagger A = P_{\text{Fil}(A)}$

Si quiero resolver el sistema $Ax = b$ por cuadrados mínimos, entonces busco $x^\dagger$ tal que $x^\dagger = A^\dagger b$

Luego puedo sumarle cualquier vector del subespacio nulo a la solución para encontrar todas las soluciones. Además. $x^\dagger$ pertenece al subespacio fila de $A$, por lo que podemos asegurar que su norma es minima. (esto se debe a que $U_k$ esta compuesta por $\text{Fil}(A)$, por lo que el vector resultante también pertenece a este.
