Es un framework de coordinación basado en transmisión y recepción de mensajes.

Se utiliza como biblioteca con abstracciones de uso general con foco en cómputo distribuido. La ejecución se vuelve transparente a la cantidad de nodos involucrados.

Un modo de uso típico consiste en tener un proceso maestro que coordina al resto enviándoles información y operaciones a realizar:

- La operación scatter particiona datos y los envía a los nodos para procesarlos.
- La operación gather unifica datos provenientes de diferentes nodos.
