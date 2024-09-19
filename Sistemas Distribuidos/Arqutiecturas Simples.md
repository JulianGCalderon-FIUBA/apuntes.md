## Cliente Servidor

Se definen roles para los participantes:

- Servidor como elemento pasivo y provee servicios
- Clientes activos que envían pedidos al servidor

Permite centralización en toma de decisiones, suele asumirse que los servidores tienen más capacidades de hardware que los clientes

Los clientes deben conocer la ubicación del servidor.

Los clientes no entablan comunicaciones entre sí, salvo a través del servidor.

Para obtener respuestas, hay distintas opciones:

- Long Polling: Se queda conectado esperando una respuesta
- Push Notificación: Cada cierto tiempo se conecta para ver si hay alguna notificación para el cliente. Son conexiones cortas.

## Peer to Peer

Se establece una red de nodos que se consideran pares entre sí. Se asume capacidades de recursos similares entre los pares.

Es muy útil cuando existen objetivos de colaboración por parte del negocio:

- Protocolo acordado entre partes
- La lógica distribuida requiere coherencia entre los nodos

Es muy difícil establecer comunicación entre pares.

- Es común un esquema mixto donde hay un servidor que provee un servicio de nombres.
- Otra opción es tener un grupo de comunicación donde ser comparten dirección de miembros.

Requieren mayores permisos de networking (reglas de firewall de entrada, rangos de puertos, etc)
