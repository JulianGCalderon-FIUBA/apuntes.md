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

Una **barrera** permite a múltiples hilos esperar hasta que todos los hilos hayan llegado a cierto punto.

## Semáforos en Rust

Utilizaremos el *crate* `std-semaphore`.

- Para crear un semáforo, utilizamos: `fn new(k: usize)`.
- Para obtener acceso, utilizamos `fn acquire(&self)`.
- Para liberar un semáforo, utilizamos: `fn release(&self)`.
- Para acceder con patrón RAII, utilizamos: `fn access(&self)`. Esto permite que el semáforo se libere en cuanto la variable devuelta (una guarda) se vaya del entorno.

## Barreras en Rust

Permiten sincroniza varios hilos en puntos determinados de un cálculo o algoritmo.

- Para crear una barrera, utilizamos `fn new(n: usize)`
- Para bloquear el hilo hasta que todos se encuentren en el punto, utilizamos `fn wait(&self)`.

El método `is_leader()` devolverá `true` en el hilo líder. Al levantar la barrera, un hilo arbitrario se designa como líder.

Las barreras son reutilizables automáticamente.

## Productor - Consumidor

Se definen dos familias de procesos: productores y consumidores.

Existen algunos requisitos, o propiedades:

- No se puede consumir lo que no hay.
- Todos los elementos producidos son eventualmente consumidos.
- Al espacio de almacenamiento se accede de a uno.
- Se debe respetar el orden de almacenamiento y retiro de los elementos.

Al utilizar un *buffer* de comunicación, se presentan los siguientes problemas de sincronización:

- No se puede consumir si el *buffer* está vacío.
- No se puede producir si el *buffer* está lleno.

Vamos a estudiar dos casos:

### Buffer Infinito

En este caso, solo se presenta el primer problema.

Inicialmente, definimos un buffer y un semáforo:

```C
buffer := emptyQueue
notEmpty := semaphore(0)
```

Desde el productor, tendremos:

```C 
dataType d
loop forever
	p1: append(d, buffer)
	p2: signal(notEmpty)
```

Desde el consumidor, tendremos:

```C
dataType d
loop forever
	q1: wait(notEmpty)
	q2: d <- take(buffer)
```

Tenemos un solo recurso y, por lo tanto, un solo semáforo.

### Buffer acotado

En este caso se presentan ambos problemas.

Inicialmente, definimos un buffer y dos semáforos.

```C
buffer := emptyQueue
notEmpty := semaphore(0)
notFull := semaphore(N)
```

Desde el productor, tendremos:

```C
dataType d
loop forecer
	p1: producir
	p2: wait(notFull)
	p3: append(d, buffer)
	p4: signal(notEmpty)
```

Desde el consumidor, tendremos:

```C
dataType d
loop forever
	q1: wait(notEmpty)
	q2: d <- take(buffer)
	q3: signal(notFull)
	q4: consume(d)
```

Tenemos dos recursos, en consecuencia, dos semáforos:

- La cantidad de recurso disponible.
- La cantidad de espacio disponible.
