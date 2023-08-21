---
title: Mobile IP
---

La arquitectura de internet y los protocolos para soportar la movilidad, conocidos como ***mobile IP***, se definen principalmente en el ***RFC 5499*** para IPv4. Este estándar consiste en tres elementos importantes:

- ***Agent Discovery.*** Define los protocolos a utilizar para el agente local y el agente externo, para publicitar sus servicios a los nodos móviles, y los protocolos a utilizar para que los nodos móviles soliciten servicios a los agentes locales y externos.
- ***Registration with the Home Agent.*** Define los protocolos usados por los nodos móviles y los agentes externos para registrar y des-registrar COA con un agente local.
- ***Indirect Routing of Datagrams:*** Define la forma en la que los datagramas son enviados a los nodos móviles, desde los agentes locales. Incluye reglas para el envío, manejo de errores, y diversas formas de encapsulación.

Ademas, se deben considerar temas de seguridad, para evitar que un nodo malicioso se registre y cause que los datagramas destinados al usuario real, se destinen al nodo malicioso.

## Agent Discovery

Con ***agent advertisement***, un nodo extranjero o local publicita sus servicios a partir una extensión del ***existing router discovery protocol***. El agente periódicamente envía mensajes ICMP con el type field en 9, a todos los links a los que esta conectado. Esto permite a los nodos móviles, aprender la dirección de los agentes. Los campos mas importantes en la extensión, son:

- **Home agent bit (H)**. Indica que es un agente local para la red en la cual recide.
- ***Foreign agent bit (F).*** Indica que es un agente externo a la red en la cual recide.
- **Registration required bit (R).** Indica que un usuario local debe registrarse con el agente externo. No puede simplemente obtener la COF y sumir la funcionalidad del agente externo por si mismo
- ***M, G encapsulation bits.*** Indica si una forma de encapsulación que no sea ***IP-in-IP*** es utilizada
- ***Care-of address (COA) fields.*** Una lista de uno o mas COA provistas por el agente externo. El agente externo seleccionara una de las direccionas cuando se registra con su agente local.

Con **agent solicitation**, un nodo móvil que quiere descubrir agentes puede realizarlo sin necesidad de esperar un ***broadcast*** de los mismos. Para hacerlo, realiza un ***broadcast*** de un ***agent solicitation message.*** Este es un paquete ICMP con un *type value* de 10. Cuando un agente recibe la solicitud, este envía un ***agent advertisement*** directamente al nodo móvil (unicast).

## Registration with the Home Agent

Una vez un nodo móvil recibe un COA, esta dirección debe ser registrada con el agente local. Veremos el caso en el que esta funcionalidad es realizada por el agente externo.

1. Luego de la recepción del advertisement, el nodo móvil envía un paquete de registración al agente externo, este contiene el COA, la dirección del agente local (HA), la dirección permanente del nodo móvil (***MA)***, el tiempo de vida solicitado para la registración, y un identificador de la registración, de 64 bits. Este ultimo es utilizado como numero de secuencia, para identificar la respuesta.
2. Al agente externo recibe el mensaje de registración, y guarda la dirección permanente del nodo móvil. El agente ahora sabrá que debe estar atento a paquetes encapsulados, cuya dirección de destino interna sea la de la dirección permanente del nodo móvil. Ahora, el agente externo envía un paquete de registración al agente local, conteniendo la información indicada, ademas del formato de encapsulación requerida.
3. El agente local recibe el mensaje de registración y verifica la autenticidad del mismo. Luego, asocia la dirección permanente del nodo móvil con el COA. En el futuro, los datagramas recibidos dirigidos al nodo móvil, serán enviados a su COA. El agente local envía un ***registration reply*** para indicar que la solicitud fue aceptada.
4. El agente externo recibe la respuesta de registración y se lo envía al nodo móvil.

En este punto, la registración esta completa y el nodo móvil puede recibir datagramas enviados a su dirección permanente.
