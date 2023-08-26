Cuando movemos un paquete con una dirección de envío y destino dentro del mismo AS, el camino que este sigue es totalmente determinado por el *intra-AS routing protocol.* Para moverlo a través de múltiples AS, necesitamos un *inter-autonomous system routing protocol.* Todo el internet ejecuta el mismo *inter-AS routing protocol*, llamado **Border Gateway Protocol**, también conocido como BGP. Es un protocolo descentralizado y asincrónico que utiliza *distance-vector routing*.

## 1. The Role of BGP

En BGP los paquetes no son enviados a una dirección específica de destino, sino a *CIDRized prefixes*. Cada uno de ellos puede representar una **subred** o una colección de **subredes**. Las entradas de la tabla de envío serán de la forma `(x,l)` donde `x` es un prefijo `(138.16.68/22)` y `l` es el número de interfaz de una de las interfaces del router.

El protocolo BGP provee una forma para que cada router:

1. Obtenga información de accesibilidad de un prefijo de sus AS vecinos. Cada subred puede anunciar su existencia en el internet.
2. Determine las mejores rutas a los prefijos. Para realizarlo, ejecuta localmente un procedimiento de selección de BGP.

## 2. Advertising BGP Route Information

Por cada AS, cada router puede ser un *gateway router* o un *internal router*. El primero está en el borde del AS y puede comunicarse con uno o más routers externos, mientras que el segundo se conecta únicamente a hosts y routers dentro del AS.

Para anunciar la información de *ruteo*, los routers intercambian información a través de una conexión semipermanente de TCP a través del puerto 179. Este es conocida como una **BGP connection**.

Aquellas conexiones entre dos AS distintos se denominan *external BGP connection (eGBP)*, mientras que las conexiones entre routers de un mismo AS se denominan *internal BGP connection (iGBP).* Generalmente, hay una conexión *eGBP* por cada enlace que conecta de forma directa *gateway routers* en los distintos AS, y una conexión **iBGP** entre cada router dentro del AS

Los mensajes intercambiados son propagados a través de toda la red y contienen información de la ruta de AS a tomar para llegar desde cualquier router a un prefijo cualquiera.

## 3. Determining the Best Routes

Pueden existir múltiples caminos a una misma subred de destino, a través de distintos AS. Para decidir un camino, cuando un router se anuncia a través de una conexión, BGP incluye una serie de atributos, entre ellos **AS-PATH** y **NEXT-HOP**.

**AS-PATH** es una lista de AS por el cual el mensaje atravesó, la cual es actualizada cada vez que el mensaje llega a un nuevo AS. La lista también sirve para detectar y prevenir anuncios en *loops;* si un router ve que su AS ya está en la lista, ignora el anuncio.

**NEXT-HOP** tiene el valor de la dirección IP de la interfaz del router que comenzó el *AS-PATH*.

### Hot Potato Routing

En este protocolo, se elige la ruta que tenga menor costo hasta el router NEXT-HOP. Una vez determinado el mejor camino, se lo agrega a la *forwarding table* del router aclarando el prefijo y la interfaz que está en el mejor camino. Se utiliza tanto el protocolo *inter-AS* como el *intra-AS* para agregar un camino a una AS externa. Puede suceder que dos routers elijan caminos distintos para el mismo prefijo

La idea detrás de este protocolo es sacarte el paquete de encima lo antes posible (por esto, la analogía con una papa caliente), sin preocuparse por el costo de las demás porciones del sistema. Es un algoritmo egoísta.

### Route-Selection Algorithm

En la práctica, se utiliza un algoritmo más complejo que incorpora **hot potato routing.** Por cada prefijo de destino, la entrada del algoritmo es un conjunto de todas las rutas a ese prefijo que son conocidas y aceptadas por el router. Si hay más de un camino posible, se invocan reglas de eliminación hasta quedar uno solo:

1. Una ruta es asignada un valor preferencia local como uno de sus atributos. Esta preferencia local puede haber sido elegida por el router o recibida de oro router en el mismo AS. Es un valor que depende de una decisión política tomada por el administrador de la red.
2. De las rutas restantes, se selecciona la ruta con el *AS-PATH* más corto
3. De las rutas restantes, se utiliza *hot potato routing*. Se selecciona la ruta con el router *NEXT-HOP* más cercano.
4. Si queda más de una ruta, se utilizan identificadores BGP para seleccionar una.

## 4. IP-Anycast

BGP también se utiliza para implementar el servicio *anycast* de IP, utilizado comúnmente en DNS. Es útil para replicar el mismo contenido en múltiples servidores esparcidos geográficamente y que los usuarios accedan al servidor más cercano.

Durante el estado de configuración del *anycast*, la compañía CDN asigna la misma dirección IP a cada uno de sus servidores, y utiliza BGP para anunciar esa dirección desde cada servidor. Cuando un router recibe los múltiples anuncios para esa dirección, los toma como provenientes de distintos caminos de la misma dirección física, por lo que cuando configura su tabla de envío va a elegir la mejor ruta a esa dirección, efectivamente eligiendo el servidor más cercano.

En la práctica, los CDN eligen no usar *IP-anycast*, ya que los cambios en el ruteo de BGP pueden resultar en distintos paquetes de la misma conexión TCP llegando a distintas instancias del servidor. Sin embargo, es utilizado por el sistema DNS para dirigir consultas DNS al *servidor root* DNS más cercano.

## 5. Routing Policy

Usualmente, los puntos de acceso no permiten el tráfico externo (paquetes que atraviesan el punto sin tener ni origen ni destino en algún host de la *subnet* asociada). Para realizarlo, estos puntos de acceso no anuncian sus conexiones externas con otros AS, sino únicamente las conexiones internas. Nótese que únicamente es necesaria esta distinción para los *multi-homed access point*.

Los *backbone provider networks* no suelen querer gastar recursos en envíos de paquetes externos a su red, entonces por regla general solo se permite el manejo de tráfico de un flujo si el destino o el remitente se encuentran en esa red.

### Why are there different inter-AS and intra-AS routing protocols?

Existen diversas razones:

- **Policy:** Dentro de los AS, dominan las decisiones de política. Puede ser relevante que el tráfico en un AS no pase por otro AS específico, o un AS puede controlar el tráfico que lleva de un AS a otro. BGP permite tener atributos de *path* para tener una distribución controlada de la información.
- **Scale:** En el ruteo *inter-AS* la habilidad de un algoritmo y sus estructuras de datos de ser escalable para manejar *ruteos* entre números grandes de redes es un asunto crítico. Dentro de un AS, la escalabilidad no es tanto problema, ya que sé siempre se puede dividir en dos AS.
- **Performance:** Como el *ruteo* inter-AS es orientado a las políticas, la calidad de las rutas suele ser un tema secundario. Dentro de un AS, las políticas no son ta importantes, por lo que se le da más prioridad al *performance* de la ruta.
