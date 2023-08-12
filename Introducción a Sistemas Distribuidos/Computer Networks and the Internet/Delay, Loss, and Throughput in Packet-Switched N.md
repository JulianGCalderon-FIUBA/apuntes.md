## 1. Overview of Delay in Packet-Switched Networks

A medida que un paquete viaja de un nodo al siguiente, este sufre de de diversos tipos de ***delays*** en cada nodo a lo largo del camino. Los más importantes son: ***nodal processing delay, queuing delay, transmission delay,*** y ***propagation delay***. Juntos, estos ***delays*** se acumulan en un único ***total nodal delay***.

La contribución de estos componentes puede variar significativamente según las condiciones. El ***processing delay*** suele ser insignificante.

$$
d_{\text{nodal}} = d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}}
$$

### Processing Delay

El tiempo requerido para examinar el ***header*** del paquete y determinar a donde enviarlo es parte del ***processing delay***, aunque también puede incluir otros factores, como los chequeos de errores a nivel de bit. Luego de este procesamiento, el router dirige el paquete a la ***queue*** que le precede al ***link*** correspondiente.

### *Queuing Delay*

En la cola, el paquete experimenta el ***queuing delay*** mientras espera a ser transmitido al link. El tiempo de este paquete dependerá de la cantidad de paquetes que se encuentren delante de él.

### Transmission Delay

Sea $L$ el largo en *bits* de un paquete, y $R$ la tasa de transmisión del ***link*** en ***bits/secs***. Entonces el ***transmission delay*** sera de $L/R$. Esta es la cantidad de tiempo requerida para ***pushear*** el paquete al ***link***.

### ***Propagation Link***

Una vez ***pusheado*** el paquete en el ***link***. Necesita propagarse al router siguiente. El tiempo requerido para propagar el paquete desde el inicio al final del ***link*** se conoce como ***propagation delay***. Este dependera del medio fisico y la longitud del trayecto.

## 2. Queuing Delay and Packet Loss

Es ***queuing delay*** es el retraso más interesante y complicado de todos. Varía de paquete a paquete, por lo que se suelen usar métricas como el promedio o la varianza para analizarlo.

Supongamos que los paquetes tendrán una largo de $L$ bits. Sea $a$ la frecuencia promedio en la los paquetes llegan a la cola, en unidades de ***packets/secs***. y $R$ la tasa de transmisión (***bits/secs)***. Entonces la frecuencia de arribo de bits a la cola será de $La$ ***bits/secs.*** Denominamos ***traffic intensity*** a la relación entre el arribo y la transmisión: $La/R$. Evitaremos a toda costa que esta relación sea menor a 1, ya que eso implicaría un retraso creciente en el envió de información.

Cuando la intensidad es menor a 1, entonces la naturaleza del tráfico impacta el retraso. Si la llegada se produce en cortos estallidos de información, entonces se pueden producir pequeños retrasos estables. Afortunadamente, el arribo de datos suele tener una distribución aleatoria.

A medida que la intensidad del tráfico se acerca a 1, El retraso promedio aumenta rápidamente. Un pequeño incremento en la intensidad resultará en un gran aumento en el ***queuing*** ***delay***

### Packet Loss

La capacidad de cola de un ***packet switch*** es limitada. Cuando un paquete llega, este puede encontrarse con una cola llena. Sin lugar donde ser almacenado, el ***router*** descarta el paquete.

Desde el punto de vista de un ***end system***. El paquete parecerá ser enviado pero jamás arribara a destino.

## 3. End-to-End Delay

Ahora, analizaremos el retraso de una comunicación al atravesar un número $n{-}1$ de **nodos**. En este caso, los retrasos de cada nodo se acumularian para llegar al retraso de punta a punta. Podemos llegar a una ecuación generalizada de el retraso de punta a punta. Sumando los retrasos de cada uno de los nodos. Asumiremos que el ***delay*** es constante en cada nodo

$$
d_{\text{end-end}} = N\times d_{\text{nodal}}
$$

### End System, Application, and Other Delays

Además de los delays mencionados, algunos protocolos introducen nuevos delays como parte de un protocolo para compartir el medio con otros sistemas. Otro ejemplo es el el *media packetizacion delay.* Es un retraso que ocurre al tener que llenar cierto ***packet*** con información adicional, como en **VoIP (Voice-over-IP)**

## 4. Throughput in Computer Networks

El i***nstantaneous throughput*** en cualquier instante del tiempo es la tasa a la cual el receptor está recibiendo el paquete. Definiremos el ***average throughput*** como el valor medio a lo largo de la transferencia

Supongamos un servidor y un cliente conectados por dos ***communication links*** y un ***router***. Si definimos $R_s$ como la tasa del ***link*** entre el servidor y el *router* y $R_c$ como la tasa del link entre el ***router*** y el cliente. Entonces el ***throughput*** sera el minimo de estos dos valores, este será la ***transmission rate*** del ***bottleneck link***. Hoy en día, este ***bottleneck*** link ***se suele encontrar en la red de acceso.

Para casos donde no hay tráfico interviniendo, el ***throughput*** se puede aproximar simplemente como el mínimo de los ***transmission rates*** a lo largo del recorrido. Pero en casos donde hay ***tráfico***, un ***link*** con alta ***transmission rate*** puede perfectamente ser el ***bottleneck link***.
