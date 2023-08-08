# Enunciado

Nos informan que los equipos deberán incorporar médicos: tres por cada equipo de combate del fuego y uno por cada equipo de apoyo logístico. ¿Qué sucedería si contáramos con 36 médicos? ¿Y si fueran 26?

# Resolución

Se puede pensar a los médicos como un nuevo recurso disponible, en cuyo caso hay que pensar la situación como una nueva restricción:

$$
3X_1 + X_2 \le B_6
$$

donde $B_6$ es la cantidad de médicos disponibles. 

Lo primero que hay que hacer, entonces, es analizar si la solución óptima cumple con esta nueva restricción. En caso de que haya $36$ médicos sería:

$$
3 \cdot 8 + 8 = 32 \le 36
$$

Como se cumple la nueva restricción, no es necesairo realizar modificaciones a la tabla, pues la solución sigue siendo óptima. Recordemos que al agregar restricciones se está achicando el poliedro, por lo que, si la restricción se cumple, no es posible que aparezca una mejor solución. 

Sin embargo, si fueran $26$ los médicos disponibles la restricción ya no se cumpliría:

$$
32 \not\le 26
$$

Por lo que hay que agregar la nueva restricción a la tabla óptima, e iterar hasta hallar la solución óptima que cumpla todas las restricciones. 

Para hacerlo, es necesario agregarla en la tabla del ***problema dual***, multiplicando el vector que se quiere agregar por la matriz de cambio de base correspondiente.

$$
\text{Matriz de Cambio de Base} =\begin{pmatrix} 
1/2 & 0\\
0 & 1
\end{pmatrix}
$$

$$
\text{Nueva Columna Inicial} = \begin{pmatrix}
3\\
1
\end{pmatrix}
$$

Al hacerlo, obtenemos:

$$
\text{Nueva Columna Óptima =}\begin{pmatrix}
3/2 \\
1\end{pmatrix}
$$

Si calculamos su $z_j-c_j$, podemos confirmar que la solución previa ya no es más óptima, y que hay que iterar en la tabla para hallar la nueva solución:

$$
z_j - c_j =\begin{pmatrix}
16 & 8
\end{pmatrix} \cdot \begin{pmatrix}
3/2\\
1
\end{pmatrix} - 26 = 6
$$

Calculamos el $\theta$ para $X_8$, y vemos que debe entrar $Y_8$ y salir $Y_2$ de la base.

|  |  |  | $28$ | $16$ | $8$ | $24$ |  |  |  | $26$ |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $A_8$ | $\theta$ |
| $16$ | $Y_2$ | $5$ | $1/2$ | $1$ | $0$ | $1/2$ | $1/2$ | $-1/2$ | $0$ | $3/2$ | $10/3$ |
| $8$ | $Y_3$ | $8$ | $1$ | $0$ | $1$ | $2$ | $-2$ | $0$ | $-1$ | $1$ | $8$ |
|  |  | $Z = 144$ | $-12$ | $0$ | $0$ | $0$ | $-8$ | $-8$ | $-8$ | $6$ |  |

|  |  |  | $28$ | $16$ | $8$ | $24$ |  |  |  | $26$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $A_8$ |
| $26$ | $Y_8$ | $10/3$ | $1/3$ | $2/3$ | $0$ | $1/3$ | $1/3$ | $-1/3$ | $0$ | $1$ |
| $8$ | $Y_3$ | $14/3$ | $2/3$ | $-2/3$ | $1$ | $5/3$ | $-7/3$ | $1/3$ | $-1$ | $0$ |
|  |  | $Z = 124$ | $-14$ | $-4$ | $0$ | $-2$ | $-10$ | $-6$ | $-8$ | $0$ |

En caso de que hubiera disponibles $26$ médicos la nueva solución óptima tendría $124$ puntos de eficacia (menos que si no hubiera médicos, o si hubiera $36$), y el nuevo esquema es el siguiente:

- Se arman $6$ equipos de Combate del Fuego y $8$ equipos de Apoyo Logístico.
- Sobran $8$ brigadas, $4$ autobombas, $2$ drones, y podrían armarse $10$ equipos más de Combate del Fuego para alcanzar la restricción de la relación entre los equipos.
- Ahora hay sobrante de autobombas, que antes no pasaba.
- Disminuye el valor marginal de los helicópteros, lo que implica que por cada unidad nueva que se consiga se aumentará menos el funcional.

## Análisis gráfico

Primero agregamos la restricción con $36$ médicos, y observamos que no afecta al poliedro previo, por lo que la solución óptima seguirá siendo la misma y no es necesario hacer un análisis posterior.

Graficamos curva de nivel del funcional y vemos que sigue pasando por el mismo punto.

![[Apuntes/Modelos y Optimización I/Trabajo práctico - Análisis Post-Optimal/Attachments/Ejercicio 3 1.png|Untitled]]

Sin embargo, al cambiar la disponibilidad de médicos a $26$ vemos que sí se modifica el poliedro de soluciones, y se hace más chico ya que hay una restricción nueva que limita el espacio de soluciones. 

Al achicar el poliedro, podemos observar que la solución que antes era óptima ahora ni siquiera forma parte del espacio de soluciones, y la nueva solución óptima se encuentra en el punto $E = (6,8)$.

![[Apuntes/Modelos y Optimización I/Trabajo práctico - Análisis Post-Optimal/Attachments/Ejercicio 3 2.png|Untitled]]

Además, vemos que si modificamos la curva de nivel del funcional ahora pasa por el nuevo punto óptimo $E$. 

![[Apuntes/Modelos y Optimización I/Trabajo práctico - Análisis Post-Optimal/Attachments/Ejercicio 3 3.png|Untitled]]

## Análisis por software

Antes de agregar la nueva restricción, la corrida de software era la siguiente:

![[Apuntes/Modelos y Optimización I/Trabajo práctico - Análisis Post-Optimal/Attachments/Ejercicio 3 4.png|Untitled]]

Al agregar la nueva restricción con disponibilidad de $36$ médicos, vemos que no se modifica el esquema productivo, es decir, nos quedamos en el mismo punto óptimo, con la diferencia de que ahora aparece la nueva restricción, que indica que se utiliza un total de $32$ médicos. 

![[Apuntes/Modelos y Optimización I/Trabajo práctico - Análisis Post-Optimal/Attachments/Ejercicio 3 5.png|Untitled]]

Sin embargo, observamos que al reducir la cantidad de médicos a $26$ la solución óptima cambia, y ahora se consiguen $124$ puntos totales de eficacia, y se arman $6$ equipos de Combate del Fuego y $8$ de Apoyo Logístico.

![[Apuntes/Modelos y Optimización I/Trabajo práctico - Análisis Post-Optimal/Attachments/Ejercicio 3 6.png|Untitled]]

Además, se utilizan todos los médicos y helicópteros disponibles, y hay sobrante del resto de los recursos.