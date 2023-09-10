## Pattern Matching

Es una manera de acceder a los campos de una estructura de datos y obtener los valores

Un patrón *matchea* sobre un registro cuando coincide en su largo, etiqueta, y características.

```Oz
declare EsVacio L

proc {EsVacio L}
	case L of H|T then
		{Browse 'No'}
	else
		{Browse 'Si'}
	end
end

L = nil
{EsVacio L} % Si
```

El *pattern matching* trata de asignar la variable al patrón. Si es posible hacerlo, entonces el patrón coincide.

```Oz
declare L H T
L = [10 20 30] % 10|20|30|nil
L = H|T
{Browse H} % 10
{Browse T} % [20, 30]
```

Esto puede ser utilizado para, por ejemplo, calcular el largo de una lista

```Oz
declare Largo L Res
fun {Largo L}
	case L of H|T then
		{Largo T} + 1
	else
		0
	end
end

L = [10 20 30]
Res = {Largo L}
{Browse Res} % 3
```

También pueden utilizarse múltiples patrones

```Oz
declare EsVacio L1 L2 L3
fun {EsVacio L}
	case L of H|T then
		{Browse 'No'}
	[] nil then
		{Browse 'Si'}
	else
		{Browse 'No es una lista'}
	end
end

L1=[10]
L2=nil
L3=10

{EsVacio L1} % No
{EsVacio L2} % Si
{EsVacio L3} % No es una lista
```
