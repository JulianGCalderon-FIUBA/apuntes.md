Es similar al patrón de [[Producer-Consumer]]. Es un modelo basado en comunicación por tareas entre productores y consumidores.

Existen 2 tipos de nodos:

- **Publishers**: Son los emisores de eventos. Tienen la posibilidad de generar algún elemento de interés.
- **Subscribers**: Son los receptores. Esperan la aparición de algún evento de su propio interés sobre el cual efectuaran alguna acción.

Hay dos posibles arquitecturas:

- Basada en **tópicos**: Publicación y subscripción indicando el tipo de evento.
- Basada en **canales**: Publicaciones y suscripciones orientadas a canales específicos.

Los [[MOMs]] ofrecen este patrón.
