---
title: Ejecución Directa
---

Para virtualizar el procesador, el sistema operativo necesita de alguna forma compartir el procesador físico entre múltiples procesos. ***Time sharing*** es una simple idea que soluciona este problema.

Hay algunos desafíos que surgen al tratar de construir esta maquinaria de virtualización. El primero es el **rendimiento**: ¿Como podemos implementar esta virtualización sin agregar excesivos gastos al sistema? El segundo problema es el ***control***: ¿Como podemos correr estos procesos sin perder el control sobre el procesador?

## Ejecución Directa Limitada

Esta simple idea consiste en correr un programa directo en la CPU. Se carga el programa en memoria, se crean las estructuras necesarias del proceso y se ejecuta. Este enfoque trae muchos problemas sobre el ***control***. ¿Cómo limitamos lo que puede hacer el proceso? ¿Cómo lo frenamos para correr otro proceso e implementar el ***time sharing***?

## Operaciones Restringidas

La ejecución directa es rápida, pero que pasa si el proceso quiere realizar alguna operación que no debería tener permiso de hacer, como emitir un solicitud de entrada/salida. Para solucionar esto, el hardware debe proveer el conocido ***dual mode***. Una forma entre cambiar entre los sets de operaciones permitidos, para que únicamente el kernel pueda realizar ciertas operaciones. Tendremos entonces dos modos: ***kernelmode**, **usermode***.

¿Cómo hacemos para que el usuario pueda realizar estos pedidos, pero de forma controlada? Para esto, utilizaremos las ***system calls***. Funciones del sistema que levantan el ***kernel*** para que realicen la operación deseada en modo privilegiado, devolviendole el control al proceso cuando termine.

El proceso debe ejecutar cierta instrucción ***trap*** interpretada por el ***hardware*** que se encarga de despertar el ***kernel***. Cuando termine, se llama a la instrucción ***return-from-trap,*** que le devuelve el control al usuario.

Cuando el *kernel* arranca, prepara la conocida ***trap table***. Esta es configurada para que el ***hardware*** pueda saber que instrucciones ejecutar en cada caso. Cuando el usuario llama a algunas de estas instrucciones, el hardware ejecuta el ***trap handler*** correspondiente.

Para especificar que ***system call*** se quiere ejecutar, se utiliza el ***system-call number***, asignado a cada una. Este se carga en el registro correspondiente.

Hay dos fases en de la ***LDE*** o ***limited direct execution***. La primer es en el arranque, el kernel inicializa la ***trap table.*** La segunda fase ocurre cuando se corre un proceso, antes de la instrucción ***return-from-trap***. El ***kernel*** debe cambiar el modo a ***usermode*** y correr nuevamente el proceso. (***context switch***)

## Cambio entre Procesos

Para solucionar esto, debemos encontrar una forma para el ***kernel*** de recuperar el control del procesador, para correr otro proceso.

Una forma de solucionarlo es con el enfoque cooperativo. El *kernel* espera ***a que el usuario realice una **system call**, para poder cambiar entre procesos. Este enfoque es peligroso, ya que el usuario puede nunca delegarle el control al sistema operativo, manteniendo el control del procesador.

El enfoque no cooperativo consiste, utilizamos algo conocido como ***timer interrupt***. Un dispositivo programado para lanzar una interrupción cada ciertos milisegundos. Cuando se lanza, se llama al pre-configurado *interrupt handler.* De esta forma, el kernel recupera el control del procesador y puede cambiar entre procesos.

Para este enfoque, es necesario que el ***hardware*** tenga los mecanismos necesarios para utilizarlo. Además de lanzar la excepción, debe almacenar suficiente información del estado del proceso para poder continuar luego. Esta información es almacenada en el ***hardware*** para poder continuar si el ***scheduler*** lo decide.

## Guardando y Restaurando Contexto

Una vez que el *kernel* recupera el control, debe tomarse una decisión. Esta es tomada por una parte del sistema conocido como planificador o ***scheduler***. Si se realiza un cambio de proceso, entonces se realiza un *context switch. G*uarda los registros del procesador como información del proceso para poder continuar más tarde, y carga los registros del nuevo proceso./h1

## Concurrencia

Hay un par de detalles aún por definir. ¿Que pasa si ocurre un ***timer interrupt*** mientras se ejecuta una ***system call***? El sistema operativo debe tener esto en cuenta. Una simple forma de solucionarlo es deshabilitando los *interrupts* durante la ejecución de otra interrupción.

Los sistemas operativos han desarrollado una cantidad de esquemas de bloqueo **(locking)** sofisticados para solucionar estos problemas que surgen con la concurrencia.
