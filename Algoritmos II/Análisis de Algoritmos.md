Una vez diseñado un algoritmo, es necesario analizar los recursos que consume, refiriéndose al tiempo e espacio que requiere su ejecución.

Los recursos que utiliza pueden ser:

- Memoria
- Ancho de Banda
- Hardware
- Tiempo Computacional

Hay muchas propiedades, además de tiempo y espacio, que son de interés para ser estudiadas, por lo que es difícil en ocasiones analizar un algoritmo.

- El **primer** enfoque para analizar algoritmos, se concentro en determinar el crecimiento del peor de los casos en lo que respecta a la eficiencia de un algoritmo.
- El **segundo** enfoque se concentro en categorizar el mejor, el peor, y el promedio de la eficiencia de un algoritmo.

## Complejidad de Un Algoritmo

Vamos a definir algunas funciones que permiten analizar la complejidad de un algoritmo. Estas funciones tienen una base matemática y estudian el comportamiento de los algoritmos en los casos limites.

### Big-O

Se dice que la tasa de crecimiento de un algoritmo es **Big-O:**

$$
T(N) = O(f(N)) \impliedby T(N) \leq c\cdot f(N):\quad c \in \mathbb{R}^+, N > N_0
$$

Esto quiere decir que la tasa de crecimiento $T(N)$ no superara $f(N)$. Es la cota superior

### Big-Omega

Se dice que la tasa de crecimiento de un algoritmo es **Big-Omega:**

$$
T(N) = \Omega(f(N)) \impliedby T(N) \geq c\cdot f(N):\quad c \in \mathbb{R}^+, N > N_0
$$

Esto quiere decir que, para algún valor de $c$, la tasa de crecimiento $T(N)$ nunca sera menor a $f(N)$. Es la cota inferior

### Small-O

Se dice que la tasa de crecimiento de un algoritmo es **Small-o:**

$$
T(N) = o(f(N)) \impliedby T(N) < c \cdot f(N):\quad \forall c \in \mathbb{R}^+, N > N_0
$$

Esto quiere decir que la tasa de crecimiento $T(N)$ es estrictamente menor a la de $f(N)$.

### Big-Theta

Se dice que la tasa de crecimiento de un algoritmo es **Big-Theta:**

$$
T(N) = \Theta(f(N)) \impliedby T(N) = O(f(N)),\quad T(N) = \Omega(f(N))
$$

Esto quiere decir que la tasa de crecimiento va a estar acotada por una tasa superior e una inferior. Es tanto **Big-O**, como **Big-Omega**.

## Teorema Maestro

Es el "libro de cocina" para resolver recurrencias de la forma:

$$
T(n) = a(T(n/b)) + f(n)
$$

Donde el algoritmo es una función recursiva que divide el problema $b$ veces y resuelve $a$.

- $n:$ Equivale al tamaño del problema
- $a:$ Equivale a la cantidad de llamadas recursivas que hago
- $b:$ Equivale a en cuanto divido el problema
- $f(n):$ Es el costo de dividir y combinar el problema

Entonces, el algoritmo posee las siguientes cotas asintóticas:

$$
T(n):\begin{cases} 

f(n) < n^{log_ba} \implies T(n) = \Theta(n^{log_ba} ) \\ 

f(n) = n^{log_ba} \implies T(n) = \Theta(n^{log_ba} \cdot log( n)) \\

f(n) > n^{log_ba} \implies T(n) = \Theta(f(n))

\end{cases}
$$
