Se definen dos familias de procesos: productores y consumidores.

Existen algunos requisitos, o propiedades:

- No se puede consumir lo que no hay.
- Todos los elementos producidos son eventualmente consumidos.
- Al espacio de almacenamiento se accede de a uno.
- Se debe respetar el orden de almacenamiento y retiro de los elementos.

Al utilizar un *buffer* de comunicación, se presentan los siguientes problemas de sincronización:

1. No se puede consumir si el *buffer* está vacío.
2. No se puede producir si el *buffer* está lleno.

Vamos a estudiar dos casos, ambos se pueden resolver con la utilización de [[Semáforos]].

- Buffer **infinito**
- Buffer **acotado**

## Buffer Infinito

En este caso solo se presenta el primer problema. Debemos definir un semáforo que represente la cantidad de recurso disponible.

```C
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

## Buffer acotado

En este caso se presentan ambos problemas descritos.

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

Tenemos dos recursos, en consecuencia, dos semáforos. Los recursos son

- La cantidad de recurso disponible.
- La cantidad de espacio disponible.
