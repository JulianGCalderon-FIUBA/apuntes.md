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

- **OLTP** (*Online Transaction Processing*): Se busca acceder a pocos registros, y con un acceso aleatorio. Se utlizan en las bases de datos mas comunes. La magnitud de los datos está en el orden de los MB o GB.
- **OLAP** (*Online Analytics Processing*): Se busca acceder a muchos datos, y a realizar análisis estadísticos. Se trabaja en baches o streams. La magnitud de los datos está en el orden de los TB o PB.

## Tipos de Almacenamiento

Hay distintas formas de almacenar información:

- En un modelo relacional: Se accede a la información fila a fila.
- En un modelo columnar: Se accede a la información de a columnas, y es útil para 
