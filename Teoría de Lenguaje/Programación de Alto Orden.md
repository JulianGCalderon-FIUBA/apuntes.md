Cuando las funciones son consideradas como cualquier otro tipo de dato, se dice que son ciudadanos de primera clase.

En estos casos, podremos pasar funciones como parámetro a otras funciones. Esto permite programar en un contexto más funcional.

```Oz
declare Seleccionar Mayor Menor L
fun {Mayor A B} if (A > B) then A else B end end
fun {Menor A B} if (A < B) then A else B end end

fun {Seleccionar Op L}
	case L of H|nil then
		H
	[] H|T then
		{Op H {Seleccionar Op T}}
	else
		'Error: Se espera una lista'
	end
end

L = [1 2 3 4 5 99 6 7 8 9 10]
{Browse {Seleccionar Mayor L}} % 99
{Browse {Seleccionar Menor L}} % 1
```

## Operaciones Básicas

### Abstracción Procedural

Está relacionado con los identificadores libres. En una declaración, un identificador es libre si no está definido en el mismo.

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
