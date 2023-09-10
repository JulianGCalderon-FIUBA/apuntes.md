## Objeto

Definiremos un objeto como una función con memoria interna.

```Oz
declare C Bump
C = {NewCell 0}
Bump = proc {$}
	C := @C + 1
end

Read = fun {$}
	@C
end
	
{Browse {Read}} % 0
{Bump}
{Browse {Bump}} % 1
{Browse {Bump}} % 2
```

## Clases

Las clases nos permiten tener múltiples instancias de un mismo objeto. Una clase es una fábrica de objetos.

```Oz
declare NewCounter Counter1 Counter2
NewCounter = fun {$}
	local C Bump Read in
		C = {NewCell 0}
		Bump = fun {
			
		}
		counter(bump: Bump read:Read)
	end
```
