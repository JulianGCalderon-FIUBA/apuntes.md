Los sistemas reales sufren múltiples tipos de fallas:

- Fallas de sistema: Por errores de software o hardware que detienen la ejecución de un programa. Por ejemplo: fallas de segmentación, memoria, división por cero.
- Fallas de aplicación: Aquellos que provienen de la aplicación que utiliza la base de datos. Por ejemplo: la cancelación o vuelta atrás de una transacción.
- Fallas de dispositivos: Aquellas que provienen de un dato físico en dispositivos como discos rígidos o memoria.
- Fallas naturales externas: Son aquellas que provienen desde afuera del *hardware* en que se ejecuta nuestro gestor. Por ejemplo: caídas de tensión, terremotos, incendios.
En situaciones catastróficas como los últimos dos, es necesario contar con mecanismo de *backup* para recuperar la información.

Si un sistema falla y se reinicia en medio de una transacción, la base de datos deberá ser llevada al estado inmediato anterior al comienzo de la transacción. Para ello, es necesario mantener información en el *log* acerca de los cambios que la transacción fue realizando.

## Técnicas de Volcado

Para cada instrucción de escritura, primero se guarda en un *buffer*, y luego en disco. Tendremos dos técnicas de volcado:

- **Actualización inmediata:** Los datos se guardan en disco lo antes posible, antes del commit de la transacción
- **Actualización diferida:** Los dos se guardan en disco después del commit de la transacción.

## Reglas WAL y FLC

El gestor de *logs* se guía por dos reglas básicas:

- **WAL (Write Ahead Log):** Indica que antes de guardar un ítem modificado en disco, se debe escribir el registro de *log* correspondiente, en disco.
- **FLC (Force Log at Commit):** Indica que antes de realizar el commit el *log* debe ser volcado a disco.

Esto implica que una vez está hecho el *commit*, toda la transacción fue registrada correctamente.

## Algoritmos de Recuperación

En los tres algoritmos, se asume que los solapamientos de transacción son recuperables y, es más, evitan *rollbacks* en cascada.

Como evito *rolbacks* en cascada, entonces no se permiten lecturas no *commiteadas*. Luego, no necesitaremos los registros de lectura `(READ, T, X, v)`.

### Algoritmo UNDO

Este algoritmo trabaja bajo la técnica de volcado de actualización inmediata.

- Antes de que una transacción $T_i$ modifique el ítem $X$ remplazando un - valor $v_{old}$ por $v$, se escribe $(\text{WRITE}, T_i, X, v_{old})$ en el *log* y se hace *flush* del *log* a disco.

Antes de que $T_i$ haga *commit*, se escribe $(\text{COMMIT}, T_i)$ en el *log* y se hace *flush* del *log* a disco.

Cuando el sistema reinicia, se siguen los siguientes dos pasos:

1. Se recorre el *log* de adelante hacia atrás, y por cada transacción de la que no se encuentra el $\text{COMMIT}$ se aplica cada uno de los $\text{WRITE}$ para restaurar el valor anterior a la misma en disco. Esto se debe a que ya sabemos que todas las transacciones que ya commitearon volcaron todos sus cambios en el disco.
2. Luego, por cada transacción de la que no se encontró el $\text{COMMIT}$, se escribe $(\text{ABORT}, T)$ en el *log* y se hace *flush* del *log* a disco.

Sí ocurre una falla durante el reinicio, esto no es un problema porque el procedimiento de reinicio es `IDEMPOTENTE`. Si se ejecuta más de una vez, no cambiará el resultado.
