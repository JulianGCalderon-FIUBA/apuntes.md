Fue desarrollado por Carl Hewitt en 1973, y popularizado por el lenguaje Erlang.

## Actor

El **actor** es la primitiva principal del modelo. Son livianos, se pueden crear miles. Estos encapsulan comportamiento y un estado. Están compuestos por:

- **Dirección:** Lugar a donde enviarle mensajes. En un sistema distribuido, la dirección del actor puede ser una dirección remota.
- **Casilla de correo:** Un FIFO de los últimos mensajes recibidos.

El actor **supervisor** puede crear otros actores hijos.

Los actores son aislados de otros actores, no comparten memoria.

## Mensajes

Los actores se comunican entre ellos solamente usando mensajes. Estos son procesados de forma asincrónica y de uno a la vez. Esto resuelve muchos problemas de concurrencia.

## Actores en Rust - Actix

Usa *tokio* y *futures* como *runtime* de sustento. Se ejecutan dentro del sistema de actores.

### Arbitro

El núcleo es de tipo *Arbitrer*. Un hilo que crea un *event loop* por debajo y provee un *handler*.

- Cada actor se ejecuta dentro de un arbitrer
- El handler se usa para enviar mensajes al actor
- Se ejecutan en un contexto de ejecución `Context<A>` separado para cada uno.

Provee el contexto de ejecución asincrónica para los actores, funciones, y futuros. Alojan el entorno donde se ejecuta el actor.

### Creación de un Actor

Primero, debemos crear un tipo de dato que implemente `trait Actor`.

Luego, definimos un mensaje e implementamos `trait Handler<M>` para ese tipo del actor.

Finalmente creamos un actor y hacemos *spawn* en uno de los árbitros.

### Ciclo de Vida del Actor

Tendremos los siguientes estados:

- **Iniciado (Started):** Se inicia con el método `started()`.
- **En ejecución (Running):** Es el estado siguiente a la ejecución de `started()`. Puede estar en este estado de forma indefinida.
- **Parando (Stopping):** Puede pasar a este estado en las siguientes situaciones:
	- Llamando `Context::stop` en el mismo actor
	- Ningún otro actor lo referencia
	- No hay objetos registrados en el contexto
- **Detenido (Stopped)**: Desde el estado anterior no modificó su situación. Es el último estado de ejecución.

### Dirección

Un actor es referenciado por su dirección, la cual se devuelve luego de ejecutar `.start()` sobre un actor.

### Mensaje

Los mensajes deben implementar `trait Message`. Para enviar mensajes, necesitaremos la dirección.

- `Addr::do_send(M)`: Ignora los errores en el envío del mensaje. Si la casilla de mensaje está cerrada, se descarta. No retorna resultado.
- `Addr::try_send(M)`: Trata de enviar el mensaje inmediatamente. Si la casilla de mensajes está llena o cerrada, retorna `SendError`.
- `Addr::send(M)`: Retorna un futuro que devuelve como el resultado del proceso de manejo de mensaje.

### Contexto

Los actores mantienen el contexto interno de ejecución, o estado. Permite al actor determinar su dirección, cambiar los límites de la casilla de mensajes, o detenerse. Los mensajes llegan a la casilla primero, luego el contexto de ejecución llama al *handler* especifico.

### Arbitro

El arbitro provee
