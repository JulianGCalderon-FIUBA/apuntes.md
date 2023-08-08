# Integrantes - Grupo 2

| Nombre | Padrón | Mail |
| --- | --- | --- |
| Julián González Calderón | 107938 | jgonzalezc@fi.uba.ar |
| María Sol Moon | 107976 | mmoon@fi.uba.ar |
| Federico Adrián Solari Vazquez | 106895 | fsolariv@fi.uba.ar |

# Enunciado

Seguidamente se plantea una serie de variantes al problema de la Primer Entrega. Cada una debe resolverse (justificando cómo obtiene las respuestas) en forma independiente a partir de la solución óptima del problema. La justificación puede realizarse mediante algún método válido (método Simplex, resolución por software o resolución gráfica). Al menos una de las variantes deberá ser justificada mediante el método Simplex.

1. El Ministerio evalúa dos alternativas para el plan: conseguir 4 drones más con los que formar equipos o destinar 4 de los 24 drones actuales para entrenamiento intensivo, con lo que no estarán disponibles para la formación de equipos, pero se podrá obtener una mejora de 18 puntos en la eficacia resultante. ¿Cuál de estas dos alternativas será la mejor?
2. El Ministerio está evaluando la conformación de un nuevo tipo de equipo especializado en entrenamiento. Estará integrado por cuatro brigadas, una autobomba y cuatro drones. Si cada uno de estos equipos mejorase la eficacia del plan en 5 puntos, ¿cuántos convendría formar? ¿Y si aportaran una mejora de 10 puntos?
3. Nos informan que los equipos deberán incorporar médicos: tres por cada equipo de combate del fuego y uno por cada equipo de apoyo logístico. ¿Qué sucedería si contáramos con 36 médicos? ¿Y si fueran 26?
4. Hubo una modificación en la eficacia de los equipos de combate del fuego, y pasará de 10 a 12 puntos por equipo. ¿Cómo cambiará la solución encontrada?
5. Graficar la cantidad de equipos de apoyo logístico, el valor del funcional y el valor marginal de los helicópteros al variar la disponibilidad de autobombas entre 15 y 24. Justificar cómo obtiene cada gráfico. NOTA: las respuestas de este punto deben justificarse obligatoriamente mediante la resolución por software; opcionalmente, puede agregarse una justificación mediante la resolución por método Simplex o resolución gráfica.

# Anexo

## Versión del Ejercicio

Para nuestra resolución, planteamos las restricciones propuestas inicialmente, pero corrigiendo la tabla óptima primal para que corresponda con las mismas.

## Planteo Matemático Primal

Definimos las dos variables de nuestro problema:

$$
\begin{alignat*}{2}
&X_1: \text{Cantidad de equipos de Combate del Fuego}
\quad &[X_1] =\text{equipos}/T \\

&X_2: \text{Cantidad de equipos de Apoyo Logístico}
\quad &[X_2] =\text{equipos}/T
\end{alignat*}
$$

Luego planteamos las restricciones, dadas por la limitación de recursos y la relación entre cantidad de equipos de cada tipo.

$$
\begin{alignat*}{2}
&\text{Brigadas}) &\quad X_1 + X_2 &\le 28\\

&\text{Autobombas}) &\quad 2X_1  &\le 16 \\

&\text{Helicópetros}) &\quad  X_2 &\le 8 \\

&\text{Drones}) &\quad X_1 + 2X_2 &\le 24 \\

&\text{Relación CF-AL})\quad &X_1 - 2X_2 &\le 0
\end{alignat*}
$$

El objetivo del problema será de maximización de la efectividad del plan a formar.

$$
Z(\max) = 10X_1 + 8X_2 
$$

## Planteo Matemático Dual

Definimos la correlación entre las variables del primal y las variables del dual.

$$
\begin{matrix}
Y_1 & Y_2 & Y_3 & Y_4 & Y_5 & Y_6 & Y_7 \\
| & | &| & | &| & | & |\\
X_3 & X_4 & X_5 & X_6 & X_7 & X_1 & X_2
\end{matrix}
$$

El planteo dual lo obtenemos al transmutar la matriz de coeficientes del problema dual, con los coeficientes del funcional como términos independientes.

$$
\begin{alignat*}{2}
&X_1) &\quad 1Y_1 + 2Y_2 +1Y_4 + 1Y_5&\ge 10\\

&X_2) &\quad 1Y_1 + 1Y_3 + 2Y_4 - 2Y_5  &\ge 8 \\

\end{alignat*}
$$

El objetivo del problema dual será de minimización de los valores marginales de los recursos.

$$
Z(\min) = 28Y_1 + 16Y_2 + 8Y_3 + 24Y_4 
$$

## Tabla Óptima Primal

|  |  |  | $10$ | $8$ |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $X_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ |
| $10$ | $X_1$ | $8$ | $1$ | $0$ | $0$ | $1/2$ | $0$ | $0$ | $0$ |
| $8$ | $X_2$ | $8$ | $0$ | $1$ | $0$ | $0$ | $1$ | $0$ | $0$ |
|  | $X_3$ | $4$ | $0$ | $0$ | $1$ | $\color{red}{\cancel{-1}} -1/2$ | $-1$ | $0$ | $0$ |
|  | $X_6$ | $0$ | $0$ | $0$ | $0$ | $-1/2$ | $-2$ | $1$ | $0$ |
|  | $X_7$ | $8$ | $0$ | $0$ | $0$ | $-1/2$ | $2$ | $0$ | $1$ |
|  |  | $Z = 144$ | $0$ | $0$ | $0$ | $5$ | $8$ | $0$ | $0$ |

## Tabla Óptima Dual

|  |  |  | $28$ | $16$ | $8$ | $24$ |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $C_k$ | $Y_k$ | $B_k$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ |
| $16$ | $Y_2$ | $5$ | $\color{red}{\cancel 1}\  1/2$ | $1$ | $0$ | $1/2$ | $1/2$ | $-1/2$ | $0$ |
| $8$ | $Y_3$ | $8$ | $1$ | $0$ | $1$ | $2$ | $-2$ | $0$ | $-1$ |
|  |  | $Z = 144$ | $-4$ | $0$ | $0$ | $0$ | $-8$ | $-8$ | $-8$ |

## Análisis de la Solución Óptima

- Obtenemos una puntuación de eficacia final de $144\ (Z)$.
- Formamos $8\ (X_1)$ equipos de *combate de fuego*, y $8\ (X_2)$ equipos de *apoyo logístico.*
- Tenemos un sobrante de $4\ (X_3)$ *brigadas.*
- Tenemos un sobrante de $8\ (X_7)$ equipos en la restricción de relación entre los equipos de combate de fuego y los equipos de apoyo logístico. Es decir, podríamos armar $8$ equipos más de combate de fuego, sin incumplir esa restricción.
- Saturamos totalmente las autobombas $(X_4)$.
- Saturamos totalmente los helicópteros $(X_5)$.
- Saturamos totalmente las drones $(X_6)$.
- Estamos ante un punto degenerado, ya que $X_6$ pertenece a la base con un valor nulo.

## Gráfica del Poliedro de Soluciones

Graficamos las restricciones para entender mejor la situación. El punto óptimo actual se encuentra en $X = (8, 8)$; en la gráfica, este punto corresponde a $B$.

Para el funcional, se graficó una recta que indica la dirección de mayor crecimiento. Podemos corroborar, a partir de visualizarla, la optimalidad del punto $B$.

Podemos visualizar que el punto óptimo se encuentra en la intersección de las restricciones: Drones, Helicópteros, y Autobombas. Del resto de recursos, tendremos sobrante.

También podemos observar que la restricción de brigadas se encuentra alejada del poliedro, y por lo tanto no lo afecta.

![[Apuntes/Modelos y Optimización I/Trabajo práctico - Análisis Post-Optimal/Attachments/Análisis Inicial 1.png|Untitled]]