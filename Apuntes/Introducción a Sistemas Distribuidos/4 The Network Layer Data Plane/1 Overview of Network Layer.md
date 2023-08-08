El principal rol del ***data plane*** es el de enviar los ***datagrams*** de un ***input link*** al ***output link*** en cada ***router*** del camino. El principal rol del ***control plane*** es el de coordinar estos envíos para que los ***datagrams*** sean transferidos ***end-to-end***, a lo largo de los caminos de routers entre los ***hosts*** en comunicación.

# 1. Forwarding and Routing: The Data and Control Planes

Podremos identificar dos funciones de capa de red importantes:

- ***Forwarding:*** Cuando un paquete llega a un router, este debe mover el paquete al ***output link*** adecuado. Este puede ser bloqueado de salir del router, debido a que fue originado por un ***malicious host*** o la dirección de destino está prohibida.
- ***Routing:*** La capa de red deberá determinar la ruta o el camino que toman los paquetes a medida que viajan desde un ***host*** a otro. Los algoritmos para calcular estos paths son conocidos como **routing algorithms.**

Un elemento clave para la capa de red es la ***forwarding table.*** El router examina algunos campos del ***datagram*** recibidos y los utiliza para indexar esta tabla, la cual le indica a cual ***output link*** deberá enviar el paquete.

Existen dos tipos principales de ***packet switches: Los*** link-layer switches ***basarán las decisiones de envió a partir de los valores del ***link-layer-frame***, mientras que los ***packet switches*** basarán las decisiones en los campos de cabecera del ***datagram***.

## Control Plane: The Traditional Approach

Los **routing algorithms** determinan el contenido de la ***forwarding table***. Para hacerlo, se comunican con los algoritmos de otros ***routers*** intercambiando ***routing information*** de acuerdo a un ***routing protocol***, computando así su propia tabla.

## Control Plane: The SDN Approach

Otro enfoque utilizado para estos algoritmos es el de utilizar un controlador remoto, el cual calculará y distribuirá las ***forwarding tables*** a todos los ***routers***. En este caso, los ***routers*** únicamente realizan la operación de ***forwarding.*** 

Estos controladores son implementados en un ***data center*** remoto con alta confiabilidad y redundancia, y puede ser administrado por un ISP ***o alguna otra organización. Para la comunicación entre los elementos, utilizaremos mensajes conteniendo ***forwarding tables*** y otras piezas ***de*** routing ***para comunicar los controladores con los ***routers***.

Se dice que este enfoque es de ***software-defined networking (SDN),*** debido a que las  tablas computadas y la interacción entre ***routers*** se implementa en ***software***.

# 2. Network Service Model

El modelo de servicio de red define las características del envío end-to-end entres dos ***hosts,*** estos pueden incluir:

- ***Guaranteed delivery:*** Garantiza que un paquete enviado llegue eventualmente a destino
- ***Guaranteed delivery with bounded delay:*** El paquete enviado llegara a destino dentro de un rango de ***delay*** especificado
- ***In-order packet delivery:*** Los paquetes llegaran a destino en el orden que fueron enviados
- ***Guaranteed minimal bandwidth:*** Asegurara un ancho de banda mínimo, mientras que la aplicación envíe los datos a por lo menos ese ancho de banda
- ***Security:*** La capa de red podría encriptar los datagrams y proveyendo confidencialidad de los paquetes.

La capa red del internet provee un único servicio, conocido como ***best-effort service***. Hará el mayor esfuerzo posible para cumplir con el envío, aunque no puede garantizar nada. Este servicio combinado con un ancho de banda adecuado han probado ser mas que suficientes para habilitar un amplio rango de aplicaciones