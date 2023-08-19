---
title: Proportional-Share Scheduler
---

A veces conocido como **fair-share scheduler,** este es un tipo distinto de planificador. En lugar de basarse alrededor de la optimización del *turnaround* o *response*, se trata de garantizar que cada proceso obtenga el mismo porcentaje de tiempo del CPU. Un ejemplo conocido de este tipo de planificador es: *lottery scheduling*.

Detrás de este planificador, existe un concepto muy simple: **tickets,** los cuales se usan para representar el porcentaje de un recurso que debe recibir un proceso. Para lograr esto, no se utiliza un enfoque determinístico, sino probabilístico. Los procesos con más tickets tienen más probabilidad de ser ejecutados.

Este planificador utiliza la aleatoriedad para tomar decisiones, un enfoque robusto y simple. Lo que proporciona tres ventajas claras. En primer lugar, los algoritmos basados en aleatoriedad no tienen **peores casos** como otros algoritmos, suelen funcionar bien en muchas circunstancias. En segundo lugar, estos algoritmos son ligeros, ya que no se requiere guardar mucha información. Por último, son rápidos.

Esta métrica $F$, se utiliza para medir la equidad del algoritmo. Se calcula como el tiempo que tarda el primer proceso en completarse, dividido el tiempo que tarda el segundo proceso en ejecutarse. Este valor tiende a $F=1$ cuando nuestro planificador es totalmente justo.

## Mecanismos

Este planificador también provee algoritmos para manipular los tickets de formas distintas. Cada usuario puede administrar sus tickets como desee, creando su propia moneda para manejarlos. El sistema, luego, convierte los tickets del usuario a una moneda global. Esto se llama *ticket currency.*

Otro mecanismo útil es el de **ticket transfer.** Los procesos pueden temporalmente entregarle sus tickets a otro proceso. Esto es útil cuando un proceso requiere de otro, por lo que puede optar por transferir sus tickets.

Finalmente, **ticket inflation** puede ser muchas veces una técnica útil. Mediante esta técnica, un proceso puede temporalmente aumentar o disminuir la cantidad de tickets que posee. Este concepto puede aplicarse en situaciones donde los procesos pueden confiar unos de otros.

## Implementación

La implementación de este algoritmo es muy simple. Lo único que se necesita es un generador de números aleatorios, una estructura para registrar los proceso del sistema, y el número total de tickets de cada uno.

Primero, debemos generar un número aleatorio dentro del número total de tickets. Luego, iteramos la lista de procesos utilizando un simple contador para elegir el proceso ganador.

## Stride Scheduling

Este es un planificador justo que no utiliza aleatoriedad. Para hacerlo, cada proceso tiene un **stride**, que es inversamente proporcional al número de tickets que tiene.

Cada vez que se ejecuta un proceso, se aumenta el contador *pass* de cada proceso en una medida de *stride* del mismo. El planificador elige el proceso según el que tenga el menor *pass*.

Este algoritmo tiene sus fallas. Cuando un proceso nuevo entra, ¿qué valor de *pass* se le asigna? Si se le asigna el valor cero, entonces monopolizará el control de la CPU. El planificador de lotería no tiene que guardar esta información ni tener en cuenta estas situaciones.

## The Linux Completely Fair Scheduler (CFS)

Este planificador apunta a ser eficiente y justo, dedicándole el menor tiempo posible a tomar decisiones. Para cumplir esto, depende de un buen diseño y un ingenioso uso de las estructuras de control.

Para dividir el uso del CPU entre todos los procesos, este planificador utiliza una simple técnica de conteo llamada **virtual runtime**, o *vruntime*. A medida que un proceso corre, acumula *vruntime*. El planificador siempre toma el proceso con **menor vruntime.**

Para definir los *time-slices* a utilizar, utiliza un parámetro llamado *sched_latency.* Se utiliza para definir que tanto deberá correr un proceso antes de considerar un *context switch*. Este número se dividirá por el número de procesos del sistema para determinar él *time slice* adecuado.

Cuando tenemos muchos procesos, se harán muchos cambios de contexto, lo que reducirá el rendimiento de la CPU. Para hacer esto, se introduce un nuevo parámetro: *min_granularity.* Es la mínima duración que tendrá un *time slice.*

### Niceness

El parámetro **nice** de un proceso puede tomar cualquier valor entre -20 y 19, con un valor por defecto de 0. Se utiliza para controlar la prioridad del mismo. Los valores negativos indican una mayor prioridad.

El planificador *mapea* este valor con el peso o *weight* de un proceso. Estos pesos se utilizan para controlar el *time slice* de cada proceso utilizando la siguiente fórmula

$$
\text{time\_slice}_k = \frac{\text{weight}_k}{\sum \text{weight}_i} \times \text{sched\_latency}
$$

También, el *vruntime* de cada proceso debe ser adaptado para utilizar los pesos. Esto se calcula con la siguiente fórmula.

$$
\text{vruntime}_i = \text{vruntime}_i + \frac{\text{weight}_0}{\text{weight}_i} \times \text{runtime}_i
$$

### Árbol Rojo-Negro

Para encontrar el próximo proceso a correr, el planificador utiliza este tipo de estructura. Este es un árbol balanceado que permite operaciones en tiempo logarítmico. El planificador solo mantiene procesos que estén listos para correr en la estructura.

### Lidiando con procesos frenados

Cuando un proceso fue frenado por un largo periodo de tiempo, su *vruntime* no estará ajustado y monopolizará el procesador. Para solucionar esto, el *vruntime* se actualiza cuando un proceso despierta. Este valor se establece al valor mínimo encontrado en el árbol.
