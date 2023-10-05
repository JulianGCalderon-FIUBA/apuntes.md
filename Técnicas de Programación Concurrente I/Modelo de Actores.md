Fue desarrollado por Carl Hewitt en 1973, y popularizado por el lenguaje Erlang.

El **actor** es la primitiva principal del modelo. Son livianos, se pueden crear miles. Estos encapsulan comportamiento y un estado. Están compuestos por:

- **Dirección:** Lugar a donde enviarle mensajes. En un sistema distribuido, la dirección del actor puede ser una dirección remota.
- **Casilla de correo:** Un FIFO de los últimos mensajes recibidos.

El actor **supervisor** puede crear otros actores hijos.

Los actores son aislados de otros actores, no comparten memoria.

## Mensajes

Los actores se comunican entre ellos solamente usando mensajes. Estos son procesados de forma asincrónica y de uno a la vez. Esto resuelve muchos problemas de concurrencia.
