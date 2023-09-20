## Variables de Condición

Un variable de condición tiene las siguientes propiedades:

- No guarda ningún valor
- Tiene asociado una cola

Consta de tres operaciones atómicas:

- `waitC(cond)`
- `signalC(cond)`
- `empty(cond)`

## Monitores

Nos permite sincronizar hilos con exclusión mutua y la posibilidad de esperar a que una condición se vuelva falsa. Tienen un mecanismo para señalizar otros hilos cuando su condición se cumple.

Un monitor consiste en:

- Un nombre
- Variables internas
- Procedimientos del monitor: rutinas que acceden directamente a las variables internas
- Una interfaz pública para que los procesos puedan acceder a las variables internas
- Inicialización de las variables internas
- Un conjunto de variables de condición que incorporan sincronismo al monitor.

Los procesos pueden tomar distintos estados:

- Esperando para entrar al monitor.
- Ejecutando el monitor (solo un proceso a la vez puede, hay exclusión mutua).
- Bloqueada en la cola de variables de condición.
- Recién liberado de la cola.
- Recién completó una operación `signalC`.

### Diferencias con un Semáforo

Algunas diferencias con los semáforos son:

- La operación `waitC` siempre bloquea, a diferencia de `wait` que puede hacerlo o no.
- La operación `signalC` no tiene efecto si la cola está vacía, a diferencia de `signal` que en caso de no haber procesos en la cola, incrementa el contador.
- Si no está vacía la cola, `signalC` desbloquea el proceso del tope de la cola. `signal` por el otro lado desbloquea un proceso arbitrario.
- Un proceso desbloqueado con `signalC` debe esperar que el proceso señalizador deje el monitor.

## Java

En Java, los hilos son distintos a los hilos de Rust. Esto se debe a que no utilizan al sistema operativo. Están implementados por el propio lenguaje. Hay dos formas de crear hilos:

- Heredando la clase `Thread`.
- Implementando la interfaz `Runnable`.

### Secciones Críticas
