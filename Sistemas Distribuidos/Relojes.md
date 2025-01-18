El **tiempo** es una magnitud para medir duración y separación de eventos. Se lo puede definir mediante una variable monotónica creciente. No necesariamente está vinculada con la hora de la vida real.

La medición del tiempo permite, ordenar y sincronizar procesos. Tambien se puede utilizar para registar eventos con un timestamps: 

- Marcar la ocurrencia de un proceso, con un timestamp: punto absoluto en la línea de tiempo

## Relojes Físicos

Los relojes físicos no son confiables, ya que tienen **drift**. Hay que sincronizarlos periódicamente, y al despertar la computadora.

## Protocolo NTP

Es un protocolo de red para sincronizar relojes entre computadoras a través de redes con latencia variable.

Está diseñado para tener alta escalabilidad y alta disponibilidad.

## Relojes Lógicos

Un evento es un suceso relativo a un proceso que modifica su estado.

El estado es el valor de todas las variables de un proceso

La relación `ocurre antes` es una relación de causalidad entre eventos, tal que:

- $a \to b$ si pertenecen al mismo proceso y $a$ ocurre antes que $b$.
- $a \to b$ si pertenecen a procesos distintos, pero $a$ es el envío de un mensaje y $b$ su recepción.
- $a \to c$, si $a \to b$ y $b \to c$ (transitividad)
