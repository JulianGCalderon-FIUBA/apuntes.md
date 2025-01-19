> Speedup should be measured by scalling the problem to the number of processors, not by fixing the problem size.

A diferencia de la [[Ley de Amdahl]], Gustafson plantea que el problema no tiene un tamaño fijo: si no podemos mejorar la solución, podemos modificar el problema para aprovechar más los recursos, o realizar más trabajo en la misma cantidad de tiempo.

Si el problema se modifica (crece), caben dos alternativas:

- La parte serial disminuye, por lo que el *speedup* aumenta.
- El paralelismo aumenta, por lo que el *speedup* aumenta.
