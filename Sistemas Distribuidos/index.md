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

### Topologías

- Bus
- Star
- Tree
- Mesh
- Sequential
- Ring

[[Sistema Centralizado]]

### Sistema Distribuido

En un sistema distribuido, los componentes están conectados y realizan trabajo colaborativo buscando un objetivo común.

Escalan distribuyendo trabajo y recursos.

- **Disponibilidad**: aún frente a fallos aislados, el sistema general puede prestar servicios.
- **Escalabilidad**: mejores alternativas de adaptarse a nuevas escalas
- **Reducción de Latencia**: al favorecer principios de localidad de recursos.
- **Colaboración**: permite interacciones entre sistemas de forma orgánica y natural.
- **Movilidad**: no están circunscritos al alcance de un único computador.
- **Costo**: componentes más simples. Subsistemas delegados en servicios terceros

#### Descentralizar vs. Distribuir

**Centralizar** implica la concentración de la autoridad en los niveles más altos de una jerarquía.

**Descentralizar** implica transferir la toma de decisiones a eslabones inferiores de cierta organización.

**Distribuir** implica utilizar un modelo descentralizado de control de computadoras para la coordinación de actividades con una coherencia dada.

## Fundamentos de Sistemas Distribuidos

## Aplicaciones Reales
