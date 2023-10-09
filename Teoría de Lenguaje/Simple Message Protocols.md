Refiere a la invocación de métodos remota a través de mensajes. Existen varias implementaciones (ligadas a la implementación de puertos):

- Sincrónico / Asincrónico: Un protocolo sincrónico exige obtener una respuesta antes de realizar la siguiente consulta. En un protocolo asincrónico puedo hacer múltiples consultas antes de recibir sus respuestas.
- Servidor Secuencial / Concurrente: Un servidor secuencial solo puede atender a un cliente a la vez, mientras que un servidor concurrente puede abrir múltiples hilos y resolver varias consultas a la vez.
- Con Callbacks / Sin Callbacks: Si el protocolo tiene callbacks, se le manda por mensaje un canal auxiliar a través del cual se debe reenviar la respueta.
