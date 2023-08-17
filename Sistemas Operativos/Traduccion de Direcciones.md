---
title: Traducción de Direcciones
---

Para favorecer la eficiencia, se utiliza conocido como ***hardware-based address translation.*** El hardware transforma cada dirección de memoria por la dirección de memoria física correspondiente.

Aunque por supuesto, el hardware por sí solo no puede realizar esta tarea. El sistema operativo debe intervenir en momento clave para preparar el hardware. Debe manejar la memoria, teniendo en cuenta los espacios de memoria libres y los ocupados.

## Base and Bound

Una idea simple y primitiva para organizar la memoria, funcionaba bajo el supuesto de que los espacios de memoria eran contiguos. Requiere dos registros nuevos para cada procesador: ***Base***, y ***Límite***. El primero indica la dirección de memoria real donde empieza el espacio del proceso, y el segundo indica el tamaño de este espacio de memoria.

Cada programa se comporta como si su memoria empezará en la dirección cero, para luego ser traducida por el hardware a la dirección física correspondiente, ya que esta traducción se realiza en tiempo de ejecución, esta técnica es conocida como ***reubicación dinámica.***

Antes de realizar la traducción revisa que la dirección de memoria no esté fuera del límite, en tal caso lanza una excepción (El control es delegado al sistema operativo, el cual probablemente termine la ejecución del programa).

La porción del procesador encargada de realizar esta traducción de memoria es conocida como ***MMU.*** o ***memory management unit***.*

## Soporte del Hardware

El hardware debe poder soportar ***dual mode***, éste consiste en tener dos sets de instrucciones, uno para el kernel llamado ***kernelmode*** y otro para el usuario, llamado ***usermode*** **(esta información puede ser guardada en el procesador) **El hardware debe proporcionar una forma de realizar el pasaje entre estos modos.

Además, debe tener dos registros, el ***base*** y ***bound***, para poder realizar las traducción de direcciones.

El hardware debe contener instrucciones para modificar estos registros, pero privilegiadas para que solo el kernel tenga acceso.

Finalmente, debe poder generar excepciones para situaciones en las que el usuario acceda a memoria que no le pertenece, delegando el control al kernel nuevamente, otras operaciones ilegales también tendrán su propio ***handler***.

## Problemáticas del Sistema Operativo

Cuando se ejecuta un programa, el sistema primero debe encontrar un espacio libre en la memoria, para esto puede implementar una simple lista de espacios libres. Una vez encontrado, puede inicializar el proceso como lo visto anteriormente.

Cuando un proceso termina, el sistema también se debe encargar de liberar la memoria reservada para él, y limpiando cualquier estructura de datos asociada.

Cuando ocurre un ***context switch***, El sistema operativo debe cargar el par ***Base and Bound***, para que sea acorde al próximo programa en correr. Estos valores se pueden guardar en alguna estructura asociada al proceso, como el ***PCB***.

Gracias a este espacio de traducciones, es muy simple para el sistema operativo mover la memoria física a otro lado, simplemente copiandola y actualizando los registros asociados. El proceso es transparente a estas situaciones.

Por último, el sistema operativo debe proveer **exception handlers**, funciones a ser llamadas en cuanto se lance la excepción correspondiente. Estos handlers son instalados en ***boot*** ***time***.

Como la memoria del proceso tiene tamaño fijo, puede tener reservada memoria que no utiliza, esto es conocido como ***fragmentación interna***. El primer enfoque para solucionar esto sera una técnica un poco más avanzada llamada **segmentación**.
