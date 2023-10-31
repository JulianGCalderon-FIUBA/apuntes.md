La necesidad de diseñar un [[Gestor de Base de Datos]] no relacional surgió en la década del 2000 a partir de la masificación de la WEB. Se buscaban diseñar soluciones al problema de almacenamiento que tuvieran:

- **Mayor escalabilidad** para trabajar con grandes volúmenes de datos. Fue uno de los objetivos principales en el desarrollo de *BigTable* (Google, 2005)
- **Mayor performance** en las aplicaciones WEB. Se buscaban formatos que fueran fáciles de serializar, como XML y JSON.
- **Mayor flexibilidad** sobre las estructuras de datos. Queremos permitir una estructura que facilite la evolución de datos. En un modelo relacional, el sistema es muy rígido. El desarrollo WEB busca darle mayor libertad al desarrollador para organizar los datos.
- **Mayor capacidad de distribución**. El modelo relacional no fue pensado como esto en mente. Se busca tener mayor disponibilidad y tolerancia a fallas. Para ello, se requieren mecanismos de replicación y fragmentación automática de los datos. Se prioriza la capacidad de procesamiento distribuido.

En un [[Modelo Relacional]], las operaciones de junta entre datos que se encuentran en nodos distintos puede ser un problema. Por otro lado, garantizar las [[Transacción#Propiedades ACID|propiedades ACID]] en un sistema distribuido es difícil, necesitamos que los nodos se sincronicen entre sí. Si bien es posible distribuir una base de datos relacional, tiene diversas dificultades.

Desde los últimos años, la velocidad de las redes y la capacidad de almacenamiento aumenta, mientras que el procesamiento se mantiene estancado. Debido a esto, las bases de datos *"noSQL"* no fragmentarán los datos, sino que los replicaran. Esto permite que las bases de datos no se sincronicen.

Tendremos cuatro tipos principales de bases de datos no relacionales:

- **Clave/Valor:** Permiten guardar información en un formato de diccionarios, con clave y valor.
- **Orientadas a documentos:** Permiten guardar documentos como JSON o XML.
- **Wide Column:** Tienen diccionarios con columnas que permiten ser extendidas, pero con ciertas reglas. Tienen una serie de "columnas" que se repiten.
- **Basadas en grafos**

![[Modelo No Relacional 1698782230.png|500]]

En cada uno de ellos cambia la definición de *agregado*, es decir, de como conjuntos de objetos relacionados se agrupan en colecciones para ser tratados como una unidad y ser almacenados en el mismo lugar. Las bases de datos relacionales y las basadas en grafos carecen de la noción de agregado.
