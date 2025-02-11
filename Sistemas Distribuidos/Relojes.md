El **tiempo** es una magnitud para medir duración y separación de eventos. Se lo puede definir mediante una variable monotónica creciente. No necesariamente está vinculada con la hora de la vida real.

La medición del tiempo permite, ordenar y sincronizar procesos. También se puede utilizar para registrar eventos con un **timestamp**: punto absoluto en la línea de tiempo, o con un **timespan**: intervalo en la línea de tiempo.

## Relojes Físicos

Los relojes físicos no son confiables, ya que tienen **drift** (debido a cambios en la temperatura, presión, etc.). Hay que sincronizarlos periódicamente, y al despertar la computadora.

Hay relojes globales y relojes locales, los relojes globales se utilizan como referencia para sincronizar relojes locales.

![[Relojes 1739235128.png]]

Algunas referencias conocidas son:

- **GMT** (*greamwich mean time*): ya no se utiliza como referencia, sino para el huso horario. Está basado en el tiempo de rotación terrestre.
- **UTC** (*universal time coordinated*): basado en relojes atómicos, y recibe ajustes periódicos.
- **GPS Time** (*global positioning system time*): basado en relojes atómicos, permite ajustar satélites, pero no recibe ajustes periódicos.
- **TAI** (*Temps Atomique International*): Hay 200 relojes atómicos en 70 países. No recibe ajustes astronómicos.

Para sincronizar un reloj físico, debemos compararnos con alguna referencia y aplicar una corrección.

### Algoritmo de Cristian

El algoritmo asume que los retrasos en la red son constantes. Mide el tiempo de retraso $D$ entre que el cliente envía la request y recibe la respuesta, y luego actualiza su reloj:

$$
T = T_\text{server} + D / 2
$$

![[Relojes 1739235204.png]]

### Network Time Protocol (NTP)

Es un protocolo de red para sincronizar relojes entre computadoras a través de redes con latencia variable.

- Debe tener una alta disponibilidad, para sobrevivir a largas caídas de conectividad. Para eso necesita tener servidores y rutas redundantes.
- Debe ser escalable, y soportar a un gran número de clientes sincronizados de forma frecuente.
- Debe tener en cuenta los efectos del drift.
- Debe ofrecer sincronización. Sé puede hacer un análisis estadístico para filtrar datos y obtener resultados de calidad.

La arquitectura está basada en estratos:

- El estrato cero son los *master clocks*
- Los estratos inferiores se conectan con estratos superiores en formato de árbol.
- Utilizan el [[#Algoritmo de Cristian]] para sincronizarse.
- Los servidores también se pueden conectar con servidores en el mismo estrato, en conexiones peer-to-peer, en caso de ser necesario.
- Al final de la estructura de estratos se encuentran los clientes.
- Hay muchos estratos

![[Relojes 1737227315.png]]

Los mensajes son enviados utilizando UDP.

Hay diversos modos de sincronización:

- **Cliente-Servidor**: Las aplicaciones se conectan formando un grupo, donde las aplicaciones entre sí no pueden sincronizarse. Esto da la confianza de que todas las aplicaciones están sincronizadas, puesto que se sincronizan con el mismo grupo de servidores. Es utilizado por los clientes.
- **Modo Simétrico**: Los peers se conectan entre sí, ofreciendo respaldo mutuo. Es utilizado por los estratos 1 y 2.
- **Multicast o Broadcast**: Es utilizado en LAN de alta velocidad, es eficiente pero de baja precisión. Por lo general no se utilizan para sincronizar computadoras.

## Relojes Lógicos

Un **evento** es un suceso relativo a un proceso que modifica su estado.

El **estado** es el valor de todas las variables de un proceso

La relación **ocurre antes** ($\to$) es una relación de causalidad entre eventos, tal que:

- $a \to b$ si pertenecen al mismo proceso y $a$ ocurre antes que $b$.
- $a \to b$ si pertenecen a procesos distintos, pero $a$ es el envío de un mensaje y $b$ su recepción.
- Además, se define la transitividad: $a \to c$, si $a \to b$ y $b \to c$

Dado $S$, el conjunto de todos los estados posibles del sistema, entonces un **reloj lógico** es una función $C$ monotónica creciente que asocia estados con un número natural, garantiza:

$$
\forall s,t \in S : s \to t \implies C(s) < C(t)
$$

### Algoritmo de Lamport

Dado un conjunto de $n$ procesos. Todos comienzan con un reloj lógico inicializado en $0$. Cada evento toma como timestamp el valor del reloj actual, y lo incrementa en $1$.

1. Los mensajes enviados entre procesos incluyen el *timestamp* de ese evento.
2. Cuando un proceso recibe un mensaje, actualiza el reloj para obtener el máximo entre el reloj actual y el timestamp del mensaje, de modo que la recepción del mensaje tenga un valor mayor al envió del mismo (el timestamp dentro del mensaje).

Esto, garantiza la definición de reloj lógica, pero no garantiza la recíproca. Esto implica que no necesariamente los relojes mostrarán la verdad.

![[Relojes 1737228063.png]]

### Vector de Relojes

Un vector de relojes es la asociación de todo estado del sistema, compuesto por $k$ procesos, con un vector de $k$ números naturales, y garantiza:

$$
\forall s,t \in S: s \to t \iff s.v < t.v
$$

Donde $s.v, t.v$ son los vectores para los estados $s, v$ respectivamente.

$$
s.v < t.v \iff \forall k: s.v[k] <= t.v[k] \land \exists j : s.v[j] < t.v[j]
$$

Dado un conjunto de $n$ procesos. Todos comienzan con un vector lógico inicializado en $0$. Cada evento toma como timestamp el valor de vector actual, e incrementa la posición del vector correspondiente a sí mismo en $1$.

1. Los mensajes enviados entre procesos incluyen el *timestamp* de ese evento (vector completo).
2. Cuando un proceso recibe un mensaje, actualiza cada posición del reloj para obtener el máximo entre el vector actual, y el vector contenido en el mensaje. Esto asegura que la recepción del mensaje tenga un timestamp mayor al envío del mismo (el timestamp dentro del mensaje).

![[Relojes 1737228759.png]]

Esto, garantiza la definición de reloj lógica, y también garantiza la recíproca. Si dados dos eventos $s, v$ tal que $s \not < v$ y $v \not < s$, diremos que los eventos son concurrentes.

Esto lo hace redefiniendo la operación de $<$ de modo que solo se cumpla cuando se sabe que los eventos asociados ocurrieron uno después del otro. En el resto de casos, no se cumplirá $<$, $=$, ni $>$.
