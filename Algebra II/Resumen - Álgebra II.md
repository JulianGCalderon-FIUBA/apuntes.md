## Matriz de Cambio de Base

Se le llama $M_B^{B’}$ a la matriz de cambio de base de $B$ a $B’$. Si multiplico la matriz por una coordenada en la base $B$, me devuelve la misma coordenada en la base $B’$

Si $B = \text{gen}(v_1, v_2, v_n)$. Entonces podemos encontrar fácilmente:

$$
M_B^e = \begin{bmatrix}
v_1 | v_2 | \cdots | v_n
\end{bmatrix} = (M_e^B)^{-1}
$$

Tambien se puede encontrar cualquier matriz de cambio de base de $B$ en $B’$ de la forma

$$
M_B^{B'} = M_e^{B'}M_B^e
$$

## Subespacios Fundamentales de Una Matriz

- $\text{Col}(A)$. Generador por las columnas de $A$, Representa la imagen de la transformación lineal definida por $A$
- $\text{Fil}(A)$. Generado por las filas de $A$, Representa el dominio que no pertenece al nulo de la transformación lineal definido por $A$
- $\text{Nul}(A).$ Formado por los elementos del dominio que, pasados por la transformación lineal, se vuelven nulos. Es ortogonal al subespacio fila.

**Propiedades:**

- $\text{Dim}(\text{Col}(A)) = \text{Dim}(\text{Fil}(A)) = \text{Rg}(A)$
- $\text{Rg}(A) + \text{Dim}(\text{Nul}(A)) = n$
- Si $\text{Nul}(B) \subseteq \text{Nul}(AB)$ y $\text{Col}(B) \cap \text{Nul}(A) = \{{0_{\Bbb K^n}}\}$, entonces $\text{Nul}(B) = \text{Nul}(AB)$
- Si $\text{Col}(AB) \subseteq \text{Col}(A)$ y $\text{Rg}(B) = n$, entonces $\text{Col}(AB) = \text{Col}(A)$

## Operaciones entre Subespacios

- **Intersección:** Contiene los elementos del espacio que pertenecen a ambos subespacios. Es el subespacio más grande incluido en ambos conjuntos
- **Union:** La union no genera otro subespacio
- **Suma:** Genera otro subespacio, el más chico que incluye ambos conjuntos. Se calcula combinando los generadores de ambos subespacios. Si los subespacios no tienen intersección, entonces se denomina suma directa
- **Suplemento:** Se define suplemento como el subespacio que en suma directa con el original, forman el espacio vectorial.

## Transformaciones Lineales

Las transformaciones lineales se pueden clasificar de la siguiente forma:

- **Monomorfismo**: Si es una transformación lineal **inyectiva** $:\text{Null}(A) = \{0\}$
- **Epimorfismo**: Si es una transformación lineal **suryectiva** $: Im(F) = Cod(F) = \Bbb W$
- **Isomorfismo:** Si es una transformación lineal **biyectiva** (inyectiva y suryectiva)

Una forma rápida de calcular una transformación lineal es a partir del cambio de base

$$
[T]_E^E = [M]_{B'}^E \cdot[T]_B^{B'} \cdot [M]_E^B
$$

## Ecuaciones Diferenciales Ordinarias

$$
L(y)=y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1 y' + a_0y = f
$$

Para encontrar soluciones a estas ecuaciones, planteamos el polinomio característico para encontrar la solución general y después usamos la tabla para encontrar una solución particular

Si el polinomio característico tiene raíces no reales $(a \pm ib)$, entonces podemos conseguir dos funciones reales linealmente independientes. $\{e^{ax}\cos(bx),\,e^{ax}\sin(bx)\}$

$$
\def\arraystretch{1.4}\begin{array}{|c|c|c|}\hline
\boldsymbol{f} & \boldsymbol{y_p} & \textbf{Raíces del polinomio caracteristico}
\\\hline
P_n & P_n & r \neq 0
\\\hline
P_n & P_{n+1} & r = 0:\text{Raíz Simple}
\\\hline
P_n & P_{n+k} & r=0:\text{Raiz mult. }k
\\\hline
e^{\lambda x} & ke^{\lambda x} & r \neq \lambda
\\\hline
e^{\lambda x} & P_k e^{\lambda x} & r = \lambda:\text{Raíz mult. } k
\\\hline
\sin(cx) & k_1\sin(cx) + k_2\cos(cx) &  r \neq ci 
\\\hline
\sin(cx) & P_k\sin(cx) + Q_k\cos(cx) & r = ci: \text{Raiz mult. } k 
\\\hline
\cos(cx) & k_1\sin(cx) + k_2\cos(cx) & r \neq ci
\\\hline\end{array}
$$

## Producto Interno

El producto interno es una operación que cumple con las siguientes propiedades

- $\langle \alpha u + \beta v, w\rangle = \alpha \langle u, w\rangle + \beta \langle v, w\rangle
\impliedby \forall u,v,w \in \Bbb V \ \land\  \forall \alpha, \beta \in \Bbb K$
- $\langle u,v\rangle = \overline{\langle v,u\rangle } \impliedby \forall u,v \in V$
- $\langle u,u\rangle > 0 \iff u \in \Bbb V \neq 0_V$
- $\langle u,u\rangle = 0 \iff u \in \Bbb V = 0_V$

### Nociones del PI

**Norma:** (inducida por el producto interno)

$$
\|u\| = \sqrt{\langle u,u\rangle}
$$

**Distancia:** Sean $u,v \in \Bbb V$, definimos la distancia entre $u,v$ como

$$
d(u,v) = \|u - v\| = \|v - u\|
$$

**Ortogonalidad:** Sean $u, v \in \Bbb V$, se dice que son ortogonales si

$$
\langle u,v \rangle = 0 \iff u \perp v
$$

**Ángulo entre** $u, v$:

$$
\cos(\theta) = \frac{\langle u,v \rangle}{\|u\| \|v\|} \impliedby \theta \in [0, \pi]
$$

**Area de un triangulo**

Sea $\triangle$ un triangulo de vértices $(0, e_1, e_2)$, entonces el area de este triangulo se calcula con la siguiente fórmula

$$
A(\triangle) = \frac 12 \cdot \sqrt{\|e_1\|^2\|e_2\|^2 - \langle e_1, e_2\rangle^2}
$$

**Area de un paralelogramo**

Se puede dividir el paralelogramo en dos triángulos y usar la formula anterior para encontrar su area.

$$
A(\triangle) = \sqrt{\|e_1\|^2\|e_2\|^2 - \langle e_1, e_2\rangle^2}
$$

### Base del PI

Sea $B = \{v_1,...,v_n\}$ Entonces podemos definir el producto interno en todo el espacio a partir de los generadores de la base de la siguiente manera.

$$
\langle x, y\rangle = [x_1,x_2,...,x_n]
\begin{bmatrix}
\langle v_1, v_1\rangle & \langle v_1, v_2\rangle & \cdots &  \langle v_1, v_n\rangle \\  \langle v_2, v_1\rangle &  \langle v_2, v_2\rangle & \cdots &  \langle v_2, v_n\rangle \\ \vdots & \vdots & \ddots & \vdots \\  \langle v_n, v_1\rangle &  \langle v_n, v_2\rangle & \cdots &  \langle v_n, v_n\rangle
\end{bmatrix}
\begin{bmatrix}\overline{y_1} \\ \overline{y_2} \\ \vdots \\ \overline{y_n}\end{bmatrix}
$$

La matriz del producto interno $G_b$ es hermetica y definida positiva.

## Proyección Ortogonal

La proyección ortogonal de $v$ sobre $S$ es el punto de $S$ mas cercano a $v$.

$$
P_S(v) = v'
$$

$$
v = P_S(v) + P_{S^\perp}(v)
$$

Podemos definir una matriz se la proyección ortogonal sobre un subespacio a partir del producto interno definido.

$$
P_S(v) = \frac{\langle v, v_1\rangle} {\|v_1\|^2} v_1 + \frac{\langle v, v_2\rangle} {\|v_2\|^2} v_2 + \cdots + \frac{\langle v, v_k\rangle} {\|v_k\|^2} v_k
$$

$$
P_S(v) = \begin{bmatrix}
\frac{v_1}{\|v_1\|}  & \frac{v_2}{\|v_2\|} & \cdots & \frac{v_k}{\|v_k\|} 
\end{bmatrix} \cdot
\begin{pmatrix}
\frac{\overline{v_1}^T}{\|v_1\|} \\[1em]
\frac{\overline{v_2}^T}{\|v_2\|} \\[1em]
\vdots \\[1em]
\frac{\overline{v_k}^T}{\|v_k\|}
\end{pmatrix} \cdot v
$$

## Cuadrados Mínimos

Si queremos resolver el sistema $Ax = b$, Pero $b$ no pertenece a la imagen de $A$, entonces buscamos el punto de $\text{Col}(A)$ más cercano a $b$. Para esto planteamos las ecuaciones normales

$$
\overline A^T A\ \hat x = \overline A^T b
$$

Si el problema tiene soluciones infinitas, entonces la solución de menor norma es aquella que pertenezca al subespacio $\text{fil}(A)$. Es decir, que sea ortogonal al subespacio nulo.

Si $rg(A) = n$, entonces el problema tiene solución única y podemos encontrar la pseudo-inversa.

$$
A^\# = (\overline A^T A)^{-1} \overline A^T
$$

$$
\hat x =A^\# b
$$

## Regresión Lineal

Si tenemos un conjunto de datos, podemos encontrar una ecuación que se ajuste mejor a los datos. Podemos proponer distintas curvas, cambiando los parámetros de las mismas

$$
\begin{bmatrix}
x_1 & 1 \\
x_2 & 1 \\
\vdots & \vdots \\
x_n & 1 \\
\end{bmatrix}
\begin{bmatrix}
m \\
b
\end{bmatrix} =
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_1^2 & x_1 & 1 \\
x_2^2 & x_2 & 1 \\
\vdots & \vdots & \vdots\\
x_n^2 & x_n & 1 \\
\end{bmatrix}
\begin{bmatrix}
a \\
b \\
c
\end{bmatrix} =
\begin{bmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{bmatrix}
$$

Para hacer esto, debemos resolver el problema por mínimos cuadrados, ya que probablemente los datos obtenidos sean imprecisos.

## Gram-Schmidt

Si tenemos una base $B = \{v_1, v_2, \cdots, v_n\}$, podemos construir una nueva base $B' = \{w_1, w_2, \cdots, w_n\}$ ortogonal. Aplicando el algoritmo de Gram-Schmidt

$$
w_1 = v_1
$$

$$
w_2 = v_2 - P_{S_1}(v_2) = v_2 - \frac{\langle v_2, w_1\rangle}{\|w_1\|^2} w_1
$$

$$
w_3 =v_3 - P_{S_2}(v_3) = v_3 - \Bigg(\frac{\langle v_3, w_1\rangle}{\|w_1\|^2} w_1 + \frac{\langle v_3, w_2\rangle}{\|w_2\|^2} w_2\Bigg)
$$

$$
w_n = v_n - \Bigg(\frac{\langle v_n, w_1\rangle}{\|w_1\|^2} w_1 + \frac{\langle v_n, w_2\rangle}{\|w_2\|^2} w_2 + \cdots +\frac{\langle v_n, w_{n-1}\rangle}{\|w_{n-1}\|^2} w_{n-1}\Bigg)
$$

## Autovalores y Autovectores

Algunas matrices, pueden ser escritas de la forma $A$ = $PDP^{-1}$, Siendo $D$ una matriz diagonal. Esto permite elevar matrices de forma muy sencilla.

$$
A^n = P D^n P^{-1}
$$

Los autovalores $\lambda_i$ se resuelven a partir de la ecuación $\text{det}(A -\lambda I) = 0$.

Los autovectores $v_i$ se resuelven a partir de la ecuacion $v_i = \text{Null}(A - \lambda_i I)$.

Para cada autovalor y su vector asociado, se cumple que

$$
Av_i = \lambda v_i
$$

Algunas propiedades de los autovalores:

- $\text{det}(A) = \prod_{i = 0}^n \lambda_i$. (Se consideran los autovalores con repetición)
- $\text{tr}(A) = \sum_{i=1}^n \lambda_i$. (Se consideran los autovalores con repetición)
- Si $p(A) = B$, entonces $p(\lambda_A) = \lambda_B$
- Si $\lambda$ es autovalor de $A$, entonces es autovalor de $A^T$
- La multiplicidad algebraica indica la multiplicidad del autovalor, mientras que la geométrica indica la dimension de su autoespacio

### Matrices de Jordan

Si una matriz $A \in \Bbb C^{3 \times 3}$ no es diagonalizable, podemos encontrar matrices de Jordan similares a una matriz diagonal, tal que $A \sim J_i$

Llamamos $V_1, V_2, V_3$ las columnas de $Q$

#### Algebraica 2, Geométrica 1

$$
A_1 = 
Q
\begin{bmatrix}
\lambda_1 & 1 & 0 \\
0 & \lambda_1 & 0 \\
0 & 0 & \lambda_2
\end{bmatrix}
Q^{-1}
$$

$V_2$ el vector que cumple con el sistema $: (A - \lambda_1I)V_2 = V_1$

#### Algebraica 3, Geométrica 1

$$
A_2 = 
Q
\begin{bmatrix}
\lambda & 1 & 0 \\
0 & \lambda & 1 \\
0 & 0 & \lambda
\end{bmatrix}
Q^{-1}
$$

$V_2$ el vector que cumple con el sistema $:(A - \lambda I)V_2 = V_1$

$V_3$ el vector que cumple con el sistema $: (A- \lambda I)V_3 = V_2$

En este caso, debemos elegir el $V_2$ que pertenezca a la imagen de $A- \lambda I$

#### Algebraica 3, Geométrica 2

$$
A_3 = 
Q
\begin{bmatrix}
\lambda & 0 & 0 \\
0 & \lambda & 1 \\
0 & 0 & \lambda
\end{bmatrix}
Q^{-1}
$$

$V_3$ el vector que cumple con el sistema $: (A- \lambda I)V_3 = V_2$

En este caso, debemos elegir el $V_2$ que pertenezca a la imagen de $A- \lambda I$

## Sistemas de E.D. Homogéneas

Si tenemos el sistema $AY = Y’$, entonces encontramos que al diagonalizar $Y$, las soluciones son de la forma

$$
\text{gen}\{v_1 e^{\lambda_1t},\ v_2 e^{\lambda_2t},\ \cdots,\ v_n e^{\lambda_nt}\}
$$

En caso de que tengo autovalores complejos, entonces podemos encontrar combinaciones lineales reales de la siguiente forma. Siendo $\lambda = a + bi$, y $v = w + ri$

$$
Re(Y_1(t)) = e^{at} \cdot \Big[\cos(bx)w - \sin(bx)r\Big]
$$

$$
Im(Y_1(t)) = e^{at} \cdot \Big[\cos(bx)r + \sin(bx)w\Big]
$$

### Matrices de Jordan

Si tiene un autovalor de multiplicidad algebraica $2$ y multiplicidad geométrica $1$

$$
\text{gen}\{e^{\lambda t}v_1, e^{\lambda t}(v_2+tv_1), e^{\eta t}v_3\}
$$

Si tiene un autovalor de multiplicidad algebraica $3$ y multiplicidad geométrica $2$

$$
\text{gen}\{e^{\lambda t}v_1, e^{\lambda t}v_2, e^{\lambda t}(v_3+tv_2)\}
$$

Si tiene un autovalor de multiplicidad algebraica $3$ y multiplicidad geométrica $1$

$$
\text{gen}\{e^{\lambda t}v_1, e^{\lambda t}(v_2 + tv_1), e^{\lambda t}(v_3 + tv_2 +\frac{t^2}{2}v_1)\}
$$

## Clasificación de Matrices

- **Matrices Simétricas** $\to A^t = A$. Son diagonalizables ortogonalmente
- **Matrices Ortogonales** $\to A A^T = A^T A = I$
- **Matrices Anti Simétricas** $\to A^t = -A$

Para matrices complejas, tenemos que:

- **Matrices Herméticas** $\to A^* = A$, donde $A^*$ representa la matriz adjunta (transpuesta y conjugada)
- **Matrices Unitarias**$\to A A^* = A^* A = I$. Sus autovalores tienen modulo 1. Preservan la norma
- **Matrices Anti Herméticas** $\to A^* = -A$

Para matrices de transformaciones lineales, tenemos:

- **Isometrías** $\to$ ***$\|Ax\| = \|x\|$. Son matrices que preservan la norma de un vector

## Valores Singulares

Se dice que $\sigma$ es un valor singular de $A$ si $\sigma = \sqrt \lambda$, con $\lambda$ autovalor de $A^* A$. Si $v_i$ son autovectores de $A^*A$, entonces encontramos que. Los autovectores deben ser ortogonales.

$$
\|Av_i\| = \sigma_i
$$

$$
\frac{Av_i}{\sigma_i} = u_i
$$

Podemos a partir de este conjunto, definir el subespacio columna, fila, y nulo de $A$. Todos estos conjuntos son ortonormales. Los primeros $k$ autovalores son estrictamente positivos y ordenados de forma decreciente, mientras que el resto son nulos.

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
\text{Nul}(A^T) = \Big\{ \frac{Av_{k+1}}{\sigma_{k+1}},\ \cdots,\ \frac{Av_n}{\sigma_n}\Big\}
$$

### Descomposición en V.S.

A partir de los conjuntos encontrados, podemos encontrar $A$ a partir la siguiente factorización

$$
A = U \Sigma V^*
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

$$
U = \Big[|u_1|, \ |u_2|,\ \cdots ,\ |u_k|\Big]
$$

$$
V = \Big[|v_1|, \ |v_2|,\ \cdots ,\ |v_n|\Big]
$$

### D.V.S. Reducida

Podemos escribir la matriz, omitiendo las filas y columnas que resultan nulas.

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

$$
A = U_k D_k V_k^*
$$

### Pseudo Inversa de Moore-Penrose

Se le llama así a la matriz $A^\dagger = V_K D_K^{-1} U_K^*$. Definida para toda matriz $m \times n$

- $A A^\dagger = P_{\text{Col}(A)}$
- $A^\dagger A = P_{\text{Fil}(A)}$

Para resolver el problema de cuadrados mínimos, podemos encontrar $\hat x$ de norma minima mediante la formula. ($\hat x$ ya pertenece al subespacio fila)

$$
\hat x = A^\dagger b
$$

## Formas Cuadráticas

Dada una matriz $A \in \mathbb{R}^{n \times n}$ simétrica, una **forma cuadrática en** $\mathbb{R}^n$ es una función $Q: \mathbb{R}^n \to \mathbb{R}$ tal que $Q(x) = x^T Ax$

### Teorema de Rayleigh

Para simplificar, se puede diagonalizar la matriz $A = P D P^T$, y aplicar un cambio de variables.

$$
\tilde Q(y) = y^T D y
$$

$$
x = Py
$$

Luego podemos aplicar el teorema de Rayleigh para encontrar los extremos de la función.

$$
\lambda_\text{min} \cdot \|x\|^2 \leq Q(x) \leq \lambda_\text{max} \cdot \|x\|^2
$$

Además, los extremos se encuentran en los autoespacios asociados a los autovalores máximos y mínimos.

### Restricciones

Si las restricciones son de la forma $R(x) = 1$, Entonces podemos encontrar los autovalores generalizados para el par de matrices $A,B$. Siendo $B$ una matriz definida positiva

$$
\det(A - \lambda_i B) = 0
$$

$$
v_i = \text{null}(A - \lambda_1 B)
$$

Los máximos y mínimos para la restricción son los autovalores generalizados máximos y mínimos, y se encuentran en sus respectivos autoespacios.

Por ultimo podemos hallar el vector especifico a partir de la siguiente relación:

$$
x = \alpha v
$$

$$
R(x) = \alpha^2 R(v) = 1
$$

> [!note]
> Si la restricción es indefinida, entonces la solución no esta acotada y el mínimo de la forma cuadrática estará asociado al autovalor máximo.
