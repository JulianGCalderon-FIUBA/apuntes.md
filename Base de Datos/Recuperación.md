Los sistemas reales sufren múltiples tipos de fallas:

- Fallas de sistema: Por errores de software o hardware que detienen la ejecución de un programa. Por ejemplo: fallas de segmentación, memoria, división por cero.
- Fallas de aplicación: Aquellos que provienen de la aplicación que utiliza la base de datos. Por ejemplo: la cancelación o vuelta atrás de una transacción.
- Fallas de dispositivos: Aquellas que provienen de un dato físico en dispositivos como discos rígidos o memoria.
- Fallas naturales externas: Son aquellas que provienen desde afuera del *hardware* en que se ejecuta nuestro gestor. Por ejemplo: caídas de tensión, terremotos, incendios.
En situaciones catastróficas como los últimos dos, es necesario contar con mecanismo de *backup* para recuperar la información.

Si un sistema falla y se reinicia en medio de una transacción, la base de datos deberá ser llevada al estado inmediato anterior al comienzo de la transacción. Para ello, es necesario mantener información en el *log* acerca de los cambios que la transacción fue realizando.

Para cada instrucción de escritura, primero se guarda en un *buffer*, y luego en disco.

Tendremos dos tecnicas de volcado:

- Actualización inmediata: Losdatos se guardan en disco lo antes posible, antes del commit de la transacción
- Actualización diferida: Los dtos se guardan en disco despues del commit de la transacción.
