---
title: Sistemas Distribuidos
---

> "Colección de computadoras independientes que el usuario ve como un solo sistema coherente." ~ Tanenbaum

> "Un sistema distribuido es aquel en el que el fallo de una computadora que ni siquiera sabes que existe, puede dejar tu propio computador inutilizable." ~ Lamport

## Herramientas

### Multiprogramación

- Multi-threading: Hilos compartiendo memoria
- Multi-processing: Procesos con memoria independiente
- Multi-computing: Distintas computadoras independientes

### Modelos de Análisis

- Modelo de estados (interleaved model)
- Modelo de eventos (happened before)

### Paralelismo vs. Concurrencia

- En un ambiente concurrente, los procesos se turnan para acceder a un recurso compartido (memoria, procesador)
- En un ambiente paralelo, los procesos acceden a recursos distintos y, por lo tanto, pueden avanzar a la vez.

### Topologías de Comunicación

- Bus
- Star
- Tree
- Mesh
- Sequential
- Ring

### Centralizados vs. Distribuidos

#### Centralizados

En un sistema centralizado no hay conexiones, o las conexiones son sin trabajo colaborativo y sin un objetivo común. Por ejemplo: sistemas de tiempo compartido, o terminales de conexión.

Son sistemas difíciles de escalar (procesamiento, memoria, disco).

- **Control**: lógica de control muy simple, efectiva y, en ocasiones, eficiente.
- **Homogeneidad**: la centralización incita a definir estándares para software y hardware.
- **Consistencia**: es posible definir fuertes políticas de consistencia de información y monitoreo del estado global del sistema.
- **Seguridad**: se disminuye la superficie de ataque frente a amenazas.

#### Distribuidos

En un sistema distribuido, los componentes están conectados y realizan trabajo colaborativo buscando un objetivo común.

Escalan distribuyendo trabajo y recursos.

## Fundamentos de Sistemas Distribuidos

## Aplicaciones Reales
