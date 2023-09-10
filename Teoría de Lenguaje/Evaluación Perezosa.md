Hay dos tipos de evaluación. La evaluación **eager** y la evaluación **lazy**.

En la evaluación **lazy**, los cálculos se hacen recién al momento en que se necesitan. Por ejemplo, podremos crear un generador de enteros infinito.

```Oz
declare Ints L
fun lazy {Ints N}
	N|{Ints N+1}
end

L = {Ints 0}
{Browse L.2.2.2.1} % 3
{Browse L} % 0|1|2|3|_
```

Normalmente, ejecutar la función declarada rompería el programa, ya que entraría en un bucle infinito. Al agregar la palabra clave `lazy`, le indicamos al programa que queremos que la función se ejecuta de forma perezosa.

Al imprimir la lista completa, únicamente imprimiremos hasta el último elemento calculado.
