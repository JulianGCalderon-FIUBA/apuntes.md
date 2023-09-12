El *scoping* de un lenguaje refiere a su manejo de ámbitos o *scopes*.

Supongamos el siguiente código:

```Oz
local P Q in
	proc {Q X}
		{Browse stat(X)}
	end
	proc {P X}
		{Q X}
	end
	local Q in
		proc {Q X}
			{Browse dyn(X)}
		end
		{Q 'X'}
	end	
end
```

Si el scoping del lenguaje de programación es estático, se imprimirá `stat(X)`. En caso contrario, se imprimirá `dyn(X)`. Oz es un lenguaje con scoping estático.

En un lenguaje de scoping estático, las variables libres toman valor en el momento de la definición. En un lenguaje de scoping dinámico, las variables libres toman valor en el momento de la ejecución.

Los lenguajes estáticos son mas declarativos. Su comportamiento es mas facil de analizar.
