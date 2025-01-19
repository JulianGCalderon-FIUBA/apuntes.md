Se define el **estado local** $s_j$ de un proceso $j$ en un momento dado $t$, como una tupla con el valor de todas las variables.

$$
s_j = (X_0(t), X_1(t), \cdots, X_n(t))
$$

Se define el **estado global** es la unión de todos los estados locales del sistema.

$$
S = s_1 \cup s_2 \cdots \cup s_n
$$

## Máquina de Estados

En una máquina de estados, el estado en todo momento está dado por un estado anterior, y un evento que lo modifica. Es importante que las transiciones sean determinísticas.

La historia es la secuencia de todos los eventos procesados por la máquina de estados.

Un corte es el subconjunto de historias de todos los procesos hasta cierto evento $k$ de cada proceso.

Un corte es consistente si por cada evento que contiene, también contiene a aquellos que ocurren antes. El algoritmo de Chandy & Lamport se utiliza para obtener corte consistente de un sistema distribuido.
