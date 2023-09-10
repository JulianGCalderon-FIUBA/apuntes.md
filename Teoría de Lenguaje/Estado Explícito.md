Este concepto proviene del [[Modelo Imperativo]]. En algunos lenguajes, se utiliza el concepto de **función pura**. Una función pura es aquella que no tiene efectos secundarios. Únicamente devuelve un valor, sin mutar el estado ninguna variable.

En la programación funcional, no existe el estado. Cuando se habla del estado, entonces estaremos hablando de variables mutables. En la programación funcional, hablamos de la programación determinística. No existe el estado, siempre se devuelve la misma salida ante la misma entrada de datos.

En el **estado explícito**, se hacen explícitas las modificaciones de estados. Para el caso del lenguaje Oz, existe el concepto de celda.

```Oz
declare C Bump
C = {NewCell 0}
C := @C+1
{Browse @C} % 1
C :== @C+10
{Browse @C} % 11
```
