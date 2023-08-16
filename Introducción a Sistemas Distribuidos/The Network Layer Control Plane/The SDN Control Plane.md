Existe cuatro características claves de la arquitectura ***SDN*** (Software Distributed Networks):

- ***Flow-based forwarding***: El reenvío de paquetes puede ser basado en numerosos valores de multiples campos de cabecera tanto en la capa de transporte, como en la de red, como en la de enlace. Las reglas son especificas de una ***flow table***, la cual es computada y administrada por el ***control plane*** del ***SDN***.
- **Separation of data plane and control plane:** El plano de datos consiste en ***switches*** simples pero veloces que ejecutan reglas ***match plus action*** a partir de sus ***flow tables.*** El plano de control consiste en multiples servidores y ***software*** que determine el manejo de estas tablas.
- **Network Control Functions. External to Data-Plane Switches:** El plano de control consiste en dos componentes. Un controlador ***SDN*** y una serie de aplicaciones de ***network-control.*** El controlador mantiene información precisa de la red, provee esta información a las aplicaciones de control que ejecutan el ***control plane,*** y provee una forma mediante las cuales se pueden comunicar con los dispositivos de red subyacentes. El controlador es lógicamente centralizado, pero típicamente implementado en multiples servidores.
- ***A Programmable Network:*** La red es programable a través de las aplicaciones de control de red que se ejecutan en el plano de control. El controlador ofrece una interfaz que permite especificar y controlador los dispositivos del ***data plane***. Las aplicaciones pueden diversas cosas: determinar el camino de menor costo entre fuente y destino, realizar control de acceso para bloquear ciertos paquetes, ejecutar ***server load balancing***, entre otros.

## 1. The SDN Control Plane: SDN Controller and SDN Network-control Applications

La funcionalidad de un controlador puede ser separada en tres capas:

- ***A Communication Layer:*** Los controladores deberán poder transferir información a los dispositivos del plano de datos para poder administrarlos. Por el otro lado, los dispositivos deberán poder comunicar eventos observados localmente a el controlador, para que tengan una visión actualizada del estado de la red.
- ***A Network-wide State-management Layer:*** Para poder tomar las decisiones de control, los valores de las ***flow tables*** deberán estar disponibles para las aplicaciones. Debido a esto, el controlador puede mantener una copia de estas tablas para su fácil acceso.
- **The interface to the Network-control Application Layer:** El controlador provee una api mediante la cual las aplicaciones de control de red pueden leer y actualizar el estado de la red y sus tablas de flujo. Las aplicaciones a su vez pueden querer ser notificadas cuando ocurrió un cambió de estado, para poder tomar decisiones en respuesta.

Debido a que los controladores suelen ser implementados en multiples servidores, la semántica de las operaciones debe ser considerada (se debe mantener consistencia entre los servidores). Existen controladores que colocaron su énfasis en proveer un controlador lógicamente centralizado y físicamente distribuido *(OpenDaylight, ONOS).*

## 2. OpenFlow Protocol

Este protocolo opera entre un controlador ***SDN*** y un ***SDN-controlled*** switch, a través de ***TCP*** en el puerto por defecto ***6653.***

Entre los mensajes mas importantes enviados desde el controlador al ***switch*** están:

- ***Configuration:*** Este mensaje permite al controlador consultar o establecer los parámetros de configuración del ***switch***
- ***Modify-State:*** Este mensaje es utilizado por el controlador para agregar, eliminar, o modificar entradas en la tabla de flujo del ***switch,*** y establecer propiedades en los puertos del mismo.
- ***Read-State:*** Este mensaje es utilizado por el controlador para recolectar estadísticas y contadores de la tabla de flujo y los puertos.
- ***Send-Packet:*** Este mensaje es utilizado por el controlador para enviar un paquete particular a un puerto especifico del ***switch***.

Entre los mensajes mas importantes enviados desde el ***switch*** al controlador, están:

- ***Flow-Removed:*** Este mensaje informa al controlador que una entrada en la tabla de flujo fue eliminada, por ejemplo por un ***timeout*** o por la recepción de un mensaje ***modify-state***.
- ***Port-Status:*** Este mensaje informa al controlador de un cambio en el estado de un puerto
- ***Packet-In:*** Este mensaje informa al controlador del arribo de un paquete sin correspondiente entrada en la tabla. Tambien pueden ser enviados paquetes que tengan una entrada en la tabla, en consecuencia de una acción determinada.
