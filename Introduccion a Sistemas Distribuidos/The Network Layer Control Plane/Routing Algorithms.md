El objetivo de un algoritmo de ruteo es el de determinar el camino que minimice el costo entre remitentes y receptores. Se puede utilizar un grafo para formular el problema, donde los nodos serán los ***routers*** y las aristas serán los enlaces entre los ***routers***. Cada enlace tendrá un costo asociado a múltiples factores, como el largo del enlace, la velocidad del mismo, el costo monetario de utilizarlo, etc. Diremos que dos nodos son vecinos si existe una arista directa que los une. Notemos que si todas las aristas tienen el mismo costo, entonces el camino más corto se transforma en el camino más eficiente.

Los algoritmos de rutina se pueden clasificar según si son centralizados o no:

- Un algoritmo de ruteo centralizado computará los caminos de menor costo utilizando el conocimiento global de la red. Se deberán conocer todos los ***routers***, enlaces, y sus costos. Son conocidos como ***link-state (LS) algorithms.***
- Un algoritmo descentralizado de ruteo computará los caminos de forma iterativa, ningún nodo conocerá el estado completo de la red. En su lugar, cada nodo comienza con el conocimiento de sus enlaces inmediatos, y a través de un proceso iterativo de cálculo e intercambio de información, gradualmente se calculará el camino óptimo

Una segunda forma de clasificarlos se según si son estáticos o dinámicos:

- En un algoritmo estático, las rutas cambiarán lentamente a lo largo del tiempo, debido a la intervención humana.
- En un algoritmo dinámico, las rutas cambiarán debido al tráfico de la red y cambios de topología. Estos pueden ser ejecutados periódicamente o en respuesta directa a un cambio.

Por último, podremos clasificar los algoritmos según si son ***load-sensitive*** o ***load-insensitive.*** En un algoritmo *load-sensitive*, los costos en los enlaces varían según el nivel de congestión de la red. Si un enlace tiene mucha congestión, se utilizará una ruta que evite ese enlace.

## 1. The Link-State (LS) Routing Algorithm

En un algoritmo de LS se requiere que todos los nodos tengan información completa acerca de la red. Para esto, todos los nodos realizan un ***broadcast*** de su información.

El algoritmo utilizado es el algoritmo de ***Dijkstra***. Una vez finalizado el algoritmo, la tabla de envío de cada nodo puede construirse a partir de almacenar para cada destino posible, el próximo nodo en el camino de menor longitud. La complejidad de este algoritmo es del orden de $O(n^2)$.

Los algoritmos de ruteo pueden fallar, causando oscilaciones, cuando el costo de los enlaces depende de la cantidad de tráfico. Una solución es decir que el algoritmo no dependerá del tráfico, pero esta solución no es aceptable.

Otra solución es la de asegurar que no todos los routers ejecutarán el algoritmo al mismo tiempo. Curiosamente, los tiempos de sincronización de los ***routers*** pueden sincronizarse con el tiempo de forma automática. Debido a esto, se podría aleatorizar el tiempo en el que envía un ***link advertisement***.

## 2. The Distance-Vector (DV) Routing Algorithm

Este algoritmo es iterativo (el proceso continúa hasta que no haya más información para intercambiar entre los vecinos), asincrónico (el algoritmo no requiere que los nodos operen de forma bloqueante los unos con los otros), y distribuido (todos los nodos reciben cierta información, realizan una calculación, y reenvían la información al resto de la red). Curiosamente, el algoritmo es ***auto-terminante***. No hay una señal para la finalización, simplemente lo hace. Este algoritmo es utilizado por muchos protocolos de rutina en la práctica.

Este algoritmo se desarrolló alrededor de la ecuación de ***Bellman-Ford***. Sea $dx(y)$ el camino de menor costo entre $x, y$. Entonces. $dx(y) = \min\{c(x,v) + dv(y): \forall v\}$, siendo $c(x,v)$ el costo de viajar desde el nodo $x$ a su adyacente $v$.

### Distance-Vector (DV) Algorithm

Cada nodo $x$ mantiene la siguiente información de ruteo:

- Por cada vecino $v$, el costo de viajar de $x$ hacia $v$.
- El vector de distancias de $x$. Un estimado del costo de viajar de $x$ a $y$, siendo $y$ cualquier nodo de la red.
- Los vectores de distancias de sus nodos vecinos

Cada cierto tiempo, cada nodo envía una copia de su vector de distancias a sus vecinos. Cuando un nodo $x$ recibe un vector de partes de alguno de sus vecinos, guarda el vector y utiliza la ecuación para actualizar su propio vector de distancias. Si el camino optimo es actualizado para algun destino, se reenvía a sus nodos vecinos. Este algoritmo converge al camino óptimo ideal.

Para actualizar la propia tabla de envío, se debe encontrar el nodo vecino siguiente en el camino de menor longitud. Este es, el vecino que alcance el mínimo en la ecuación de ***Bellman-Ford***.

### Distance-Vector Algorithm: Link-Cost Chances and Link Failure

Cuando un nodo ejecutando este algoritmo detecta un cambio en el costo, entonces actualiza su vector de distancias. Si hay algún cambio en el camino óptimo para alguno de los posibles destinos, se le informa a los nodos vecinos.

Es posible que se forme un bucle, en el cual un cambio local del vector de distancias cause que paquetes oscilan entres dos routers, hasta que el otro actualice su vector de distancias. Este problema es comúnmente referido como el ***count-to-infinity problem***.

### Distance-Vector Algorithm: Adding Poisoned Reverse

EL escenario descrito puede ser evitado utilizando una técnica conocida como ***poisoned reverse***. Cuando un router $z$ envía un paquete a $y$ para llegar a $x$, también le informa (miente) que su distancia a $x$ es infinito, evitando así que el router le devuelva el paquete enviado. Cuando $z$ actualiza su vector de distancias (cambiando así el ruteo de $z$ a $x$ para no pasar por $y$), entonces le informe del valor real de $dz(x)$.

Lamentablemente, los bucle de más de dos nodos no son solucionados a partir de esta técnica.

### A Comparison of LS and DV Routing Algorithms

Podemos analizar la diferencia entre estos algoritmos bajo tres categorías:

- ***Message Complexity:*** LS requiere que se envíen $O(N\cdot E)$ mensajes. Además cuando cambian los costos del enlace de un nodo, deberá enviar los nuevos costos a todos los nodos. Por otro lado, DV requiere que los mensajes se intercambian entre nodos vecinos tras cada iteración. El tiempo de convergencia dependerá de muchos factores. Cuando cambia el costo de un enlace, solo se enviaran mensajes si se cambia una ruta óptima
- ***Speed of Convergence:*** Vimos que la complejidad de LS es de $O(N^2)$. El algoritmo DV puede converger lentamente y formar bucles de rutina mientras está convergiendo. También sufre del problema de ***count-to-ininity***.
- ***Robustness:*** Bajo LS, el cómputo es separado en los distintos nodos, por lo que es un enfoque más robusto. Bajo DV, un error de cálculo puede ser por toda la red, causando grande problemas
