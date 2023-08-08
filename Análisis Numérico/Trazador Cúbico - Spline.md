**Fenómeno de Runge:** Mayor número de nodos no garantiza una mejor interpolación.

El trazador cúbico es una función partida que cumple las siguientes condiciones, para el conjunto de $x_0, \dots, x_n$ nodos.

1. Debe interpolar todos los nodos.
    
    $$
    S(x_j) = f(x_j) \quad, j=0\dots n
    $$
    
2. La función debe ser continua.
    
    $$
    S_j(x_{j+1}) = S_{j+1}(x_{j+1})\quad ,j = 0\dots n{-}2
    $$
    
3. Las derivada debe ser una función continua.
    
    $$
    S'_j(x_{j+1}) = S'_{j+1}(x_{j+1})\quad ,j = 0\dots n{-}2
    $$
    
4. La derivada segunda también debe ser una función continua.
    
    $$
    S''_j(x_{j+1}) = S''_{j+1}(x_{j+1})\quad ,j = 0\dots n{-}2
    $$
    
5. Dependiendo de si es una Spline libre (natural) o ligada, se debe cumplir que:
    1. Libre: $S''(x_0) = S''(x_n)$
    2. Ligada: $S'(x_0) = f'(x_0) \quad S'(x_n) = f'(x_n)$

Para que se cumpla esto, la spline tendrá la siguiente estructura

$$
S(x) = \begin{cases}

S_0(x) =a_0 + b_0(x-x_0) + c_0(x - x_0)^2 + d_0(x-x_0)^3 \quad \\ \qquad \text{Si}:x\in[x_0, x_1] \\\ \\

S_1(x) =a_1 + b_1(x-x_1) + c_1(x - x_1)^2 + d_1(x-x_1)^3 \\ \qquad \text{Si}:x\in[x_1, x_2] \\\ \\

\quad \vdots \\\ \\

S_{n-1}(x) =a_{n-1} + b_{n-1}(x-x_{n-1}) + c_{n-1}(x - x_{n-1})^2 + d_{n-1}(x-x_{n-1})^3 \\ \qquad \text{Si}:x\in[x_{n-1}, x_n]

\end{cases}
$$

Para encontrar las $4n$ constantes, entonces debo plantear las condiciones y resolver el sistema lineal. El sistema es cerrado.

# Forma Matricial

Si resolvemos el sistema en forma genérica, llegamos al siguiente sistema de ecuaciones cerrado

$$
\begin{bmatrix}

1 & 0 & 0 & \dotsb & \dotsb & 0 \\
h_0 & 2(h_0+h_1) & h_1 & 0 & \dotsb & 0 \\
0 & h_1 & 2(h_1+h_2) & h_2 & \ddots& \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & \ddots & \ddots & h_{n-2} & 2(h_{n-2} + h_{n-1}) & h_{n-1} \\
0 & \dotsb & \dotsb & \dotsb & \dotsb & 1

\end{bmatrix} 

\begin{bmatrix}

c_0 \\ c_1 \\ c_2 \\ \vdots\\ \vdots\\ c_n

\end{bmatrix} 

= 

\begin{bmatrix}

0 \\
\frac 3{h_1}(a_2-a_1)-\frac 3{h_0}(a_1-a_0) \\
\vdots \\
\frac 3{h_{n-1}}(a_n-a_{n-1})-\frac 3{h_{n-2}}(a_{n-1}-a_{n-2}) \\
0

\end{bmatrix}
$$

Una vez hallados los $c_j$, debemos encontrar $b_j$ y $d_j$ a partir de las siguientes ecuaciones.

$$
b_j = \frac{1}{h_j}(a_{j+1} - a_j) - \frac{h_j}{3}(2c_j + c_{j+1})
$$

$$
d_j = \frac{c_{j+1} - c_j}{3h_j}
$$