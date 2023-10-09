La recurrencia implica llamar a una función desde la propia función. En un paradigma declarativo, la mayoría de problemas se resuelven con recursión.

Podemos, por ejemplo, calcular el largo de una lista de forma recursiva.

```Oz
fun {Length L}
	case L of _|T then
		{Length T} + 1
	else
		0
	end
end

def length([]) do


```

## Last Call Optimization

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

La utilización de acumuladores es importante si queremos lograr algoritmos con recursividad de cola.
