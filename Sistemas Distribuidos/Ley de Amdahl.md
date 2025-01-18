
> The effort expended on achieving high parallel processing rates is wasted unless it is accompanied by achievements in sequential processing rates of very nearly the same magnitude.

Esto implica que, mientras mayor sea la fracción de tiempo que sea utilizado un componente, mayor *speedup* se espera al paralelizarlo.

Permite obtener el beneficio de invertir en la paralelización de las tareas. Depende de la naturaleza del problema. Una tarea altamente secuencial no obtendrá beneficio si se paraleliza.

Es un modelo que simplifica el problema en dos partes, por lo que no se centra en la naturaleza del problema. El problema se divide en la parte serial y en la parte paralelizable.

$$
T_p = W_s + W_p / P = f + (1 - f) / P
$$

El speedup $S$ maximo se encuentra acotado por la fracción de tiempo que no puede ser paralelizable.

$$
S = 1/f
$$
