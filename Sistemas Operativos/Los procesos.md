---
title: Los procesos
---

La definición simple (aunque incompleta) de un proceso es: un programa corriendo en memoria. Un programa por si solo existe en el disco, un conjunto de instrucciones esperando a ser ejecutadas. El sistema operativo se encarga de ejecutar este programa.

## Mecanismos

Para generar la ilusión de que un sistema pueda tener cientos de programas siendo ejecutados al mismo tiempo, el sistema operativo genera abstracciones del hardware. A partir de la técnica básica ***time sharing***, múltiples programas pueden compartir el procesador.

Para lograr estas virtualizaciones, el sistema operativo necesita tanto mecanismos de bajo nivel, como inteligencia de alto nivel.

El *context switch* es un mecanismo del hardware que permite quitarle control a un proceso y devolverle el control al kernel, para que administre el sistema. Luego este le delegará el control a otro proceso, este ciclo se repetirá infinitamente mientras la computadora esté ejecutándose.

La contraparte del ***time sharing*** es el ***space sharing***, el sistema operativo también tiene mecanismos de hardware para poder administrar la memoria de forma concurrente entre dispositivos.

Por encima del hardware están las ***policies***, algoritmos que toman decisiones en cuanto a como se ejecuta el sistema como por ejemplo: ***scheduling policy.*** La cual decide que proceso se ejecutará en cada momento, a partir de un conjunto de reglas.

## Abstracción

Llamaremos entonces un proceso, a la abstracción generada por el sistema operativo para ejecutar un programa. El *machine state* son los componentes principales que un proceso necesita:

- **Address Space**: Espacio de direcciones virtual del proceso
- **Program Counter**: Contiene la dirección a la próxima instrucción a ejecutar
- **Stack Pointer**: Puntero al tope del stack
- **Frame Pointer**: Se utiliza para manejar los parámetros y el retorno de funciones.

## API del Proceso

El sistema operativo debe proveer una serie de mecanismos para poder crear nuevos procesos.

- ***Create**:* Debe incluir algún método para crear un proceso
- ***Destroy**:* Así como existe la creación, también debe poder destruirse.
- ***Wait**:* Muchas veces es útil tener algún mecanismo para hacer que un proceso espere a que otro proceso termine su ejecución
- ***Miscellaneous Control**:* El sistema operativo suele proveer otras funciones útiles para el control de un proceso
- ***Status:*** Se debe poder obtener el estado de un proceso, información acerca del mismo.

### API de Linux

En Linux, tenemos tres system calls principales para administrar procesos:

- `fork()`

	Al llamarse a esta rutina, el sistema operativo crea un proceso completamente nuevo, como copia casi totalmente idéntica del proceso padre. Toda la información del proceso es clonada a otro espacio de memoria. Creando un nuevo proceso totalmente independiente. El PID o ***process identifier*** es lo único que se modifica, ya que estamos tratando con un proceso distinto.

	Para que el proceso conozca si es el padre o el hijo, la system call tiene dos valores de retorno. El hijo recibe un cero, mientras que el padre recibe el PID del hijo.

	Debido a que el scheduler es complejo, nunca podremos definir en que orden se ejecutarán los procesos.

- `wait()`

	Esta system call permite frenar la ejecución de un proceso hasta que alguno de sus procesos hijos termine su ejecución, recolectando la información de los procesos zombies y eliminandolos, es recomendable hacer esto siempre para no dejar procesos ***huérfanos***.

- `exec()`

	Esta system call ejecuta un nuevo proceso, interrumpiendo totalmente el proceso anterior. Algunos datos se mantienen, como por ejemplo el *PID* y los ***file descriptors*** del proceso original. Carga el nuevo programa en memoria, y se reinicializa el *stack* y el *heap.*

La separación de las *system calls* `fork()` *y* `exec()` es muy útil ya que permite modificar un proceso entre el llamado a esas dos funciones. Lo que permite por ejemplo, modificar los file descriptors de un proceso.

Además de estas funciones principales, existen funciones que permiten enviar señales a los procesos. `kill()` permite enviar señales a un sistema, como pausarlo o terminarlo. El sistema operativo posee un infraestructura compleja para poder entregarle eventos externos a los procesos.

Un proceso, puede utilizar la función `signal()` para capturar señales, pausando la ejecución hasta recibirlas.

Para que no todos pueden terminar cualquier proceso, el concepto de ***user*** define los limites de lo que este puede ejecutar. Usualmente existe un administrador del sistema o ***superuser*** que puede controlas a todos los procesos, aunque debe ser usado con cautela.

## Creación del Proceso

- El programa deberá leerse del disco y carga las instrucciones en la memoria del proceso, para ser ejecutadas. Para esto, debe realizar un manejo de memoria para obtener un espacio donde se guardará la información del proceso. Esta porción es conocida como `.code`
- Una vez que el código es cargado en memoria, debe reservarse memoria para el *stack* del proceso (el cual es limitado). Este es utilizado constantemente en todo el código debido a su velocidad. Esta porción es conocida `.data` o `.stack`
- El sistema operativo también debe poder reservar memoria en el ***heap*** del proceso, memoria dinámica que es administrada únicamente por el sistema operativo. Esta porción es conocida como `.heap`

![[Los procesos 1.png]]

- También debe realizar algunas tareas de inicialización, por ejemplo los ***file descriptors*** iniciales del proceso.
- Una vez finalizada la creación del proceso, el sistema operativo empieza a correr el programa en el punto de entrada `main()`

## Estados del Proceso

Los procesos pueden tener los siguientes estados, los cuales son administrados por el sistema operativo:

- ***Running:*** El proceso está siendo ejecutado
- ***Ready:*** El proceso está a la espera para ser ejecutado
- ***Blocked:*** El proceso realizó alguna operación que lo dejo en este estado, debe esperar al sistema operativo (solicitud de entrada/salida, excepcion). El proceso es bloqueado para que otros procesos puedan utilizar el procesador.

![[Los procesos 2.png]]

Existen otros estados en los que un proceso puede estar, pero esta es una simplificación. Los estados son: *UNUSED, EMBRYO, SLEEPING, RUNNABLE, RUNNING, ZOMBIE*

## Estructuras de Datos

El sistema operativo tiene estructura de datos importantes para registrar información relevante:

- ***Process List***: Lista de todos los procesos que están disponibles para correr, así como información sobre el proceso que está siendo ejecutado actualmente. También deben tener un registro de los procesos bloqueados, para cambiarlo de estado en cuanto termine su petición.
- ***Register Context:*** Almacena la información de los registros de un proceso cuando este no está corriendo, para poder cargarla en cuanto se ejecute nuevamente.
- **Process Control Block:** Contiene información sobre el proceso, su estado, sus registros, la memoria. La lista de procesos contiene un puntero a este bloque.
