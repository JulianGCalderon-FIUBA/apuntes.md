El **tiempo** es una magnitud para medir duración y separación de eventos. Se lo puede definir mediante una variable monotónica creciente. No necesariamente está vinculada con la hora de la vida real.

La medición del tiempo permite, ordenar y sincronizar procesos. También se puede utilizar para registrar eventos con un **timestamp**: punto absoluto en la línea de tiempo, o con un **timespan**: intervalo en la línea de tiempo.

## Relojes Físicos

Los relojes físicos no son confiables, ya que tienen **drift** (debido a cambios en la temperatura, presión, etc.). Hay que sincronizarlos periódicamente, y al despertar la computadora.

Hay relojes globales y relojes locales, los relojes globales se utilizan como referencia para sincronizar relojes locales.

Algunas referencias conocidas son:

- **GMT** (*greamwich mean time*): ya no se utiliza como referencia, sino para el huso horario. Está basado en el tiempo de rotación terrestre.
- **UTC** (*universal time coordinated*): basado en relojes atómicos, y recibe ajustes periódicos.
- **GPS Time** (*global positioning system time*): basado en relojes atómicos, permite ajustar satélites, pero no recibe ajustes periódicos.

Para sincronizar un reloj físico, debemos compararnos con alguna referencia y aplicar una corrección.

### Algoritmo de Cristian

El algoritmo asume que los retrasos en la red son constantes. Mide el tiempo de retraso $D$ entre que el cliente envía la request y recibe la respuesta, y luego actualiza su reloj:

$$
T = T_\text{server} + D / 2
$$

### Network Time Protocol (NTP)

Es un protocolo de red para sincronizar relojes entre computadoras a través de redes con latencia variable. Se puede hacer un análisis estadístico para filtrar datos y obtener resultados de calidad.

- Debe tener una alta disponibilidad, para sobrevivir a largas caídas de conectividad. Para eso necesita tener servidores y rutas redundantes.
- Debe ser escalable, y soportar a un gran número de clientes sincronizados de forma frecuente.
- Debe tener en cuenta los efectos del drift.

La arquitectura está basada en estratos:

- El estrato cero son los *master clocks*
- Los estratos inferiores se conectan con estratos superiores en formato de árbol.
- Utilizan el [[#Algoritmo de Cristian]] para sincronizarse.
- Los servidores también se pueden conectar con servidores en el mismo estrato, en conexiones peer-to-peer, en caso de ser necesario.
- Al final de la estructura de estratos se encuentran los clientes.

Los mensajes son enviados utilizando UDP.

Hay diversos modos de sincronización:

- **Cliente-Servidor**: Las aplicaciones se conectan formando un grupo, donde las aplicaciones entre sí no pueden sincronizarse. Esto da la confianza de que todas las aplicaciones están sincronizadas (puesto que se sincronizan con el mismo grupo de servidores)
- **Modo Simétrico**: Los peers se conectan entre sí, ofreciendo respaldo mutuo. Es utilizado por los estratos 1 y 2.
- **Multicast o Broadcast**: Es utilizado en LAN de alta velocidad, es eficiente pero de baja precisión. Por lo general no se utilizan para sincronizar computadoras.

## Relojes Lógicos

Un evento es un suceso relativo a un proceso que modifica su estado.

El estado es el valor de todas las variables de un proceso

La relación `ocurre antes` es una relación de causalidad entre eventos, tal que:

- $a \to b$ si pertenecen al mismo proceso y $a$ ocurre antes que $b$.
- $a \to b$ si pertenecen a procesos distintos, pero $a$ es el envío de un mensaje y $b$ su recepción.
- $a \to c$, si $a \to b$ y $b \to c$ (transitividad)
