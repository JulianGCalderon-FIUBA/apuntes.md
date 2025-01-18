
> The overall performance improvement gained by optimizing a single part of a system is limited by the fraction of time that the improved part is actually used

Esto implica que, mientras mayor sea la fracción de tiempo que sea utilizado un componente, mayor *speedup* se espera al paralelizarlo. El speedup a obtener depende de la naturaleza del problema. Una tarea altamente secuencial no obtendrá beneficio si se paraleliza.

El modelo simplifica el cómputo a realizar en dos partes. En una parte paralelizable $W_p$, y una parte serial $W_s$.

El speedup se encuentra acotado por la fracción de tiempo que no puede ser paralelizable.
