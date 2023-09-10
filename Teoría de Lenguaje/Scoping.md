## Global vs. Local

Podemos limitar el ambiente de variables a un entorno particular.

```Oz
local A B Var in
	A = 4
	B = 5
	Var = A*B + 3
	{Browse Var} % 23
end
```

En un entorno global, las variables pueden ser accedidas en todo el programa, lo cual puede traer problemas.

Las variables pueden ser reasignadas al definir un nuevo entorno.

```Oz
local A in
	A = 4
	local A in
		A = 7
		{Browse A} % 7
	end
	{Browse A} % 4
end
```

Si se referencia a una variable que no pertenece al entorno, se buscara en un entorno superior.

## Estático vs. Dinámico

Supongamos el siguiente código:

```Oz
local P Q in
	proc {Q X}
		{Browse }
end
```
