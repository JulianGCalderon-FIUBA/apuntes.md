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

Una función anónima es aquella que no está ligada a un identificador de variable. A veces son llamadas funciones **lambda**. Podemos utilizar funciones anónimas para pasarlas por parámetro sin declararlas junto a un identificador. Siguiendo el anterior ejemplo:

```Oz
local Seleccionar L in
Seleccionar = fun ...
L = [1 2 3 4 5]
{Browse {Seleccionar fun {$ A B} if A > B then A else B end}}
end
```

## Operaciones Básicas

Definimos algunas operaciones básicas que se permiten en la programación de alto orden.

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

Debido a que el [[scoping]] es dinámico, no necesitamos siquiera pasarle como argumento la variable a establecer

```Oz
local X P in
proc {P} X = 1 end
{P}
```

### Genericidad

Enviar procedimientos como parámetro permite realiza procedimientos genéricos.

- Sumar todos los elementos de una lista
- Multiplicar todos los elementos de una lista

Estas funciones se pueden generalizar en un concepto comúnmente conocido como reducir una lista. Se aplican operaciones dos a dos hasta llegar a un solo elemento.

```Oz
local Sumar Multiplicar Reducir L in
	fun {Multiplicar A B}
		A * B
	end
	
	fun {Sumar A B}
		A + B
	end
	
	fun {Reducir Op L}
		case L of H|nil then
			H
		[] H|T then
			{Op H {Reducir Op T}}
		end
	end

	L = [1 2 3 4 5 6]
	{Browse {Reducir Sumar L}}
	{Browse {Reducir Multiplicar L}}
end
```

### Instanciación

Devolver un procedimiento como resultado de una expresión. A las funciones que devuelven funciones se les denomina *factories* o fabricas. Son funciones que fabrican otras funciones.

Este concepto está relacionado con el [[scoping]], ya que las funciones fabricadas dependen de variables externas. De no ser el caso, todas las funciones fabricadas serían idénticas.

Siguiendo del ejemplo anterior, podemos definir:

```Oz
local Reducir Sumar Multiplicar FabricarReducir SumarLista L in
	Reducir = fun ...
	Sumar = fun ...
	Multiplicar = fun ...

	fun {FabricarReducir Op}
		fun {$ L}
			{Reducir Op L}
		end
	end

	SumarLista = {FabricarReducir Sumar}
	MultiplicarLista = {FabricarReducir Multiplicar}

	L = [1 2 3 4 5 6]
	{Browse {SumarLista L}}
	{Browse {MultiplicarLista L}}
end
```

### Embedding

Los procedimientos pueden ser parte de una estructura de datos. De esta forma podemos modelar [[objetos y clases]].

## Funciones Anónimas

## Currying

Es una técnica mediante la cual todos los procedimientos reciben solo un parámetro. Si tiene más de un parámetro, en realidad es tomado como una función que tiene, a su vez, un solo parámetro.

``` Oz
local Sumar in
	fun {Sumar A}
		fun {$ B}
			A + B
		end
	end
	
	{Browse {{Sumar A}B}}
end
```
