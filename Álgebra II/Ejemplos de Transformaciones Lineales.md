## Rotación en $\mathbb{R}^2$

La siguiente transformación lineal rota un vector un ángulo $\theta$ en sentido antihorario:

$$
R(x_1, x_2) = \begin{pmatrix}\cos(\theta) & -\sin(\theta)\\ \sin(\theta) & \cos(\theta)\end{pmatrix}
\begin{pmatrix}x_1 \\ x_2\end{pmatrix}
$$

## Rotación en $\mathbb{R}^3$

En $\mathbb{R}^3$, podemos rotar un vector alrededor de cualquiera de los 3 ejes:

$$
R_{\theta,z} = \begin{pmatrix}\cos(\theta) & -\sin(\theta) & 0\\\sin(\theta) & \ \ \ \cos(\theta) & 0 \\ 0&0&1\end{pmatrix}
$$

$$
R_{\theta,x} = \begin{pmatrix}1&0&0\\0&\cos(\theta)&-\sin(\theta)\\0&\sin(\theta)&\ \ \ \cos(\theta)\end{pmatrix}
$$

$$
R_{\theta,y} = \begin{pmatrix}\ \ \ \cos(\theta) &0&\sin(\theta)\\0&1&0\\-\sin(\theta)&0&\cos(\theta)\end{pmatrix}
$$

## Proyectores

En álgebra lineal, definimos proyector a una transformación lineal que, compuesta consigo misma, da la misma transformación lineal.

$$
\Pi \circ \Pi = \Pi
$$

### Observaciones

- Si $w \in Im(\Pi) \implies \Pi(w) = w$

Esto es evidente, ya que la proyección de cualquier vector que se encuentra en la superficie a la cual proyectar, da el mismo vector.

- $Nu(\Pi) \oplus Im(\Pi) = \Bbb V$

Supongamos que $v \in Nu(\Pi) \cap Im(\pi)$, entonces $\underbrace{\Pi(v) = v}_{\text{Por Imagen}},\quad \underbrace{\Pi(v) = 0}_{\text{Por Núcleo}}$.

### Definición

Ya que todo vector de $\Bbb V$ se puede representar como combinación única de vectores de $Im(\Pi)$ y $Nu(\Pi)$. Entonces, si definimos ambos subespacios, siendo $S_1 = Im(\Pi)$, y $S_2 = Nu(\Pi)$, queda definida una proyección transversal que se denota como $\Pi_{S_1 S_2}$, se lee la proyección sobre $S_1$ en la dirección de $S_2$.

### Propiedades

- $\Pi_{S_1 S_2} + \Pi_{S_2 S_1} = I_{\Bbb V}$

Ya que podemos descomponer $v$ como dos vectores $v_1, v_2$, uno perteneciente a $S_1$ y otro perteneciente a $S_2$, entonces definimos si los evaluamos en ambas funciones se anularía uno de los componentes en cada función. Entonces $\Pi_{S_1 S_2} + \Pi_{S_2 S_1} = v_1 + v_2 = v$

## Simetría

Podemos encontrar rápidamente la simetría con respecto de $S_1$ en la dirección de $S_2$ a partir del uso de los proyectores

$$
\Sigma_{S_1 S_2}(v) = v - 2\Pi_{S_2 S_1}(v)
$$

## Cambio de Base

Aunque podemos usar los casos más simples para definir una de las transformaciones mencionadas en la base canónica, es más sencillo definirlas en las bases previamente definidas de $\Bbb V$ y utilizar matrices de cambio de bases para pasarlas a la base canónica

$$
[T]_E^E = [M]_B^E \cdot[T]_B^B \cdot [M]_E^B
$$

Partimos de un vector en la base canónica, primero lo pasamos a la base $B$. Luego aplicamos la transformación, la cual nos devuelve un vector en la misma base $B$. Por último usamos nuevamente la matriz de cambio de base para pasar el vector resultante a la base canónica $E$.

También es posible pasarlo a las bases $B$ y $B'$, partiendo de la base $A$ y $A'$:

$$
[T]_B^{B'} = [M]_{A'}^{B'} \cdot [T]_A^{A'} \cdot [M]_B^A
$$
