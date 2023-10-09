En Oz, debemos crear puertos. Estos son un canal asincrónico que tiene un stream asociado.

El puerto en su interior tiene un estado interno, por lo que nos saca del modelo declarativo.

```Oz
local Puerto Stream Leer Escribir in
	proc {Leer Stream}
		case Stream of H|T then
			{Browse H}
			{Leer T}
		end
	end
	
	Puerto = {NewPort Stream}
	thread {Leer Stream} end
	
	{Send P 'Mensaje'}
	{Send P 'Mensaje 2'}
	
```
