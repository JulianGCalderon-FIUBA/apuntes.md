Es sistemas con datos de gran escala, podemos encontrar flujos del siguiente estilo:

![[Data Intensive Applications 1737298627.png]]

Encontramos tres tipos de datos:

- **Master Data**: Contiene información que no crece indefinidamente.
- **Transactional Data**: Crece indefinidamente a medida que se utiliza el servicio.
- **Search Indexes**: Suele tener pocas escrituras, costosas, pero muchas lecturas. Estas escrituras se pueden realizar de forma recurrente, o ante la detección de cambios.

Para que el servicio sea más rápido, se suele utilizar una caché.

Si una petición es muy demandante, se puede encolar en algún [[Message Oriented Middleware|MOM]], y resuelta de forma asincrónica.

## Tipos de Transacciones

Hay dos tipos de transacciones:

- **OLTP** (*Online Transaction Processing*): Se busca acceder a pocos registros, y con un acceso aleatorio. Se utilizan en las bases de datos más comunes. La magnitud de los datos está en el orden de los MB o GB.
- **OLAP** (*Online Analytics Processing*): Se busca acceder a muchos datos, y a realizar análisis estadísticos. Se trabaja en baches o streams. La magnitud de los datos está en el orden de los TB o PB.

## Tipos de Almacenamiento

Hay distintas formas de almacenar información:

- **Modelo Relacional**: Se accede a la información fila a fila, y tiene buen soporta para realizar *joins*.
- **Modelo Columnar**: Se accede a la información de a columnas, y es útil para realizar agregaciones. Si los datos se repiten mucho, entonces es más fácil comprimirlos.
- **Cubos de Información**: Se utiliza mucho en transacciones de tipo OLAP. Mantienen vistas materializadas con cálculos estadísticos. Se crean grillas agrupadas por diferentes dimensiones, y se consultan operaciones sobre dicho cubos (como `sum`, `count`, `max`, etc.).

## Distributed Shared Memory (DSM)

Es un patrón para manejar el *storage* en un sistema distribuido. Brinda la ilusión de que los procesos tienen una memoria compartida centralizada.

Es un patrón intuitivo, y permite que los algoritmos no distribuidos se traduzcan fácilmente, pero desalienta la distribución y poco performante, y tiene un único punto de falla.

### Lock Centralizado

La información es almacenada en el servidor. Los clientes acceden mediante consultas de escritura y lectura. El servidor puede garantizar la consistencia muy fácilmente serializando los consultas.

![[Data Intensive Applications 1737302115.png]]

Este enfoque ofrece muy baja performance.

### Migración de Memory Pages

La información es almacenada en el servidor, pero delegada a los clientes. Esto permite a los clientes manejarla y optimizar su acceso. Otros clientes pueden pedir la página delegada al cliente que la tiene.

![[Data Intensive Applications 1737302128.png]]

Este enfoque no permite acceso concurrente a una página, pero permite optimizar la localidad de acceso.

### Replicación de Memory Pages

Las lecturas implican una replicación read-only, y las escrituras son coordinadas por el servidor, invalidando a las réplicas.

![[Data Intensive Applications 1737302255.png]]

Este enfoque favorece un escenario de muchas lecturas, y pocas escrituras.

Si queremos permitir lectura-escritura, entonces el servidor funciona como un secuenciador de operaciones. Las páginas se encuentran en múltiples lugares a la vez, y el servidor debe notificar a las réplicas cuando se deben actualizar las réplicas.

![[Data Intensive Applications 1737302364.png]]

## Distributed File System (DFS)

Es un sistema que permite compartir archivos en redes locales e intranets.

Posee un esquema centralizado de información persistente, ofrece:

- Control de backups.
- Control de acceso y monitoreo.

Además, permite optimizar los recursos debido a la centralización, ya que podremos tener discos de mayor capacidad y menor costo de administración.

Los objetivos de este sistema son:

- **Transparencia a los clientes**:
	- **Acceso**: obtener los recursos con credenciales usuales.
	- **Localización**: operar con archivos como si fueran locales.
	- **Movilidad**: el movimiento interno de archivos no debe ser percibido.
	- **Performance**: las optimizaciones no deben afectar al cliente
- **Concurrencia**: El acceso concurrente no debe requerir operaciones particulares de los clientes.
- **Heterogeneidad de Hardware**: El sistema puede estar compuesto por hardwares distintos.
- **Tolerancia a Fallos**: Capacidad de ocultar o minimizar fallos

### Network File System

Fue diseñado para ser independiente de las plataformas, pero desarrollado en UNIX en 1984.

Desde un primer lugar, se diseñó para que el file system siga el estandar POSIX.

Requiere de una abstracción del kernel llamada *Virtual File System*. Las aplicaciones utilizarían VFS para acceder los archivos, lo que requiere de una invocación remota.

![[Data Intensive Applications 1737303143.png]]

Las consultas se harían utilizando [[Remote Procedure Control|RPC]], tanto sobre UDP como TCP.

### Apache Hadoop DFS

Es un sistema de archivos distribuido, diseñado para utilizar hardware de bajo costo. La implementación está basada en el diseño de Google File System (GFS).

No soporta el estándar POSIX, por lo que se considera un *storage* en lugar de un *file system*. Se pensó para soportar operaciones útiles en ambientes de cómputo distribuido (como [[Map Reduce]]).

Los objetivos del sistema, son:

- Tolerancia a Fallos: Los fallos en el hardware son comúnes, por lo que es mas económico soportarlos.
- Volumen y Latencia: Favorece operaciones de streaming, y sobre archivos volumétricos.
- Portabilidad: Preparado para ser ejecutado en hardware de bajo costo, utilizando TCP entre servidores, y RPC con los clientes.
- Performance: Favorece operaciones de lectura.

### Arquitectura

La arquitectura consta de un *namenode* que conoce donde está cada porción de cada archivo y contiene toda la metadata, y múltiples *datanodes*.

Los clientes consultan al *namenode* por el *file system* y la ubicación de los archivos, y luego se comunican con los *datanodes* correspondientes.

![[Data Intensive Applications 1737303640.png]]

Los archivos se particionan en bloques de 128 MB, y los bloques son replicados en distintos *datanodes*.

El *namenode* mantiene el listado de *datanodes* para un archivo. La metadata se mantiene en memoria para optimizar su acceso, con un log de transacciones.

También se permite un rebalanceo de bloques entre los *datanodes*.

### Acceso a Datos

Una operación es mucho más eficiente si se encuentra cerca de los datos con los que opera.

> "Moving computation is cheaper than moving data"

Para el acceso a los datos se favorece el principio de localidad de los datos. El cliente obtiene una lista de *datanodes* para cada bloque y sus réplicas, y se intenta acceder a los bloques más cercanos.
