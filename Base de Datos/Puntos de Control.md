Cuando [[Recuperación|reiniciamos]] el sistema, no sabemos hasta donde tenemos que retroceder en el archivo de [[Recuperabilidad#Bitácora (Log)|log]]. Aunque muchas transacciones antiguas ya *commiteadas* seguramente tendrán sus datos guardados ya en disco.

Para evitar este retroceso hasta el inicio del sistema y el crecimiento ilimitado de los archivos de *log* se utilizan puntos de control.

Un punto de control, o*checkpoint*, es un registro especial en el archivo de *log* que indica que todos los ítems modificados hasta ese punto han sido almacenados en disco.

La presencia de un *checkpoint* en el *log* implica que todas las transacciones cuyo registro de *commit* aparece con anterioridad tienen todos sus ítems guardados de forma persistente, y, por lo tanto, ya no deberán ser deshechas ni rehechas.

## Checkpoints Inactivos vs. Activos

Los *checkpoints* inactivos *(quiescent checkpoints)* tienen un único tipo de registro: $\text{CKPT}$.

La creación de un *checkpoint* inactivo en el *log* implica la suspensión momentánea de todas las transacciones para hacer el volcado de todos los *buffers* en memoria a disco.

Para aminorar la perdida de tiempo de ejecución en el volcado a disco, puede utilizarse una técnica conocida como *checkpoining* activo (*non-quiescent* o *fuzzy checkpointing*). Esta utiliza dos tipos de registros de *checkpoint*: $(\text{BEGIN CKPT}, t_\text{act}$) y $(\text{END CKPT})$, en donde $t_\text{act}$ es un listado de todas las transacciones que se encuentran activas.

## Algoritmo [[Recuperación#Algoritmo UNDO|UNDO]]

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

## Algoritmo [[Recuperación#Algoritmo REDO|REDO]]

En este algoritmo, el procedimiento con un *checkpointing* activo se realiza de la siguiente manera:

1. Escribir un registro $(\text{BEGIN CKPT}, t_\text{act})$ con el listado de todas las transacciones activas hasta el momento, y volcar el *log* a disco.
2. Hacer el volcado a disco de todos los *ítems* que hayan sido modificados por transacciones que ya *commitearon*.
3. Escribir $(\text{END CKPT})$ en el *log* y volcarlo a disco.

En la recuperación, se dan dos situaciones:

- Si encontramos primero un registro $(\text{END CKPT})$, deberemos retroceder hasta el $(\text{BEGIN}, T_x)$ de la transacción más antigua del listado que figure en el $(\text{BEGIN CKPT})$.
- Si encontramos primero un registro $(\text{BEGIN CKPT})$, entonces debemos retroceder
