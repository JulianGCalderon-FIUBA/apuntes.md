Los canales conectan un proceso emisor con un proceso receptor, y tienen un nombre y un tipo de dato.

- Son sincrónicos
- Son unidireccionales

Podremos implementar el problema del productor consumidor facilmente. Al tener un canal `ch`, podemos enviar mensajes:

```
loop
	Produce(I);
	ch <- I
```

Desde el otro extremo, podemos recibirlos:

```
loop
	ch -> I
	Consume(I)
```

## Selective Input

Es una sintaxis permitida por los lenguajes que soportan canales, y permite escuchar en varios canales de forma bloqueante y desbloquearse con el primero que recibe un mensaje

```
either
	ch1 => var1
or
	ch2 => var2
or
	ch3 => var3
```

## Fliósofos Comensales

Modelaremos los cinco tenedores con cinco canales. No es relevante el elemento que se envía, sino el hecho de enviarlo.

```
loop
	Think;
	forks[i] -> dummy;
	forks[i+1] -> dummy;
	Eat;
	forks[i] <- true;
	forks[i+1] <- true;
```

También necesitaremos un proceso por cada tenedor, que lo administre

```
loop
	forks[i] -> true;
	forks[i] <- dummy;
```
