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
// --- DEFINITION ---
Buffer buffer = buffer_new()
Semaphore not_empty = semaphore_new(0)
```

```C 
// --- PRODUCTOR ---
Resource r
while true {
	append(buffer, r)
	signal(not_empty)
}
```

```C
// --- CONSUMIDOR ---
Resource r
while true {
	wait(not_empty)
	r = take(buffer)
}
```

Nos aseguramos de esta forma que un productor nunca tome un elemento del *buffer* cuando este está vacío, gracias a la utilización de un semáforo.

## Buffer acotado

En este caso se presentan ambos problemas descritos. Ademas del semáforo que representa la cantidad de recurso disponible, tendremos un semaforo mas

```C
// --- DEFINITION ---
Buffer buffer = buffer_new()
Semaphore not_empty = semaphore_new(0)
```

```C 
// --- PRODUCTOR ---
Resource r
while true {
	append(buffer, r)
	signal(not_empty)
}
```

```C
// --- CONSUMIDOR ---
Resource r
while true {
	wait(not_empty)
	r = take(buffer)
}
```

Tenemos dos recursos, en consecuencia, dos semáforos. Los recursos son

- La cantidad de recurso disponible.
- La cantidad de espacio disponible.
