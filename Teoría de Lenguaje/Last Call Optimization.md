Es una optimización muy utilizada en la programación funcional. Cuando la última instrucción de una función recursiva es la propia llamada recursiva, el compilador puede deshacerse de las variables del *stack* del ambiente actual. Esto permite que el *stack* no crezca con cada recursión.

Este tipo de recursividad se conoce como recursividad de cola, muchos algoritmos pueden implementarse de esta forma.

```Oz
fun {Fact X Acum}
	if X==0 then 
		Acum
	else
		{Fact X-1 Acum*X}
	end
end
```

## Manejo de Memoria

Un **valor alcanzable** es un valor que es referenciado por el *stack*, o referenciado por algún otro valor que sea alcanzable.

La **memoria activa** se compone por el *stack* y los valores alcanzables por el.

El manejo de memoria puede ser manual, o a través de un **garbage collector**. Algunos problemas del manejo de memoria manual son:

- Referencias colgadas (*dangling references*)
- Perdidas de memoria (*memory leaks*)
