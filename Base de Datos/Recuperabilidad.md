La seriabilidad de las transacciones ya nos asegura la propiedad de aislamiento. Nos interesa ahora asegurar que una vez que una transacción commiteó, la misma no deba ser deshecha. Esto nos ayudará a implementar de una forma sencilla la propiedad de durabilidad.

Un solapamiento es **recuperable** si y solo si ninguna transacción $T$ realiza el *commit* hasta tanto todas las transacciones que escribieron datos antes de que $T$ los leyera hayan commiteado.

Un gestor nunca debería permitir un solapamiento no recuperable, ya que debe asegurar la propiedad de durabilidad. Si se informó al usuario que se completó la transacción, debe persistir.

> [!note] Nota
> La recuperabildiad no implica serializabilidad, ni viceversa.

## Bitácora (Log)

Dado un solapamiento recuperable, puede ser necesario deshacer (abortar) una transacción antes de llegado su *commit*, para ello el gestor deberá contar con una serie de información que es almacenada por su gestor de recuperación en un *log* (bitácora).

El *log* almacena los siguientes registros:

- `(BEGIN, T_id):` Indica que la transacción $T_{id}$ comenzó.
- `(WRITE, T_id, X, X_old, X_new):` Indica que la transacción $T_{id}$ escribió el ítem $X$, cambiando su viejo valor $x_{old}$ por su nuevo valor $x_{new}$
- `(READ, T_id, X):` Indica que la transacción $T_{id}$ leyó el ítem $X$.
- `(COMMIT, T_id):` Indica que la transacción $T_{id}$ commiteó.
- `(ABORT, T_id):` Indica que la transacción $T_{id}$ abortó.

En particular, los valores viejos de cada ítem almacenados en los registros del `WRITE` son los que permitirán deshacer los efectos de la transacción en el momento de hacer *rollback*.

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

## Recuperabilidad con Timestamps

En este método, cuando se aborta una transacción $T_i$, cualquier transacción que haya usado datos que $T_i$ modificó debe ser abortada en cascada.

Para garantizar la recuperabilidad, se debe escoger entre varias opciones:

- No hacer el *commit* de una transacción hasta que todas aquellas transacciones que modificaron datos que ella leyó hayan hecho su commit
- Bloquear a la transacción lectora hasta tanto el escritor haya hecho su commit (esto evita *rollbacks* en cascada)
- Hacer todas las escrituras durante el commit, manteniendo una copia paralela de cada **ítem** para cada transacción. Para esto, la escritura de los ítems en el *commit* debe ser centralizada y atómica.
