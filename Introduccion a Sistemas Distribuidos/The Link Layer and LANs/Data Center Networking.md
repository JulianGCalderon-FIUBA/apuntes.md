---
title: Data Center Networking
---

Recientemente, muchas grandes compañías han construido ***data centers*** masivos que utilizan para almacenar mucha información y soportar de forma concurrente muchas aplicaciones nube. Cada ***data center*** tiene su propia data center network.

Los hosts dentro de un data center, llamados ***blades***, son hosts que incluyen CPU, memoria, y almacenamiento de disco. Estos son apilados en racks. Por encima de los racks, hay un ***switch,*** comúnmente llamado ***Top of Rack (TOR) Switch,*** que interconecta los hosts en el rack con el resto de hosts del ***data center***. Los hosts tienen tarjeta de interfaces de red que se conectan con el ***TOR switch,*** y cada ***TOR Switch*** tiene puertos adicionales para conectarse con otros ***switches***. Cada host tiene asignada su propio IP interna del ***data center***.

En los ***datacenters*** hay dos tipos de tráfico. El primero es entre clientes externos y hosts internos, para manejar este tráfico se incluyen ***border routers*** que conectan los ***data centers*** con el internet. Los ***racks*** conectan a los hosts ***con los*** border routers*.* El segundo tipo de tráfico es entre los ***hosts internos*** y se resuelve a partir de la red de ***switches*** que conectan los ***racks***.

## Load Balancing

Cada aplicación tiene asociada una IP pública que es recibida por el ***data center.*** Para soportar peticiones de clientes externos, las peticiones son primero dirigidas a un ***load balancer*** que tiene el trabajo de tomar las peticiones y repartirlas entre los hosts de forma distribuida. En grandes ***data centers***, puede haber multiples ***load balancers***, cada uno encargado de una aplicación distinta. Cuando el host termina de resolver la petición, este envía la respuesta al ***load balancer*** el cual le devolverá la respuesta al cliente.

Estos ***load balancers*** suelen ser referidos como ***layer-4 switch*** debido a que toma decisiones basadas en el puerto de destino y a la dirección de destino. Tambien realiza funciones de NAT, traduciendo las direcciones de IP externas en direcciones de IP internas al ***data center***.

## Hierarchical Architecture

Para ***data centers*** grandes, se emplea una estructura jerárquica para la red. Por encima de todo, están los ***border routers***, que se conectan con los ***access routers.*** Cada ***access router*** se conecta con un ***top tier switch***, los cuales a su vez se conectan con multiples ***second-tier-switch*** y un ***load balancer***. Cada ***second tier switch*** a su vez se conecta con múltiples ***racks*** a través de los ***TOR switches***. Típicamente todos los links utilizan ethernet para la capa de enlace y la capa física.

Debido a la importancia de proveer servicio de alta disponibilidad, los ***datacenters*** suelen contar con equipamiento y enlaces redundantes en sus diseños. Cada ***TOR switch*** se puede conectar con dos **tier-2 switches**, y cada ***access router, tier-1 switch*** y ***tier-2 switch*** puede ser duplicado e integrado en el diseño.

Para localizar el tráfico de ***broadcast***, cada *subnet* es particionada en pequeñas redes VLAN, cada uno con algunos cientos de hosts.

Esta arquitectura sufre de limitada capacidad ***host-to-host,*** y es todavía más evidente si deben conectarse más arriba en la jerarquía. Una posible solución podría ser mejorar la velocidad de los ***switches*** y routers, pero es una solución muy cara.

Soportar un gran ancho de banda es un requerimiento clave para los ***datacenters***, ya que se centran en la alta coordinación y comunicación entre sus hosts para resolver los pedidos.

## Trends in Data Center Networking

Para reducir el costo de los *data centers* y aumentar el rendimiento, se despliegan constantemente nuevos diseños de redes para los ***data centers***.

Un enfoque puede ser el de reemplazar la jerarquía de ***switches*** por una topología ***fully connected***. En este diseño, los ***tier-1 switches*** se conectan con todos los ***tier-2 switches***. De esta forma, el tráfico no exceda la jerarquía de switches, y halla muchos caminos posibles (se distribuiría mejor el tráfico)

Este diseño no solo alivia la limitación *host-to-host*, sino que además crea un ambiente flexible de computación y servicio en el que dos racks que no pertenezcan al mismo switch puedan comunicarse entre sí sin importar de donde están en el data center.

Otro enfoque, llamado ***MDC (modular data center)*** consiste en agrupar en contenedores pequeños y cercanos entre sí miles de hosts, agrupados en decenas ***de racks***. ***Múltiples*** contenedores son a su vez interconectados entre ellos y con el internet. Estos contenedores ya son prefabricaos y son difíciles de mantener, por lo que su rendimiento se degradara lentamente, pero continuaran operando. Una vez la tasa de errores pasa cierto umbral, son removidos y reemplazados por uno nuevo

Con MDC tendremos dos tipos de redes, las redes internas de los contenedores, y la red central que conecta los contenedores. El diseño de la red central es un problema desafiante, ya que consiste en conectar múltiples contenedores, cada uno con miles de hosts.

Cuando se usan topologías altamente interconectadas, uno de los mayores problemas es diseñar los algoritmos de ***ruteo*** entre los ***switches***. Existen múltiples posibilidades como ***random routing***, o dejar que los hosts se encarguen de inteligentemente dirigir tráfico a los ***switches***.

Otra estrategia es la de construir y customizar todos los dispositivos y protocolos dentro de un ***datacenter*** para que se ajuste a sus necesidades.

Amazon fue el pionero en mejorar la fiabilidad de los ***data centers*** mediante replicar distintos ***data centers*** en edificios cercanos. Al estar cerca, se puede sincronizar fácilmente la información entre edificios.

Muchas innovaciones surgirán en el futuro acerca de como diseñar un ***data center*** de forma eficiente.
