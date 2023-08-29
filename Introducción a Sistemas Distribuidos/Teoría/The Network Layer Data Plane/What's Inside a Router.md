Podemos identificar cuatro componentes principales:

- **Input ports:** Ejecuta varias funciones clave. Realiza la función de capa física de terminación del enlace de entrada. También realiza funciones de capa de enlace necesarias para operar con la capa de enlace del otro lado del enlace. Consulta la *forwarding table*, para determinar el link de salida del paquete. Los *control packets* son enviados al *routing processor*.
- **Switching fabric:** Conecta los puertos de entrada con los puertos de salida
- **Output ports:** Almacena los paquetes recibidos por el *switching fabric*, y los envía al enlace de salida asociado, realizando las funciones de capa de red y capa física necesarias. Para los casos de enlaces bidireccionales, usualmente se asocia un *input port* al mismo enlace.
- **Routing processor:** Este ejecuta las funciones del plano de control. En los routers tradicionales ejecuta los protocolos de ruteo, mantiene las tablas y los estados de los enlaces y computa la *forwarding table*. En *SDN routers*, es el responsable de comunicarse con el controlador remoto para recibir las entradas de la *forwarding table* e instalarlas en los *input ports*.

Debido a la velocidad necesaria, los *input ports*, *output ports*, y el *switching fabric* suelen ser implementados por hardware, mientras que las funciones del plano de control suelen estar implementadas por *software.*

## 1. Input Port Processing and Destination-Based Forwarding

La tabla de envío es copiada del procesador a los *input ports* a través de un bus distinto, como un *PCI bus*. De esta forma, las decisiones son toman localmente en cada *input port*.

Para la creación de la tabla, no podremos tener una entrada para cada dirección posible, ya que tendríamos más de cuatro billones de entradas. Esto se resuelve teniendo entradas para distintos rangos de valores de la dirección de destino. El router busca coincidencias en el prefijo de la dirección de destino, si la encuentra, envía el paquete al link asociado a esa entrada en la tabla. Para los casos con múltiples coincidencias, el router utiliza la entrada con la mayor regla de prefijo que encuentre.

Debido a la existencia de esta tabla, la búsqueda es un proceso relativamente simple, que tiene que realizarse de la forma más eficiente posible. Una simple búsqueda lineal no será suficiente.

Una vez determinado el *output port* de un paquete, este será enviado al *switching fabric*. En algunos diseños, este puede estar temporalmente bloqueado por otros paquetes actualmente usando el *fabric.* En estos casos, el paquete será encolado en el *input port* y programado para ser enviado posteriormente.

Aunque el proceso de *lookup* es el más importante, existen otras acciones que deben ser tomadas: procesamiento de cada física y de red, la versión del paquete, el *checksum* y el *time-to-live* del paquete deben ser verificados (y los últimos dos actualizados), los contadores utilizados para el manejo de red (como el contador de *datagrams* recibidos) deben ser actualizados.

## 2. Switching

Existen diversas formas para cumplir esta funcionalidad:

- **Switching via memory:** Los routers más simples y antiguos eran computadoras tradicionales. El *input port* señalaba al procesador con un *interrupt.* Este luego copiaba el paquete en la memoria, indexaba la tabla de envío y copiaba el paquete en el buffer de salida adecuado. Hoy en día se puede utilizar esta técnica, pero el *lookup* y el guardado en memoria ases realizado por la *input line card.*
- **Switching via a bus:** En este enfoque, el *input port* transfiere el paquete directamente al *output* a través de un *bus* compartido, sin ninguna intervención. El *input port* agrega un *header* al paquete indicando el puerto utilizado, el cual es posteriormente removido por el *output port*. Al ser compartido, todos reciben el paquete, pero solo el indicado lo mantiene. Únicamente un único paquete puede atravesar el *bus* a la vez. Esta técnica suele ser suficiente para routers de áreas locales y redes empresariales.
- **Switching via an interconnection network:** Se utiliza un *crossbar switch* en una red interconectada de $2N$ *buses* que conectan $N$ *input ports* con $N$ *output ports.* Esta técnica es no bloqueante, únicamente habrá espera si dos paquetes deben ser enviados al mismo *output port*. Redes más sofisticadas de múltiples etapas se puede utilizar para permitir enviar múltiples paquetes al mismo link al mismo tiempo.

## 3. Output Port Processing

El procesamiento de *output ports* toma paquetes almacenados en el buffer correspondiente y los transmite a través del link.

## 4. Where Does Queuing Occur?

El encolamiento de paquetes puede ocurrir tanto en los puertos de entrada como en los de salida, aunque el lugar y la extensión de la espera dependerá del tráfico.

### Input Delay

Si el *switch fabric* no es suficientemente rápido como para transferir todos los paquetes recibidos, puede ocurrir encolamiento en los *input ports*. Para el *crossbar switch*, esto puede ocurrir cuando hay más de un paquete destinado a un *output switch*, o cuando hay más de un paquete en un mismo *input port.* Este fenómeno se conoce como **head-of-the-line blocking (HOL).**

### Output Queuing

Si el *output port* no es suficientemente rápido como para enviar todos los paquetes que llegaron a su buffer, entonces se producirá encolamiento en los *output ports*. Eventualmente, esta cola puede crecer lo suficiente como para ocupar todo espacio disponible, produciendo pérdida de paquetes.

Llegada a esta situación, se puede elegir eliminar el paquete reciente (política conocida como **drop-tail**), o eliminar uno o más paquetes ya llegados. En algunos casos, será útil eliminar paquetes (o marcarlos) antes de que llegue al límite para indicar la congestión de la red.

Por muchos años, se creyó que una buena regla para la capacidad del buffer es de $RTT\cdot C$, siendo $C$ la capacidad del link y $RTT$ el *round trip time* promedio. Estudiamos más recientes sugieren que para conexiones con una gran cantidad de flujos, la necesidad de una gran capacidad del buffer disminuye considerablemente.

## 5. Packet Scheduling

Existen múltiples técnicas para determinar el orden en que paquetes encolados son transmitidos a través del enlace de salida.

### First-in-First-Out (FIFO)

Técnica simple que consiste en enviar los paquetes en el mismo orden en el que fueron encolados. También es conocida como **first-come-first-server (FCFS)**

### Priority Queuing

Bajo esta política, los paquetes son clasificados cuando llegan al buffer en distintas clases, dependiendo de la prioridad. Los paquetes de información de la red o aplicaciones en vivo pueden recibir una prioridad más alta, mientras aquellas aplicaciones que otras tendrán una menor prioridad. Cada clase tendrá su propia cola, la cual será vaciada antes de seguir con la cola de la siguiente prioridad. Bajo técnicas *non-preemptive*, la transmisión de un paquete no es interrumpida una vez comenzó.

### Round Robin and Weighted Fair Queuing

Los paquetes son ordenados en clases, aunque un *round robin scheduler* se utilizará para alternar entre las clases. La disciplina *work-conserving queuing* nunca permitirá que un link permanezca inactivo mientras haya paquetes encolados para la transmisión.

La técnica **weighted fair queuing (WFQ)** es similar a *round robin*, pero alterna entre clases de forma circular, donde cada clase tiene un peso que se utilizara para asegurar que cada clase una fracción de tiempo acorde a su peso y al de las otras clases.
