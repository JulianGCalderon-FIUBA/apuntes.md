---
title: Intra-AS Routing in the Internet OSPF
---

En la práctica, la idea de que todos los routers ejecutan el mismo algoritmo de ruteo es demasiado errónea por dos importantes razones:

- **Scale.** A medida que aumenta el número de routers, el costo de comunicación y cómputo se vuelve inmanejable.
- **Administrative Autonomy.** El internet es una red interconectada de ISP, cada uno consistiendo en su propia red de routers. Usualmente, los ISP querrán administrar su red de la forma que quieran, por lo que sería imposible que todos ejecuten el mismo algoritmo.

Ambos problemas se solucionan al organizar los routers en *autonomous system* *(AS)*. Cada AS consiste en un grupo de routers bajo el mismo control administrativo. Usualmente, los ISP constituyen un único AS, aunque algunos ISP pueden dividir su red en múltiples de ellos. Los sistemas autónomos son identificados por su **globally unique autonomous system number (ASN)**.

Los routers dentro de un mismo AS ejecutarán el mismo algoritmo de ruteo y compartirán información entre ellos. El protocolo de ruteo se llamará *intra-autonomous system routing protocol*.

## Open Shortest Path First (OSPF)

OSPF routing es ampliamente usado para *intra-AS routing* en el internet. *Open* indica que el protocolo de rutina está públicamente disponible. Es un protocolo de *link-state* que utiliza *broadcast* y *dijkstra* para calcular el camino de menor costo en cada router. Cada uno de ellos construye un mapa topológico completo del sistema. Los costos individuales son configurados por el administrador de red.

En este protocolo, los routers transmiten información a todos los routers del sistema autónomo, no solo hacia sus vecinos. Esta información se envía cuando cambia el estado de un *line*, y periódicamente (cada aproximadamente 30 minutos) incluso si el estado del link no cambió.

Los avances incluidos en OSPF incluyen:

- **Security.** Los mensajes intercambiados por los routers pueden ser autenticados para permitir que únicamente los routers con confianza puedan participar en el protocolo, previniendo intrusos. Existen dos tipos de autenticación, aunque por defecto ninguna es configurada. La autenticación simple utiliza contraseñas en los routers, la cual es enviada a través de los mensajes de red. La autenticación MD5 utiliza claves secretas compartidas configuradas en los routers. Se agregan códigos de hash a los paquetes, los cuales serán luego verificados por los routers que lo reciben, asegurándose que el remitente también contenga la clave secreta.
- **Multiple same-cost paths:** Cuando múltiples destinos tienen el mismo costo, el protocolo permite que múltiples caminos sean utilizados.
- **Integrated support for unicast and multicast routing.** El *Multicast OPSF* provee extensiones simples a OSPF para proveer *multicast routing*.
- **Support for hierarchy within a single AS:** Los AS pueden ser configurados jerárquicamente en áreas, donde cada área corre su propio algoritmo de ruteo. Dentro de cada área, se deben configurar *area border routers* responsables de redirigir paquetes fuera del área. Por último, debe existir un área configurada para ser la *backbone área*, la cual contiene todos los *area border routers* en el AS, pero puede contener algunos *non-border routers* también.
