---
title: Modelos de Concurrencia
---

Los modelos de concurrencia nos ayudan a diseñar programas concurrentes, sin mucha complejidad adicional

## Estado Mutable Compartido

Consiste en **serializar** el acceso al estado compartido. Se utilizan estructuras conocidas como *locks* para que ciertos procedimientos **críticos** se ejecuten de forma exclusiva.

Si se está ejecutando algún procedimiento crítico, entonces cualquier otro proceso que quiera ejecutarlo deberá esperar a que el *lock* sea liberado.

## Paralelismo Fork-Join

Cuando los procesos no deben interactuar entre ellos, y el resultado final depende de la **combinación** de los resultados de aquellos procesos independientes, puedo utilizar este modelo. Espero a que todos los hilos finalicen y **combino** los resultados.

## Canales y Mensajes

Los hilos se comunican entre sí al enviar mensajes a través de canales. De esta forma, no se accede a memoria compartida, sino que sé comparte la memoria a través del envío de mensajes.

> "Don't communicate by sharing memory; share memory by communicating." (R. Pike)

## Actor

Existe un actor que recibe mensajes de distintos hilos a través de un canal y resuelve peticiones. El actor toma control de un recurso y se encarga de manejarlo.

## Asincronismo

Busca realizar concurrencia **colaborativa**. Ejecuta tareas livianas en un entorno de ejecución que maximiza su eficiencia. Busca que el programa parezca secuencial, pero que se comporte de forma concurrente.
