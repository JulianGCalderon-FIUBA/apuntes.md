## P.V.I. de Segundo Orden

Si tenemos un problema de valores iniciales de segundo orden:

$$
\begin{cases}
y'' = f(x, y, y') \\
y(x_0) = y_0 \\
y'(x_0) = u_0
\end{cases}
$$

Luego puedo realizar una sustitución para obtener un sistema de primer orden

$$
y' = u \qquad u' = f(x,y,u)
$$

Luego, nuestro P.V.I. se vería de la siguiente forma

$$
\begin{cases}
y' = u\\
u' = f(x, y, u) \\
y(x_0) = y_0 \\
u(x_0) = u_0
\end{cases}
$$

Ahora, podemos aplicar el método de Euler a cada ecuación del sistema

$$
\begin{pmatrix}
y_{i+1} \\
u_{i+1}
\end{pmatrix} =

\begin{pmatrix}
y_{i} \\
u_{i}
\end{pmatrix} + h

\begin{pmatrix}
u_{i} \\
f(x_i, y_i, u_i)
\end{pmatrix}
$$

El método de Runge-Kutta de orden 4 sería:

$$
\begin{pmatrix}
y_{i+1} \\
u_{i+1}
\end{pmatrix} =

\begin{pmatrix}
y_{i} \\
u_{i}
\end{pmatrix} + \frac h6

\begin{pmatrix}
m_1 + 2m_2 + 2m_3 + m_4 \\
k_1 + 2k_2 + 2k_3 + k_4
\end{pmatrix}
$$

$$
\begin{cases}
m_1 =  u_i\\
m_2 = u_i + \frac{k_1h}{2}\\
m_3 = u_i + \frac{k_2h}{2}\\
m_4 = u_i + k_3h\\
\end{cases}
$$

$$
\begin{cases}
k_1  = f(x_i, y_i, u_i) \\
k_2 = f(x_i + \frac h2, y_i + \frac{m_1h}{2}, u_i + \frac{k_1h}{2})\\
k_3 = f(x_i + \frac h2, y_i + \frac{m_2h}{2}, u_i + \frac{k_2h}{2})\\
k_4 = f(x_i + h, y_i + m_3h, u_i + k_3h)\\
\end{cases}
$$

## P.V.I. de $n$-ésimo Orden

En general, puedo expresar una ecuación diferencial de $n$-ésimo orden de la forma:

$$
\begin{cases}
y^{(n)} = f(x, y, y', \cdots, y^{(n-1)}) \\
y(x_0) = u_{1,0} \\
y'(x_0) = u_{2,0} \\
\vdots \\
y^{(n-1)} = u_{n,0}
\end{cases}
$$

Luego, puedo llegar a un sistema de $n$ ecuaciones diferenciales.

Donde $u_1 = y,\ u_2 = y',\  \cdots, \ u_n = y^{(n-1)}$

$$
\begin{cases}
u_1' = u_2\\
u_2' = u_3\\
\vdots \\
u_{n-1}' = u_n \\
u_n' =  f(x, u_1, u_2, \cdots, u_n)
\end{cases}
$$

$$
\begin{cases}
u_1(x_0) = u_{1,0} \\
u_2(x_0) = u_{2,0} \\
\vdots \\
u_{n-1}(x_0) = u_{n-1,0}\\
u_n(x_0) = u_{n,0} \\
\end{cases}
$$

## Sistema de Ecuaciones Diferenciales

Dado un sistema de ecuaciones diferenciales, podemos usar cualquiera de los métodos vistos en cada ecuación para aproximar la solución.

Si tenemos un sistema de ecuaciones diferenciales de dos ecuaciones

$$
\begin{cases}
x' = f(t,x,y)\\
y' = g(t,x,y)\\
x(t_0) = x_0 \\
y(t_0) = y_0
\end{cases}
$$

Entonces, podemos aplicar el método de Euler para encontrar la solución

$$
\begin{pmatrix}
x_{i+1} \\
y_{i+1}
\end{pmatrix} =

\begin{pmatrix}
x_{i} \\
y_{i}
\end{pmatrix} + h

\begin{pmatrix}
f(t_i, x_i, y_i) \\
g(t_i, x_i, y_i)
\end{pmatrix}
$$

También podemos aplicar el método de Runge-Kutta de orden 4

$$
\begin{pmatrix}
x_{i+1} \\
y_{i+1}
\end{pmatrix} =

\begin{pmatrix}
x_{i} \\
y_{i}
\end{pmatrix} + \frac h6

\begin{pmatrix}
m_1 + 2m_2 + 2m_3 + m_4 \\
k_1 + 2k_2 + 2k_3 + k_4
\end{pmatrix}
$$

$$
\begin{cases}
m_1  = f(t_i, x_i, y_i) \\
m_2 = f(t_i + \frac h2, x_i + \frac{m_1h}{2}, y_i + \frac{k_1h}{2})\\
m_3 = f(t_i + \frac h2, x_i + \frac{m_2h}{2}, y_i + \frac{k_2h}{2})\\
m_4 = f(t_i + h, x_i + m_3h, y_i + k_3h)\\
\end{cases}
$$

$$
\begin{cases}
k_1  = g(t_i, x_i, y_i) \\
k_2 = g(t_i + \frac h2, x_i + \frac{m_1h}{2}, y_i + \frac{k_1h}{2})\\
k_3 = g(t_i + \frac h2, x_i + \frac{m_2h}{2}, y_i + \frac{k_2h}{2})\\
k_4 = g(t_i + h, x_i + m_3h, y_i + k_3h)\\
\end{cases}
$$
