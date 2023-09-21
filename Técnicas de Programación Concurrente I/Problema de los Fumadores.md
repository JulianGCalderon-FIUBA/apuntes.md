Consideremos que para fumar un cigarrillo se necesitan tres ingredientes: tabaco, papel, y fósforos.

Hay tres fumadores alrededor de una mesa. Cada uno tiene una cantidad infinita de uno solo de los ingredientes, y necesita los otros dos para fumar. Cada fumador posee un ingrediente distinto.

Existe además una gente que pone aleatoriamente dos ingredientes en la mesa. El fumador que los necesita tomará para hacer su cigarrillo y fumará un rato. Cuando el fumador termina, el agente pone otros dos ingredientes.

Se puede pensar como el [[Problema de los Filósofos]], en el caso donde no todos los recursos están disponibles al mismo tiempo. Es decir, falta uno de los palitos chinos.

Este problema surgió para desmentir que todos los problemas de concurrencia podían resolver con [[Semáforos]]. Existe una solución, pero no es lo suficientemente eficiente.

## Solución con [[Semáforos]]

Utilizamos un solo semáforo binario que sincronice a todos los ingredientes a la vez. De esta forma, los fumadores accederán a la mesa periódicamente para verificar que estén los ingredientes que necesita y los toma.

Esta solución tiene la desventaja de que como estamos utilizando el semáforo como un lock, ya perdemos su capacidad de señalizar que necesitamos para que el agente notifique a los fumadores que están los ingredientes en la mesa.

Para aislar la capacidad de señalización del contenido de un lock podemos utilizar las variables de condición.

## Solución con [[Variables de Condición]]

Tendremos un lock que sincronice el acceso a todos los ingredientes a la vez, y una variable de condición que utilizará el agente para notificar