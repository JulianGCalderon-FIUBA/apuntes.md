Los sistemas reales sufren múltiples tipos de fallas:

- **Fallas de sistema:** Por errores de software o hardware que detienen la ejecución de un programa. Por ejemplo: fallas de segmentación, memoria, división por cero.
- **Fallas de aplicación:** Aquellos que provienen de la aplicación que utiliza la base de datos. Por ejemplo: la cancelación o vuelta atrás de una transacción.
- **Fallas de dispositivos:** Aquellas que provienen de un dato físico en dispositivos como discos rígidos o memoria.
- **Fallas naturales externas:** Son aquellas que provienen desde afuera del *hardware* en que se ejecuta nuestro gestor. Por ejemplo: caídas de tensión, terremotos, incendios.
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

Este algoritmo trabaja bajo la técnica de volcado de actualización inmediata. Debemos respetar las reglas:

- **Regla WAL:** Antes de que una transacción $T_i$ modifique el ítem $X$ remplazando $v_{old}$ por $v$, se escribe $(\text{WRITE}, T_i, X, v_{old})$ en el *log* y se vuelca al disco.
- **Regla FLC:** Antes de que $T_i$ haga *commit*, se escribe $(\text{COMMIT}, T_i)$ en el *log* y se vuelca al disco.
- Los ítems modificados deben ser guardados en disco antes de hacer *commit*.

Cuando el sistema reinicia, se siguen los siguientes dos pasos:

1. Se recorre el *log* de adelante hacia atrás, y por cada transacción de la que no se encuentra el $\text{COMMIT}$ se aplica cada uno de los $\text{WRITE}$ de forma inversa para restaurar el valor anterior a la misma en disco. Esto se debe a que ya sabemos que todas las transacciones que ya commitearon volcaron todos sus cambios en el disco.
2. Luego, por cada transacción de la que no se encontró el $\text{COMMIT}$, se escribe $(\text{ABORT}, T)$ en el *log* y se hace *flush* del *log* a disco.

Si ocurre una falla durante el reinicio, esto no es un problema porque el procedimiento de reinicio es **idempotente**. Si se ejecuta más de una vez, no cambiará el resultado.

### Algoritmo REDO

Este algoritmo trabaja bajo la técnica de volcado de actualización diferida. Debemos respetar las reglas:

- **Regla WAL:** Cuando una transacción $T_i$ modifica el ítem $X$ reemplazando el valor viejo por $v$, se escribe $(\text{WRITE}, T_i, X, v)$ en el *log* y se vuelca al disco.
- **Regla FLC:** Cuando una transacción $T_i$ hace *commit*, se escribe $(\text{COMMIT}, T_i)$ en el *log* y se vuelca al disco.
- Los ítems modificados deben ser guardados en disco después de hacer *commit*.

Cuando el sistema reinicia, se siguen los siguientes pasos:

1. Se analiza cuáles son las transacciones de las que está registrado el $\text{COMMIT}$.
2. Se recorre el *log* de atrás hacia adelante, volviendo a aplicar cada uno de los $\text{WRITE}$ de las transacciones que *commitearon*.
3. Luego, por cada transacción de la que no sé encontró el $\text{COMMIT}$, se escribe $(\text{ABORT}, T)$ en el *log* y se vuelca a disco.

Este algoritmo nos **obliga** a que nos volquemos los datos a disco hasta después de realizar el *commit*. Esto es un problema.

### Algoritmo UNDO/REDO

Este algoritmo nos permite volcar a disco en cualquier momento, no es necesario respetar alguna de las técnicas de volcado.

- **Regla WAL:** Antes de que una transacción $T_i$ modifique el ítem $X$ reemplazando un valor $v_{old}$ por $v$, se escribe $(\text{WRITE}, T_i, X, v_{old}, v)$ en el *log* y se vuelca a disco.
- **Regla FLC:** Cuando $T_i$ hace *commit*, se escribe $(\text{COMMIT}, T_i)$ en el *log* y se vuelca a disco.
- Los ítems modificados pueden ser guardados en disco antes o después de hacer *commit*.

Cuando el sistema reinicia, se siguen los siguientes pasos:

- Se recorre el *log* de adelante hacia atrás, y por cada transacción de la que no se encuentra el *commit*, se aplica cada una de las escrituras para restaurar el valor anterior a la misma a disco.
- Luego, se recorre de tras hacia adelante, volviendo a aplicar cada una de las escrituras de las transacciones que commitearon, para asegurar que quede asignado el nuevo valor de cada ítem.
- Finalmente, por cada transacción de la que no se encontró el *commit*, se escribe $(\text{ABORT}, T)$ en el *log* y se vuelca a disco.
