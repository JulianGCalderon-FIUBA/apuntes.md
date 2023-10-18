Cuando se ejecutan [[Transacción|transacciones]] en forma [[Base de Datos/Concurrencia|concurrente]] se da lugar a distintas situaciones anómalas que pueden violar las [[Transacción#Propiedades ACID|propiedades ACID]].

## Lectura Sucia

La anomalía de la **lectura sucia** ocurre cuando una transacción $T_2$ lee lo que ha sido modificado por otra transacción $T_1$.

Si luego $T_1$ debe ser deshecha, entonces la lectura de $T_2$ no fue válida, esto implica que $T_2$ también debe ser deshecha. Si cuando se debe deshacer $T_2$, encontramos que ya se había realizado *commit*, entonces estaremos ante un error.

Esta anomalía también se la conoce con el nombre de *temporary update* o *read uncommited data*.

Esta anomalía es un conflicto del tipo $WR$ (escritura-lectura)

$$
W_{T_1}(X)\dots R_{T_2}(X)\dots (a_{T_1} \lor c_{T_1})
$$

## Actualización perdida

La anomalía de la **actualización perdida** ocurre cuando una transacción $T_1$ lee un valor que es luego modificado por $T_2$. Si la primera transacción luego modifica el valor, lo hará en base al valor leído inicialmente, y la modificación de $T_2$ se perderá.

Si, en cambio, la primera transacción volvería a leer el ítem luego de que la segunda la escribiera, se encontraría un valor distinto. Este caso se conoce como **lectura no repetible** (*unrepeatable read*)

Esta anomalía es un conflicto del tipo $RW$, seguido por otro de tipo $WW$ o $WR$.

$$
R_{T_1}(X)\dots W_{T_2}(X)\dots(a_{T_1} \lor c_{T_1})
$$

## Escritura Sucia

La anomalía de **escritura sucia** ocurre cuando una transacción $T_2$ escribe un item que ya habia sido escrito por otra transacción $T_1$.

Si $T_1$ luego aborta, se deshacera el cambio de $T_2$ también. También se conoce con el nombre de *overwrite uncommited*.

Esta anomalía es un conflicto del tipo $WW$.

$$
W_{T_1}\dots W_{T_2}\dots (a_{T_1} \lor c_{T_1})
$$

## Fantasma

La anomalía del **fantasma**, se produce cuando una transacción $T_1$ observa un conjunto de items que cumplen determinada condición, y luego dicho conjunto cambia porque algunos de sus items son modificados/creados/eliminados por otra transacción $T_2$.

Si esta modificación se hace mientras $T_1$ aún se esta ejecutando, $T_1$ podría encontrarse con que el conjunto de ítems que cumplen la condición cambío. Esta condición atenta contra la serializabilidad.

Se puede caracterizar como:

$$
R_{T_1}(\{X|\text{cond}\})\dots W_{T_2}(X_\text{cond})\dots(a_{T_1} \lor c_{T_1})
$$
