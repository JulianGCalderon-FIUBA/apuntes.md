Se define el **estado local** $s_j$ de un proceso $j$ en un momento dado $t$, como una tupla con el valor de todas las variables.

$$
s_j = (X_0(t), X_1(t), \cdots, X_n(t))
$$

Se define el **estado global** es la unión de todos los estados locales del sistema.

$$
S = s_1 \cup s_2 \cdots \cup s_n
$$

## Máquina de Estados

En una máquina de estados, el estado en todo momento está dado por un estado anterior, y un evento que lo modifica. Es importante que las transiciones sean determinísticas, esto permite volver hacia atrás en el tiempo y continuar con la ejecución, volviendo al estado actual.

![[Estados del Sistema 1737246065.png]]

## Historia y Corte

Se define **historia** $h_i$ o corrida, como la secuencia de todos los eventos procesados por un solo proceso $p_i$.

$$
h_1 = (e_0, e_1, e_2, \cdots)
$$

Se define **corte** $C$ como el subconjunto de historias de todos los procesos hasta cierto evento $k$ de cada proceso.

$$
C = h_0 \cup h_1 \cup \cdots \cup h_n
$$

Se dice que un corte es **consistente** si por cada evento que contiene, también contiene a aquellos que ocurren antes: $\forall e \in C: f \to e \implies f \in C$

![[Estados del Sistema 1737246521.png]]

## Algoritmo de Chandy & Lamport

Es un algoritmo que permite obtener *snapshots* (o cortes consistentes), de estados globales en sistemas distribuidos.

El algoritmo toma las siguientes suposiciones:

- Los procesos y canales de comunicación no fallan.
- Los canales son unidireccionales y tienen un [[Orden de Mensajes#Orden FIFO|orden fifo]].
- El grafo de comunicación es fuertemente conexo.
- Cada proceso puede iniciar un snapshot en cualquier momento.
