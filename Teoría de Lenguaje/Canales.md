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

Definimos un `NewPortObject` como un puerto con estado interno. Realiza un `reduce` con todos los elementos enviados al puerto, aplicando la función `Fun` con un acumulador inicial `Init`.

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
```
