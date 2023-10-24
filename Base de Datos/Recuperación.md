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

Antes de que una modificación sobre un ítem $X \leftarrow v_{new}$ por parte de una transacción no *commiteada* sea guardada en disco, se debe salvaguardar en el *log* en disco el último valor commiteado $v_{old}$ de ese ítem.

Cuando una transacción modifica el ítem 
