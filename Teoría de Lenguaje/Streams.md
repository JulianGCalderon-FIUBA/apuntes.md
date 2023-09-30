Un *stream* es una lista cuyo último elemento aún no está definido, es una lista sin fin. Esto permite que la lista se expanda posteriormente a ser definida, ya sea manualmente o a través de una función recursiva.

```Oz
local A B C in
	A = 1|2|3|B
	B = 4|5|6|C
	C = 7|8|9|nil
end
```

Esto puede ser utilizado para comunicar hilos. Un hilo expande progresivamente una lista, mientras que otro hilo tome los valores a medida que se van generando.
