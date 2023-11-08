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

Los documentos a su vez pueden referenciar otros documentos a través de esta clave, conocid
