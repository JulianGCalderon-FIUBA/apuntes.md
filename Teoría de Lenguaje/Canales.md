En Oz debemos crear puertos. Estos son un canal asincrónico que tiene un stream asociado.

El puerto en su interior tiene un estado interno, por lo que nos saca del modelo declarativo.

```Oz
local Puerto Stream Recibir Enviar in
	proc {Recibir Stream}
		case Stream of H|T then
			{Browse H}
			{Leer T}
		end
	end
	
	proc {Enviar Puerto From To}
		if From < To then
			{Send Puerto From}
			{Enviar Puerto From+1 To}
		end
	end
	
	Puerto = {NewPort Stream}
	thread {Enviar Stream 1 5} end
	thread {Enviar Stream 5 10} end
	thread {Recibir Stream} end % Ej: 1 2 5 3 6 7 8 4 9
end
```

## Port Object

Definimos un `NewPortObject` como un puerto con estado interno. Realiza algo similar a un `reduce` con todos los elementos enviados al puerto, aplicando la función `Fun` con el elemento actual y un acumulador inicial `Init` (el cual luego se actualizará con el retorno de la función).

```Oz
fun {NewPortObject Init Fun}
	local MsgLoop Sin in
		proc {MsgLoop S1 State}
			case S1 of Msg|S2 then
				{MsgLoop S2 {Fun Msg State}}
			end
		end
		thread {MsgLoop Sin Init} end
		{NewPort Sin}
	end
end
```

Si no hace falta un estado interno (acumulador), entonces podríamos definir `NewPortObject2`. Ahora la función es un procedimiento, pues no se actualiza su estado interno.

```Oz
fun {NewPortObject2 Proc}
	local Sin in
		thread
			for Msg in Sin do
				{Proc Msg}
			end
		end
		{NewPort Sin}
	end
end
```

## Actores

El modelo de actores puede ser utilizado para resolver problemas de concurrencia de forma eficiente. Tendremos hilos que encapsulan un estado interno y se comunican entre ellos a través de recibir y enviar mensajes.

Los actores resuelven los pedidos de los clientes secuencialmente, por lo que se resuelve el problema de la sección crítica.
