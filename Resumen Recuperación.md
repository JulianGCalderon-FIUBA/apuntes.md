## Algoritmo UNDO

Este algoritmo trabaja bajo la técnica de volcado de actualización inmediata. Debemos respetar las reglas:

- **Regla WAL:** Antes de que una transacción $T_i$ modifique el ítem $X$ remplazando $v_{old}$ por $v$, se escribe $(\text{WRITE}, T_i, X, v_\text{old})$ en el *log* y se vuelca al disco.
- **Actualización Inmediata:** Los ítems modificados deben ser guardados en disco antes de hacer *commit*.
- **Regla FLC:** Antes de que $T_i$ haga *commit*, se escribe $(\text{COMMIT}, T_i)$ en el *log* y se vuelca al disco.

Notemos que no debemos rehacer las transacciones que ya *commitearon*, pues volcaron todo a disco.

Cuando el sistema reinicia, se siguen los siguientes dos pasos:

1. Se recorre el *log* de adelante hacia atrás, y por cada transacción de la que no se encuentra el $\text{COMMIT}$, se aplica cada uno de los $\text{WRITE}$ de forma inversa para restaurar el valor anterior a la misma en disco.
2. Luego, por cada transacción $T_i$ que no *commiteo* se escribe $(\text{ABORT}, T_i)$ en el *log* y se vuelca a disco.

Si ocurre una falla durante el reinicio, esto no es un problema porque el procedimiento de reinicio es **idempotente**. Si se ejecuta más de una vez, no cambiará el resultado.

### Checkpointing Inactivo

En este algoritmo, el procedimiento con un *checkpointing* inactivo se realiza de la siguiente manera:

1. Dejar de aceptar nuevas transacciones.
2. Esperar a que todas las transacciones hagan su *commit*.
3. Escribir $(\text{CKPT})$ en el *log* y volcarlo a disco.

Durante la recuperación solo debemos deshacer las transacciones que no hayan hecho *commit*, hasta el momento en que encontremos un registro $(\text{CKPT})$. De hecho, todo el archivo de *log* anterior podría ser eliminado.

### Checkpointing Activo

El procedimiento de un *checkpointing* activo se realiza de la siguiente manera:

1. Escribir un registro $(\text{BEGIN CKPT}, t_{act})$ con el listado de todas las transacciones activas hasta el momento
2. Esperar a que todas esas transacciones activas hagan su *commit* (sin dejar por eso de recibir nuevas transacciones)
3. Escribir $(\text{END CKPT})$ en el *log* y volcarlo a disco.

En la recuperación, se dan dos situaciones:

- Si encontramos primero un registro $(\text{END CKPT})$, solo debemos retroceder hasta el $(\text{BEGIN CKPT})$ durante el *rollback*, porque ninguna transacción incompleta puede haber comenzado antes.
- Si encontramos primero un registro $(\text{BEGIN CKPT})$, implica que el sistema cayó sin asegurar los *commits* del listado de transacciones. Deberemos volver hacia atrás, pero solo hasta el inicio de la más antigua del listado.

## Algoritmo REDO

Este algoritmo trabaja bajo la técnica de volcado de actualización diferida. Debemos respetar las reglas:

- **Regla WAL:** Cuando una transacción $T_i$ modifica el ítem $X$ reemplazando el valor viejo por $v$, se escribe $(\text{WRITE}, T_i, X, v)$ en el *log* y se vuelca al disco.
- **Regla FLC:** Cuando una transacción $T_i$ hace *commit*, se escribe $(\text{COMMIT}, T_i)$ en el *log* y se vuelca al disco.
- **Actualización Diferida:** Los ítems modificados deben ser guardados en disco después de hacer *commit*.

Notemos que no debemos deshacer las transacciones que no commitearon, pues no volcaron nada en disco.

Cuando el sistema reinicia, se siguen los siguientes pasos:

1. Se analiza cuáles son las transacciones de las que está registrado el $\text{COMMIT}$.
2. Se recorre el *log* de atrás hacia adelante, volviendo a aplicar cada uno de los $\text{WRITE}$ de las transacciones que *commitearon*.
3. Luego, por cada transacción que no *commiteo*, se escribe $(\text{ABORT}, T)$ en el *log* y se vuelca a disco.

Este algoritmo nos **obliga** a que nos volquemos los datos a disco hasta después de realizar el *commit*. Esto es un problema.

### Checkpointing Activo

En este algoritmo, el procedimiento con un *checkpointing* activo se realiza de la siguiente manera:

1. Escribir un registro $(\text{BEGIN CKPT}, t_\text{act})$ con el listado de todas las transacciones activas hasta el momento, y volcar el *log* a disco.
2. Hacer el volcado a disco de todos los *ítems* que hayan sido modificados por transacciones que ya *commitearon*.
3. Escribir $(\text{END CKPT})$ en el *log* y volcarlo a disco.

En la recuperación, deberemos retroceder hasta el $(\text{BEGIN}, T_x)$ de la transacción más antigua del listado que figure en el $(\text{BEGIN CKPT})$.

Si encontramos primero un registro $(\text{BEGIN CKPT})$, entonces no nos sirve, y debemos buscar un *checkpoint* anterior en el log.

## Algoritmo UNDO/REDO

Este algoritmo nos permite volcar a disco en cualquier momento, no es necesario respetar alguna de las técnicas de volcado.

- **Regla WAL:** Antes de que una transacción $T_i$ modifique el ítem $X$ reemplazando un valor $v_{old}$ por $v$, se escribe $(\text{WRITE}, T_i, X, v_{old}, v)$ en el *log* y se vuelca a disco.
- **Regla FLC:** Cuando $T_i$ hace *commit*, se escribe $(\text{COMMIT}, T_i)$ en el *log* y se vuelca a disco.
- Los ítems modificados pueden ser guardados en disco antes o después de hacer *commit*.

Notemos que con este algoritmo, debemos tanto rehacer transacciones *commiteadas*, como deshacer transacciones no *commiteadas*, pues no impusimos una restricción sobre el volcado.

Cuando el sistema reinicia, se siguen los siguientes pasos:

- Se recorre el *log* de adelante hacia atrás, y por cada transacción de la que no se encuentra el *commit*, se aplica cada una de las escrituras para restaurar el valor anterior a la misma a disco.
- Luego, se recorre de atrás hacia adelante, volviendo a aplicar cada una de las escrituras de las transacciones que *commitearon*, para asegurar que quede asignado el nuevo valor de cada ítem.
- Finalmente, por cada transacción de la que no se encontró el *commit*, se escribe $(\text{ABORT}, T)$ en el *log* y se vuelca a disco.

### Checkpointing Activo

En este algoritmo, el procedimiento con un *checkpointing* activo se realiza de la siguiente manera:

1. Escribir un registro $(\text{BEGIN CKPT}, t_\text{act})$ con el listado de todas las transacciones activas hasta el momento, y volcar el *log* a disco.
2. Hacer el volcado a disco de todos los *ítems* que hayan sido modificados antes del $(\text{BEGIN CKPT})$
3. Escribir $(\text{END CKPT})$ en el *log* y volcarlo a disco.

En la recuperación, debemos retroceder hasta el inicio de la transacción más antigua en el listado del listado, para deshacerla en caso de que no haya *commiteado*, o para rehacer sus operaciones posteriores al $(\text{BEGIN CKPT})$ en caso de que haya *commiteado*.

Si encontramos primero un registro $(\text{BEGIN CKPT})$, entonces no nos sirve, y debemos buscar un *checkpoint* anterior en el log.
