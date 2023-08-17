Para resolver problemas de programación lineal entera, tendremos distintas técnicas. Ninguna de ellas logra resolver el problema en tiempo polinomial, por lo que son muy costosas.

La técnica trivial para problemas cuyas variables son bivalentes es la de enumeración o fuerza bruta. Probamos todas las posibilidades hasta hallar la óptima.

Los métodos pseudo-booleanos son aquellos cuyas todas variables son **bivalentes**. En ese caso, el problema se convierte en un conjunto de expresiones de álgebra de Boole y se resuelve para maximizar la función objetivo.

## Branch & Bound

Tendremos un árbol de enumeración con la raíz correspondiente al problema real. El problema original se resuelve con programación lineal continua y se verifica si las variables deseadas tomaron valores enteros. Si tomaron valor entero, entonces finaliza el método.

Si alguna variable deseada no tomo valor entero, debemos aplicar **branching**. Este método consiste en dividir en dos el poliedro con el que estamos trabajando. Supongamos que la variable $X_2$ un valor continuo $\alpha$, entonces creamos dos subproblemas a partir del nodo raíz. Estos subproblemas contienen las mismas restricciones del problema anterior, y además $X_2 \leq \lfloor X_2 \rfloor$ o $X_2 \geq \lceil X_2 \rceil$, respectivamente.

Una vez realizada la bifurcación, resolvemos ambos problemas como si las variables fueran continuas (relajación lineal).

- Si alguno de los dos problemas encontró solución con las variables deseadas enteras, entonces anotaremos esta solución como una posible solución al problema entero.
- Si alguno de los dos problemas no encontró solución con las variables deseadas enteras, entonces continuaremos el algoritmo bifurcando dicha solución. En caso de que el funcional hallado sea menor que el de alguna solución entera ya hallada, entonces no valdrá seguir explorando este camino. Esto se debe a que al bifurcar el modelo, acortamos el poliedro de soluciones, por lo que el funcional solo podrá bajar. Esto se denomina **bound**.
- Si ninguno de los dos problemas encontró solución, se continúa con aquel de mayor funcional y el otro se deja en espera hasta agotar la otra rama elegida.
- Si alguno de los dos problemas no encontró solución (incompatible), entonces ignoramos esta rama (no bifurcamos).

Una vez se agotaron todas las ramas, entonces revisaremos los problemas recolectados y nos quedaremos con aquel que tenga el mayor funcional. Si hay más de una solución, entonces estas serán soluciones alternativas al problema.

## Planos de Corte

Este método consiste en resolver el problema con relajación lineal e ir agregando restricciones para acortar el poliedro de soluciones hasta llegar a una solución entera.

Definiremos algunos conceptos para comenzar a estudiar este método:

- Una **desigualdad válida** es aquella que se cumpla en todos los puntos del poliedro entero. Esta desigualdad puede ser válida para el problema entero, pero no para el continuo. Justamente son estos problemas los que nos interesan.
- Una **cara** es una desigualdad válida cuya intersección con el poliedro no sea vacía.
- Una **faceta** es una desigualdad válida cuya intersección con el poliedro tiene una dimensión menos que el poliedro original.
- Una **cápsula convexa** es el recinto más chico que contiene todas las soluciones factibles (enteras). Este se lo puede formular a partir de únicamente facetas. Todos los métodos que veremos se tratan de reducir el poliedro a su cápsula convexa equivalente.

Un **plano de corte** es una desigualdad válida entera que no es parte de la formulación original y no es satisfecha por la solución actual de la relajación lineal actual (continúa). Existe un algoritmo para encontrarlos.

Los **planos de corte generales** solo se basan en la condición de integralidad de las variables y pueden ser utilizados para cualquier problema de programación lineal entera, aunque suelen ser muy débiles.

### Planos de Corte Gomory

Partimos del problema original, con sus variables slack asociadas.

$$
\begin{align}
a_{11}X_1 + a_{12}X_2 + \cdots +a_{1n}X_n = b_1 \\
a_{21}X_1 + a_{22}X_2 + \cdots + a_{2n}X_n = b_2 \\
\cdots \\
a_{m1}X_1 + a_{m2}X_2 + \cdots + a_{mn}X_n = b_m \\\ \\
Z = c_1X_1 + c_2X_2 + \cdots + c_nX_n
\end{align}
$$

Luego, resolvemos el sistema lineal, para obtener cada una de las variables en función de otras. Del mismo modo, reemplazando los valores obtenidos, reemplazamos el funcional para que este también se halle a partir de las variables independientes. Denotamos con $' (\text{prima})$ los componentes del planteo equivalente, despejado. Notemos que podremos despejar tantas variables como ecuaciones tendremos.

$$
\begin{align}
X_1 = b_1' + a'_{1,m+1}X_{m+1} + a'_{1,m+2}X_{m+2} + \cdots + a'_{1,n}X_n \\
X_2 = b_2' + a'_{2,m+1}X_{m+1} + a'_{2,m+2}X_{m+2} + \cdots + a'_{2,n}X_n \\
\cdots \\
X_m = b_m' + a'_{m,m+1}X_{m+1} + a'_{m,m+2}X_{m+2} + \cdots + a'_{m,n}X_n \\\ \\
Z = c_1'X_1 + c_2'X_2 + \cdots c_m'X_m
\end{align}
$$

Este sistema de ecuaciones despejado, puede ser obtenido de la matriz de coeficientes de la tabla Símplex. Notemos que esta tabla ya tiene los vectores canónicos en las variables pertenecientes a la base.

Aplicamos al problema un plano de corte de **Chvatal/Gomory**, como:

$$
X_i + \sum_{k=m+1}^{n} \lfloor -a'_{ik} \rfloor X_k  \leq \lfloor \text{Valor de $X_i$}\rfloor,  j\in1,\cdots,m
$$

El signo menos de la ecuación corresponde a volver la restricción despejada a la forma normal (con coeficiente a la derecha). El término independiente de la ecuación será el valor que tomará $X_i$ en el óptimo actual, del problema con relajación lineal.

El algoritmo de resolución será entonces:

1. Resuelvo el problema con relajación lineal
2. Si la resolución es entera en las variables que deseamos, finalizamos el algoritmo.
3. Si la resolución no es entera. Identificamos una variable fraccionaria y agregamos el plano de corte. Esta nueva restricción puede ser agregada en el problema dual y volver a optimizar.
4. Volvemos al paso 1.

### Cortes para Problemas de la Mochila

Los cortes cover son utilizados para la resolución de problemas de la mochila. Trabajaremos con un ejemplo de restricción:

$$
11X_1 + 6X_2 + 6X_3 + 5X_4 + 5X_5 + 4X_6 + 7X_6 \leq 19
$$

Generaremos un corte **cover** a partir de una suma de elementos tal que la elección de todos ellos exceda el peso máximo permitido. Por ejemplo, si elijo $X_3, X_4, X_5, X_6$ me excedo del peso límite, pero si saco uno solo, los demás cumplen la restricción. Luego construyo el plano de corte:

$$
X_3 + X_4 + X_5 + X_6 \leq 3
$$

Un plano de corte **cover extendido** es aquel que agrega todos los elementos cuyo coeficiente es mayor al de todos los elementos del cover, entonces agregamos.

$$
X_1 + X_2 + X_3 + X_4 + X_5 + X_6 \leq 3
$$

Un plano de **corte lifteado** o ajustado es aquel que incrementa el coeficiente de los elementos agregados en el corte extendido, en función de la cantidad de peso que aportan. Por ejemplo, el peso de $X_2$ es similar al doble del peso del resto de elementos, luego si elijo este, debo sacar dos.

$$
2X_1 + X_2 + X_3 + X_4 + X_5 + X_6 \leq 3
$$

## Cortes para Problemas de Coloreo

Primero, debemos obtener un ciclo de grafo $C$, también llamado agujero. El agujero puede ser par o impar, según su cantidad de nodos. Si el agujero es par, no aporta nada para la técnica.

Si el agujero es impar, entonces planteamos la restricción

$$
\sum X_{ik} \leq \frac{|C| - 1}2 \cdot W_k
$$

Recordemos que la bivalente $X_{ik}$ toma valor si el nodo $i$ se pinta con el color $k$. $W_k$ toma valor si utilizamos el color $k$.

Si en lugar de un agujero, obtenemos una rueda $W$. Entonces podemos plantear un mejor plano de corte. El color del nodo central no podrá estar en ningún otro lugar de la rueda. Llamaremos $X_0$ al nodo central de la rueda. Luego planteamos

$$
\sum X_{ik} \leq \frac{|C| - 1}2 \cdot X_{0k}
$$
