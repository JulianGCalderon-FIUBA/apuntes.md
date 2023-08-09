La web permite que los usuario consulten información de forma dinámica, en el momento que ellos quieren. Por otro lado, es sorprendentemente fácil para cualquier individuo publicar información en la red.

## 1. Overview of HTTP

El ***HyperText Transfer Protocol (HTTP)*** es el corazón de la web, un protocolo de capa de aplicación que utiliza el protocolo de transporte ***TCP***.

Una página web consiste en un conjunto de objetos, los objetos son simplemente archivos, como un ***HTML*** o ***JPEG,*** accesibles a través de una única ***URL***. La mayoría de las páginas web consisten en un único archivo base, y múltiples objetos referenciados.

El navegador implementa el lado del cliente del protocolo ***HTTP***, mientras que los ***web servers*** implementan el lado del servidor del protocolo. Estos almacenan objetos direccionables por una ***url***.

Cuando un usuario pide una página web, envía un ***HTTP request*** para los objetos en esa página web, el servidor recibe los ***requests*** y reenvía los objetos en ***HTTP responses***.

El protocolo ***HTTP es stateless***. El servidor no almacena ninguna información de la conexión con los clientes, esto permite que sea más simple de implementar.

## 2. Non-Persistent and Persistent Connections

En las aplicaciones con conexiones no persistentes, se genera una conexión ***TCP*** por cada objeto a pedir, mientras que persistentes se mantiene una misma conexión para pedir todos los objetos.

Esto era originalmente así debido a que la cantidad de objetos de una página web y la velocidad de la conexión eran limitadas, por lo que no había necesidad de mantener conexiones abiertas con los clientes.

El navegador puede configurar la cantidad de conexiones paralelas a utilizar para hacer múltiples ***requests*** al mismo tiempo.

Si definimos el ***round-trip time*** que es el tiempo que le toma a un pequeño paquete viajar al servidor y volver, entonces el tiempo de pedir un archivo a un servidor ***web*** es de aproximadamente de 2 ***round-trip times***. Esto se debe a que ocurre un saludo inicial debido al protocolo ***TCP***.

### HTTP with Persistent Connections

En las conexiones no persistentes, se debe establecer y mantener una conexión por cada objeto a pedir. En las conexiones persistentes, el servidor deja la conexión ***TCP*** abierta luego de enviar la respuesta, esto permite que los siguientes llamados se envíen a través de esta misma conexión.

Además, múltiples pedidos pueden ser pedidos al mismo tiempo sin esperar a las respuestas de cada uno (pipelining), el servidor enviará las respuestas en cuanto pueda.

Hoy en día, la mayoría de los servidores web utilizan conexiones persistentes sin pipelining, aunque esto puede ser especificado en los mensajes ***HTTP***.

## 3. HTTP Message Format

Existen dos tipos de mensajes ***HTTP***. Los ***request messages*** y los ***response messages***.

Un ***request message*** consiste en múltiples líneas separadas por un ***CRLF***, organizadas en tres secciones. La primer línea se llama ***request line*** e indica el tipo de ***request*** (método), la *url* con la cual debe interactuar y la versión de ***http*** que se utiliza. Los métodos más comunes son: ***GET***, utilizado para pedir un objeto, y *POST, HEAD, PUT, DELETE*.

Luego, siguen una serie de ***header lines,*** cada una con el nombre del campo y su valor. Entre las campos más comunes se encuentran: ***Connection,*** utilizado para indicar si se quiere intentar tener una conexión persistente, *User-agent,* utilizado para indicar el tipo de navegador utilizado, ***Accept-language,*** utilizado para indicar el lenguaje de preferencia de la página web. Para indicar la finalización de la sección de cabecera se utiliza un ***CRLF*** extra.

Finalmente, está ***entity body***. El contiene el contenido del mensaje.

Un ***response message*** tiene una estructura similar a la del pedido. La primera línea se conoce como ***status line*** y contiene información acerca del resultado del pedido. Este tiene tres campos: la versión del protocolo, un código de estado, y el mensaje de estado correspondiente. Los códigos de error más comunes son: ***200 OK***, indicando que el pedido fue exitoso. ***301 Moved Permanently,*** indicando que el objeto no está disponible en esa dirección y indicando la nueva ***url*** en los ***headers. 400 Bad Request***, es un código de error genérico para cualquier pedido que no fue entendido. ***404 Not Found,*** indicando que el documento no existe en el servidor. y ***505 HTTP Version Not Supported,*** indicando que la versión del protocolo utilizada no es soportada por el servidor.

A continuación, al igual que en el ***request***, siguen las ***header lines*** y el *entity body.* Para el caso de una respuesta a un pedido de ***GET,*** esta sección contiene el objeto en sí.

Para generar las líneas de cabecera adecuadas, el navegador genera estas líneas en función de la versión del protocolo utilizada, la configuración del usuario, y el ***cache*** del ***end system***. El servidor ***web*** se comporta de la misma forma, generando automáticamente ***header lines*** según la información disponible.

## 4. User-Server Interaction: Cookies

Muchas veces, es necesario que una página web pueda identificar usuarios. Para esto, se utilizan las cookies. Estos se utilizan por los servidores web para llevar un registro de los usuarios.

Este tecnología utiliza cuatro componentes principales. Una línea de cabecera en la respuesta ***HTTP***. Una línea de cabecera en el pedido ***HTTP***. Un archivo de cookies que se almacena en el ***end system*** del usuario y es manejado por el navegador. Y una base de datos del servidor utilizada para almacenar la información de los usuarios.

Cuando un usuario se conecta a una página a la que nunca se había conectado, el servidor crea un identificador único y crea una entrada en una base de datos de los clientes, indexada por el identificador. Luego, envía este identificador en los ***headers*** de la respuesta al cliente a través del header ***"Set-cookie"***.

El usuario recibe el identificador en la respuesta y lo guarda en su navegador. La próxima vez que el usuario se conecte a la página web, enviará este identificador en uno de los ***headers*** para que el servidor pueda identificar al usuario. De esta forma, el servidor puede llevar un registro de los mensajes que envía un usuario al servidor web.

Las ***cookies*** pueden usarse para crear una capa de ***use session*** por encima del ***HTTP***. Aunque pueden simplificar algunos aspectos de la web para los usuarios, son controversiales debido a que se consideran una invasión a la privacidad.

## 5. Web Caching

Un ***web cache***, también conocido como un ***proxy server***, es una entidad que satisface pedidos ***HTTP*** en nombre del servidor de origen. Usualmente, estos ***web caches*** son instalados por los ***ISP***. El navegador puede ser configurado para que los pedidos ***HTTP*** se dirijan directamente el ***cache***.

El navegador se conecta a un ***web cache*** y le hace un pedido ***HTTP***. Si el ***caché*** tiene una copia del objeto entonces la envia. Si no la tiene, entonces abre una conexión con el servidor de origen y envía un ***request*** para el objeto. Una vez recibido, guarda el objeto en su copia local y envía una copia al cliente original.

Estos ***caches*** son desplegados usualmente por un ***ISP***, por dos razones principales. En primer lugar puede reducir sustancialmente el tiempo de respuesta de un pedido de un cliente. Por otro lado, también reduce drásticamente el tráfico del ***access link*** de una institución hacia el internet.

A través del uso de ***CDNs (Content Distribution Networks)***, los ***web caches*** cada vez cumplen un rol más importante en el internet. Estas compañías instalan múltiples ***caches*** distribuidos geográficamente para localizar el tráfico de internet.

### The Conditional GET

El ***caché*** introduce un nuevo problema, la copia del objeto que almacena puede quedar obsoleta. Para que los ***web caches*** puedan verificar la validez de una copia local, existe el ***conditional get***. Este es un mensaje HTTP que incluye la línea de cabecera "***If-Modified-Since"***.

Cuando se hace un pedido de un objeto a un ***caché***, este le envía un pedido al servidor original con el ***header*** indicado. Si este no ha modificado el archivo desde la fecha indicada, devolverá un mensaje vacío con el status line ***"304 Not Modified"***.
