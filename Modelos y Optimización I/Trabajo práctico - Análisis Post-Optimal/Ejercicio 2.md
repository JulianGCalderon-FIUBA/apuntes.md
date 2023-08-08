# Enunciado

El Ministerio está evaluando la conformación de un nuevo tipo de equipo especializado en entrenamiento. Estará integrado por cuatro brigadas, una autobomba y cuatro drones. Si cada uno de estos equipos mejorase la eficacia del plan en 5 puntos, ¿cuántos convendría formar? ¿Y si aportaran una mejora de 10 puntos?

# Resolución

Se indica que se puede agregar un nuevo tipo de equipo, lo que implica modificar las restricciones. Si se considera una nueva variable $X_8$ que representa al nuevo tipo de equipo, el planteo queda de la siguiente forma:

$$
\begin{alignat*}{2}
&\text{Brigadas}) &\quad X_1 + X_2 + 4X_8 &\le 28\\

&\text{Autobombas}) &\quad 2X_1   + X_8 &\le 16 \\

&\text{Helicópetros}) &\quad  X_2 &\le 8 \\

&\text{Drones}) &\quad X_1 + 2X_2  + 4X_8 &\le 24 \\

&\text{Relación CF-AL})\quad &X_1 - 2X_2 &\le 0
\end{alignat*}
$$

Al funcional, debemos agregarle el coeficiente del nuevo producto.

$$
Z(\max) = 10X_1 + 8X_2 + 5X_8
$$

Realizamos un análisis inicial del lucro cesante para descartar rápidamente la alternativa en caso de que no sea conveniente. Si el lucro cesante fuera mayor al beneficio del nuevo equipo, significaría que el beneficio que se obtendría sería menor al gasto que requeriría formar los nuevos equipos, por lo que sin realizar otro análisis ya se sabría que la alternativa no sería conveniente. 

Para el análisis, debemos obtener el valor marginal de los recursos saturados (a partir de la tabla optima). Los recursos no saturados tendrán un valor marginal de $0$.

- $X_4 - \text{Autobombas}:$ Tiene un valor marginal de $5$.
- $X_5 - \text{Helicópteros}:$ Tiene un valor marginal de $8$.
- $X_6 - \text{Drones}:$ Tiene un valor marginal de $0$.

A partir de estos valores, calculamos el lucro cesante

$$
\text{Lucro Cesante} = 0 \cdot 8 + 5 \cdot 1 + 0 \cdot 4 = 5
$$

Como el lucro cesante es igual al beneficio que aporta cada equipo nuevo, no podemos descartar la alternativa. Hay que realizar un análisis con las tablas de simplex para ver si es conveniente formar equipos nuevos o no, y cuántos.

Primero, debemos definir la matriz de cambio de base, formada por los vectores de la tabla óptima asociados a las variables ***slack.***

$$
\text{Matriz de Cambio de Base} =\begin{pmatrix}
0 & 1/2 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
1 & -1/2 & -1 & 0 & 0 \\
0 & -1/2 & -2 & 1 & 0 \\
0 & -1/2 & 2 & 0 & 1
\end{pmatrix}
$$

$$
\text{Nueva Columna Inicial} = \begin{pmatrix}4\\ 
1\\ 
0\\
4\\
0\\
\end{pmatrix}
$$

Luego, multiplicamos la matriz de cambio de base por la nueva columna inicial, para obtener:

$$
\text{Nueva Columna Óptima =}\begin{pmatrix}1/2 \\0 \\3 \\ 7/2 \\ -1/2\end{pmatrix}
$$

Calculamos el costo de oportunidad del producto, multiplicando la nueva columna óptima por el vector de coeficientes de la base, y le restamos el coeficiente del funcional del nuevo producto.

$$
z_j - c_j =\begin{pmatrix}
10 & 8 & 0 & 0 & 0
\end{pmatrix} \cdot \begin{pmatrix}1/2\\ 
0\\ 
7/2\\
7/2\\
-1/2\\
\end{pmatrix} - 5 = 0
$$

Observamos que el costo de oportunidad de los nuevos equipos es $0$, lo que nos indica que hay múltiples soluciones óptimas alternativas; es decir, si formamos nuevos equipos obtenemos el mismo valor de eficacia total. Para encontrar la otra solución óptima hay que hacer entrar a $X_8$ a la base, y sacar $X_6$. Observamos que $X_8$ va a ingresar con un valor de $0$, indicando que no es necesario hacer equipos nuevos en la nueva solución.

|  |  |  | $10$ | $8$ |  |  |  |  |  | $5$ |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $X_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $A_8$ | $\theta$ |
| $10$ | $X_1$ | $8$ | $1$ | $0$ | $0$ | $1/2$ | $0$ | $0$ | $0$ | $1/2$ | $16$ |
| $8$ | $X_2$ | $8$ | $0$ | $1$ | $0$ | $0$ | $1$ | $0$ | $0$ | $0$ | $-$ |
|  | $X_3$ | $4$ | $0$ | $0$ | $1$ | $-1/2$ | $-1$ | $0$ | $0$ | $7/2$ | $8/7$ |
|  | $X_6$ | $0$ | $0$ | $0$ | $0$ | $-1/2$ | $-2$ | $1$ | $0$ | $7/2$ | $0$ |
|  | $X_7$ | $8$ | $0$ | $0$ | $0$ | $-1/2$ | $2$ | $0$ | $1$ | $-1/2$ | $-$ |
|  |  | $Z = 144$ | $0$ | $0$ | $0$ | $5$ | $8$ | $0$ | $0$ | $0$ |  |

Sin embargo, si la mejora de los nuevos equipos fuera de $10$ puntos ya no estaríamos en la solución óptima, por lo que es necesario seguir iterando hasta encontrar el nuevo punto óptimo.

|  |  |  | $10$ | $8$ |  |  |  |  |  | $10$ |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $X_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $A_8$ | $\theta$ |
| $10$ | $X_1$ | $8$ | $1$ | $0$ | $0$ | $1/2$ | $0$ | $0$ | $0$ | $1/2$ | $16$ |
| $8$ | $X_2$ | $8$ | $0$ | $1$ | $0$ | $0$ | $1$ | $0$ | $0$ | $0$ | $-$ |
|  | $X_3$ | $4$ | $0$ | $0$ | $1$ | $-1/2$ | $-1$ | $0$ | $0$ | $7/2$ | $8/7$ |
|  | $X_6$ | $0$ | $0$ | $0$ | $0$ | $-1/2$ | $-2$ | $1$ | $0$ | $7/2$ | $0$ |
|  | $X_7$ | $8$ | $0$ | $0$ | $0$ | $-1/2$ | $2$ | $0$ | $1$ | $-1/2$ | $-$ |
|  |  | $Z = 144$ | $0$ | $0$ | $0$ | $5$ | $8$ | $0$ | $0$ | $-5$ |  |

Calculamos los $\theta_j$ y observamos que nuevamente debemos hacer entrar $X_8$ a la base, y sacar $X_6$. También podemos notar que $X_8$ entrará tomando un valor inicial nulo.

|  |  |  | $10$ | $8$ |  |  |  |  |  | $10$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $X_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $A_8$ |
| $10$ | $X_1$ | $8$ | $1$ | $0$ | $0$ | $4/7$ | $2/7$ | $-1/7$ | $0$ | $0$ |
| $8$ | $X_2$ | $8$ | $0$ | $1$ | $0$ | $0$ | $1$ | $0$ | $0$ | $0$ |
|  | $X_3$ | $4$ | $0$ | $0$ | $1$ | $0$ | $1$ | $-1$ | $0$ | $0$ |
| $10$ | $X_8$ | $0$ | $0$ | $0$ | $0$ | $-1/7$ | $-4/7$ | $2/7$ | $0$ | $1$ |
|  | $X_7$ | $8$ | $0$ | $0$ | $0$ | $-4/7$ | $12/7$ | $1/7$ | $1$ | $0$ |
|  |  | $Z = 144$ | $0$ | $0$ | $0$ | $30/7$ | $36/7$ | $10/7$ | $0$ | $0$ |

Vemos que la nueva solución óptima tiene el mismo valor del funcional, lo cual tiene sentido pues $X_8$ entró con un valor nulo. Esto nos indica que estamos en un punto degenerado, por lo que ambas tablas representan la misma solución óptima.

En conclusión, en ambos casos la solución óptima seguirá siendo en el mismo punto, seguirá siendo un punto degenerado. Luego, el esquema productivo se mantendrá igual, indicando que no es necesario armar ningún equipo nuevo.

## Análisis por Software

Para el análisis por software, resolvemos el modelo con la nueva restricción, e inicialmente un coeficiente de $c_8=5$.

![[Ejercicio 2 1.png|Untitled]]

Vemos que en la solución optima, no se forman equipos del nuevo tipo. Esto implica que el funcional también se mantiene igual.

Ahora, probamos con un coeficiente de $c_8 = 10$.

![[Ejercicio 2 2.png|Untitled]]

Nuevamente, la solución optima nos indica que no debemos formar equipos del nuevo tipo. Esto implica que el funcional también se mantiene igual.