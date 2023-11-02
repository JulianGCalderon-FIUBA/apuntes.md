La necesidad de diseñar un [[Gestor de Base de Datos]] no relacional surgió en la década del 2000 a partir de la masificación de la WEB. Se buscaban diseñar soluciones al problema de almacenamiento que tuvieran:

- **Mayor escalabilidad** para trabajar con grandes volúmenes de datos. Fue uno de los objetivos principales en el desarrollo de *BigTable* (Google, 2005)
- **Mayor performance** en las aplicaciones WEB. Se buscaban formatos que fueran fáciles de serializar, como XML y JSON.
- **Mayor flexibilidad** sobre las estructuras de datos. Queremos permitir una estructura que facilite la evolución de datos. En un modelo relacional, el sistema es muy rígido. El desarrollo WEB busca darle mayor libertad al desarrollador para organizar los datos.
- **Mayor capacidad de [[Base de Datos Distribuida|distribución]]**. Se busca tener mayor disponibilidad y tolerancia a fallas. Para ello, se requieren mecanismos de replicación y fragmentación automática de los datos. Se prioriza la capacidad de procesamiento distribuido.

Tendremos cuatro tipos principales de bases de datos no relacionales:

- **Clave/Valor:** Permiten guardar información en un formato de diccionarios, con clave y valor.
- **Orientadas a documentos:** Permiten guardar documentos como JSON o XML.
- **Wide Column:** Tienen diccionarios con columnas que permiten ser extendidas, pero con ciertas reglas. Tienen una serie de "columnas" que se repiten.
- **Basadas en grafos**

![[Modelo No Relacional 1698782230.png|500]]

En cada uno de ellos cambia la definición de *agregado*, es decir, de como conjuntos de objetos relacionados se agrupan en colecciones para ser tratados como una unidad y ser almacenados en el mismo lugar. Las bases de datos relacionales y las basadas en grafos carecen de la noción de agregado.

> [!note] Nota
> En el caso de una base de datos orientada a documentos, los documentos serán los agregados.

## Clave/Valor

Almacenan vectores asociativos o diccionarios, es decir, conjuntos formados por pares de elementos de la forma `(clave, valor)`.

Las claves son únicas, y el único requisito sobre su dominio es que sea comparable por igual. Algunos ejemplos son:

- **Berkeley DB**
- **Dynamo**
- **Redis**

Este tipo de bases de datos tiene cuatro operaciones elementales:

- Insertar un nuevo par: `put`
- Eliminar un par existente: `delete`
- Actualizar el valor de un par: `update`
- Encontrar un par asociado a una clave particular: `get`

Sus ventajas son:

- **Simplicidad:** no se define un esquema, [[Lenguajes#Data-Definition Language|DDL]], restricciones de integridad, ni dominios. El agregado es mínimo, y está limitado al par. El objetivo es guardar y consultar grandes cantidades de datos, pero no de interrelaciones entre los datos.
- **Velocidad:** Ya que prioriza la eficiencia de acceso, por sobre la integridad de los datos.
- **Escalabilidad:** Generalmente, proveen replicación (ya sea maestro-esclavo o distribuida), y permiten repartir las consultas entre los nodos.

## Orientadas a Documentos

En las bases de datos orientadas a documentos, un documento es un agregado, que almacena datos bajo una cierta estructura.

Sin necesidad de definir un esquema rígido para la estructura del documento, estas bases de datos ofrecen la posibilidad de manejar estructuras un poco más complejas que un par `(clave, valor)`

Generalmente, un documento se define como un conjunto de pares `(clave, valor)` que representan los atributos del documento y sus valores. Se admiten atributos multivaluados, y también se admite que el valor de un atributo sea a su vez un documento

Comparten algunas características con las bases de datos relacionales, como hacer consulta de selección o agregar datos. Algunos ejemplos son:

- **MondoDB**
- **RethinkDB**
- **CouchDB**
- **RavenDB**

### MongoDB

Es un gestor basado en *hashes* para identificar objetos. No utiliza esquemas, ni existe un [[Lenguajes#Data-Definition Language|DLL]].

Los documentos tienen un formato JSON, por lo que almacena pares de clave/valor.

Organiza los datos de una base de datos en colecciones, que contienen documentos. Los documentos a su vez tienen múltiples campos.

Fue desarrollada en C++, pero tiene APIs en múltiples lenguajes, como Python, Java, C#, etc.

Los atributos pueden ser multivaluados, ya que un vector es un tipo de dato valido.

MondoDB utiliza un modelo distribuido de procesamiento conocido como [[Sharding]].
