Cuando hablamos del estado, este puede ser **implícito** o **explicito**. En un estado **implícito** (del modelo declarativo) está compuesto por los argumentos de la función y las variables libres que definimos. El estado está dado por el entorno de nuestra clausura. Las variables son inmutables.

El estado explícito ocurre cuando el estado excede a la llamada del procedimiento. La modificación de una variable dentro de un procedimiento afecterá también el estado de la función padre. Este concepto proviene del [[Modelo Imperativo]].

En algunos lenguajes, se utiliza el concepto de **función pura**. Una función pura es aquella que no tiene efectos secundarios. Únicamente devuelve un valor, sin mutar el estado ninguna variable.

En la programación funcional, no existe el estado. Cuando se habla del estado, entonces estaremos hablando de variables mutables. En la programación funcional, hablamos de la programación determinística. No existe el estado, siempre se devuelve la misma salida ante la misma entrada de datos.

En el **estado explícito**, se hacen explícitas las modificaciones de estados. Para el caso del lenguaje Oz, existe el concepto de celda de memoria.

```Oz
declare C
C = {NewCell 0}

C := @C+1
{Browse @C} % 1

C :== @C+10
{Browse @C} % 11
```
