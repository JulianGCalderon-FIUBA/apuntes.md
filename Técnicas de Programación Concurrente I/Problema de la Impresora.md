En una oficina hay una impresora compartida

Habitualmente, las personas que trabajan allí envían documentos para ser impresos. Sin embargo, muchas veces se generan inconvenientes, ya que varias personas envían documentos al mismo tiempo, y luego las impresiones se encuentran intercaladas en la bandeja de salida, entorpeciendo el trabajo.

## Solución con [[Exclusión Mutua Distribuida#Algoritmo Centralizado|Mutex Centralizado]]

Un proceso es elegido coordinador. Cuando un proceso quiere imprimir, envía un mensaje al coordinador.

- Si no hay ningun proceso imprimiendo, el coordinador envía OK.
- Si hay, el coordinador no envía respuesta hasta que se libre la impresora.
