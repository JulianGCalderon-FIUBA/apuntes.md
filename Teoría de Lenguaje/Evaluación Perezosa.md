Hay dos tipos de evaluación. La evaluación **eager** y la evaluación **lazy**.

En la evaluación **lazy**, los cálculos se hacen recién al momento en que se necesitan. Por ejemplo, podremos crear un generador de enteros infinito.

```Oz
declare Ints L
fun lazy {Ints N}
	N|{Ints N+1}
end

L = {Ints 0}
{Browse L.2.2.2.1} % 3
{Browse L} % 0|1|2|3|_
```

Normalmente, ejecutar la función declarada rompería el programa, ya que entraría en un bucle infinito. Al agregar la palabra clave `lazy`, le indicamos al programa que queremos que la función se ejecuta de forma perezosa.

Al imprimir la lista completa, únicamente imprimiremos hasta el último elemento calculado.

## Funcionamiento

En realidad, `lazy` es un *syntax sugar* de un *trigger*. La sintaxis real será `{ByNeed <x> <y>}`. Cuando se necesite `<y>`, se ejecutará `<x>` de la siguiente forma: `thread {<x> <y>} end`. Para realizar esto, `<x>` debe recibir `<y>` como primer argumento.

Las siguientes dos bloques son equivalentes.

```Oz
local F A B in
	fun lazy {F} 125 end
	A = {F}
	B = A + 10
	{Browse B} % 135
end

local F A B in
	proc {F X} X = 125 end
	{ByNeed F A}
	B = A + 10
	{Browse B} % 135
end
```
