En las bases de datos orientadas a documentos, un documento es un agregado, que almacena datos bajo una cierta estructura.

Sin necesidad de definir un esquema rígido para la estructura del documento, estas bases de datos ofrecen la posibilidad de manejar estructuras un poco más complejas que un par `(clave, valor)`

Generalmente, un documento se define como un conjunto de pares `(clave, valor)` que representan los atributos del documento y sus valores. Se admiten atributos multivaluados, y también se admite que el valor de un atributo sea a su vez un documento

Comparten algunas características con las bases de datos relacionales, como hacer consulta de selección o agregar datos. Algunos ejemplos son:

- **MondoDB**
- **RethinkDB**
- **CouchDB**
- **RavenDB**

## MongoDB

Es un gestor basado en *hashes* para identificar objetos. No utiliza esquemas, ni existe un [[Lenguajes#Data-Definition Language|DLL]].

Los documentos tienen un formato JSON, por lo que almacena pares de clave/valor.

Organiza los datos de una base de datos en colecciones, que contienen documentos. Los documentos a su vez tienen múltiples campos.

Fue desarrollada en C++, pero tiene APIs en múltiples lenguajes, como Python, Java, C#, etc.

Los atributos pueden ser multivaluados, ya que un vector es un tipo de dato valido.

MondoDB utiliza un modelo distribuido de procesamiento conocido como [[Modelo Sharding]].
