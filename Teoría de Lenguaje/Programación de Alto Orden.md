## Programación de Alto Orden

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