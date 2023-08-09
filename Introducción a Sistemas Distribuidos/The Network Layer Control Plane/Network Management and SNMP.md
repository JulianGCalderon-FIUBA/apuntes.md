El ***network management*** incluye el despliegue, integración, coordinación del ***hardware***, ***software***, y elementos humanos a monitorear, verificar, consultar, configurar, analizar, evaluar y controlar la red y los recursos necesarios para alcanzar un rendimiento operacional y en tiempo real, y los servicios de calidad necesarios a un costo razonable.

## 1. The Network Management Framework

Los componentes claves del manejo de red son:

- El ***managing server*** es una aplicación, supervisada por un humano, corriendo una estación de manejo de red centralizada en un centro de operaciones de red. El servidor controla la colección, el procesado, el análisis, y la visualización de la información del manejo de la red. Aquí se inicial as acciones necesarias para el control de comportamiento de la red.
- Un ***managed device*** es una pieza de equipamiento de red, incluyendo a su ***software***, que reside en una red manejada. Puede ser un ***host, router, switch, middlebox, modem, thermometer,*** o cualquier otro dispositivo conectado a la red. Los ***managed objects*** son las actuales piezas de ***hardware*** dentro de un ***managed*** device, y puede haber multiples por cada dispositivo.
- Cada ***managed object*** dentro de un ***managed device*** tiene información la cual es recolectada en un ***management information base (MIB)***. Estos valores están disponibles para el servidor. Los objetos ***MIB*** son especificados in un lenguaje de descripción de datos llamado ***SMI (Structure of Management Information). Los objetos*** MIB ***son reunidos en modulos MIB***.
- Dentro de cada ***managed device*** hay un ***network management agent***. Un proceso ejecutándose que se comunica con el servidor, tomando acciones locales debajo del comando y control del servidor.
- Finalmente, el ***network management protocol*** es ejecutado entre el servidor y los ***agents*** para permitirle al servidor consultar y establecer el información del dispositivo. Los ***agents*** también pueden utilizar el protocolo para informarle al servidor de eventos excepcionales. El protocolo no maneja la red, sino que provee una forma para que los administradores lo hagan.

## 2. The Simple Network Management Protocol (SNMP)

Este es un protocolo de capa de aplicación utilizado para el manejo de red. El uso mas común el modo de ***request-response***. El servidor envía una ***request***, el ***agent*** realiza cierta acción y envía una respuesta al servidor. Usualmente las ***requests*** serán de ***(query) consulta*** o *(set)* ***establecimiento de*** MIB objects ***asociados al dispositivo.*** Un segundo uso es el notificar al servidor de un evento excepcional mediante ***un trap message.***

Se definen siete tipos de mensajes, conocidos como ***protocol data units (PDUs)***.

- ***Get Request, Get Next Request, y Get Bulk Request***:** Son utilizados por el servidor para consultar uno o mas objetos ***MIB al dispositivo.*** Estos difieren en la granularidad de las consultas. El primero puede consultar uno o mas objetos, el segundo consulta el siguiente objeto en una lista, y el ultimo consulta grandes cantidades de información, por ejemplo de una gran tabla.
- ***Set Request*** es utilizado por un servidor para establecer uno o mas valores del dispositivo.
- ***Inform Request*** es utilizado por el servidor para notificar otro servidor información ***MIB***.
- ***Response PDU ***es típicamente utilizado por el dispositivo en respuesta a una consulta del servidor.
- ***Trap Message*** es utilizado para notificar al servidor de algún evento excepcional

Usualmente, el protocolo es implementado a través de ***UDP***. Hay un campo de **ID** utilizado por el servidor para detectar consultas o respuestas perdidas. No hay ningún procedimiento de reenvío implementado, o si quiera si debe realizarse en primer lugar.

El protocolo evoluciono a tres versiones, SNMPv1, SNMPv2, y SNMPv3. Se puede pensar a la tercera versión como una versión con mas capacidades de seguridad y administración.
