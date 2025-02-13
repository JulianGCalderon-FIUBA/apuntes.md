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

Hay que analizar que el estado del sistema sea válido o inválido.

![[Estados del Sistema 1739238268.png]]

En este ejemplo, el estado $u_1 \cup u_0$ es válido, pero el estado $u_1 \cup t_0$ no lo es, puesto que $u_1$ depende del mensaje $m$ enviado por el evento $e_2$, que ocurrió luego de $t_0$.

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

El algoritmo tiene cuatro reglas principales:

- **Inicio del algoritmo**: Cuando un proceso quiere generar un corte (el observador), guarda su propio estado y envía un marcador al resto de procesos.
- **Primera recepción del marcador**: Cuando un proceso recibe un marcador por primera vez, envía su propio estado al observador, y comienza a registrar todos los mensajes recibidos exeptuando .
- **Siguientes recepciones del marcador**: Cuando un proceso vuelve a recibir un marcador, entonces envía todos los mensajes registrados hasta el momento al observador.
- **Fin del algoritmo**: Cuando el observador recibe el marcador de cada uno de los otros procesos, da por finalizado el algoritmo.

El corte final contendrá el estado al iniciar el algoritmo para cada proceso, y además todos los mensajes enviados antes de que finalice el corte.
