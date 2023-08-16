---
title: Multi-Level Feedback Queue
---

Este es uno de los enfoques más conocidos para la planificación. El problema fundamental que este enfoque trata de solucionar es minimizar tanto el ***turnaround time*** como el ***response time***. Para realizar esto, en lugar de depender de conocimiento ***a priori*** de los procesos, se observa su ejecución.

## Reglas Básicas

Este algoritmo utiliza un número de colas distintas, donde cada una tiene asignada un cierto nivel de prioridad. Se utiliza un sistema de prioridad para decidir que proceso ejecutar. Cuando algunos procesos tienen la misma prioridad, entonces se utiliza el algoritmo ***round robin***.

- **Regla 1:** `if priority(A) > priority(B), A runs`
- **Regla 2:** `if priority(A) > Priority(B), A & B run in RR`

La clave de este algoritmo reside en como se calculan estas prioridades. En lugar de darle un prioridad fija a cada proceso, esta varía según el comportamiento observado del proceso a medida que corre.

Los ***time-slice*** para cada prioridad suele variar. Las colas con mayor prioridad tendrán menos tiempo de ejecución. Por otro lado, los ***time-slice*** largos suelen funcionar bien para procesos largos.

Algunas implementaciones reservan las colas de máxima prioridad para procesos del sistema, dejando los procesos de usuario con menor prioridad.

Otras, permiten al usuario ayudar a configurar la prioridad de su ejecución.

## Cambio de Prioridad

Para cambiar la prioridad de un proceso, se introducen nuevas reglas a nuestro algoritmo. Se tiene en cuenta nuestra carga de trabajo usual: Una mezcla de procesos cortos e interactivos, y algunos procesos largos que necesita mucho tiempo de procesamiento, donde el **response** no es tan importante.

- ***Regla 3:*** Cuando un proceso llega al sistema, este se coloca en la cola de máximas prioridad
- **Regla 4a:** Si un proceso utiliza todo su *time-slice*, su prioridad se reduce.
- **Regla 4b:** Si un proceso delega el procesador antes de que termine su time-slice, entonces se mantiene con el mismo nivel de prioridad.

Cuando el proceso delega el control, por ejemplo para un pedido de **IO**, entonces su prioridad no se reduce. No queremos penalizar un proceso interactivo.

Hasta ahora. nuestro planificador es justo entre procesos largos, dejando que los procesos interactivos y cortos corran rapido.

Sin embargo, aún tenemos algunos problemas:

- ***Starvation:*** Si tenemos demasiados procesos interactivos, estos consumirian el procesador sin dejar que los procesos largos terminen.
- ***Cambio de Comportamiento:*** Si un proceso cambia de comportamiento durante la ejecución, este tendrá una prioridad no acorde a la que debería tener (por ejemplo, pocos pedidos de ***IO*** al principio, pero muchos al final).
- ***Cheating***: Si los procesos están al tanto del planificador, estos pueden delegar el control voluntariamente para no perder prioridad

## Priority Boost

Para encarar los primeros dos problemas mencionados, se introduce el concepto de ***priority boost***. De forma periódica, se aumenta la prioridad de los procesos.

- **Regla 5:** Luego de un cierto período, todos los procesos vuelven a la cola máxima prioridad.

De esta forma, se garantiza que ningún proceso sufra de ***starvation***. Por el otro lado, si un proceso cambia de comportamiento, será tratado de forma correcta una vez reciba el ***boost***.

Surge la pregunta entonces, ¿Qué duración deberá tener el periodo de tiempo entre ***boosts?*** Si este periodo se muy largo, entonces los procesos largos sufrirán ***starvation;*** Si es muy corto, lo procesos interactivos no serán tratados correctamente. Algunos algoritmos varían estos parámetros durante la ejecución, utilizando fórmulas matemáticas.

## Accounting

Para solucionar nuestro último problema, debemos realizar una mejor contabilización. En lugar de olvidarse cuando ***time-slice*** le quedaba a un proceso cuando delegó el procesamiento, podemos tenerlo en cuenta para nuestro cálculo de prioridad. Entonces, volveremos a escribir nuestra cuarta regla

- **Regla 4:** Una vez un proceso haya usado un ***time-slice*** completo, independiente de cuantas veces haya cedido el procesador, su prioridad se reducirá en uno.
