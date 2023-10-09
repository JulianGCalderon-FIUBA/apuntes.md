Refiere a la invocación de métodos remota a través de mensajes. Existen varias implementaciones (ligadas a la implementación de puertos):

- Sincrónico/Asincrónico: Un protocolo sincrónico exige obtener una respuesta antes de realizar la siguiente consulta. En un protocolo asincrónico puedo hacer múltiples consultas antes de recibir sus respuestas.
- Servidor Secuencial/Concurrente: Un servidor secuencial solo puede atender a un cliente a la vez, mientras que un servidor concurrente puede abrir múltiples hilos y resolver varias consultas a la vez.
- Con/Sin *Callbacks*: Si el protocolo tiene *callbacks*, el cliente envía a través del mensaje un canal auxiliar a través del cual el servidor puede enviarle una consulta al cliente. Notemos que para que el cliente pueda resolver la consulta del servidor, entonces el protocolo debe ser asincrónico.
