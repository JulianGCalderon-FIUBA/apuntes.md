Las funciones lógicas tienen dos valores posibles. $0,1$ Se pueden representar por una expresión algebraica a través de operadores lógicos $(+; .)$, o a través de tablas de verdad

# Tabla de Verdad

Cada función tiene definida una única tabla de verdad. Esta tabla indica cada resultado posible de la función

Supongamos todas las funciones lógicas posibles con dos variables. Algunas de estas funciones tienen nombre

$$

\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
a & b & f_1 & f_2 & f_3 & f_4 & f_5 & f_6 & f_7 & f_8 & f_9 & f_{10} & f_{11} & f_{12} & f_{13} & f_{14} & f_{15} & f_{16} \\
\hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1  & 1  & 1  & 1  & 1  & 1  & 1  \\
\hline
0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0  & 0  & 0  & 1  & 1  & 1  & 1  \\
\hline
1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0  & 1  & 1  & 0  & 0  & 1  & 1  \\
\hline
1 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1  & 0  & 1  & 0  & 1  & 0  & 1 \\
\hline
\end{array}

$$

Algunas de las funciones aca expresadas son conocidas

- $f_2 - \text{and}: a.b$
- $f_{15} - nand: \overline a + \overline b$
- $f_8 - or: a+b$
- $f_9 -nor: \overline a.\overline b$
- $f_7 - \text{xor}: \overline ab + a. \overline b$

# Expresión Algebraica

Cada función lógica tiene infinitas expresiones algebraicas que le corresponden, para eso, vamos a tratar con las expresiones canónicas. Dada la siguiente tabla de verdad, vamos a escribir su expresión algebraica de dos formas distintas.

![[Funciones Lógicas 1.png]]

## Suma de Minitérminos

Se genera a partir de las filas que contienen un $1$ en la columna de la función. Cada término contiene todas las variables booleanas multiplicadas, complementadas si valen $0$ en esa fila de la tabla

$$
f(A,B,C) = \sum[m(2, 4, 5, 6)] =\overline ab\overline c + a \overline b \overline c + a \overline b c + ab \overline c
$$

## Producto de Maxitérminos

Se genera a partir de las filas que contienen un $0$ en la columna de la función. Cada término contiene todas las variables booleanas sumadas, complementadas si valen $1$ en esa fila de la tabla

$$
f(a,b) = \Pi[M(0, 1, 3, 7)] =(a+b+c)(a+b+\overline c)(a + \overline b + \overline c)(\overline a + \overline b + \overline c)
$$
