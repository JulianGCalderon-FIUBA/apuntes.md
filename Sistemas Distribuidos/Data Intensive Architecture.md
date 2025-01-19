Es sistemas con datos de gran escala, podemos encontrar flujos del siguiente estilo:

![[Data Intensive Applications 1737298627.png]]

Encontramos tres tipos de datos:

- **Master Data**: Contiene información que no crece indefinidamente.
- **Transactional Data**: Crece indefinidamente a medida que se utiliza el servicio.
- **Search Indexes**: Suele tener pocas escrituras, costosas, pero muchas lecturas. Estas escrituras se pueden realizar de forma recurrente, o ante la detección de cambios.

Para que el servicio sea más rápido, se suele utilizar una caché.

Si una petición es muy demandante, se puede encolar en algún [[Message Oriented Middleware|MOM]], y resuelta de forma asincrónica.

## Tipos de Procesamiento

Hay dos tipos de procesamiento:

- **OLTP** (*Online Transaction Processing*): Se busca acceder a pocos registros, y con un acceso aleatorio. Se utilizan en las bases de datos más comunes. La magnitud de los datos está en el orden de los MB o GB.
- **OLAP** (*Online Analytics Processing*): Se busca acceder a muchos datos, y a realizar análisis estadísticos. Se trabaja en baches o streams. La magnitud de los datos está en el orden de los TB o PB.

## Tipos de Almacenamiento

Hay distintas formas de almacenar información:

- **Modelo Relacional**: Se accede a la información fila a fila, y tiene buen soporta para realizar *joins*.
- **Modelo Columnar**: Se accede a la información de a columnas, y es útil para realizar agregaciones. Si los datos se repiten mucho, entonces es más fácil comprimirlos.
- **Cubos de Información**: Se utiliza mucho en transacciones de tipo OLAP. Mantienen vistas materializadas con cálculos estadísticos. Se crean grillas agrupadas por diferentes dimensiones, y se consultan operaciones sobre dicho cubos (como `sum`, `count`, `max`, etc.).
