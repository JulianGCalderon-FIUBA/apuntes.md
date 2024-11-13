Permite ejecución remota de procedimientos, con un esquema de cliente-servidor

- El cliente realiza una llamada a un procedimiento
- El servidor responde con el resultado de la operación

La comunicación remota es transparente para el usuario.

Hay portabilidad a través de implementación de interfaces bien definidas.

## Interface Description Language

Son lenguajes que permiten que múltiples lenguajes puedan ser invocados entre sí.

Definen la interfaz de la comunicación en función de los tipos de entrada y de salida. Los tipos de dato se deben enviar como valor, ya que los punteros no tienen sentido en una llamada a través de la red.

Un ejemplo de esto es *Google Protocol Buffers*, que ofrece un estándar para el formato de los procedimientos y los mensajes a enviar.

## Tolerancia a Fallas

A diferencia de en una llamada local. Un mensaje puede llegar a ser recibidos 0, 1, o muchas veces. Hay distintas estrategias para mitigar esto:

- Request-Retry con Time out.
- Filtrado de operaciones duplicadas.
- Retransmisión y reejecución si se pierde un reintento.

## Implementación

En términos generales, tendremos las siguientes entidades:

- **Cliente**: Se conecta al *stub* y realiza llamadas de forma transparente al servidor**:
- **Servidor**: Se encuentra conectado a un *stub* del cual recibe llamadas y envía resultados. Posee lógica de negocio.
- **Stub**: Administra el *marshalling* de la información, y el envío al módulo de comunicación.
- **Comunicación**: Encapsula la comunicación con el servidor.
