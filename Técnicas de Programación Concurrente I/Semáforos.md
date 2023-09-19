Los semáforos son mecanismo de sincronización entre dos o más procesos. Está compuesto por dos campos:

- Un entero no negativo llamado $V$
- Un conjunto de procesos llamado $L$

El entero $V$ inicializa con un valor $k \geq 0$ y con el conjunto vacío $\theta$.

Se definen dos operaciones atómicas sobre un semáforo $S$:

- `wait(S)`, también llamado $p(S)$.
- `signal(S)`, también llamado $v(S)$.

Un semáforo es un contador.

- Si el contador es mayor a cero, entonces el recurso está disponible.
- Si el contador es menor o igual a cero, el recurso no está disponible.

El valor del semáforo representa la cantidad de recursos disponibles. Si el valor es cero o uno, se llaman semáforos binarios y se comportan igual que los *locks* de escritura.
