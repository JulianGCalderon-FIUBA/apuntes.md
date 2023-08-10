El método ***Simplex***, desarrollado por ***George Dantzig*** en 1947, se utiliza para resolver problemas de programación lineal continua, de forma eficiente.

Una vez planteado el problema con las inecuaciones, el modelo deberá transformar las inecuaciones en igualdades utilizando las variables ***slack***.

> [!example]- Planteo Del Problema
> 
> Partiremos de un ejemplo de un modelo simple, utilizando únicamente restricciones de menor o igual.
> 
> ```bash
> maximize 8*X1 + 10*X2;
> 
> 2*X1 + 2*X2 <= 600;
> 4*X2 <= 600;
> 2*X1 + 4*X2 <= 801;
> end;
> ```
> 
> Automáticamente, el *software* generará las variables ***slack*** necesarias para convertir las desigualdades en igualdades. Además, en el funcional todas la variables deben tener un coeficiente (puede ser cero)
> 
> ```bash
> maximize 8*X1 + 10*X2 + 0*X3 + 0*X4 + 0*X5;
> 
> 2*X1 + 2*X2 + X3 = 600;
> 4*X2 + X4 = 600;
> 2*X1 + 4*X2 + X5 = 801;
> ```

## Modelo Matemático

Algebraicamente, nuestros modelos transformados tendrán la siguiente forma:

$$
\begin{align*}
Z = &\sum_{j = 1}^n c_jx_j  \\
&x_j \geq 0 ,&\forall j = 1, \cdots, n \\
&\sum_{j=1}^n a_{ij}x_{j} = b_i ,&\forall i = 1,\cdots, m
\end{align*}
$$

Se definen las variables:

- $c_j:$ Son los coeficientes asociados a las variables $x_j$. Las variables ***slack*** también seran tenidas en cuenta.
- $a_{ij}:$ El coeficiente de la variable $j$ en la restricción $i$
- $b_i:$ El termino independientes de la restricción $i$

Matricialmente podremos reescribir el modelo,

$$
\begin{align*}
Z = \ & CX  \\
&X \geq 0 \\
&AX = B
\end{align*}
$$

Análogamente definimos, siendo $n$ la cantidad de variables, y $m$ la cantidad de restricciones:

- $C^{1\times n}:$ Vector de coeficientes de las variables en el funcional.
- $X^{n\times 1}:$ Vector de variables del problema.
- $A^{m\times n}:$ Matriz de coeficientes de las variables en las restricciones.
- $B^{m\times 1}:$ Vector de términos independientes de las restricciones.
- ***Planteo Matricial***

	A partir de los datos del problema, transformamos la forma algebraica a su forma matricial. El vector $C$ tendrá los coeficientes del funcional, entonces:

	$$
	Z =
    \begin{pmatrix}
    8 & 10 & 0 & 0 & 0
    \end{pmatrix}
    \begin{pmatrix}
    x_1 & x_2 & x_3 & x_4 & x_5
    \end{pmatrix}^T
	$$

	La matriz $A$ tendrá los coeficientes de las restricciones, y el vector $B$ tendrá los términos independientes, entonces:

	$$
    \begin{pmatrix}
    2 & 2 & 1 & 0 & 0 \\
    0 & 4 & 0 & 1 & 0 \\
    2 & 4 & 0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
    x_1 \\
    x_2 \\
    x_3 \\
    x_4 \\
    x_5
    \end{pmatrix} =
    \begin{pmatrix}
    600 \\
    600 \\
    801
    \end{pmatrix}
    $$

	Notamos que debido a las restricciones ***slack***, podremos hallar una matriz ***identidad*** dentro de $A$.

## Teoremas

Debido a que el funcional es una función lineal, hallaremos el máximo (o el mínimo) en uno de los vértices del poliedro de soluciones factibles. Para reconocer un vértice, sabemos que la cantidad máxima de variables que pueden ser distintas de cero en un vértice es igual a la cantidad de restricciones que tiene el problema (en nuestro caso hay tres restricciones).

Para desarrollar el método, ***Dantzig*** se basó en varios teoremas:

### Teorema 1

El conjunto de todas las soluciones factibles a un problema de programación lineal es un conjunto convexo (poliedro convexo).

A partir ***de este teorema, podemos concluir que cuando encontramos un óptimo local (su funcional es mayor al de todos sus vértices adyacentes), entonces estamos también ante un óptimo global.

### Teorema 2

La función objetivo alcanza su mínimo (o máximo) en un punto extremo del conjunto convexo $K$ de soluciones factibles del problema de programación lineal. Si alcanza ese mínimo (máximo) en más de un punto extremo, entonces la función objetivo tiene el mismo valor para cualquier combinación convexa de esos puntos extremos.

### Teorema 3

Si se puede encontrar en la matriz $A$ del problema un conjunto de $m$ vectores $A_1, A_2, \cdots, A_m$ linealmente independientes y tal que $x_1 A_1 + x_2A_2 + \cdots + x_mA_m = B$ y todos los $x_i \geq 0$. Entonces este es un punto extremo del conjunto convexo de soluciones posibles.

$X$ es un vector $n$-dimensional cuyos últimos $n-k$ elementos son cero.

Para encontrarse en un extremo, deben intersecar $n-k$ restricciones, por cada restriccisón, su variable ***slack*** debe ser 0, entonces hay por lo menos $n - k$ variables que valen cero. Luego a lo sumo tendremos $k$ variables con valor positivo.

### Teorema 4

Si $X = (x_1, x_2, \cdots, x_n)$ es un punto extremo del poliedro, entonces los vectores asociados con las componentes $x_i$ que son mayores que cero forman un conjunto linealmente independiente.

### Teorema 5

$X = (x_1, x_2, \cdots, x_n)$ es un punto extremo del poliedro si y solo si las componentes $x_i$ que son mayores que cero están asociadas con vectores linealmente independientes de $A$ en $\sum_{j=1}^n x_jA_j = B$

### Consecuencia

Como consecuencia, se deduce que:

1. Existe un punto extremo del poliedro de $K$ soluciones factibles en el cual la función objetivo alcanza su máximo (mínimo).
2. Cada solución factible básica corresponde a un punto extremo del poliedro solución $K$
3. Cada punto extremo de $K$ tiene asociados, a el $m$ vectores linealmente independientes del conjunto dado de $n$ vectores asociados con el. Estos corresponderán a los asociados a las variables positivas. Las restantes variables tendran valores nulos.

## Resolución

Se plantea un esquema de tabla por cada vértice, de la siguiente forma:

$$
\begin{array}{|c c c|c c c c c|}
\hline
C & X & B & A_1 & A_2 & A_3 & A_4 & A_5\\
\hline
\\
 \\
\hline
\end{array}
$$

El significado de las columnas será, para un vértice dado:

- $C:$ Coeficiente que tienen en el funcional las variables distintas positivas.
- $X:$ Nombre de las variables que son positivas.
- $B:$ Valor que toman las variables que son distintas de cero.
- $A_j:$ Columna $j$ de la matriz $A$

El método simplex elige comenzar por el vértice en el cual las variables reales son cero. Esto tiene la ventaja de que los vectores de las variables positiva son canónicos distintos y, por lo tanto, linealmente independientes:

> [!example]- Vectores Iniciales
> 
> $$
> A =\begin{pmatrix}
> 2 & 2 & 1 & 0 & 0 \\
> 0 & 4 & 0 & 1 & 0 \\
> 2 & 4 & 0 & 0 & 1
> \end{pmatrix}
> $$
> 
> $$
> AX = B \\
> \begin{pmatrix}
> 2 & 2 & 1 & 0 & 0 \\
> 0 & 4 & 0 & 1 & 0 \\
> 2 & 4 & 0 & 0 & 1
> \end{pmatrix}
> \begin{pmatrix}
> x_1 \\
> x_2 \\
> x_3 \\
> x_4 \\
> x_5 \\
> \end{pmatrix} = B
> $$
> 
> $$
> x_1 \begin{pmatrix}
> 2 \\
> 0 \\
> 2
> \end{pmatrix} +
> x_2 \begin{pmatrix}
> 2 \\
> 4 \\
> 4
> \end{pmatrix} +
> x_3 \begin{pmatrix}
> 1 \\
> 0 \\
> 0
> \end{pmatrix} +
> x_4 \begin{pmatrix}
> 0 \\
> 1 \\
> 0
> \end{pmatrix} +
> x_5 \begin{pmatrix}
> 0 \\
> 0 \\
> 1
> \end{pmatrix} =
> B
> $$
> 
> Entonces, un punto extremo sera $X = (0, 0, 600, 600, 801)$ debido a que los vectores asociados a las componentes positivas forman la base canónica.

> [!example]- Tabla Inicial
> 
> Desarrollamos la tabla del vértice inicial para el problema dado.
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | 0 | $x_3$ | 600 | 2 | 2 | 1 | 0 | 0 |
> | 0 | $x_4$ | 600 | 0 | 4 | 0 | 1 | 0 |
> | 0 | $x_5$ | 801 | 2 | 4 | 0 | 0 | 1 |

### ¿Como sabemos si el vértice hallado es óptimo?

Siendo $A$ la matriz de la tabla, se define $A_{ij}$ como la reducción de la variable $i$ por cada unidad de $j$ que aumento. Entonces $z_j$ equivale a la reducción del funcional esperada por cada unidad de $j$ que me fuerzo a producir, sin tener en cuenta la mejora de funcional que obtengo tras agregar la unidad.

Debemos calcular, para cada columna $A_j$, el valor de $z_j - c_j$, siendo $z_j = C \times A_j$. Este sera el desmejoro unidad total si se introduce la variable $x_j$ a la base. Para cada tabla, se calcula el próximo funcional como $Z_{p+1} = Z_p - \theta_{\min}(z_j - c_j)$

> [!example]- Calculo de $z_j - c_j$
> Calculamos para cada columna:
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | $0$ | $x_3$ | $600$ | $2$ | $2$ | $1$ | $0$ | $0$ |
> | $0$ | $x_4$ | $600$ | $0$ | $4$ | $0$ | $1$ | $0$ |
> | $0$ | $x_5$ | $801$ | $2$ | $4$ | $0$ | $0$ | $1$ |
> | | | $Z = 0$ | $-8$ | $-10$ | $0$ | $0$ | $0$ |

#### Teorema A

Si existe alguna columna $j$ de la matriz $A$ para la cual $z_j - c_j < 0$ (para un problema de máximo) entonces puede construirse un conjunto de soluciones posibles tal que su $Z$ es mejor que el actual, donde el límite superior de $Z$ puede ser finito o infinito.

#### Teorema B

Dado un $Z$ de máximo, si para una solución básica factible $X = (x_1, x_2, \cdots, x_m)$ las condiciones $z_j - c_j \geq 0$ se cumplen para todas las $j = 1, \cdots, n$, entonces $X$ es una solución factible máxima.

### ¿Como encontramos el próximo vértice?

Para hallar el nuevo vértice, un vector debe salir de la base, y otro debe entrar. Para determinar cual vector ingresa, elegimos alguno cuyo $z_j - c_j$ sea negativo.

Para determinar que vector sale de la base, debemos calcular el coeficiente $\theta$ para cada vector de la base. Siendo $j$ el vector entrante a la base, se calculara como $\theta_i = B_i/A_{ij}$, para todas las filas de la tabla con coeficiente positivo:

- Si el coeficiente es negativo, entonces la variable saliente aumentara por lo que nunca se podrá llegar a cero (no podremos sacar a esta variable).
- Si el coeficiente es cero, nuevamente no podremos sacar la variable ya que esto indicaria que son independientes ambas variables (al aumentar una, la otra permanece constante).
- Si el coeficiente es positivo, entonces el valor indica cuanto debo utilizar de la variable entrante para reducir la variable saliente a cero.

Tendremos que elegir el menor de los tres cocientes (se toman los casos invalidos como infinito), ya que elegir uno mayor causará que las variables que tenían cocientes menores tomen valores negativos.

> [!example]- Calculo de $\theta$
> 
> Para este ejemplo, se ingresara el vector $A_1$
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $\theta$ |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | $0$ | $x_3$ | $600$ | $2$ | $2$ | $1$ | $0$ | $0$ | $300$ |
> | $0$ | $x_4$ | $600$ | $0$ | $4$ | $0$ | $1$ | $0$ | - |
> | $0$ | $x_5$ | $801$ | $2$ | $4$ | $0$ | $0$ | $1$ | $400.5$ |
> | | | $Z = 0$ | $-8$ | $-10$ | $0$ | $0$ | $0$ | |

### ¿Como construimos la siguiente tabla?

Inicialmente, planteamos la tabla con los valores ya conocidos. Los coeficientes y las variables a tomar valor. Ademas, las columnas de las variables de la base deben tener la base canónica. El vector entrante deberá ser reemplazado por el vector saliente.

> [!example]- Planteo Inicial
> Quitamos la variable $x_3$ y entramos la variable $x_1$:
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | $8$ | $x_1$ | | $1$ | | | $0$ | $0$ |
> | $0$ | $x_4$ | | $0$ | | | $1$ | $0$ |
> | $0$ | $x_5$ | | $0$ | | | $0$ | $1$ |

En definitivamente, estaremos realizando un cambio de base para que los vectores canónicos le correspondan a los elementos que estarán en la base.

Para calcular el resto de valores, utilizamos la técnica del pivote. Se llama pivote de una tabla al elemento que está en la intersección de la columna de la variable que entra y la fila de la variable que sale. El pivote lo tomaremos de la tabla anterior.

1. Dividimos todos los elementos de la fila de la variable que ingresa por el valor del pivote
2. Para cada valor restante, se forma un cuadrilátero con las esquinas en el pivote y el valor anterior de la posición que queremos calcular. El nuevo valor se calculara como, la resta entre el valor anterior de la posición que queremos calcular, y el producto de las diagonales del rectángulo dividido por el pivote.

$$
\text{Valor Nuevo} = \text{Valor Anterior} - \frac{\text{Producto de las Diagonales}}{\text{Pivote}}
$$

> [!example]- División por Pivote
> 
> Debido a que ingresa la variable $x_1$ y sale la variable $x_3$, el valor del pivote será de: $2$.
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | $8$ | $x_1$ | $300$ | $1$ | $1$ | $0.5$ | $0$ | $0$ |
> | $0$ | $x_4$ | | $0$ | | | | |
> | $0$ | $x_5$ | | $0$ | | | | |

> [!example]- Regla del Cuadrilátero
> 
> Teniendo la tabla anterior, resaltamos los elementos:
> 
> - ***Rojo: Valor Pivote**
> - ***Verde: Valor Anterior**
> - ***Azul: Diagonales**
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | $0$ | $x_3$ | $\color{Teal}{600}$ | $\color{Red} 2$ | $2$ | $1$ | $0$ | $0$ |
> | $0$ | $x_4$ | $\color{Green}{600}$ | $\color{Teal}0$ | $4$ | $0$ | $1$ | $0$ |
> | $0$ | $x_5$ | $801$ | $2$ | $4$ | $0$ | $0$ | $1$ |
> | | | $Z = 0$ | $-8$ | $-10$ | $0$ | $0$ | $0$ |
> 
> Luego, calculamos en la nueva tabla el valor, como $600 - (0\cdot600)/2 = 600$
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | $8$ | $x_1$ | $300$ | $1$ | $1$ | $0.5$ | $0$ | $0$ |
> | $0$ | $x_4$ | $\color{Green}{600}$ | $0$ | | | $1$ | $0$ |
> | $0$ | $x_5$ | | $0$ | | | $0$ | $1$ |
> 
> Repetimos esta lógica para el resto de elementos de la tabla
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | $8$ | $x_1$ | $600$ | $1$ | $1$ | $0.5$ | $0$ | $0$ |
> | $0$ | $x_4$ | $600$ | $0$ | $4$ | $0$ | $1$ | $0$ |
> | $0$ | $x_5$ | $200$ | $0$ | $2$ | $-1$ | $0$ | $1$ |

### Finalización

Esta secuencia de pasos se repite hasta que lleguemos a una solución optima.

> [!example]- Tabla Final
> 
> Podemos observar que no hay valores negativos en la ultima fila, por lo que nos encontramos ante un punto optimo
> 
> | $C$ | $X$ | $B$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | 8 | $x_1$ | 199.5 | 1 | 0 | 1 | 0 | -1/2 |
> | 0 | $x_4$ | 198 | 0 | 0 | 2 | 1 | -2 |
> | 10 | $x_2$ | 100.5 | 0 | 1 | -1/2 | 0 | 1/2 |
> | | | 2601 | 0 | 0 | 3 | 0 | 1 |

### Problemas de Minimización

Si lo que queremos es disminuir el valor del funcional, entonces las variables que entraran a la base serán las que tendrán un valor positivo de $z_j - c_j$. Hallaremos el mínimo si son todos negativos.

### Restricciones de Mayor Igual

Supongamos la siguiente restricción:

$$
x_1 \geq 2
$$

Luego de agregar las variables ***slack***, tendremos:

$$
x_1 - x_2 = 2
$$

Para resolverlo por el método simplex, agregamos una nueva variable

$$
x_1 -x_2 + \mu_1 = 2
$$

En el funcional, agregamos

$$
Z_{\max} = x_1 + 2x_2 - M\mu_1
$$

Si nos encontramos por debajo de la restricción de mayor o igual, entonces la variable $\mu_1$ tomará valor. Forzaremos a que esta variable no tome valor con agregarla en el funcional. El método nunca le dará valor a esta variable debido a su alto peso en el funcional.

La razón por la que debemos agregar la variable ficticia $\mu_1$ es para permitirnos comenzar desde el eje de coordenadas. De otra forma deberíamos encontrar inicialmente un vértice que cumpla las restricciones.

### Restricciones de Igualdad

Tambien debemos agregar variables ficticias para que el funcional la haga valer cero

$$
x_1 = 0
$$

$$
x_1 + \mu_1 = 0
$$

$$

Z_{\max} = x_1 + 2x_2 - M\mu_1

$$

De la misma forma que antes, permitimos utilizar el vértice inicial como punto de comienzo.

## Casos Particulares

### Soluciones Alternativas Optimas

Cuando el $z_j - c_j = 0$, para una variable que no se encuentra en la base, entonces estaremos ante una solución alternativa. Si cambiamos la variable, veremos que en la siguiente tabla, tendremos una variable (la que acabamos de sacar de la base) con $z_j - c_j = 0$.

### Punto Degenerado

Tendremos un punto donde habrá dos $\theta$ mínimos, uno de los valores de las variables ingresadas sera cero. En este caso, la próxima tabla sera la de un punto degenerado. Una vez en la nueva tabla, se puede observar que en la base, hay una variable con valor cero.

El coeficiente $\theta$ de la variable con valor cero no deberá ser calculado si el coeficiente para el vector que voy a entrar próximamente es negativo (estaría realizando un paso hacia atrás algorítmicamente). En otro caso, si lo debo calcular y tendrá un valor de cero.

En un punto degenerado, dos tablas diferentes muestran el mismo vértice. Hay casos donde puedo llegar a alcanzar un ciclo donde llego a una tabla donde ya estuve. Para salir del ciclo, debo buscar en alguna de las tablas y descartar uno de los $\theta = 0$, eligiendo otro vértice.

### Poliedro Abierto

Ocurre cuando una variable quiere entrar a la base, pero ninguna puede salir (no habrá ningún $\theta$ valido). Hay soluciones, pero ninguna es la optima.

### Problema Incompatible

Ocurre cuando se halla una solución optima, pero una variable artificial $\mu$ se encuentra en la base. Esto indica que la supuesta solución optima es en realidad, incompatible.
