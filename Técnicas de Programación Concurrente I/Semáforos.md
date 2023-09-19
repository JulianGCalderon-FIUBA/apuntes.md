Los semáforos son mecanismo de sincronización entre dos o más procesos. Está compuesto por dos campos:

- Un entero no negativo llamado $V$. Se inicializa con un valor $k \geq 0$.
- Un conjunto de procesos llamado $L$. Se inicializa con el conjunto vacío $\theta$.

El valor del semáforo representa la cantidad de recursos disponibles. Si el valor es cero o uno, se llaman semáforos binarios y se comportan igual que los *locks* de escritura.

Un semáforo es un contador.

- Si el contador es mayor a cero, entonces el recurso está disponible.
- Si el contador es cero, el recurso no está disponible.

Se definen dos operaciones atómicas sobre un semáforo $S$:

- La operación $p(S)$ o `wait(S)` resta uno al contador. Si el contador no es mayor a cero, entonces el proceso se bloqueara hasta que pueda decrementar el contador.
- La operación $v(S)$ o `signal(S)` suma uno al contador. Esto lo libera para que otro proceso tome el recurso.

Algunas propiedades de los semáforos son:

- $S.V \geq 0$
- $S.V = k + \#\text{signal}(S) - \#\text{wait}(S)$
