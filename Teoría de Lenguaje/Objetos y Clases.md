## Objetos

Definiremos un objeto como una función con memoria interna. Esta memoria interna debe ser mutable, por lo que recurriremos al estado explícito.

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
{Browse {Read}} % 1
```

## Clases

Las clases nos permiten tener múltiples instancias de un mismo objeto. Una clase es una fábrica de objetos.

```Oz
declare NewCounter Counter1 Counter2

NewCounter = fun {$}
	local C Bump Read in
		C = {NewCell 0}
		Bump = proc {$}
			C := @C + 1
		end
		Read = fun {$}
			@C
		end
		counter(bump:Bump read:Read)
	end
end

Counter1 = {NewCounter}
Counter2 = {NewCounter}

{Browse {Counter1.read}} % 0
{Counter1.bump}
{Browse {Counter1.read}} % 1

{Browse {Counter2.read}} % 0
```
