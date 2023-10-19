Tenemos una sección crítica que puede ser ejecutada a la vez por un solo proceso dentro de todo el sistema.

## Algoritmo Centralizado

Para resolver esto de forma centralizada, necesitaremos la ayuda de un coordinador:

1. Un proceso es elegido como **coordinador**. Usualmente, es denominado *lider*.
2. Cuando un proceso quiere entrar a la sección crítica, envía un mensaje al coordinador.
3. Si no hay ningún proceso en la sección crítica, el coordinador envía OK; si hay, el coordinador no envía respuesta hasta que se libere la sección crítica.

## Algoritmo Distribuido

Cuando un proceso quiere entrar en una sección crítica, construye un mensaje con el nombre de la sección crítica, el número de procesos, y el *timestamp*. Al recibir el mensaje:

- Si no está en la sección crítica y no quiere entrar, envía OK
- Si está en la sección crítica, no responde y encola el mensaje. Cuando sale, envía OK.
- Si quiere entrar en la sección crítica, compara el *timestamp*, y gana el menor (más antiguo)

## Algoritmo Token Ring

Se conforma un anillo mediante conexiones punto a punto. Al inicializar, el proceso 0 recibe un token que va circulando por el anillo (de forma ordenada).

Solo el proceso que tiene el token puede entrar a la sección crítica. Cuando el proceso dale de la sección crítica, continúa circulando el *token*.

El proceso no puede entrar a otra sección crítica con el mismo token. Esto permite que el sistema sea justo.
