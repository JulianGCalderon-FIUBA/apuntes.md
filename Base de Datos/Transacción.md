Una transacción es una unidad lógica de trabajo. También puede ser pensado como una secuencia ordenada de instrucciones atómicas.

Una misma transacción puede realizar varias operaciones de consulta/AMB durante su ejecución.

Antes de existir el multitasking, las transacciones se serializaban. Hasta tanto no se terminara una, no se iniciaba la siguiente. Esto no es una buena idea, nos gustaría poder ejecutar las transacciones simultáneamente. No es deseable que la ejecución de una transacción lenta demore a otras de ejecución rápida.

Si dos transacciones utilizan conjuntos de datos distintos, debería poder ejecutarse concurrentemente en distintos procesadores.

Las transacciones comparten recursos (tablas) entre sí. Esto es un problema importante para la [[Base de Datos/Concurrencia|Concurrencia]].

## Propiedades ACID

La ejecución de transacciones por un SGBD deben cumplir cuatro propiedades deseables:

- **Atomicidad:** Desde el punto de vista del usuario, las transacciones deben ser ejecutadas de forma atómica. Esto quiere decir que, o se ejecutan de forma completa, o no se ejecutan.
- **Consistencia:** Cada ejecución, por sí misma, debe preservar la consistencia de la base de datos. La consistencia se define a partir de las reglas de integridad.
- **Aislamiento:** El resultado de la ejecución concurrente de las transacciones debe ser el mismo que si las transacciones se ejecutaran de forma aislada. Debe ser equivalente a alguna ejecución serial.
- **Durabilidad:** Una vez que el gestor informa que la transacción fue completada, debe asegurar la persistencia de la misma, independiente de toda falla que pueda ocurrir.

Para garantizar estas propiedades, los gestores disponen de mecanismos de recuperación para deshacer las operaciones realizadas. En algún lado, el gestor debe tener un *log* de todas las operaciones que ejecuta. El gestor a veces utiliza el *log* no solo para deshacer transacciones, sino para rehacerlas. Esto nos permite satisfacer la propiedad de *durabilidad*.

Este *log* debe estar en disco para asegurar que vamos a poder recuperarnos de cualquier falla. En el disco del *log* se puede aprovechar la estructura secuencial, que es mucho más rápida que una escritura de acceso aleatorio (como ocurriría con un disco normal).

## Instrucciones Atómicas

Las instrucciones atómicas básicas de una transacción son:

- `leer_item(X)`: Lee el valor del ítem $X$, cargándolo en una variable en memoria. Se denota como $R_T(X)$
- `escribir_item(X)`: Ordena escribir el valor que está en memoria del ítem $X$ en la base de datos. Se denota como $W_T(X)$

Un ítem puede representar:

- El valor de un atributo en una fila determinada
- Una fila de una tabla
- Un bloque del disco
- Una tabla

En el único momento en el que la CPU interactúa con la base de datos, es cuando ejecuta alguna de las dos operaciones vistas. Cualquier otra operación (manipulación de datos en memoria) es independiente del resto de transacciones.

> [!note] Nota
> Ordenar escribir no es lo mismo que efectivamente escribir. El nuevo valor podría quedar temporalmente en un *buffer* en memoría.

## Instrucciones Especiales

Para ello, es necesario agregar a la secuencia de instrucciones de cada transacción, algunas instrucciones especiales.

- `begin`: Indica el comienzo de una transacción. Se denota como $b_T$
- `commit`: Indica que la transacción ha terminado exitosamente, y se espera que su resultado haya sido efectivamente almacenado de forma persistente. Se denota como $c_T$
- `abort`: Indica que se produjo un error o falla, y que, por lo tanto, todos los efectos de la transacción deben ser deshechos (*rolled back*). Se denota como $a_T$.

## Notación

A partir de las operaciones definidas, podemos denotar una transacción $T$ como una secuencia de $m(T)$ operaciones:

$$
\{I_T^1; I_T^2; \dots; I_T^{m(T)}\}
$$

Por ejemplo, una transacción puede ser escrita como:

$$
b_T\dots R_T(X)\dots W_T(X)\dots c_T
$$
