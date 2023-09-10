Un modelo computacional es un sistema formal que define cómo se ejecutan los cálculos. Se define en términos de los conceptos que incluye. Un modelo computacional es una definición más precisa de un paradigma de programación.

Vamos a estudiar la transición entre un modelo **declarativo** a un modelo **imperativo**, a través de agregarle características.

Los lenguajes de programación declarativos se centran en el ¿qué?, mientras que los lenguajes de programación imperativos se centran en él ¿cómo?

Notemos que, aunque el imperativo tenga más características, no significa que es mejor que el otro.

> More is not better (or worse), just different

## ¿Qué nos permite estudiar?

El modelo computacional nos permite estudiar tres elementos:

- **Correctitud:** Nos permite estudiar matemáticamente que la ejecución de nuestro programa sea correcta.
- **Complejidad Temporal:** Tiene que ver con expresar un orden de magnitud temporal del tiempo de ejecución de nuestro programa.
- **Complejidad Espacial:** Tiene que ver con expresar un orden de magnitud espacial para la memoria que ocupa nuestro programa. En esta materia, vamos a hacer hincapié en este elemento.

## Modelo Declarativo

Debido a su naturaleza, las instrucciones escritas un lenguaje declarativo son mucho más difíciles de seguir. Pueden ser pensadas como una lista de definiciones.

> [!example] Receta de torta en lenguaje declarativo
> - Una torta es 45 minutos de 200ºC de calor aplicado a 200 mg de masa de torta final
> - 100 mg de masa de torta final es una mezcla de 99 mg de masa de torta etapa 2 y 1 mg de sal.
> - 99mg de masa de torta etapa 2 es una mezcla de 79 mg de harina y un huevo

Algunas características de este modelo son:

- Sin estados
- Paralelizable
- Determinístico
- Sin efectos secundarios
- Fácil de probar
