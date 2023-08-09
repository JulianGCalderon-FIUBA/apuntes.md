En esta sección, consideraremos las redes ***Multiprotocol Label Switching (MPLS)***. En lugar de las ***circuit-switched telephone networks, MLPS*** es una ***packet-switched, virtual-circuit network***. Tiene sus propios formatos de paquetes y comportamientos de envío.

## 1. Multiprotocol Label Switching (MPLS)

El objetivo no era abandonar la infraestructura centrada en direcciones de destino en **IP**, sino selectivamente etiquetar datagramas y permitir a los routers ***reenviarlos utilizando etiquetas de tamaño fijo siempre que sea posible.

Los ***frames*** de ***MLPS*** agregan un pequeño ***header*** entre los ***headers*** de **IP** y los ***headers*** de *link-layer.* Entre ellos están: **Una etiqueta, tres bits reservados para uso experimental, un único bit S que es utilizado para indicar el final de una serie de ***stacked MPLS headers***, y un campo ***TTL***.

Los paquetes pueden ser enviados únicamente entre ***routers*** ***MPLS capable,*** usualmente conocido como ***label-switched router***.

La principalmente ventaja de ***MPLS*** subyace en la nuevas capacidades de manejo de trafico que estas ofrecen. El administrador de red puede configurar que distintos flujos viajen por distintos caminos, aunque estos tengan la misma dirección de destino. Esto es a partir de las etiquetas de MPLS.

A pesar de esto, ***MPLS*** siempre fue usado principalmente para la implementación de las conocidas ***VPNs***, o ***virtual private network***.
