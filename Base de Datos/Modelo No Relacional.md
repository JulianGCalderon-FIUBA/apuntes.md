La necesidad de diseñar un [[Gestor de Base de Datos]] no relacional surgió en la década del 2000 a partir de la masificación de la WEB. Se buscaban diseñar soluciones al problema de almacenamiento que tuvieran:

- **Mayor escalabilidad** para trabajar con grandes volúmenes de datos.
- **Mayor performance** en las aplicaciones WEB. Se buscaban formatos que fueran fáciles de serializar, como XML y JSON.
- **Mayor flexibilidad** sobre las estructuras de datos. Queremos permitir una estructura que facilite la evolución de datos. En un modelo relacional, el sistema es muy rígido (la información no crecia de forma tan rapida
- **Mayor capacidad de distribución**. El modelo relacional o fue pensado como esto en mente. Se busca tener mayor disponibilidad y tolerancia a fallas. Para ello, se requieren mecanismos de replicación y fragmentación automática de los datos. Se prioriza la capacidad de procesamiento distribuido.

En un [[Modelo Relacional]], las operaciones de junta entre datos que se encuentran en nodos distintos puede ser un problema. Por otro lado, garantizar las [[Transacción#Propiedades ACID|propiedades ACID]] en un sistema distribuido es difícil, necesitamos que los nodos se sincronicen entre sí.
