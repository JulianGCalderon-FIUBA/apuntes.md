# Enunciado

Hubo una modificación en la eficacia de los equipos de combate del fuego, y pasará de 10 a 12 puntos por equipo. ¿Cómo cambiará la solución encontrada?

# Resolución

Aumentar los puntos por equipo de Combate del Fuego implica aumentar el coeficiente en el funcional asociado con la variable $X_1$, es decir, $C_1$. Esto hace que el funcional quede de la siguiente forma:

$$
Z(\max) = 12X_1 + 8X_2 
$$

Si lo analizamos con las tablas simplex, podemos observar que como $X_1$ ya se encuentra en la base, aumentar su coeficiente no modificará el esquema óptimo, si no que lo mantendrá pero dándole un valor mayor al funcional.

Con este nuevo coeficiente, la tabla queda de la siguiente forma:

|  |  |  | $12 \\ \color{red}\cancel{10}$ | $8$ |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $X_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ |
| $12 \\ \color{red}\cancel{10}$ | $X_1$ | $8$ | $1$ | $0$ | $0$ | $1/2$ | $0$ | $0$ | $0$ |
| $8$ | $X_2$ | $8$ | $0$ | $1$ | $0$ | $0$ | $1$ | $0$ | $0$ |
|  | $X_3$ | $4$ | $0$ | $0$ | $1$ | $-1/2$ | $-1$ | $0$ | $0$ |
|  | $X_6$ | $0$ | $0$ | $0$ | $0$ | $-1/2$ | $-2$ | $1$ | $0$ |
|  | $X_7$ | $8$ | $0$ | $0$ | $0$ | $-1/2$ | $2$ | $0$ | $1$ |
|  |  | $Z = \color{green}160$ | $0$ | $0$ | $0$ | $6$ | $8$ | $0$ | $0$ |

## **Analisis gráfico**

Podemos ver que si se grafican el funcional original y el modificado, este último alcanza su máximo en el mismo punto que el anterior, pero con un valor mayor. Este valor es, específicamente, $16$ puntos más grande, ya que esa es la diferencia que se agrega al modificar el coeficiente de $X_1$ de $10$ a $12$ puntos.

Al sólo modificar coeficientes del funcional, como vimos con la tabla, el poliedro no se altera. 

![[Ejercicio 4 1.png|Untitled]]

## Análisis por software

A la hora de analizar la modificación por software, el único cambio que hay que hacer es en el coeficiente de $X_1$, por lo que podemos ver que la diferencia con la corrida original será un cambio en el valor final. 

![[Ejercicio 4 2.png|Corrida original.]]

Corrida original.

![[Ejercicio 4 3.png|Corrida con funcional modificado.]]

Corrida con funcional modificado.