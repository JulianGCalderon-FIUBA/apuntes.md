Permite ejecución remota de procedimientos, con un esquema de cliente-servidor

- El cliente realiza una llamada a un procedimiento
- El servidor responde con el resultado de la operación

La comunicación remota es transparente para el usuario.

Hay portabilidad a través de implementación de interfaces bien definidas.

## Tolerancia a Fallas

A diferencia de en una llamada local. Un mensaje puede llegar a ser recibidos 0, 1, o muchas veces. Hay distintas estrategias para mitigar esto:

- Request-Retry con Time out.
- Filtrado de operaciones duplicadas.
- Retransmisión y reejecución si se pierde un reintento.
