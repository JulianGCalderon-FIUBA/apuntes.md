Permite ejecución remota de procedimientos, con un esquema de cliente-servidor

- El cliente realiza una llamada a un procedimiento
- El servidor responde con el resultado de la operación

La comunicación remota es transparente para el usuario.

Hay portabilidad a través de implementación de interfaces bien definidas.

## Call Semantics

Según las estrategias adoptadas para asegurar el delivery de mensajes, los mensajes pueden llegar a ser recibidos 0, 1, o muchas veces.

- Sin control y sin garantía de recepción
- Reejecución sin filtro de duplicados.
- Retransmisión con filtro de duplicados

## Implementación

En términos generales, tendremos las siguientes entidades:

- **Cliente**: Se conecta al *stub* y realiza llamadas de forma transparente al servidor**:
- **Servidor**: Se encuentra conectado a un *stub* del cual recibe llamadas y envía resultados. Posee lógica de negocio.
- **Stub**: Administra el *marshalling* de la información, y el envío al módulo de comunicación.
- **Comunicación**: Encapsula la comunicación con el servidor.
