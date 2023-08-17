---
title: Introducción a Sistemas Operativos
---

Existe un software, responsable de hacer que los programas sean fáciles de ejecutarse, permitiendo que estos intercambien memoria e interactúen con dispositivos, entre otras cosas. Este software es conocido como ***Sistema Operativo***. En esta materia, nos vamos a centrar en ***como*** lo hace.

## Virtualización

La técnica principal mediante la cual el sistema operativo realiza esto es a partir de la v**irtualización.** Debido a esto, a veces nos referimos al sistema operativo como una máquina virtual.

El sistema operativo toma un recurso físico (procesador, memoria, disco), y lo virtualiza de forma que sea poderoso y fácil de usar para los procesos.

Para que los usuarios puedan interactuar con estos recursos, el sistema operativo provee una API (***system calls***) que nos permite interactuar con ellos. Decimos que el sistema operativo provee una ***biblioteca estándar*** para las aplicaciones.

Las ***system utilities*** son un conjunto de programas pequeños con funciones determinadas, utilidades para el usuario. Los ***distribution packages*** administran estas utilidades del sistema.

Para permitir que muchos usuarios accedan a los recursos, el sistema operativo se convierte en un ***administrador de recursos.***

### Virtualización de la CPU

Para generar la ilusión de que cada usuario tiene el control total del procesador, el sistema operativo genera una virtualización de la CPU para cada proceso, permitiendo que muchos programas corran aparentemente de forma "paralela" (esto no ocurre realmente)

Para definir como correr estos programas, el sistema operativo tiene una serie de **políticas** y **mecanismos** que utiliza para resolver estas problemáticas.

### Virtualización de Memoria

El modelo de una memoria es muy simple, es simplemente un vector de bytes. Para leer o escribir en memoria, se debe especificar una dirección de memoria.

La memoria es accedida constantemente mientras un programa corre, todas las estructuras que utiliza se guardan allí, y las accede a través de distintas instrucciones.

Cuando un proceso es ejecutado, este interactúa con su memoria de forma independiente, como si tuviese el control total del sistema, sin embargo esto no es así.

Para solucionarlo, el sistema operativo realiza una ***virtualización de memoria.*** Genera un espacio de direcciones virtual que le pertenece al proceso. Cuando el proceso accede a cierta dirección de memoria, es trabajo del sistema operativo ***mapear*** esta dirección por la dirección de memoria real en la cual se almacena la información. Este proceso es conocido como ***address translation.***

Este mecanismo, permite generar la ilusión de que cada proceso puede acceder a toda la memoria del usuario, sin embargo esto no es así. El proceso solo puede acceder a la memoria que el sistema operativo le permite.

## Concurrencia

Cuando varios procesos corriendo en simultáneo manipulan los mismo recursos se pueden producir condiciones de carrera, generando comportamiento indefinido. El sistema operativo provee formas de lidiar con estas problemáticas, que veremos más adelante.

## Persistencia

Cuando la información se encuentra en memoria, esta puede rápidamente perderse, ya que la memoria dinámica almacena valores de forma volátil.

Necesitamos un hardware que nos permita que nuestra información perdure en el tiempo, para esto utilizamos los discos. (hard drive, solid-state drive)

El sistema operativo provee una serie de abstracciones para poder acceder a esta memoria (file system), es encargado de guardar cualquier archivo que el usuario crea de un forma segura y eficiente. Estos accesos al disco suelen ser lentos y costosos

A diferencia de los otros recursos, el sistema operativo no genera una virtualización privada para cada proceso, sino que es compartida entre ellos.

## Objetivos de Diseño

Para que el sistema sea fácil de usar, el sistema operativo genera una serie de abstracciones y virtualizaciones que permiten al usuario interactuar con los recursos físicos de la computadora de forma segura, pero a la vez generando la **ilusión** de que cada proceso tiene el control total de la computadora.

Se busca diseñar un sistema operativo **eficiente**, con alto rendimiento. Las virtualizaciones hacen que el sistema sea difícil de usar, pero esto también implica un costo de rendimiento.

Otro objetivo es el de proveer **protección** entre aplicaciones, así como con el sistema operativo. Buscamos poder ejecutar distintos procesos a la vez, y que el comportamiento malicioso no afecte a otros procesos del sistema, ni al sistema operativo mismo. La clave para esto es el aislamiento entre procesos.

Cuando un proceso falla, todas las aplicaciones fallan también, por lo que tiene que minimizar las fallas, con un alto grado de **fiabilidad**.

También debe el concepto de ***pegamento,*** proveer una serie de servicios comunes entre aplicaciones. Si el sistema operativo está "pegado" bajo el mismo diseño, es más fácil de utilizar

## Kernel Mode

Las aplicaciones de usuario corren en lo que se conoce como ***user mode***. Significa que el hardware restringe lo que la aplicación puede hacer, para prevenir que tenga control total del sistema. Para realizar acciones avanzadas, dependen de las system calls.

Las ***system calls*** realizan acciones que un proceso normal no puede realizar, ya que debe acceder a los recursos físicos de la computadora. Para realizar esto, se le transfiere el control al ***trap handler*** previamente especificado para cada ***system call***, simultáneamente se elevan los privilegios del hardware. Los parámetros de estas funciones se pasan a través del registro del procesador.

En ***kernel mode,*** el sistema operativo tiene control completo de hardware, y puede realizar acciones avanzadas que requiera el usuario o el propio sistema operativo.

De esta forma, existen dos sets de instrucciones. El ***set1*** perteneciente que le pertenece a las instrucciones del usuario, y el ***set2*** con instrucciones que le pertenecen al ***kernel***.

Cuando la system call finaliza, se le delega nuevamente el control al usuario a partir de la instrucción ***return-from-trap***, para que continúe la ejecución.

El sistema operativo tiene tres instancias:

- Bajo nivel: Conocida como **kernel land**, aquí se encuentran los drivers para interactuar con el hardware
- Alto nivel: Conocido como ***user land***, aquí se ejecutan los programas, no existe posibilidad de interactuar con el hardware directamente.
- API: Mencionadas anteriormente, conjunto de funciones que permiten al usuario interactuar con el hardware.

### Modos de Transferencia

Existen algunos mecanismos que permiten delegarle el control al ***kernel***:

- **Interrupciones:** Son señales asincrónicas que delegan el control al kernel para que se siga administrando el sistema operativo.
- **Excepciones:** Son eventos del hardware causados por un proceso realizando una instrucción ilegal
- ***System Calls:*** Al llamar a una de estas funciones, se le delega el control al kernel para luego ser retornado al usuario.

## Multiprogramación

Para permitir que muchos procesos se ejecuten en simultáneo, el sistema operativo alterna rápidamente entre los procesos. Esto genera la ilusión de que se ejecutan al mismo tiempo. cuando en realidad la ejecución sigue siendo secuencial, pero alternada. Más adelante veremos como se realiza esto a partir de una entidad conocida como ***scheduler.***

Para prevenir que un proceso se ejecute indefinidamente, sin delegarle el control al sistema operativo, existen los ***timer interrupts***, esta es una herramienta del hardware que permite delegarle el control al kernel automáticamente, luego de cierto tiempo de ejecución.

## Shell

El principio primario de ***Unix*** es del utilizar programas simples y poderosos, que puedan ser conectados entre sí para generar comportamiento avanzado.

Para poder conectar estos programas simples, se utilizan los bloques primitivos de construcción. La ***shell*** contiene los ***pipes*** y la ***redirecciones***, los cuales pueden utilizarse para conectar estos programas entre sí.

La *shell*, gracias a lo mencionado anteriormente, es rápida, eficiente, y extensible. Puede realizar muchas tareas, aunque sigue siendo limitada.

## Tipos de Kernel

Existen distintos tipos de kernel:

- Kernel Monolítico: Es un único programa que está organizado en capas. El sistema operativo y el kernel corren en la misma memoria. Se utiliza cuando la seguridad del sistema no es muy importante. Tiene una accesibilidad rápida pero puede fallar completamente frente a un bug
- Microkernel: Es un kernel que maneja solo las funciones más importantes (memoria virtual, IO, cambio entre procesos). El resto de funcionalidades está en servidores, se llaman cuando son necesarios.
- Kernel Hibrido: Mezcla entre el kernel monolítico y el microkernel. Es bastante usado ya que los servicios más importantes se encuentran dentro del kernel.
