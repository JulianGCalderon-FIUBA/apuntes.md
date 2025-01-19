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

## Replicación de Datos

Hay distintas formas de replicar datos:

### Leader Based

Una réplica se designa como *master* o *leader*, y el resto de réplicas se designan como *mirrors*, *slaves*, o *followers*.

Solo se aceptan escrituras en el *leader*, los cuales se sincronizan de forma periódica.

### Multi-Leader Based

Es común en escenarios con múltiples data-centers, o donde hay separación entre los usuarios.

Frente a caídas en un data-center, se puede promover a otro como *leader* global.

Un problema común es como resolver conflictos entre distintos *leaders*. Otros problemas comunes incluyen:

- Manejo de triggers.
- Claves incrementales.
- Integridad de relaciones

### Leaderless Based

Es un sistema totalmente distribuido, y las réplicas deben sincronizarse mutuamente. Se pueden definir [[Topología de Comunicación|topologías]] de sincronización.

Son muy comunes los conflictos, a menos que se particionen los datos. Una forma de resolver los conflictos es el de conseguir consenso entre las réplicas para aplicar escrituras.

## Particionamiento de Datos

Los datos se pueden particionar por distintos motivos:

- **Performance**: Mejora de velocidad de escritura y de lectura.
- **Conflictos**: Evita colisiones o reduce los conflictos.
- **Redundancia**: Permite recuperación ante fallas (al guardar las particiones en más de un lugar).

### Tipo de Partición

Hay dos enfoques principales para realizar la partición de datos:

- **Horizontal**: La información se segrega por registros entre cada partición. Los registros se encuentran *completos* en alguna partición.
- **Vertical**: La información se segrega por atributos. Los registros se encuentran en todas las particiones, por lo que no son eficientes para consultas de filas completas.

### Función de Partición

La función de partición, que determine en que partición se encuentra cada dato, puede definirse de varias maneras:

- Por valor de Clave: Separa cada valor en una partición.
- Por rango de Clave: Separa cada rango de valores en una partición.
- Por Hash: Se aplica el hash a la clave, para obtener una distribución más uniforme.

También hay enfoques mixtos, como:

- Generar múltiples particiones para un valor.
- Particionar por claves secundarias.

### Enrutamiento

Hay distintas formas de obtener un dato en una base de datos particionada:

- Si conozco la función de particionamiento, puedo calcular en que partición se encuentra utilizando el dato.
- Si no conozco la función de partición, debo consultar en alguna de las particiones, y que esta me indique en que partición se encuentra.
- En algunas situaciones, existirá un nodo *centinela* que conocerá en que partición se encuentran los datos.

![[Data Intensive Applications 1737301563.png]]

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

Una operación es mucho más eficiente si se encuentra cerca de los datos con los que opera. Como eslogan del proyecto, se habla de:

> "Moving computation is cheaper than moving data"

La arquitectura consta de un *namenode* que conoce donde está cada porción de cada archivo y contiene toda la metadata, y múltiples *datanodes*.

Los clientes consultan al *namenode* por el *file system* y la ubicación de los archivos, y luego se comunican con los *datanodes* correspondientes.

![[Data Intensive Applications 1737303640.png]]

Los archivos se particionan en bloques de 128MB, y los bloques son replicados en dis