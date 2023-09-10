Es un término utilizado en el [[Modelo Declarativo]]. Está relacionado con los identificadores libres. En una declaración, un identificador es libre si no está definido en el mismo.

Cualquier declaración puede convertirse en un procedimiento.

```Oz
local X in
	X = 1
end
```

Crearemos un procedimiento que cumpla el mismo propósito

```Oz
local X P in
	proc {P X} X = 1 end
	{P X}
end
```

Este concepto nos permite separar la declaración de la función, de su ejecución.

Debido a que el [[Scoping]] es dinámico, no necesitamos siquiera pasarle como argumento la variable a establecer

```Oz
local X P in
proc {P} X = 1 end
{P}
```
