Se define el estado **local** como el conjunto de variables de un proceso en un momento dado.

El estado **global** es la unión de todos los estados del sistema.

En una máquina de estados, el estado en todo momento está dado por un estado anterior, y un evento que lo hace llegar al estado siguiente. Es importante que las transiciones sean determinísticas.

La historia es la secuencia de todos los eventos procesados por la máquina de estados. Un corte es el subconjunto de historias de todos los procesos hasta cierto evento $k$ de cada proceso.

Un corte es consistente si por cada evento que contiene, tambien contiene a aquellos que ocurren antes. El algoritmo de Chandy & Lamport se utiliza para corte consistente
