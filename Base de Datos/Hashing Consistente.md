Disponemos de una función de hash $h()$ que, dada una clave $k$, devuelve un valor $h(k)$ entre $0$ y $2^M-1$, en donde $M$ representa la cantidad de bits del resultado.

El valor de la función de hash para un par dado es lo que determina en cuál de los $S$ nodos el mismo será almacenado.

En otras implementaciones más triviales de una tabla de *hash* distribuida, en el que el nodo asignado se determina como $h(k) \text{ mod } S$, existe un problema cuando un servidor se cae. Habría que reordenar las claves para el nuevo número de nodos.

Al identificador de cada nodo de procesamiento se le aplica la misma función de hash. A partir de los *hashes*, los nodos organizan virtualmente en una estructura de anillo por hash creciente.

Un par $(k,v)$ se replicará en los $N$ servidores siguientes a $h(k)$, que conformarán el listado de preferencia para esa clave. Esto implica que si un servidor cae, entonces su servidor anterior asumirá estas claves. (y debido a que la información esta replicada, la puede obtener sin problema)
