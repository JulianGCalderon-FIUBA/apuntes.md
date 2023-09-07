## Futures

## Pin

Los tipos de datos autogenerados de `async` existen en el que implementan `Future` guardan una referencia a si mismas. Si estos son movidos (por estar en el *stack*), estas referencias no se actualizan.

Para resolver esto, se inventa el concepto de *pin*. Todos los tipos de dato por defecto implementan el *autotrait* `Unpin`. A menos que específicamente se marquen como `!Unpin`.

Las autorreferencias se envuelven en un tipo `Pin`.

##
