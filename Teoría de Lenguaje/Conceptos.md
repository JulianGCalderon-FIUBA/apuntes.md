## Evaluación Perezosa

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

## Concurrencia

A través del concepto de concurrencia, podremos tener hilos independientes de ejecución. Estos programas son no determinísticos, pues el orden de ejecución dependerá del *scheduler* del sistema operativo.

```Oz
declare A B C
thread
	A = B + C
end
C = 4
thread
	B = 10
end
{Browse A} % 14
```

Si el primer hilo se ejecuta primero, entonces esperará a que estén definidos los valores necesarios para continuar.

## Estado Explícito

Este concepto proviene del modelo imperativo. En algunos lenguajes, se utiliza el concepto de **función pura**. Una función pura es aquella que no tiene efectos secundarios. Únicamente devuelve un valor, sin mutar el estado ninguna variable.

En la programación funcional, no existe el estado. Cuando se habla del estado, entonces estaremos hablando de variables mutables. En la programación funcional, hablamos de la programación determinística. No existe el estado, siempre se devuelve la misma salida ante la misma entrada de datos.

En el **estado explícito**, se hacen explícitas las modificaciones de estados. Para el caso del lenguaje Oz, existe el concepto de celda.

```Oz
declare C Bump
C = {NewCell 0}
C := @C+1
{Browse @C} % 1
C :== @C+10
{Browse @C} % 11
```

## Objetos y Clases

### Objetos

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

### Clases

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

## Indeterminismos

En el momento que se combina el concepto de estados y de concurrencia, entonces surgen los indeterminismos. El orden del código cambiará el resultado final de la ejecución.

Una forma de resolver esto es con operaciones atomicas a través del uso de *locks*.
