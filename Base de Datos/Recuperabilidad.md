La seriabilidad de las transacciones ya nos asegura la propiedad de aislamiento. Nos interesa ahora asegurar que una vez que una transacción commiteó, la misma no deba ser deshecha. Esto nos ayudará a implementar de una forma sencilla la propiedad de durabilidad.

Un solapamiento es **recuperable** si y solo si ninguna transacción $T$ realiza el *commit* hasta tanto todas las transacciones que escribieron datos antes de que $T$ los leyera hayan commiteado.

## Bitácora (Log)

Dado un solapamiento recuperable, puede ser necesario deshacer (abortar) una transacción antes de llegado su *commit*, para ello el gestor deberá contar con una serie de información que es almacenada por su gestor de recuperación en un *log* (bitácora).

El *log* almacena los siguientes registros:

- sa
- asd
- asd
- asd

En particular, los valores viejos de cada ítem almacenados en los registros del *log* son los que permitirán deshacer los efectos de la transacción en el momento de hacer *rollback*.

Es necesario que este *log* se encuentre en disco (para asegurar la consistencia y la durabilidad), debido a esto podemos aprovecharnos de realizar una escritura secuencial, lo que ofrece grandes ventajas en términos de eficiencia.

## Rollback

Para deshacer los efectos de una transacción $T_j$ que hay que abortar, entonces si las modificaciones hechas por $T_j$ no fueron leídas por nadie, entonces basta con procesar el *log* de $T_j$ en forma inversa para deshacer sus efectos.

Si una transacción $T_i$ leyó un dato modificado por $T_j$, entonces será necesario hacer *rollback* de $T_i$ para volverla a ejecutar.

Para evitar *rollbacks* en cascada, es necesario que una transacción no lea valores que aún no fueron commiteados. Esto es más fuerte que la condición de recuperabilidad: si evita *rollbacks* en cascada, entonces es recuperable, por otro lado, no es necesario serializable.

Esta condición no evita la actualización perdida, ya que es posible que la transacción que la actualiza *comitee* antes de que yo lea dato.

Esta definición implica que quedan prohibidos los conflictos de la forma $(W_{T_i}(X); R_{T_j}(X))$ sin que exista en el medio un commit $c_{T_i}$. Esta regla nos evita la anomalía de la lectura sucia.

### Protocolo de Lock de Dos Fases Estricto

El protocolo de lock de dos fases no asegura la recuperabilidad. Para asegurarla, debemos utilizar el protocolo de dos fases *estricto*. Este dice que solo puedo liberar un *lock* de escritura después del *commit*.

Si los locks (de cualquier tipo) solo pueden ser liberados después del commit, se llama protocolo de lock de dos fases riguroso. Este protocolo asegura que no se producirán *rollbacks* en cascada.
