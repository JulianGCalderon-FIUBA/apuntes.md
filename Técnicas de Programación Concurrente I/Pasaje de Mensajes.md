Existen distintos de comunicación respecto al pasaje de mensajes. Se pueden catalogar según el modo de comunicación:

- Sincrónica: no hay espera entre el envío y la recepción, ocurre al mismo tiempo.
- Asíncrónica: necesitaría de un *buffer* para almacenar los mensajes hasta que son recibidos.

Según el modo de direccionamiento.

- Simétrico: Hay una única dirección de origen y destino
- Asimétrico: Hay una única dirección de destino, pero muchas direcciones de origen *(multiple producer single consumer)*
- Sin direccionamiento: Quien lo recibe dependerá de la estructura del mensaje *(matching)*.

Según el flujo de datos:

- Unidireccional
- Bidireccional.

Para enviar mensajes entre procesos, se utilizan los [[Técnicas de Programación Concurrente I/Canales|canales]]
