Con una arquitectura ***P2P*** tendremos mínima o nula dependencia en servidores. En su lugar tendremos pares de ***hosts*** conectados, llamados ***peers,*** que se comunican entre ellos de forma directa.

## Scalability of P2P Architectures

Denotemos $u_s$ la tasa de subida del servidor, $u_i$ la taza de subida del cliente $i$, y $d_i$ la taza de descarga del cliente $i$. Considerando un archivo de tamaño $F$ y un número $N$ de clientes. El tiempo de distribución es el tiempo que toma distribuir el archivo a todos los clientes.

El tiempo mínimo será el máximo entre el tiempo de subida máximo del servidor a todos los clientes, y el tiempo de descarga mínimo de los clientes.

$$
\text{DCS} = \max\{{NFu_s,Fd_{\min}}\}
$$

El tiempo de distribución aumenta linealmente con el número de clientes.

Para el caso de una arquitectura P2P, cuando un cliente recibe información, puede comenzar a transmitirla a otros ***clientes.*** Ahora, la tasa de subida del archivo es la del servidor junto a la de cada uno de los clientes. Mientras que el servidor solo tiene que subir el archivo al menos una vez.

$$

\text{DP2P} = \max\{{Fu_s,Fd_{\min}},NF(u_s + \small\sum u_i)\}

$$

Vemos que el aumento no es lineal, ya que a medida que aumenta $N$, también aumenta la capacidad de la red.

## BitTorrent

Es un protocolo popular para la distribución de archivos. En la jerga de *BitTorrent*, una colección de clientes participando en una distribución de un archivo particular se conoce como un ***torrent***. Los ***peers*** en un ***torrent*** se transfieren ***chunks*** de tamaño fijo de unos a otros. Los clientes ***descargan*** y ***envían*** ***chunks*** de forma simultánea.

Cada torrent tiene un nodo de infraestructura llamado ***tracker***. Cuando un usuario se una a un ***torrent,*** se registra en el *tracker* y le informa periódicamente que sigue allí. Cuando un ***peer*** se une a un ***tracker***, este le envía de forma aleatoria un subconjunto de *peers.* El usuario tratará de establecer conexiones *TCP* concurrentes con todos los clientes de la lista. Estos se llamarán ***neighboring peers***. El usuario solicita una lista de ***chunks*** de cada *neighboring peer* y les pide los que necesita, utilizando un enfoque de ***rarest first***.

Para determinar que ***requests*** de ***peers*** responde, el usuario le envía ***chunks*** a los clientes que más ***throughput*** le proveen ***(unchoked peers)***, agregando uno más de forma aleatoria *(optimistically unchoked)*. Este algoritmo tiene nombre de ***tit-for-tat***, produce que los ***peers*** más compatibles tienen a encontrarse, aumentando la velocidad de descarga.
