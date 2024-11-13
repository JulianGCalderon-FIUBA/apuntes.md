Se establece una red de nodos que se consideran pares entre sí. Su popularidad creció desde la invención de Napster, BitTorrent, etc.

Son muy útiles cuando existen objetivos de colaboración por parte del negocio:

   - Protocolo acordado entre partes
   - La lógica distribuida requiere coherencia entre los nodos

Asume capacidades de recursos similares entre los pares

Es muy difícil de establecer la comunicación entre pares. Hay dos alternativas para solucionar esto:

- Esquema mixto como cliente-servidor para proveer un servicio de nombres. Los pares se registran en el servidor.
- Grupo de comunicación donde se comparten dirección de miembros. Este concepto a veces se denomina *gossip*.

Estas arquitecturas requieren mayores permisos de networking (reglas de firewall de entrada, rangos de puertos, etc.).
