Se introduce el concepto de ***lock***, estos permiten exclusión mutua de una parte del código para prevenir condiciones de carrera. Las secciones críticas se ejecutan como si fuesen operaciones atómicas.

Una lock es una variable, esta almacena su estado interno en un instante de tiempo. Permitiendo que solo un hilo pueda adquirir el ***lock***. Dentro también se puede almacenar otra información, como una cola de adquisición, o a que hilo le pertenece.

El nombre de la biblioteca que usa los ***locks*** se llama ***mutex***, ya que provee ***mutual exclusión*** entre ***threads***.

La semántica de las rutinas es simple: Llamar a `lock()` para tratar de adquirir el ***lock***, si ningún otro ***thread*** lo tiene, entonces se adquiere el ***lock*** y se entra en una sección crítica. Si otro ***thread*** tiene el ***lock***, entonces se espera a que se libere. Una vez el dueño del ***lock*** lo libera, este esta libre nuevamente para que otro ***thread*** lo acceda.

# Evaluación de *Locks*

Antes de construir un ***lock,*** necesitamos entender su objetivo y como evaluar su eficacia. Existen un par de criterios para esto:

- ***Correctness***:** U*n *lock* debe poder realizar su tarea básica, proveer exclusión mutua para secciones críticas.
- ***Fairness:*** Todos los threads que quieren acceder a un lock deben tener la misma probabilidad de hacerlo.
- **Performance:** Obtener y liberar un ***lock*** debe ser eficiente en distintas circunstancias: un único thread corre y utiliza el lock; multiples ***threads*** compiten por el ***lock***; múltiples ***threads*** en distintos procesadores compiten por el ***lock***.

# Controlar Interrupciones

Una de las formas más simples de implementar un ***lock***es a través de deshabilitar las interrupciones cuando se entra en una sección crítica. Este enfoque es simple, aunque tiene muchas desventajas.

Los procesos pueden abusar este enfoque, para no ser interrumpidos y monopolizar el procesador. Además, este enfoque no funciona en multiprocesadores, ya que estos tienen sus propias interrupciones.

Por otro lado, desactivar interrupciones por mucho tiempo puede permitir que estas interrupciones se pierdan.

Por último, este enfoque es ineficiente. El código que deshabilita interrupciones suele ser ejecutado lentamente.

# Enfoque Fallido: Load/Store

Se puede pensar en utilizar un ***flag*** en memoria que indique sin un ***lock*** está desbloqueado o no. Esto tiene ciertos inconvenientes. En primer lugar, se pueden dar casos en los que ambos hilos acceden al lock al mismo tiempo, seteando el flag como ***locked***. Esto provocaría comportamiento indeseado. Por otro lado, operaciones de ***spin-waiting***, esperar indefinidamente a que ocurra algo utiliza procesamiento, por lo que los ***threads*** en estado de espera estarían consumiendo procesamiento.

# Test-And-Set

La forma más simple de ***hardware support*** se conoce como la instrucción ***test-and-set (***o ***atomic exchange).*** Esta instrucción actualiza un valor en una dirección de memoria, devolviendo el valor anterior, esta operación se realiza de forma atómica. La razón del nombre es que permite verificar el valor anterior, mientras actualizar el valor nuevo.

Esta simple instrucción es todo lo que necesitamos para implementar un ***spin lock***. 

# Evaluación de *Spin Lock*

Un ***spin lock*** es un tipo de ***lock*** donde un thread espera indefinidamente utilizando ciclos de la CPU hasta que el ***lock*** se libera. Para que esto funcione, necesitamos un *preemptive scheduler.* (para que tenga sentido, el planificador debe interrumpir ciertos hilos a través de un timer).

Podemos hacer un análisis de su efectividad según los criterios mencionados anteriormente. 

- **C***orrectness***, el spin lock provee exclusión mutua.
- **F***airness***, los spinlocks no proveen ninguna garantía de que un ***thread*** no va a esperar infinitamente.
- ***Performance,*** si trabajamos con una única CPU, entonces ***s***e desperdician muchos ciclos, por lo que esta solución es extremadamente ineficiente. Con múltiples CPUs, este enfoque performa bastante bien (siempre y cuando haya aproximadamente la misma cantidad de ***threads*** que de ***procesadores***).

# Compare-And-Swap

Otra primitiva del hardware, también conocida como ***compare-and-exchange***. Esta instrucción verifica que el valor de ***ptr*** sea igual a ***expected***, en tal caso, actualiza el valor con el nuevo valor. Devuelve el valor originalmente almacenado. Con esta instrucción atómica, podemos diseñar un ***spinlock*** muy similar al anterior. 

Esta instrucción es más poderosa que ***test-and-swap***. Estudiaremos sus beneficios más adelante.

# *Load-Linked* and *Store-Conditional*

Algunas plataformas proveen este par de instrucciones para poder construir ***locks***. La instrucción ***Load-Linked*** es similar a un típico ***load.*** La diferencia proviene de la instrucción ***store-conditional***. Esta instrucción solo se realiza si no hubo ninguna intervención desde que se realizó un ***load-linked.*** En caso de un ***store*** exitoso, se devuelve el valor 1 y se actualiza el valor.

Con estas instrucciones, podemos construir nuevamente un ***spinlock***.

# ***Fetch-And-Add***

Esta instrucción, de forma atómica, incrementa un valor, retornando el valor anterior de una dirección de memoria particular.
Esta instrucción se puede utilizar para construir un ***ticket lock***. Cuando un ***thread*** quiere adquirir un ***lock***, entonces realiza un ***fetch-and-add*** en el valor del ***ticket***. El valor es considerado como el turno de ese ***thread***. Dentro del ***lock***, se almacena un ***turn*** para indicar de quién es el turno. Para liberar el turno, se incrementa el valor de ***turn*** ***con fetch-and-add***.

Este enfoque permite cumplir el segundo criterio, se garantiza que todos los ***threads*** van a obtener el ***lock*** eventualmente.

# Simple Approach: ***Yield***

El concepto detrás de este enfoque es simple: Cuando un proceso va a hacer un ***spin***, en su lugar delega el control del procesador. Este enfoque aún tiene la desventaja de que se gasta procesamiento de igual forma, cuando se realiza un ***yield***.

# Sleeping: *Queues*

Necesitamos encontrar una forma de que los procesos que estén esperando a adquirir un ***lock*** no se planifiquen. Podemos utilizar dos rutinas: `park()`, que pone al ***thread*** que trata de adquirir un ***lock*** a dormir. y `unpark()` que despierta un hilo.

Cuando llamamos a `lock()`, el thread actual debe colocarse en la cola de espera. Cuando se realiza un `unlock()`, Entonces se debe despertar al próximo ***thread*** en la cola. Para evitar condiciones de carrera, se utiliza la instrucción atómica `set_park()`, que libera el guard y duerme el proceso.

# ***Two-Phase Lock***

Este tipo de ***locks*** tienen dos fases, una de ***spinning*** y otra de ***sleeping***. Si no se puede conseguir el ***lock*** en la etapa inicial de ***spining***, entonces se duerme hasta que se libere el ***lock.***