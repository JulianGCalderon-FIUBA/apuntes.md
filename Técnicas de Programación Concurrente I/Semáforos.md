Los semáforos son mecanismo de sincronización entre dos o más procesos. Está compuesto por dos campos:

- Un entero no negativo llamado $V$. Se inicializa con un valor $k \geq 0$.
- Un conjunto de procesos llamado $L$. Se inicializa con el conjunto vacío $\theta$.

El valor del semáforo representa la cantidad de recursos disponibles. Si el valor es cero o uno, se llaman semáforos binarios y se comportan igual que los *locks* de escritura.

Un semáforo es un contador.

- Si el contador es mayor a cero, entonces el recurso está disponible.
- Si el contador es cero, el recurso no está disponible.

Se definen dos operaciones atómicas sobre un semáforo $S$:

- La operación $p(S)$ o `wait(S)` solicita un recurso. Si el contador es mayor a cero, se disminuye. Si el contador es cero, entonces se bloquea hasta que otro proceso lo libere con `signal(S)`.

	```C
	if S.V > 0
		S.V := S.V - 1
	else
		// siendo p el propio proceso
		S.L add p
		p.state := blocked
	```

- La operación $v(S)$ o `signal(S)` libera un recurso. Si hay procesos esperando, no hace falta aumentar el contador, directamente despierta un proceso en espera.

	```C
	if S.L is empty
		S.V := S.V + 1
	else
		// sea q un proceso arbitrario en espera
		S.L remove q
		p.state := ready
	```

Los invariantes de los semáforos son:

- El contador es siempre no negativo: $S.V \geq 0$
- El cambio del valor del contador únicamente depende de la cantidad de llamadas a sus operaciones básicas: $S.V = k + \#\text{signal}(S) - \#\text{wait}(S)$

## Semáforos de UNIX

Existen dos tipos de semáforos:

- System V
- POSIX

Un semáforo System V está compuesto por:

- El valor del semáforo.
- El *process id* del último proceso que utilizó el semáforo.
- La cantidad de procesos esperando por el semáforo.
- La cantidad de procesos que está esperando que el semáforo sea cero. Esto permite que podamos implementar barreras.

## Semáforos en Rust

Utilizaremos el *crate* `std-semaphore`.

- Para crear un semáforo, utilizamos: `fn new(k: usize)`.
- Para obtener acceso, utilizamos `fn acquire(&self)`.
- Para liberar un semáforo, utilizamos: `fn release(&self)`.
- Para acceder con patrón RAII, utilizamos: `fn access(&self)`. Esto permite que el semáforo se libere en cuanto la variable devuelta (una guarda) se vaya del entorno.
