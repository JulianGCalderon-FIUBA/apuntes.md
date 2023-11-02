Existen distintos algoritmos para lidiar con deadlocks

## Algoritmos de Detección

### Algoritmo Centralizado

El proceso coordinador mantiene el grafo de uso de recursos, los procesos envían mensaje al coordinador cuando obtienen/liberan un recurso y el coordinador actualiza el grafo.

Un posible problema puede llegar ser que los mensajes lleguen desordenados, y generar falsos deadlocks.

Una posible solución es utiliza timestamps globales para ordenar los mensajes.

### Algoritmo Distribuido

Cuando un proceso debe esperar por un recurso, en