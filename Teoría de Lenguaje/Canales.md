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
	
	proc {Enviar }
	
	Puerto = {NewPort Stream}
	thread {Recibir Stream} end
	
	{Send P 'Mensaje 1'}
	{Send P 'Mensaje 2'}
	
```
