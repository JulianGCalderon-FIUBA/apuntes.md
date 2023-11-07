Debemos tener tablas de hash distribuidas (DHT's) que permiten definir en que nodo se encontrará cierta información particular.

Este método no requiere de muchos cambios a medida que yo agrego información.

Para las consultas comunes, utilizamos las **tablas de hash distribuidas**. Para otras consultas más analíticas que requieren analizar mucha información, podremos no utilizarla y consultarle a todos los nodos.

## Hashing Consistente

En esta técnica, disponemos de una función de hash $h()$ que, dada una clave $k$, devuelve un valor $h(k)$ entre $0$ y $2^M-1$, en donde $M$ representa la cantidad de bits del resultado.

El valor de la función de hash para un par dado es lo que determina en cuál de los $S$ nodos el mismo será almacenado.

Al identificador de cada nodo de procesamiento se le aplica la misma función de hash. A partir de los *hashes*, los nodos organizan virtualmente en una estructura de anillo por hash creciente.

Un par $(k,v)$ se replicará en los $N$ servidores siguientes a $h(k)$, que conformarán el listado de preferencia para esa clave. Esto implica que si un servidor cae, entonces su servidor siguiente asumirá estas claves. (y debido a que la información está replicada, la puede obtener sin problema).

En otras implementaciones más triviales de una tabla de *hash* distribuida, en el que el nodo asignado se determina como $h(k) \text{ mod } S$. Esto genera un problema cuando un servidor se cae, ya que habría que reordenar las claves para el nuevo número de nodos.
