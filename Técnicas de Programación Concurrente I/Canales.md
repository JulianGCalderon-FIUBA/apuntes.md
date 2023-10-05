Los canales conectan un proceso emisor con un proceso receptor, y tienen un nombre y un tipo de dato.

- Son sincrónicos
- Son unidireccionales

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
