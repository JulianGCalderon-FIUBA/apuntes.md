---
aliases:
  - RPC
---

Permite ejecución remota de procedimientos, con un esquema de cliente-servidor

- El cliente realiza una llamada a un procedimiento
- El servidor responde con el resultado de la operación

La comunicación remota es transparente para el usuario.

Hay portabilidad a través de implementación de interfaces bien definidas.

## Interface Definition language

Se utilizan lenguajes de definición de interfaces, que luego son utilizados para generar las estructuras necesarias en el lenguaje deseado (Python, Go, Rust).

La interfaz de las funciones está definida según sus datos de entrada (input) y sus datos de salida (output).

Un ejemplo de esto es *google protocol buffers*

## Tolerancia a Fallos

A diferencia de en una llamada local, debemos tomar medidas para prevenir fallos en la comunicación: [[Comunicacion Confiable#Perdida de Mensajes|Perdida de Mensajes]].
