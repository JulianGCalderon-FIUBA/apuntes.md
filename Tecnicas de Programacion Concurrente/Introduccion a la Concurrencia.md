---
title: Introducción a la Concurrencia
---

## Definiciones Básicas

Un **programa** es un conjunto de datos, asignaciones e instrucciones de control de flujo que compilan a instrucciones de máquina, las cuales se ejecutan secuencialmente en un procesador y acceden a datos almacenados en memoria principal o memorias secundarias.

Un **programa concurrente** es un conjunto de programas secuenciales que pueden ejecutarse en paralelo. Esto implica que no necesariamente se ejecutaran en paralelo, como por ejemplo, cuando contamos con un solo procesador (con un solo hilo de ejecución). Consiste en un conjunto finito de procesos secuenciales.

Un **proceso** es (para esta materia) cada uno de los programas secuenciales que conforman el programa concurrente Está compuesto por un conjunto finito de instrucciones atómicas.

La **ejecución del programa concurrente** resulta al ejecutar una secuencia de instrucciones atómicas que se obtiene de intercalar de forma arbitraria las instrucciones atómicas de los procesos que lo componen. Puede ser distinto cada vez, por lo que la depuración puede ser muy difícil.

Un **sistema paralelo** es un sistema compuesto por varios programas que se ejecutan simultáneamente en procesadores distintos.

El **multitasking** es la ejecución de múltiples procesos concurrentemente en un cierto periodo de tiempo. El *scheduler* se encargará de coordinar el acceso a los procesadores.

El **multithreading** es la construcción provista por algunos lenguajes de programación que permite la ejecución concurrente de *threads* dentro del mismo programa.

## Desafíos de la Concurrencia

El principal desafío es la necesidad de sincronizar y comunicar procesos diferentes.

- **Sincronización:** Coordinación temporal entre distintos procesos.
- **Comunicación:** Datos que necesitan compartir los procesos para cumplir la función del programa.

## Ventajas de la Concurrencia

La concurrencia es útil en dos escenarios principales:

- Necesitamos que nuestro programa este compuesto por partes **independientes**. Necesariamente, tendremos múltiples hilos de ejecución. Por ejemplo:
	- Leer la entrada del usuario.
	- Resolver peticiones de múltiples clientes.
	- Realizar peticiones de entrada/salida.
- Mejorar el **rendimiento** de nuestro programa, aprovechando el procesador y el tiempo muerto por las operaciones de entrada/salida
