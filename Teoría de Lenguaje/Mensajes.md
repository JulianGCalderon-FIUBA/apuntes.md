En Oz, debemos crear puertos. Estos son un canal asincrónico que tiene un stream asociado.

```Oz
local Puerto S in
	Puerto = {NewPort S}
	{Send P 'Mensaje'}
	
```