La segmentación surgió para solucionar el problema de la fragmentación interna. La idea es simple, en lugar de tener un solo par ***Base and Bound*** para cada proceso, tendremos un par para cada segmento lógico del espacio de memoria: ***code***, ***stack***, ***heap***. De esta forma, podemos utilizar libremente la memoria que se encuentra entre estos segmentos.

El hardware utiliza segmentos de registro durante la traducción. ¿Como sabe a que segmento pertenece cierta dirección de memoria virtual? Un enfoque es el enfoque **explícito**. Los primeros bits del registro se utilizan para detectar a que segmento pertenece la memoria, mientras que los otros bits representan el ***offset*** de ese segmento. 

El problema de este enfoque es que cada segmento tiene un tamaño máximo, ya que utiliza algunos bits para determinar el offset.

El *stack* se comporta de forma levemente distinta. Crece hacia abajo, por lo que debemos indicarle al hardware esto.

Más adelante, se descubrió que con un poco más de soporte del ***hardware***, se pueden alcanzar diseños más eficientes. Para hacerlo, se deben destinar algunos bits de la información del segmento para indicar la utilidad del mismo: ***read, write, execute.*** De esta forma, se puede compartir el mismo código entre múltiples procesos, manteniendo la seguridad de que no se modificara.

# Fine-grained vs. Coarse-grained

Podemos pensar la segmentación como ***coarse-grained*** o ***de grano grueso***. El sistema operativo parte el espacio de direcciones en bloques relativamente grandes. Otra opción, es tener una gran cantidad de pequeños segmentos, esto es conocido como ***fine-grained*** o ***de grano fino***.

Para realizar esto, el *hardware* debe tener una tabla de segmentos, donde pueda almacenar la información de todos ellos. Esto permite utilizar de forma más eficiente el espacio no utilizado.

# Soporte del Sistema Operativo

Hasta ahora, vimos que el enfoque de segmentación permite ahorrar una gran cantidad de memoria que anteriormente perdíamos, debido a la fragmentación interna. Sin embargo, trae nuevas problemáticas para el sistema operativo.

¿Qué debe hacer el sistema operativo en un ***context switch***? Los registros de los segmentos deben ser guardados y restaurados posteriormente. Debe almacenar correctamente la ubicación de los segmentos para cada proceso.

Otro problema surge cuando queremos aumentar nuestra memoria disponible. Esto suele ocurrir cuando un proceso pide mas memoria al sistema operativo mediante una ***system call,*** entonces el sistema operativo debe aumentar el espacio disponible para este proceso***,*** actualizando el tamaño del segmento, o creando un nuevo segmento.

Por último, como se maneja la memoria libre. Cuando se crea un espacio de direcciones, el sistema operativo debe encontrar espacio para todos los segmentos que el proceso requiera. Pero esto puede ser difícil

A veces, tendremos muchos espacios chicos de memoria disponibles, que no son suficientes para el proceso, esto se conoce como fragmentación interna.

Una forma de hacerlo es compactar la memoria física, reorganizando los segmentos existentes. Esta operación es costosa, ya que copiar segmentos requiere mucho tiempo de procesamiento. Además de que vuelve al proceso de crecimiento de un segmento más difícil.

Otro enfoque es el de tener una lista de espacios de memoria libres, utilizando algoritmos para determinar el mejor espacio a elegir. Algunos de estos algoritmos son ***best-fit, worst-fit, first-fit,*** o uno más complejo: buddy algorithm*.*