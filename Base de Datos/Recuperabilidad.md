La seriabilidad de las transacciones ya nos asegura la propiedad de aislamiento. Nos interesa ahora asegurar que una vez que una transacción commiteó, la misma no deba ser deshecha. Esto nos ayudará a implementar de una forma sencilla la propiedad de durabilidad.

Un solapamiento es **recuperable** si y solo si ninguna transacción $T$ realiza el *commit* hasta tanto todas las transacciones que escribieron datos antes de que $T$ los leyera hayan commiteado.

## Bitacora (Log)

Dado un solapamiento recuperable, puede ser necesario deshacer (abortar) una transacción antes de llegado su *commit*, para ello el gestor deberá contar con una serie de información que es almacenada por su gestor de recuperación en un *log* (bitacora).

El *log* almacena los siguientes registros:

En particular, los valores viejos de cada item almacenados en los registros del *log* son los que permitirán deshacer los efe