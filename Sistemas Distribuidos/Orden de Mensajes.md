La recepción de los mensajes no es lo mismo que el *delivery* de los mismos.

- La recepción consiste en que los mensajes lleguen al sistema
- El delivery consiste en procesar los mensajes, provocando cambios en el sistema.

Los mensajes se mantienen en una cola, llamada *hold-back queue*, permitiendo demorar su delivery. Esto también permite reordenarlos.

Por ejemplo, el protocolo TCP demora el delivery de los mensajes para asegurar que los mismos estén ordenados.

## Orden Sincrónico

Se asume que el tiempo de delivery es nulo, por lo que no hay necesidad de ordenar mensajes, o de demorarlos.

## Orden FIFO

^1dd0f4

Todo par de mensajes desde un mismo emisor a un mismo receptor, son entregados en el orden que fueron enviados.

![[Orden de Mensajes 1737241103.png]]

Este orden no requiere sincronizar relojes para implementarse.

## Orden Causal

Todo mensajes que implique la generación de un nuevo mensaje, debe ser entregado manteniendo esta secuencia de causalidad.

![[Orden de Mensajes 1737241219.png]]

El mensaje $M_1$ causa el mensaje $M_2$, y este a su vez causa el mensaje $M_3$. Luego, vemos como desde $P_1$, el delivery de $d_3$ es retrasado de modo que sea entregado luego de $d_2$.

Una forma de implementarlo podría ser agregar en cada mensaje una lista de dependencias.

## Orden Total

Todo par de mensajes entregado a los mismos receptores es recibido en el mismo orden por esos receptores

![[Orden de Mensajes 1737241468.png]]

En el ejemplo, vemos como ambos receptores reciben los dos mensajes en el mismo orden, independiente de cuando fueron enviados.

El orden total no es excluyente con el orden causal.
