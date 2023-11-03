Una compañía necesita que sus empleados puedan editar planillas de cálculo colaborativamente. Debido a que la información es altamente sensible y desconfía de la privacidad utilizando servicios externos, decide implementar la suya.

Los empleados trabajan en el campo con poca conectividad, intercalando periodos conectados y desconectados.

Con frecuencia los empleados se encuentran editando la misma planilla, incluso editan las mismas celdas. Cuando esto último ocurre, el sistema informa al operador con un error.

Este es un problema donde hay un único recurso, compartido por múltiples actores.

## Soluciones

Algunas posibles soluciones son:

- [[Transacciones#Concurrencia Optimistica|Concurrencia Optimistica]]: Modifico localmente. Al guardar la información, si veo que el valor es distinto al que leí inicialmente, debo abortar la transacción.
- [[Transacciones#Timestamps|Timestamps]]: Similar al anterior, pero aplico los cambios dependiendo del timestamp de la persona que lo modifico anteriormente.
- [[Transacciones#Writeahead Log|Writeahead Log]]: Además de guardar la información, guardo un archivo de *log* que me permite deshacer la transacción que realice. No es necesario modificar localmente.
