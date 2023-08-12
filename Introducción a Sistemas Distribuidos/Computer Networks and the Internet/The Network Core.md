En esta sección, se encuentra malla densa de ***packet switches*** y ***links*** que interconecta a los ***end systems*** de internet

## 1. *Packet Switching*

En una aplicación de red, los ***end systems*** intercambian mensajes entre ellos. Para enviar un mensaje, la fuente separa los largos mensajes en pequeños ***chunks*** de información conocidos como ***packets*** o paquetes. Cada paquete viaja a través de una serie de ***communication links*** y ***packet switches,*** de los cuales hay dos tipos principales: ***routers*** y ***link-layer switches***.

### Store-and-Forward Transmission

La mayoría de los ***packet switches*** utilizan este método en las entradas del los ***links***. Consiste en que el ***switch*** debe recibir el paquete por completo antes de ser enviado.

### Queuing Delays and Packet Loss

Ún ***packet switch*** tiene múltiples ***links*** conectados a él. Por cada ***link***, se tiene un buffer en el que se almacena el ***packet guardado.***

Si en el momento enviarlo, se encuentra que el ***link*** se está utilizando para otro paquete, entonces los datos tienen que esperar en este ***buffer***. De esta forma, además de *los retrasos de* store-and-forward, hay retrasos de cola. Estos ***delays*** son variables y dependen del nivel de congestión de la red.

Como el espacio del ***buffer*** es limitado, un paquete entrando puede encontrarse con que el buffer aún está ocupado. En este caso, ocurre una pérdida de paquetes.

### Forwarding Tables and Routing Protocols

¿Cómo determina el ***switch*** a qué ***link*** enviar el paquete? Esto varía según la red en la que se encuentra, pero en el internet cada sistema contiene una dirección IP. Esta dirección tiene una estructura jerárquica. Cuando un ***end system*** quiere enviar un paquete, se incluye la dirección final en el ***header***.

Cuando llega un ***paquete***, el ***router*** examina la dirección indicada y lo envía a través del ***link*** correspondiente, a partir de una tabla de envío (***forwarding table).*** El internet tiene una serie de protocolos de rutina ***(routine protocols)*** que se utilizan para configurar una tabla de envío. Estos, por ejemplo, buscan el mejor camino posible para llegar a un ***host***.

## 2. *Circuit Switching*

Hay dos enfoques fundamentales para mover información a través de la red: ***circuit switching*** y ***packet switching***. En las redes de ***circuit-switching,*** los recursos requeridos a lo largo de la ruta son reservados por la duración de la misma.

Las redes de teléfono tradicional utilizan este enfoque. Antes de que se pueda enviar la información, la red primero debe establecer una conexión entre ambos. Este tipo de conexión se denomina como **circuito**. Cuando una red establece un circuito, se reserva una taza de transmisión constante entre los ***links***. Esta taza está garantizada.

### Multiplexing in Circuit-Switched Networks

Para permitir que un mismo ***link*** pueda ser utilizado por más de un circuito, se utiliza alguna de las siguientes técnicas:

- ***frecuency-division multiplexing (FDM)***: El espectro de frecuencias de un ***link*** se divide entre las conexiones establecidas a través del ***link***.
- ***time-division multiplexing (TDM)***. El tiempo se divide en frames de duración fija, y cada frame se divide en *time-slots* fijos

### Packet Switching Versus Circuit Switching

Algunos argumentan que *Packet switching* no es del todo adecuado para ***real-time*** services, debido a su variabilidad y retrasos, aunque es más eficiente y más simple. Hoy en día este enfoque es más utilizado.

El factor más importante a la hora de decidir es el tiempo inactivo de los usuarios. Cómo ***circuit switching*** reserva un espacio para todos los usuarios, independientes de su actividad. No se pueden aprovechar momentos de inactividad como en el otro enfoque.

## 3. A Network of Networks

Los usuarios se conectan a ***ISP*** de accesos, pero estos a su vez deben estar conectados entre sí. Para esto, se forma una red de redes.

Los ***ISPs*** tienen inicialmente una estructura jerárquica en forma de árbol de múltiples niveles. En el nivel más bajo se encuentran los *access ISP* (de alcance local) que proveen internet a las casas. Estos se conectan a los *Regional ISP,* los cuales a su vez están conectados con los *Tier 1 ISP* (De alcance global)

Además de esta estructura, cuentan con algunos conceptos adicionales.

- **POP (Point of Presence):** Es simplemente un grupo de routers en una misma ubicación que utilizan los clientes para conectarse con su proveedor.
- ***Multi-Home:*** A veces, un *ISPs* puede conectarse a más de un proveedor, para poder funcionar incluso si uno de esos dos proveedores cae.
- ***Peer:*** Dos ***ISPs*** regionales del mismo nivel pueden conectarse para que las conexiones locales pasen por ahí, en lugar de ir a sus proveedores.
- **IXP (Internet Exchange Point):** Punto de encuentro entre distintos ***ISPs***.
- ***content-provider networks:*** Redes específicas para una empresa que manejan el tráfico de información de la misma, pero siempre conectados al internet global. Estas redes intentan evitar los niveles más altos, conectándose directamente con los ***ISPs*** de bajo nivel. De esta forma, obtienen buen rendimiento con los usuarios conectados directamente. Estas redes también se conectan con los ***ISPs*** de mayor nivel, ya que muchos **ISPs** solo pueden ser alcanzados a través de ellos.
