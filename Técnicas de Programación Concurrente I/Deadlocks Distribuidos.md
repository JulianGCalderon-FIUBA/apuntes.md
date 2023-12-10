Los *deadlocks* en los sistemas distribuidos son más difíciles de evitar, prevenir, o incluso detectar. También es más difícil resolverlos una vez fueron encontrados, ya que la información relevante se encuentra dispersa en diferentes geográficamente. Existen distintos algoritmos para lidiar con deadlocks.

## Algoritmos de Detección

Prevenirlos es dificil, por lo que se desarrollaron métodos para poder detectar los métodos una vez ocurrieron.

### Algoritmo Centralizado

El proceso coordinador mantiene el grafo de uso de recursos, los procesos envían mensaje al coordinador cuando obtienen/liberan un recurso y el coordinador actualiza el grafo.

Un posible problema puede llegar ser que los mensajes lleguen desordenados, y generar falsos deadlocks.

Una posible solución es utiliza timestamps globales para ordenar los mensajes.

### Algoritmo Distribuido

Cuando un proceso debe esperar por un recurso, envía un *probe message* al proceso que tiene el recurso. El mensaje contiene:

- Identificador del proceso que se bloquea.
- identificador el proceso que envía el mensaje.
- identificador el proceso destinatario.

Al recibir el mensaje, el proceso actualiza el *id* del proceso que envía y el *id* del destinatario, y lo envía a los procesos que tienen el recurso que necesita.

Si el mensaje llega al proceso original, tenemos un ciclo en el grafo.

## Algoritmos de Prevención

### Algoritmo Wait-Die

Se asigna un *timestamp* único y global a cada transacción al inicial (algoritmo de Lamport).

Cuando un proceso está por bloquearse en un recurso (que tiene otro proceso), se comparan los *timestamps*.

- Si el *timestamp* es menor, espera (proceso más viejo).
- Si no, el proceso aborta la transacción.

Si bien se puede hacer que el proceso más viejo sea el que aborte, es más intuitivo el sentido contrario, ya que un proceso más viejo tiende a tener más recursos y más tiempo invertido, por lo que no es bueno abortarlo.

### Algoritmo Wound-Wait

Se asigna un timestamp único y global a cada transacción al inicial (algoritmo de Lamport)

Cuando un proceso está por bloquearse en un recurso (que tiene otro proceso), se comparan los *timestamps*.

- Si el *timestamp* es menor (proceso más viejo), se aborta la transacción del proceso que tiene el recurso, para que el más viejo pueda tomarlo.
- Si no, el proceso espera.
