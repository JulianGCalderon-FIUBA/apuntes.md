La recepción de los mensajes no es lo mismo que el *delivery* de los mismos.

- La recepción consiste en que los mensajes lleguen al sistema
- El delivery consiste en procesar los mensajes, provocando cambios en el sistema.

Los mensajes se mantienen en una cola, permitiendo demorar su delivery. Esto permite reordenarlos.

Por ejemplo, el protocolo TCP demora el delivery de los mensajes para asegurar que los mismos estén ordenados.

## Orden Sincrónico
