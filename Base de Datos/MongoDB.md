Es un gestor basado en *hashes* para identificar objetos. No utiliza esquemas, ni existe un [[Lenguajes#Data-Definition Language|lenguaje de definición de datos]].

Fue desarrollada en C++, pero tiene APIs en múltiples lenguajes, como Python, Java, C#, etc.

Utiliza un modelo distribuido de procesamiento conocido como [[Modelo Sharding]].

## Estructura

Una base de datos está formada por colecciones, las cuales almacenan documentos.

Los documentos tienen un formato JSON, por lo que almacena pares de clave/valor. Organiza los datos de una base de datos en colecciones, que contienen documentos. Los documentos a su vez tienen múltiples campos.

Los atributos pueden ser multivaluados, ya que un vector es un tipo de dato válido.

## Claves

Los documentos dentro de una colección se identifican a través de un campo `_id`. Si nosotros no lo especificamos, entonces se asignará automáticamente.

El hash también asegura que no se pueda insertar dos veces el mismo documento en una colección.

Los documentos a su vez pueden referenciar otros documentos a través de esta clave, conocida como `ObjectId`. Por otro lado, los documentos pueden anidar otros documentos dentro del mismo.

## Juntas

MongoDB no está pensado para realizar operaciones de junta en forma eficiente. En general, cuando necesitamos hacer una junta, la escribimos a mano.

A lo sumo, debemos ir a buscar documentos referenciados concretos para una consulta particular, pero esto es rápido debido al *hashing*.

Si debemos acceder muy frecuentemente a un documento referenciado, hay que pensar si no sería conveniente tenerlo directamente embebido.

La no redundancia de datos y la normalización es sacrificada en las bases de datos NoSQL, y MongoDB en particular.

## Agregación

MongoDB implementa agregación a través de un *pipeline* secuencial que combina etapas de agrupamiento, selección, etc. El conjunto de resultados que devuelve una operación será utilizado como entrada por la siguiente operación.
