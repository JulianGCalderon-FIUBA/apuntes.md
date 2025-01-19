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

## Distributed Shared Memory

Es un patrón para manejar el *storage* en un sistema distribuido. Brinda la ilusión de que los procesos tienen una memoria compartida centralizada.

Es un patron intuitivo, y permite que los algoritmos