# Enunciado

Graficar la cantidad de equipos de apoyo logístico, el valor del funcional y el valor marginal de los helicópteros al variar la disponibilidad de autobombas entre 15 y 24. 

# Resolución

### Análisis por Software

Primero, resolvemos el modelo por ***software*** y observamos el reporte de análisis de sensibilidad generado. Por simplicidad, no adjuntaremos el reporte completo, sino fragmentos de los mismos.

Definimos $\alpha$ como la cantidad de autobombas disponibles, y partiremos con un valor de $\alpha = 16$.

Al resolverlo por software, este nos indica el rango de variación para la estructura óptima actual.

![[Ejercicio 5 1.png|Untitled]]

En la tercera fila, podemos visualizar las autobombas. Vemos que la estructura óptima actual se mantiene para valores de $\alpha$ entre $[0, 16]$. Además, a partir del valor marginal del recurso, podemos ver que con $\alpha = 15$, tendremos un puntaje óptimo de $139$. Recordemos que con $\alpha=16$, el puntaje óptimo es de $144$. El funcional entonces, crecerá linealmente desde $(15, 139)$ hasta $(16, 144)$.

Debido a que los valores marginales no varían durante una misma estructura óptima, sabremos que los helicópteros se mantendrán con un valor de $8$ durante el intervalo.

Volvemos a resolver el problema, con $\alpha = 15$, para poder visualizar como variará $X_2$ durante este rango.

![[Ejercicio 5 2.png|Untitled]]

Desde aquí, observamos que el valor de $X_2$ será $8$, al igual que con $\alpha=16$. Además, confirmamos que el valor del funcional será de $139$.

Lo correcto, a partir de aquí, sería proponer un valor de $\alpha$ infinitésimamente mayor a $16$, de modo que podamos observar la solución alternativa en el punto de cambio. Sin embargo, para simplificar el informe, y debido a que ya conocemos el rango de variación gracias al análisis grafico y el análisis por tablas de simplex detallado más abajo, resolveremos el modelo directamente con $\alpha = 24$. 

Desde allí, observaremos que el rango que mantiene la nueva estructura óptima es $[16, 24]$. Como el rango anterior finalizaba $\alpha = 16$, entonces sabremos que nuestro análisis fue completo.

![[Ejercicio 5 3.png|Untitled]]

Confirmamos lo que indicamos anteriormente, ya que el rango de actividad de las autobombas será entre $16$ y $24$.

El funcional en este punto será de $168$. Luego, el funcional crecerá linealmente desde $(16, 144)$ hasta $(24, 168)$. Debido a que, como mencionamos anteriormente, el valor marginal para una estructura óptima siempre será el mismo, entonces durante todo este rango, los helicópteros tomaran un valor marginal de $0$ (habrá un sobrante del recurso).

Para observar la variación de $X_2$, debemos analizar su valor en el punto óptimo con $\alpha = 24$.

![[Ejercicio 5 4.png|Untitled]]

Vemos que en el punto óptimo, $X_2$ tomará un valor de $6$. Luego, variará linealmente desde $(16, 8)$ hasta $(24, 6)$.

### Análisis Gráfico

Comenzaremos en el extremo inferior del poliedro, con $\alpha = 15$. El punto óptimo será el $B$, y la restricción de autobombas es la resaltada en azul:

![[Ejercicio 5 5.png|Untitled]]

A medida que aumentamos el valor de $\alpha$, entonces el punto óptimo se moverá hacia la izquierda, hasta agotar la restricción de drones. Visualizamos el poliedro con $\alpha = 16$.

![[Ejercicio 5 6.png|Untitled]]

Podemos observar que en el rango $[15, 16]$, el funcional aumenta, la producción de $X_1$ permanece constante, y el valor marginal de helicópteros toma valor, ya que el recurso esta agotado.

En este punto, nos encontramos en un punto degenerado, hecho que también puede observarse en las soluciones alternativas de la tabla de dual. Si seguimos aumentando el punto óptimo, veremos que no podremos simplemente aumentar la producción de $X_1$, sino que tendremos que disminuir $X_2$ para mantenernos en el poliedro. Aumentamos $\alpha$ a $21$.

![[Ejercicio 5 7.png|Untitled]]

Podemos observar que el valor de $\alpha$ aún puede crecer sin alterar la estructura del punto óptimo. Aumentamos $\alpha = 24$.

En este punto, podemos observar que nos encontramos nuevamente ante un punto degenerado. Además, sin realizar cuentas, podemos observar que el funcional nunca mejorará si seguimos aumentando $\alpha$.

![[Ejercicio 5 8.png|Untitled]]

En el rango $[16, 24]$, vemos que el funcional sigue aumentando pero a una tasa menor, ya que debemos reducir $X_1$. Además, el valor marginal de los helicópteros es nulo, ya que tendremos sobrante del recurso.

### Análisis por Método Simplex

Debemos hallar el rango de variación de las autobombas. Para hacerlo, trabajaremos con la tabla del dual. Se plantea genéricamente la cantidad de autobombas como $\alpha$, y se calculan los $z_j-c_j$ para cada columna.

|  |  |  | $28$ | $\alpha$ | $8$ | $24$ |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ |
| $\alpha$ | $Y_2$ | $5$ | $1/2$ | $1$ | $0$ | $1/2$ | $1/2$ | $-1/2$ | $0$ |
| $8$ | $Y_3$ | $8$ | $1$ | $0$ | $1$ | $2$ | $-2$ | $0$ | $-1$ |
|  |  | $Z = 5\alpha + 64$ | $\alpha - 20$ | $0$ | $0$ | $\frac12\alpha-8$ | $\frac 12 \alpha-16$ | $-\frac 12 \alpha$ | $-8$ |

Una vez calculados, debemos hallar para qué valores de $\alpha$ la estructura de la solución optima sigue siendo la misma. Esto es, el $z_j - c_j$ permanece no positivo.

$$
\begin{alignat*}{3}
& z_1 - c_1: \quad && \frac12\alpha - 20 \leq 0 \quad &&\to \alpha \leq 40 \\
& z_4 - c_4: \quad && \frac 12 \alpha - 8 \leq 0 \quad &&\to \alpha \leq 16 \\
& z_5 - c_5: \quad &&\frac 12 \alpha - 16 \leq 0 \quad &&\to \alpha \leq 32 \\
& z_6 - c_6: \quad &&-\frac 12 \alpha \leq 0 \quad &&\to \alpha \geq 0
\end{alignat*}
$$

Luego, vemos que la estructura óptima es válida para cualquier $\alpha$ entre $0$ y $16$. Vemos que el rango superior tiene sentido, ya que nos encontrábamos en un punto degenerado (en la tabla primal) desde el primer momento. Nos colocamos en el borde del rango superior y analizamos la tabla.

|  |  |  | $28$ | $\alpha =16$ | $8$ | $24$ |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $\theta$ |
| $\alpha=16$ | $Y_2$ | $5$ | $1/2$  | $1$ | $0$ | $1/2$ | $1/2$ | $-1/2$ | $0$ | $10$ |
| $8$ | $Y_3$ | $8$ | $1$ | $0$ | $1$ | $\color{red}2$ | $-2$ | $0$ | $-1$ | $\color{blue}4$ |
|  |  | $Z = 144$ | $-4$ | $0$ | $0$ | $\color{blue}0$ | $-8$ | $-8$ | $-8$ |  |

Retiramos $Y_4$ de la base, y hacemos entrar $Y_3$ ya que tiene el menor $\theta \ (4)$

|  |  |  | $28$ | $\alpha =16$ | $8$ | $24$ |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ |
| $\alpha= 16$ | $Y_2$ | $3$ | $1/4$ | $1$ | $-1/4$ | $0$ | $1$ | $-1/2$ | $1/4$ |
| $24$ | $Y_4$ | $4$ | $1/2$ | $0$ | $1/2$ | $1$ | $-1$ | $0$ | $-1/2$ |
|  |  | $Z = 144$ | $-4$ | $0$ | $0$ | $0$ | $-8$ | $-8$ | $-8$ |

Nuevamente, planteamos genéricamente $\alpha$ y calculamos los $z_j - c_j$.

|  |  |  | $28$ | $\alpha$ | $8$ | $24$ |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ |
| $\alpha$ | $Y_2$ | $3$ | $1/4$ | $1$ | $-1/4$ | $0$ | $1$ | $-1/2$ | $1/4$ |
| $24$ | $Y_4$ | $4$ | $1/2$ | $0$ | $1/2$ | $1$ | $-1$ | $0$ | $-1/2$ |
|  |  | $Z = 3\alpha +  96$ | $\frac 14 \alpha -16$ | $0$ | $-\frac14\alpha+4$ | $0$ | $\alpha - 24$ | $-\frac 12 \alpha$ | $\frac 14 \alpha -12$ |

Una vez calculados, debemos hallar para qué valores de $\alpha$ la estructura de la solución optima sigue siendo la misma. Esto es, el $z_j - c_j$ permanece no positivo.

$$
\begin{alignat*}{3}
& z_1 - c_1: \quad && \frac 14 \alpha -16 \quad &&\to \alpha \leq 64\\
& z_3 - c_3: \quad && -\frac14\alpha+4\quad &&\to \alpha \geq 16 \\
& z_5 - c_5: \quad && \alpha - 24 \leq 0\quad &&\to \alpha \leq 24 \\
& z_6 - c_6: \quad &&-\frac 12 \alpha \leq 0\quad &&\to \alpha \geq 0 \\
& z_7 - c_7: \quad &&\frac 14 \alpha -12 \leq 0 \quad &&\to \alpha \leq 48
\end{alignat*}
$$

Vemos que la estructura óptima es válida para cualquier $\alpha$ entre $16$ y $24$. Debido a que el alcance de la propuesta era hasta $\alpha = 24$, finalizamos el análisis de rango de variación.

### Gráfica: $Z$ vs. $b_2$

A partir del desarrollo realizado, podemos encontrar los valores del funcional según los distintos valores de $\alpha$. Debido a que la variación ya fue analizada particularmente para el análisis grafico y para la resolución por ***software***, para estas gráficas nos basaremos en los valores de la tabla.

A partir de la primera tabla, para $\alpha \in [0, 16]$, tendremos que el funcional estará dado por $Z=5\alpha + 64$.

De la segunda tabla, obtenemos que para $\alpha \in [16,24]$, tendremos que el funcional estará dado por $Z = 3\alpha + 96$. 

Esto coincide con el análisis gráfico, donde se indicó que en el segundo rango el funcional iba a aumentar a una tasa menor.

![[Ejercicio 5 9.png|Untitled]]

### Gráfica $X_2$ vs. $b_2$

Tendremos que $X_2 \sim Y_7$. Luego, el valor de $X_2$ estará dado por $z_7 - c_7$ en el planteo dual.

A partir de la primera tabla, para $\alpha \in [0, 16]$, tendremos que $X_2$ tomará un valor constante de $8$.

De la segunda tabla, obtenemos que para $\alpha \in [16, 24]$, el valor  de $X_2$ estará dado por $12-\frac 14 \alpha$ .

![[Ejercicio 5 10.png|Untitled]]

### Gráfica $Y_3$ vs $b_2$

A partir de la primera tabla, para $\alpha \in [0, 16]$, tendremos que $Y_3$ (el valor marginal de los helicópteros) tomará un valor constante de $8$

De la segunda tabla, obtenemos que para $\alpha \in [16, 24]$, $Y_3$ tomará un valor constante de $0$, pues, como se observó previamente, el recurso pasa a estar saturado.

![[Ejercicio 5 11.png|Untitled]]