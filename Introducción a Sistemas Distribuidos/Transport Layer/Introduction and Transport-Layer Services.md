Un protocolo de cada de transporte provee comunicación lógica entre procesos ejecutándose en diferentes ***hosts***. Con ***comunicación lógica***, nos referimos a que desde la perspectiva de la aplicación, es como si ambos ***hosts*** estén directamente conectados.

# 1. Relationship Between Transport and Network Layers

Mientras que el protocolo de capa de transporte provee comunicación lógica entre procesos ejecutándose en distintos ***hosts***, un protocolo de capa de red provee comunicación lógica entre los ***hosts***.

Dentro de un ***end system***, un protocolo de transporte mueve los mensajes desde la aplicación al borde de la red (***network layer***), pero no dice nada sobre como estos mensajes son enviados dentro del centro de la red.

Una red de computadores ofrece múltiples protocolos de transporte, con cada uno ofreciendo un modelo de servicios distinto a sus aplicaciones. Los servicios que estos protocolos proveen usualmente están limitados por los servicios del protocolo de red subyacente. Si un protocolo de red no puede proveer garantías de ***delay*** o ***bandwidth***, entonces la capa de transporte tampoco puede hacerlo.

Sin embargo, algunos servicios  pueden ser ofrecidos por los protocolos de transporte incluso cuando la capa de transporte subyacente no lo hace. Por ejemplo, la capa de transporte puede ofrecer transferencia de datos confiable a una aplicación incluso cuando la red subyacente no lo es. Otro ejemplo es el de la encriptación para garantizar que los mensajes no sean leídos por intrusos.

# 2. Overview of the Transport Layer in the Internet

El protocolo **IP** provee comunicación lógica entre *hosts*, ofrece un servicio de ***best-effort delivery***, esto significa que el protocolo hará su mejor esfuerzo para entregar la información, pero que puede garantizar nada. Debido a esto, se dice que el protocolo **IP** es un ***unreliable service***.

La extensión de la entrega ***host-to-host*** a una entrega ***process-to-process*** se llama ***transport-layer multiplexing***. Además de este servicio, ***UDP*** y ***UTP*** ofrecen ***integrity checking*** con campos de detección de error. Estos dos servicios minimales son los únicos que ofrece ***UDP***. Así como el protocolo **IP**, ***UDP*** es un ***unreliable service***.

***TCP***, por el otro lado, oferece servicios adicionales a sus aplicaciones. En primer lugar, ofrece ***reliable data transfer***. Utilizando control de flujo, números de secuencia, ***acknowledgments*** y ***timers***, este protocolo asegura que la información se enviará exitosamente y en el orden correcto. Por otro lado, también ofrece ***congestion control.*** Este no es un servicio para la aplicación que lo usa, sino para el bien de todo el internet. Previene que una conexión ***TCP*** inunda los ***links*** y ***routers*** entre los ***hosts*** con una excesiva cantidad de trafico.