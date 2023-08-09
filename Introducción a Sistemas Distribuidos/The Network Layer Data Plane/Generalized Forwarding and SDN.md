Previamente estudiamos el ***destination-based forwarding*** como un proceso de dos partes. La búsqueda de la dirección **ip** en una tabla ***(match)*** y el envió del paquete ***(action).*** Ahora consideremos un paradigma más general en el que el ***match*** se realiza a través de múltiples ***headers*** del ***datagram***, y ***action*** puede incluir múltiples acciones, como enviar el paquete a alguno de los puertos de salida, ***load balancing***, ***rewriting header values (NAT)***, bloqueando paquetes ***(firewall)***, enviando el paquete a un servidor especial para su procesamiento *(DPI)*

Debido a que la decisiones de envió pueden hacerse utilizando la capa de red o la capa de enlace, estos dispositivos fueron llamados ***packet switches***. Estudiaremos el estándar altamente visible y exitoso conocido ***OpenFlow***, el cual fue pionero en la noción de una abstracciones ***match-plus-action***.

Cada entrada en la tabla conocida como ***flow table incluye:***

- Un conjunto de valores de campos de encabezados a partir de los cuales el paquete será analizado.

    ![[Generalized Forwarding and SDN 1.png]]

- Un conjunto de contadores que serán actualizados cuando el paquete coincide con la entrada
- Un conjunto de acciones que deben tomarse cuando un paquete coincide con la entrada de la tabla

# 1. Match

La primera observación importante que la abstracciones de ***OpenFlow*** permite que el ***match*** se realice a partir de campos seleccionados a través de múltiples protocolos, permitiendo así al ***packet switch*** funcionar tanto como un dispositivo de capa tres (***router)*** como un dispositivo de capa dos (enlace).

Las entradas de la tabla también permiten comodines, permitiendo, por ejemplo, coincidir con todas los paquetes cuya dirección de destino comience con ***128.119.*.*.*** Si un paquete coincide con múltiples entradas, se tomará aquella con la mayor prioridad.

Por último, vemos que no todos los ***headers*** de **IP** pueden ser utilizados para el ***match***. Algunos ***headers*** fueron ignorados para priorizar funcionalidad por sobre complejidad.

# 2. Action

Cada entrada de la tabla puede tener cero o múltiples acciones. Si hay múltiples acciones, estás se realizan en el orden especificado. Algunas de las acciones más comunes son:

- ***Forwarding:*** Un paquete entrante puede ser direccionado a algún puerto de salida particular, también puede ser enviado a todos los puertos (***broadcast)*** o a algunos (***multicast)***. También puede ser encapsulado y enviado a un controlador remoto, para que este tome alguna acción como actualizar nuevas entradas en la tabla.
- ***Dropping:*** Un entrada sin acciones indica que el paquete será ignorado
- ***Modify-field***: Algunos valores de los ***headers*** del paquete pueden ser reescritos antes de ser enviados al/los puertos especificados.
