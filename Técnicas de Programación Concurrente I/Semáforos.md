Los semáforos son mecanismo de sincronización entre dos o más procesos. Está compuesto por dos campos:

- Un entero no negativo llamado $V$. Se inicializa con un valor $k \geq 0$.
- Un conjunto de procesos llamado $L$. Se inicializa con el conjunto vacío $\theta$.

El valor del semáforo representa la cantidad de recursos disponibles. Si el valor es cero o uno, se llaman semáforos binarios y se comportan igual que los *locks* de escritura.

Un semáforo es un contador.

- Si el contador es mayor a cero, entonces el recurso está disponible.
- Si el contador es cero, el recurso no está disponible.

Se definen dos operaciones atómicas sobre un semáforo $S$:

- La operación $p(S)$ o `wait(S)` solicita un recurso. Si el contador es mayor a cero, se disminuye. Si el contador es cero, entonces se bloquea hasta que se libere un recurso.

	```C
	if S.V > 0
		S.V := S.V - 1
	else
		S.L add p
		p.state := blocked
	```

- La operación $v(S)$ o `signal(S)` libera un recurso. Si hay procesos esperando, no hace falta aumentar el contador, ya que al mismo tiempo que un proceso libera un recurso, otro lo toma.

	```C
	if S.L is empty
		S.V := S.V + 1
	else
		// sea q un proceso arbitrario en espera
		S.L remove q
		p.state := ready
	```

Algunas propiedades de los semáforos son:

- $S.V \geq 0$
- $S.V = k + \#\text{signal}(S) - \#\text{wait}(S)$
